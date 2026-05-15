# TODO — 待办事项

## 已完成

### 准确性机制（12 轮验证，Round 10-12 连续零问题）
- [x] Manifest-first Phase 3（3A 验证 → 3B 写作 → 3C 校验）
- [x] 禁用 `// Source:`，统一 `// Simplified from:`
- [x] sources-manifest.json schema + verify_sources.py 脚本
- [x] 185 个测试覆盖结构 + manifest + 引用
- [x] import_graph.py 依赖图提取脚本

### 机制修复（2026-05-09，基于架构/模块/代码 review）
- [x] SKILL.md 准确性规则去重（3 处 → 1 处权威来源 + 引用）
- [x] Schema 支持 Phase 3A 中间态（doc_file/doc_line optional）
- [x] verify_sources.py：claim ID 校验、文件句柄修复、--strict 模式
- [x] import_graph.py：Python/Rust/TS 解析缺口修复
- [x] test_walkthrough_output.py：HTML 自包含逻辑、xfail、schema 对齐
- [x] schema.md 与 schema.json 对齐
- [x] README.md 更新到当前状态
- [x] exploration-protocol.md：Serena 工具标注、chapter template 引用

### 多语言 + 插件化（2026-05-15）
- [x] `--lang zh|en` 参数，默认 `zh`（中文正文 + 英文术语）
- [x] documentation-standards.md 重写：区分 `zh` / `en` 写作规范
- [x] `.claude-plugin/plugin.json` + `marketplace.json`（Claude Code 插件化）
- [x] SKILL.md 迁移到 `skills/project-walkthrough/` 标准目录
- [x] README.md 多平台安装说明 + 新参数文档
- [x] `en` 模式下的英文类比卡片（Analogy cards）

### 历史完成项
- [x] 现有 example walkthrough 已添加 Simplified from: 引用
- [x] HTML innerHTML 问题（已 assert，无违规）
- [x] chapter-templates.md deep 级别 source citation 要求
- [x] v1 版本兼容测试
- [x] SKILL.md 参数设计从位置参数迁移到 --flag 约定
- [x] 8 轮独立 review + 修复（连续 3 轮 clean 收工）
- [x] 扩展全项目 review（16+ 文件，连续 3 轮 clean）
- [x] verify_sources.py 单元测试（59 tests）
- [x] import_graph.py 单元测试（46 tests）
- [x] 总测试数 185 → 290，全部通过

## 待办

### 近期
- [ ] 端到端验证：用更新后的 skill 对新项目生成 walkthrough，确认 `--lang zh` 和 `--lang en` 模式都正常工作
- [ ] GitHub 仓库重命名：`research_project-walkthrough` → `project-walkthrough-skill`
- [ ] 在 Claude Code marketplace 上注册并测试安装流程
- [ ] 更新测试中的路径引用（SKILL.md 新位置）

### 未来可考虑
- [ ] Cursor 插件支持：生成 `.cursor/rules/` 的 `.mdc` 文件
- [ ] Gemini CLI 一键安装支持：确保 `gemini skills install <url>` 可用
- [ ] OpenCode / Windsurf 兼容性测试
- [ ] gstack/superpowers 的 manifest 验证（当前 MANIFEST_PROJECTS 硬编码排除）
- [ ] 更多项目类型模板（游戏引擎、数据库、编译器等）
- [ ] `convert.sh` 跨平台转换脚本（如果用户量增长到值得维护）
