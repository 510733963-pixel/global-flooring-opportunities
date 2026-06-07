# 开发环境设置指南

## 系统要求

- **Python**: 3.9+
- **Node.js**: 16+
- **Docker & Docker Compose**: (可选，推荐用于数据库)
- **PostgreSQL**: 12+ (如果不使用 Docker)
- **Redis**: 6+ (如果不使用 Docker)
- **Git**: 最新版本

## 快速开始 (推荐 - 使用 Docker)

### 1. 克隆仓库

```bash
git clone https://github.com/510733963-pixel/global-flooring-opportunities.git
cd global-flooring-opportunities
```

### 2. 配置环境变量

```bash
cp .env.example .env
# 根据需要修改 .env 文件
```

### 3. 启动所有服务

```bash
docker-compose up -d
```

此命令会启动：
- PostgreSQL 数据库
- Redis 缓存
- FastAPI 后端服务
- React 前端应用

### 4. 访问应用

- **前端**: http://localhost:3000
- **后端 API**: http://localhost:8000
- **API 文档**: http://localhost:8000/api/docs

## 本地开发设置 (不使用 Docker)

### 后端设置

#### 1. 创建虚拟环境

```bash
cd backend

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

#### 2. 安装依赖

```bash
pip install -r requirements-dev.txt
```

#### 3. 启动开发服务器

```bash
python -m uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
```

访问: http://localhost:8000/api/docs

### 前端设置

#### 1. 安装依赖

```bash
cd frontend
npm install
```

#### 2. 启动开发服务器

```bash
npm run dev
```

访问: http://localhost:3000

## 数据库设置 (本地)

### PostgreSQL 安装

#### macOS (使用 Homebrew)

```bash
brew install postgresql@15
brew services start postgresql@15
```

#### Linux (Ubuntu)

```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo systemctl start postgresql
```

#### Windows

从 https://www.postgresql.org/download/windows/ 下载并安装

### 创建数据库

```bash
# 连接到 PostgreSQL
psql -U postgres

# 创建数据库
CREATE DATABASE flooring_db;

# 创建用户
CREATE USER flooring WITH PASSWORD 'flooring';

# 授予权限
GRANT ALL PRIVILEGES ON DATABASE flooring_db TO flooring;

# 退出
\q
```

### Redis 安装

#### macOS

```bash
brew install redis
brew services start redis
```

#### Linux (Ubuntu)

```bash
sudo apt-get install redis-server
sudo systemctl start redis-server
```

#### Windows

从 https://redis.io/download 下载

### 验证连接

```bash
# PostgreSQL
psql -U flooring -d flooring_db -c "SELECT 1"

# Redis
redis-cli ping
# 应该返回: PONG
```

## 运行测试

### 后端测试

```bash
cd backend

# 运行所有测试
pytest tests/ -v

# 运行特定文件
pytest tests/test_users.py -v

# 运行带代码覆盖率
pytest tests/ -v --cov=src --cov-report=html
```

### 前端测试

```bash
cd frontend

# 运行测试
npm test

# 生成覆盖率报告
npm test -- --coverage
```

## 代码质量检查

### 后端

```bash
cd backend

# 代码格式检查 (Black)
black --check src/

# 自动格式化
black src/

# Lint 检查 (Flake8)
flake8 src/

# 排序导入 (isort)
isort src/

# 类型检查 (mypy)
mypy src/
```

### 前端

```bash
cd frontend

# ESLint 检查
npm run lint

# 自动修复
npm run lint:fix

# Prettier 格式化
npm run format
```

## 项目结构导航

```
global-flooring-opportunities/
├── backend/               # 后端代码
│   ├── src/
│   │   ├── app.py        # 主应用文件
│   │   ├── api/          # API 端点
│   │   └── config/       # 配置
│   ├── tests/            # 测试
│   ├── requirements.txt   # 依赖
│   └── Dockerfile
│
├── frontend/             # 前端代码
│   ├── src/
│   │   ├── App.jsx       # 主组件
│   │   └── index.jsx     # 入口
│   ├── public/           # 静态资源
│   ├── package.json      # 依赖
│   └── Dockerfile
│
├── docs/                 # 文档
├── docker-compose.yml    # Docker 编排
└── .env.example          # 环境变量模板
```

## 常见问题

### Python 虚拟环境问题

重新创建虚拟环境：

```bash
rm -rf venv/
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements-dev.txt
```

### 数据库连接错误

检查 `.env` 文件中的 `DATABASE_URL`：

```
DATABASE_URL=postgresql://flooring:flooring@localhost:5432/flooring_db
```

### 端口被占用

```bash
# 查找占用端口的进程
lsof -i :8000  # 后端
lsof -i :3000  # 前端
lsof -i :5432  # PostgreSQL
lsof -i :6379  # Redis

# 杀死进程
kill -9 <PID>
```

### npm 安装速度慢

使用国内镜像源：

```bash
npm config set registry https://registry.npm.taobao.org

# 或使用 pnpm (更快)
npm install -g pnpm
pnpm install
```

## 下一步

1. 查看 [API.md](API.md) 了解 API 端点
2. 阅读 [ARCHITECTURE.md](ARCHITECTURE.md) 理解项目结构
3. 查看 [CONTRIBUTING.md](../CONTRIBUTING.md) 贡献代码

## 需要帮助？

- 提交 Issue: https://github.com/510733963-pixel/global-flooring-opportunities/issues
- 查看现有讨论
- 阅读项目文档
