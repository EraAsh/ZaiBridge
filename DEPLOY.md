# ZaiBridge Docker 部署指南

## 快速部署

### 1. 克隆项目
```bash
git clone https://github.com/EraAsh/zai2api.git
cd zai2api
```

### 2. 配置环境变量
```bash
cp .env.example .env
# 编辑 .env 文件，修改 SECRET_KEY 等配置
```

### 3. 启动服务
```bash
docker-compose up -d
```

### 4. 访问服务
- Web 管理界面：http://localhost:5000
- 默认账号：admin / admin

## 生产环境部署

### 使用环境变量配置
```bash
docker-compose up -d \
  -e SECRET_KEY=your-production-secret-key \
  -e TOKEN_REFRESH_INTERVAL=3600 \
  -e PROXY_ENABLED=false
```

### 查看日志
```bash
docker-compose logs -f zaibridge
```

### 停止服务
```bash
docker-compose down
```

## 功能验证

### 1. 添加 Discord Token
- 登录管理界面
- 点击"新增 Token"
- 输入 Discord Token
- 系统自动获取 zai.is Token 和 darkknight 值

### 2. 测试 API 调用
```bash
curl -X POST http://localhost:5000/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4","messages":[{"role":"user","content":"Hello"}]}'
```

### 3. 查看 Token 状态
- 在管理界面查看 Token 列表
- 检查 zai_token 和 zai_darkknight 值
- 查看过期时间和状态

## 故障排除

### 服务无法启动
```bash
# 查看日志
docker-compose logs zaibridge

# 检查端口占用
netstat -tlnp | grep 5000
```

### Token 刷新失败
1. 检查 Discord Token 是否有效
2. 检查网络连接
3. 查看日志中的错误信息

### API 调用失败
1. 检查 API Key 是否正确
2. 检查 Token 是否有效
3. 查看请求日志

## 更新项目
```bash
git pull origin main
docker-compose up -d --build
```

## 备份数据
```bash
# 备份数据库
docker cp zaibridge:/app/instance/zai2api.db ./backup/

# 恢复数据库
docker cp ./backup/zai2api.db zaibridge:/app/instance/