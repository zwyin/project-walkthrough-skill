# Project Walkthrough Generator

为任意软件项目生成分层技术走读文档的 Claude Code skill。输出 markdown 文档 + 交互式 HTML。

## 功能

- 多深度：brief（概览）、medium（进阶）、deep（深入）、all（全部）
- 多受众：general（类比+白话）、dev（纯技术）
- 输出：编号 markdown 章节 + 自包含交互式 HTML（暗色/亮色、侧边栏、quiz）
- 自动探索协议：识别项目类型 → 读核心文件 → 提取创新点 → 生成章节
- Manifest-first 准确性保证：先验证所有声明，再写内容，每个事实可追溯到源码

## 安装

将本目录作为 Claude Code plugin 引入，或在 `settings.json` 中配置 skill 路径。

## 用法

```
/project-walkthrough                                              # Brief + general (CWD)
/project-walkthrough /path/to/project                             # Brief + general
/project-walkthrough /path/to/project --depth medium              # Medium + general
/project-walkthrough /path/to/project --depth deep --audience dev # Deep + dev
/project-walkthrough --depth all                                  # All depths + general (CWD)
```

**参数说明：**

| 参数 | 允许值 | 默认值 | 说明 |
|------|--------|--------|------|
| `[path]` | 目录路径 | 当前目录 | 项目目录 |
| `--depth` | `brief`, `medium`, `deep`, `all` | `brief` | `brief` 概览 ~30min 7-8 文档；`medium` 进阶 ~60min 12-15 文档；`deep` 深入 ~120min 8-15 文档；`all` 依次生成三级 |
| `--audience` | `general`, `dev` | `general` | `general` 类比+白话；`dev` 纯技术分析 |

**语法规则：** 空格分隔（`--depth medium`），不支持 `--depth=medium`。无效值回退到默认。重复 flag 取最后一次。flags 大小写敏感。

> 详细解析规则见 `SKILL.md` Usage 部分。

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

## 示例

`examples/` 下有多个示例项目：

- **gstack** — 虚拟工程团队项目走读（brief + medium + deep 三层）
- **superpowers** — AI 流程引擎项目走读（brief + medium + deep 三层）
- **bat** / **zod** / **fastapi** — CLI 工具 / 库 / Web App 的 brief 级别示例

## 准确性机制

核心原则：**verify before write**。通过 12 轮迭代验证建立：

- **Manifest-first**：Phase 3A 先验证所有声明写入 manifest，Phase 3B 只写已验证内容
- **Source citation**：每个代码块必须有 `// Simplified from: path:lines`
- **禁止 `// Source:`**：统一使用 `Simplified from:`（walkthrough 代码总是简化的）
- **不可验证 = 不写入**：无法验证的声明不能出现在 walkthrough 中
- **自动化验证**：`scripts/verify_sources.py` 检查 manifest 完整性和源文件存在性

## 测试

```bash
pytest tests/ -v                    # 185 个测试（结构 + manifest + 引用）
python scripts/verify_sources.py --check-all examples/ --strict  # manifest 验证
```

## 项目结构

```
├── SKILL.md                          # Skill 定义（流程、规范、checklist）
├── docs/
│   ├── html-reference.md             # HTML 模板和 CSS 组件规范
│   ├── documentation-standards.md    # 文档写作和格式规范
│   ├── chapter-templates.md          # 按项目类型的章节模板
│   ├── exploration-protocol.md       # 探索协议
│   ├── sources-manifest-schema.md    # Manifest schema 文档
│   ├── sources-manifest.schema.json  # Manifest JSON Schema
│   ├── accuracy-verification-protocol.md  # 准确性验证协议
│   └── verification-reports/         # 12 轮验证报告
├── scripts/
│   ├── verify_sources.py             # Manifest 验证脚本
│   └── import_graph.py              # 依赖图提取脚本
├── examples/                         # 已生成的走读示例
└── tests/
    └── test_walkthrough_output.py    # 185 个输出验证测试
```
