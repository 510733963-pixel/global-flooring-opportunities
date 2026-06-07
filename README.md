# 全球地坪商机情报中心

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![React](https://img.shields.io/badge/react-18+-blue.svg)

**全球地坪商机情报中心** - 采集、分析和展示全球地坪行业商机的智能平台

## 📋 项目概述

全球地坪商机情报中心是一个综合性的商业情报平台，致力于为地坪行业专业人士提供：

- 🌍 **全球商机采集** - 自动爬取全球地坪行业商机信息
- 📊 **数据分析** - 智能分析商机趋势和市场热点
- 🗺️ **地图可视化** - 全球商机分布展示
- 🔔 **实时推送** - 感兴趣商机即时通知
- 📈 **报告生成** - 专业商机分析报告下载

## 🏗️ 项目架构

```
global-flooring-opportunities/
├── backend/           # Python FastAPI 后端
├── frontend/          # React 前端应用
├── database/          # 数据库配置和迁移
├── docker/            # Docker 容器配置
├── docs/              # 项目文档
└── scripts/           # 初始化脚本
```

## 🚀 快速开始

### 前置要求

- Python 3.9+
- Node.js 16+
- Docker & Docker Compose
- PostgreSQL 12+
- Redis 6+

### 安装步骤

#### 1. 克隆仓库

```bash
git clone https://github.com/510733963-pixel/global-flooring-opportunities.git
cd global-flooring-opportunities
```

#### 2. 启动 Docker 容器

```bash
docker-compose up -d
```

#### 3. 初始化数据库

```bash
python scripts/init_db.py
python scripts/seed_data.py
```

#### 4. 启动后端服务

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
```

#### 5. 启动前端应用

```bash
cd frontend
npm install
npm start
```

访问: http://localhost:3000

## 📚 文档

- [API 文档](docs/API.md) - RESTful API 端点详解
- [架构设计](docs/ARCHITECTURE.md) - 项目架构说明
- [安装指南](docs/SETUP.md) - 详细安装步骤
- [部署指南](docs/DEPLOYMENT.md) - 生产环境部署
- [数据库](docs/DATABASE.md) - 数据库设计文档

## 🛠️ 技术栈

### 后端
- **框架**: FastAPI 0.104+
- **数���库**: PostgreSQL 12+
- **缓存**: Redis 6+
- **ORM**: SQLAlchemy 2.0+
- **任务队列**: Celery
- **爬虫**: BeautifulSoup4, Scrapy

### 前端
- **框架**: React 18+
- **状态管理**: Redux Toolkit
- **UI库**: Material-UI v5
- **地图**: Leaflet
- **图表**: ECharts
- **构建**: Vite

### DevOps
- **容器**: Docker & Docker Compose
- **CI/CD**: GitHub Actions
- **反向代理**: Nginx
- **日志**: ELK Stack (可选)

## 📦 核心功能

### 1. 商机采集模块
- 定时爬取全球地坪行业信息
- 支持多个数据源
- 智能去重和数据清洗

### 2. 数据分析模块
- 商机趋势分析
- 热门地区和行业分析
- 市场洞察生成

### 3. 搜索和过滤
- 全文搜索功能
- 多维度过滤（地区、行业、时间等）
- 排序和分页

### 4. 用户系统
- 用户注册和登录
- 个人中心管理
- 权限控制

### 5. 订阅通知
- 感兴趣商机订阅
- 实时推送通知
- 邮件提醒

### 6. 数据可视化
- 全球商机分布地图
- 趋势图表
- 热力图

## 🔧 环境变量配置

复制 `.env.example` 文件为 `.env`，填入必要的配置：

```bash
cp .env.example .env
```

## 📝 贡献指南

欢迎提交 Issue 和 Pull Request！请参考 [CONTRIBUTING.md](CONTRIBUTING.md)

### 开发流程

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 👥 联系方式

- 项目主页: https://github.com/510733963-pixel/global-flooring-opportunities
- 提交 Issue: https://github.com/510733963-pixel/global-flooring-opportunities/issues

## 🙏 致谢

感谢所有贡献者和使用者的支持！

---

**最后更新**: 2026-06-07
