# 贡献指南

感谢你对 **全球地坪商机情报中心** 的关注！我们欢迎所有形式的贡献。

## 行为准则

请遵循以下基本原则：
- 尊重所有贡献者
- 接受建设性的批评
- 专注于对项目最有利的工作

## 如何贡献

### 报告 Bug

如果发现 Bug，请创建一个 GitHub Issue，包含以下信息：

- **清晰的标题** - 简洁描述问题
- **详细的描述** - 问题的详细说明
- **重现步骤** - 如何重现这个问题
- **预期行为** - 应该发生什么
- **实际行为** - 实际发生了什么
- **环境信息** - Python版本、操作系统等
- **截图/日志** - 如果相关

### 提议新功能

如果有好的功能想法：

1. 创建一个 GitHub Issue，使用 "Feature Request" 模板
2. 清楚地描述该功能的价值
3. 提供尽可能多的细节和示例
4. 等待维护者的反馈

### 提交代码

#### 1. Fork 项目

```bash
git clone https://github.com/510733963-pixel/global-flooring-opportunities.git
cd global-flooring-opportunities
```

#### 2. 创建功能分支

```bash
git checkout -b feature/your-feature-name
# 或
git checkout -b fix/your-fix-name
```

分支命名规范：
- `feature/` - 新功能
- `fix/` - Bug 修复
- `docs/` - 文档更新
- `refactor/` - 代码重构
- `test/` - 测试相关
- `chore/` - 杂项任务

#### 3. 提交更改

遵循 Commit Message 规范：

```bash
git commit -m "type: subject

body

footer"
```

**类型 (Type):**
- `feat` - 新功能
- `fix` - Bug 修复
- `docs` - 文档
- `style` - 代码风格
- `refactor` - 代码重构
- `perf` - 性能优化
- `test` - 测试
- `chore` - 构建、依赖等

#### 4. 推送到 Fork

```bash
git push origin feature/your-feature-name
```

#### 5. 创建 Pull Request

- 创建 PR 到 `main` 分支
- 使用明确的标题
- 提供更改的详细说明
- 确保通过了所有检查

## 代码风格

### Python (PEP 8)

```bash
black backend/
flake8 backend/
isort backend/
```

### JavaScript/React (Airbnb)

```bash
npm run lint
npm run lint:fix
npm run format
```

## 测试

提交代码前，请确保通过所有测试：

```bash
# 后端
cd backend && pytest tests/ -v --cov=src

# 前端
cd frontend && npm test -- --coverage
```

## 许可证

通过贡献代码，你同意你的贡献在 MIT 许可证下发布。

感谢你的贡献！🎉
