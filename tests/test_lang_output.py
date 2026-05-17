"""
--lang 参数输出语言验证测试

验证 zh/en 两种语言模式的产出特征：
- zh 模式：中文正文 + 英文术语保留
- en 模式：纯英文输出
"""

import re
import pytest
from pathlib import Path

SKILL_ROOT = Path(__file__).parent.parent
EXAMPLES_DIR = (SKILL_ROOT / "tests" / "fixtures") if (SKILL_ROOT / "tests" / "fixtures").is_dir() and any((SKILL_ROOT / "tests" / "fixtures").iterdir()) else (SKILL_ROOT / "examples")

_CANDIDATE_BRIEF = ["zod", "fastapi", "bat"]
BRIEF_PROJECTS = [p for p in _CANDIDATE_BRIEF if (EXAMPLES_DIR / p).is_dir()]

# Chinese character detection
ZH_PATTERN = re.compile(r'[一-鿿]')
# Technical term patterns that should stay in English
TECH_PATTERNS = [
    re.compile(r'// Simplified from:'),  # source citations always English
    re.compile(r'\.md\b'),               # file extensions
    re.compile(r'\.py\b'),
    re.compile(r'\.json\b'),
]


@pytest.fixture(params=BRIEF_PROJECTS)
def project_docs(request):
    """Return docs directory for a brief project"""
    docs = EXAMPLES_DIR / request.param / "docs"
    if not docs.is_dir():
        pytest.skip(f"{request.param} has no docs/")
    return docs


def _read_all_md(docs_dir):
    """Read all markdown files in a directory"""
    texts = []
    for md in sorted(docs_dir.glob("*.md")):
        texts.append(md.read_text(encoding="utf-8"))
    return texts


class TestDefaultLangIsZh:
    """Default (no --lang specified) should produce Chinese output"""

    def test_has_chinese_in_prose(self, project_docs):
        """At least one chapter should contain Chinese characters"""
        texts = _read_all_md(project_docs)
        has_zh = any(ZH_PATTERN.search(t) for t in texts)
        assert has_zh, "Default output should contain Chinese characters"

    def test_source_citations_in_english(self, project_docs):
        """Source citations should always be in English"""
        texts = _read_all_md(project_docs)
        for text in texts:
            citations = re.findall(r'// Simplified from:.*', text)
            for c in citations:
                assert not ZH_PATTERN.search(c), f"Citation should be English: {c}"

    def test_file_paths_in_english(self, project_docs):
        """File paths in output should not contain Chinese"""
        texts = _read_all_md(project_docs)
        for text in texts:
            # Match common path patterns like src/xxx, .claude/xxx, etc
            paths = re.findall(r'(?:src|lib|test|docs|\.claude|\.cursor)/[\w./-]+', text)
            for p in paths:
                assert not ZH_PATTERN.search(p), f"Path should be English: {p}"


class TestDocumentationStandards:
    """Verify documentation-standards.md has both lang modes"""

    def test_standards_file_exists(self):
        path = SKILL_ROOT / "docs" / "documentation-standards.md"
        assert path.is_file()

    def test_has_zh_mode(self):
        path = SKILL_ROOT / "docs" / "documentation-standards.md"
        content = path.read_text()
        assert "`zh`" in content, "Should define zh mode"
        assert "`en`" in content, "Should define en mode"

    def test_has_lang_section(self):
        path = SKILL_ROOT / "docs" / "documentation-standards.md"
        content = path.read_text()
        assert "Language" in content or "language" in content


class TestManifestSchemaHasLang:
    """Verify manifest schema includes lang field"""

    def test_schema_has_lang(self):
        import json
        path = SKILL_ROOT / "docs" / "sources-manifest.schema.json"
        schema = json.loads(path.read_text())
        assert "lang" in schema["properties"], "Schema should have lang field"
        assert schema["properties"]["lang"]["enum"] == ["zh", "en"]
