# Project Walkthrough Generator

为任意软件项目生成分层技术走读文档的 Claude Code skill。输出 markdown 文档 + 交互式 HTML。

## 功能

- **多深度**：brief（概览）、medium（进阶）、deep（深入）、all（全部）
- **多受众**：general（类比+白话）、dev（纯技术）
- **多语言**：zh（中文正文+英文术语，默认）、en（纯英文）
- **输出**：编号 markdown 章节 + 自包含交互式 HTML（暗色/亮色、侧边栏、quiz）
- **自动探索协议**：识别项目类型 → 读核心文件 → 提取创新点 → 生成章节
- **Manifest-first 准确性保证**：先验证所有声明，再写内容，每个事实可追溯到源码

## 安装

### Claude Code（推荐）

```bash
# 1. 添加 marketplace
/plugin marketplace add zwyin/project-walkthrough-skill

# 2. 安装插件
/plugin install project-walkthrough@project-walkthrough-skill
```

安装后直接在任意项目中使用 `/project-walkthrough` 命令。

### 手动安装

将本仓库 clone 到本地，然后在 Claude Code 中指定 plugin 目录：

```bash
git clone https://github.com/zwyin/project-walkthrough-skill.git
claude --plugin-dir ./project-walkthrough-skill  # 保留完整目录结构，路径引用不会断裂
```

### 其他平台

| 平台 | 安装方式 |
|------|---------|
| Gemini CLI | `gemini skills install https://github.com/zwyin/project-walkthrough-skill.git` |
| OpenCode | clone 后复制到 `~/.opencode/skills/project-walkthrough/` |
| Windsurf | clone 后复制到 `~/.windsurf/skills/project-walkthrough/` |

> **注意：** Python 辅助脚本（`verify_sources.py`、`import_graph.py`）需要 Python 3 环境。在非 Claude Code 平台上，部分依赖脚本的功能可能需要手动调整路径。

## 用法

```
/project-walkthrough                                              # Brief + general + zh (CWD)
/project-walkthrough /path/to/project                             # Brief + general + zh
/project-walkthrough /path/to/project --depth medium              # Medium + general + zh
/project-walkthrough /path/to/project --depth deep --audience dev # Deep + dev + zh
/project-walkthrough --depth all                                  # All depths + general + zh (CWD)
/project-walkthrough /path/to/project --lang en                   # Brief + general + en
```

**参数说明：**

| 参数 | 允许值 | 默认值 | 说明 |
|------|--------|--------|------|
| `[path]` | 目录路径 | 当前目录 | 项目目录 |
| `--depth` | `brief`, `medium`, `deep`, `all` | `brief` | `brief` 概览 ~30min 7-8 文档；`medium` 进阶 ~60min 12-15 文档；`deep` 深入 ~120min 8-15 文档；`all` 依次生成三级 |
| `--audience` | `general`, `dev` | `general` | `general` 类比+白话；`dev` 纯技术分析 |
| `--lang` | `zh`, `en` | `zh` | `zh` 中文正文+英文术语；`en` 纯英文 |

**语法规则：** 空格分隔（`--depth medium`），不支持 `--depth=medium`。无效值回退到默认。重复 flag 取最后一次。flags 大小写敏感。

> 详细解析规则见 `skills/project-walkthrough/SKILL.md` Usage 部分。

## 输出结构

```
project_study_<project-name>/
├── docs/
│   ├── 01-overview.md              ← Brief
│   ├── sources-manifest.json       ← Brief manifest（强制性）
│   ├── medium/
│   │   └── sources-manifest.json   ← Medium manifest
│   └── deep/
│       └── sources-manifest.json   ← Deep manifest
└── interactive/
    ├── walkthrough.html
    ├── medium-walkthrough.html
    └── deep-walkthrough.html
```

## 准确性机制

核心原则：**verify before write**。通过 12 轮迭代验证建立：

- **Manifest-first**：Phase 3A 先验证所有声明写入 manifest，Phase 3B 只写已验证内容
- **Source citation**：每个代码块必须有 `// Simplified from: path:lines`
- **禁止 `// Source:`**：统一使用 `Simplified from:`（walkthrough 代码总是简化的）
- **不可验证 = 不写入**：无法验证的声明不能出现在 walkthrough 中
- **自动化验证**：`scripts/verify_sources.py` 检查 manifest 完整性和源文件存在性

## 测试

```bash
pytest tests/ -v                    # 单元测试 + 产出物结构验证
python scripts/verify_sources.py --check-all examples/ --strict  # manifest 验证
```

## 项目结构

```
├── .claude-plugin/
│   ├── plugin.json                 # Claude Code 插件元数据
│   └── marketplace.json            # Marketplace 注册信息
├── skills/
│   └── project-walkthrough/
│       └── SKILL.md                # Skill 定义（流程、规范、checklist）
├── docs/
│   ├── html-reference.md           # HTML 模板和 CSS 组件规范
│   ├── documentation-standards.md  # 文档写作和格式规范
│   ├── chapter-templates.md        # 按项目类型的章节模板
│   ├── exploration-protocol.md     # 探索协议
│   ├── sources-manifest-schema.md  # Manifest schema 文档
│   ├── sources-manifest.schema.json  # Manifest JSON Schema
│   └── accuracy-verification-protocol.md  # 准确性验证协议
├── scripts/
│   ├── verify_sources.py           # Manifest 验证脚本
│   └── import_graph.py             # 依赖图提取脚本
└── tests/
    ├── test_walkthrough_output.py  # 输出验证测试
    ├── test_verify_sources.py      # Manifest 验证测试
    └── test_import_graph.py        # 依赖图测试
```

## 示例 / Demo

本仓库包含自生成的 walkthrough 示例，展示插件产出物的实际效果：

| 示例 | 语言 | 说明 |
|------|------|------|
| [`examples/self-demo-zh/`](examples/self-demo-zh/) | `--lang zh` | 中文概览 walkthrough（本插件自身） |
| [`examples/self-demo-en/`](examples/self-demo-en/) | `--lang en` | 英文概览 walkthrough（本插件自身） |

打开 `interactive/walkthrough.html` 即可在浏览器中体验交互式走读。

## License

MIT
