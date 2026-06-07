# API 文档

全球地坪商机情报中心 RESTful API 参考文档。

## 基础信息

- **基础 URL**: `http://localhost:8000/api`
- **API 文档**: `http://localhost:8000/api/docs` (Swagger UI)
- **认证**: JWT Bearer Token

## 认证

### 用户登录

```bash
POST /users/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}
```

**响应**:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

### 使用令牌

```bash
Authorization: Bearer <your_token>
```

## API 端点

### 商机 (Opportunities)

#### 列表商机

```bash
GET /opportunities?skip=0&limit=10&region=Asia&industry=Construction
```

**查询参数**:
- `skip` (int, default=0): 跳过记录数
- `limit` (int, default=10, max=100): 返回最大数量
- `region` (string, optional): 地区过滤
- `industry` (string, optional): 行业过滤

**响应**:
```json
{
  "total": 1250,
  "skip": 0,
  "limit": 10,
  "data": [
    {
      "id": 1,
      "title": "China Flooring Project",
      "region": "Asia/China",
      "industry": "Construction",
      "description": "Large commercial flooring",
      "budget": 500000,
      "posted_date": "2026-06-01",
      "deadline": "2026-07-01"
    }
  ]
}
```

#### 获取单个商机

```bash
GET /opportunities/{opportunity_id}
```

**响应**:
```json
{
  "id": 1,
  "title": "China Flooring Project",
  "region": "Asia/China",
  "industry": "Construction",
  "description": "Large commercial flooring",
  "budget": 500000,
  "posted_date": "2026-06-01",
  "deadline": "2026-07-01"
}
```

### 用户 (Users)

#### 用户注册

```bash
POST /users/register
Content-Type: application/json

{
  "email": "newuser@example.com",
  "username": "newuser",
  "full_name": "New User",
  "password": "securepassword123"
}
```

#### 获取当前用户

```bash
GET /users/me
Authorization: Bearer <token>
```

### 分析 (Analytics)

#### 获取概览

```bash
GET /analytics/overview
```

**响应**:
```json
{
  "total_opportunities": 1250,
  "total_users": 850,
  "total_revenue": 5420000,
  "last_30_days_growth": 12.5,
  "active_regions": 45,
  "active_industries": 28
}
```

#### 获取趋势数据

```bash
GET /analytics/trends?days=30
```

#### 获取地区分析

```bash
GET /analytics/regions
```

#### 获取行业分析

```bash
GET /analytics/industries
```

### 搜索 (Search)

#### 全文搜索

```bash
GET /search?q=flooring&filter_region=Asia&filter_industry=Construction&sort_by=relevance&limit=10
```

**查询参数**:
- `q` (string, required): 搜索查询
- `filter_region` (string, optional): 地区过滤
- `filter_industry` (string, optional): 行业过滤
- `sort_by` (string, default=relevance): 排序方式 (relevance|date|budget)
- `limit` (int, default=10): 返回结果数

#### 获取搜索建议

```bash
GET /search/suggestions?q=flooring
```

## 错误处理

### 错误响应格式

```json
{
  "detail": "Error message",
  "status": "error"
}
```

### HTTP 状态码

| 状态码 | 含义 | 说明 |
|--------|------|------|
| 200 | OK | 请求成功 |
| 201 | Created | 资源创建成功 |
| 400 | Bad Request | 请求参数错误 |
| 401 | Unauthorized | 未认证 |
| 403 | Forbidden | 无权限 |
| 404 | Not Found | 资源不存在 |
| 429 | Too Many Requests | 请求过于频繁 |
| 500 | Internal Server Error | 服务器内部错误 |

## 限流

默认限流策略：**每分钟100个请求**

超出限制将返回 429 错误。

## 分页

所有列表端点都支持分页：

```bash
GET /opportunities?skip=0&limit=20
```

- `skip`: 起始位置 (默认: 0)
- `limit`: 返回数量 (默认: 10, 最大: 100)

## 交互式文档

访问 http://localhost:8000/api/docs 查看完整的交互式 API 文档 (Swagger UI)。

---

更多详情请查看项目代码中的 docstring 和 [ARCHITECTURE.md](ARCHITECTURE.md)。
