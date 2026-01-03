# ZaiBridge 部署指南

**作者**: EraAsh

## 环境要求

- Python 3.10+
- Docker 和 Docker Compose（可选）
- 至少 512MB 内存
- 至少 1GB 磁盘空间

## 安装步骤

### 方式一：Docker Compose 部署（推荐）

1. **克隆项目**

```bash
git clone https://github.com/EraAsh/zai-bridge.git
cd zai-bridge
```

2. **配置环境变量**（可选）

编辑 `docker-compose.yml`，根据需要修改环境变量：

```yaml
environment:
  - DATABASE_URI=sqlite:////app/instance/zai2api.db
  - SECRET_KEY=your-secret-key-change-me
  - TZ=Asia/Shanghai
```

3. **启动服务**

```bash
docker-compose up -d
```

4. **访问管理面板**

打开浏览器访问：`http://localhost:5000`

默认账号：`admin`
默认密码：`admin`

**重要**：首次登录后请立即修改密码！

### 方式二：源码部署

1. **克隆项目**

```bash
git clone https://github.com/EraAsh/zai-bridge.git
cd zai-bridge
```

2. **安装依赖**

```bash
pip install -r requirements.txt
```

3. **启动服务**

```bash
python app.py
```

4. **访问管理面板**

打开浏览器访问：`http://localhost:5000`

## 配置说明

### 环境变量

| 变量名 | 默认值 | 说明 |
|--------|--------|------|
| `DATABASE_URI` | `sqlite:///zai2api.db` | 数据库连接字符串 |
| `SECRET_KEY` | `your-secret-key-change-me` | Flask Session 密钥，**必须修改** |
| `TZ` | `Asia/Shanghai` | 时区设置 |

### 管理面板配置

登录管理面板后，可以在"系统配置"中修改以下设置：

1. **错误封禁阈值**：Token 错误多少次后自动禁用
2. **错误重试次数**：API 请求失败时的重试次数
3. **Token 刷新间隔**：自动刷新 Token 的时间间隔（秒）
4. **代理设置**：配置 HTTP/HTTPS 代理
5. **流式转换**：是否将流式响应转换为非流式

## 使用指南

### 1. 添加 Discord Token

1. 登录管理面板
2. 点击"新增 Token"
3. 输入 Discord Token
4. 点击"保存"

系统会自动：
- 使用 Discord Token 进行 OAuth 登录
- 提取 JWT Token
- 提取 x-zai-darkknight 值
- 获取用户信息

### 2. 刷新 Token

- **单个刷新**：在 Token 列表中点击"刷新"按钮
- **批量刷新**：点击"一键刷新 ZaiToken"按钮

### 3. 配置 API Key

1. 在管理面板中进入"系统配置"
2. 找到"API Key"设置
3. 修改为你的自定义 API Key
4. 保存

### 4. 调用 API

使用标准的 OpenAI API 格式调用：

```bash
curl -X POST http://localhost:5000/v1/chat/completions \
  -H "Authorization: Bearer your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## 轻量级版本使用

如果你只需要"自动刷新 Discord Token 并推送到 NewAPI"的功能，可以使用轻量级版本：

1. 进入轻量级版本目录：

```bash
cd 自动刷新token推送到newapi
```

2. 编辑配置文件 `config.json`：

```json
{
  "discord_tokens": [
    "your_discord_token_1",
    "your_discord_token_2"
  ],
  "zai_url": "https://zai.is",
  "newapi_base": "https://your-newapi-url.com",
  "newapi_key": "your-newapi-key",
  "newapi_channel_id": "1",
  "expires_in": 3600,
  "update_interval": 3600
}
```

3. 运行：

```bash
python zai_token.py run-loop --config config.json
```

## 故障排查

### 问题 1：Token 刷新失败

**可能原因**：
- Discord Token 无效或已过期
- 网络连接问题
- zai.is 服务异常

**解决方法**：
1. 检查 Discord Token 是否正确
2. 检查网络连接
3. 查看日志中的详细错误信息
4. 尝试配置代理

### 问题 2：API 调用返回 401

**可能原因**：
- API Key 错误
- Token 已过期

**解决方法**：
1. 检查 API Key 是否正确
2. 刷新 Token
3. 检查 Token 是否已启用

### 问题 3：darkknight 值为空

**可能原因**：
- OAuth 登录流程中未能提取到 darkknight 值
- zai.is 更改了验证机制

**解决方法**：
1. 重新刷新 Token
2. 检查日志中的提取过程
3. 如果持续失败，请提交 Issue

### 问题 4：数据库迁移失败

**可能原因**：
- 数据库文件权限问题
- 数据库文件损坏

**解决方法**：
1. 检查数据库文件权限
2. 备份数据库文件
3. 删除数据库文件，让系统重新创建

## 安全建议

1. **修改默认密码**：首次登录后立即修改管理员密码
2. **使用强密码**：使用复杂的密码保护管理面板
3. **配置 HTTPS**：在生产环境中使用 HTTPS
4. **定期备份**：定期备份数据库文件
5. **限制访问**：使用防火墙限制管理面板的访问
6. **更新代码**：定期更新到最新版本

## 性能优化

1. **调整刷新间隔**：根据实际需求调整 Token 刷新间隔
2. **使用代理**：如果网络不稳定，配置代理可以提高稳定性
3. **负载均衡**：添加多个 Token 可以提高并发处理能力
4. **数据库优化**：对于大量 Token，考虑使用 MySQL 或 PostgreSQL

## 监控和日志

### 查看日志

- **Docker 部署**：

```bash
docker-compose logs -f
```

- **源码部署**：日志会直接输出到控制台

### 请求日志

在管理面板的"请求日志"中可以查看：
- API 调用记录
- 使用的 Token
- 响应状态码
- 请求耗时

## 更新升级

### Docker 部署

```bash
git pull
docker-compose down
docker-compose up -d --build
```

### 源码部署

```bash
git pull
pip install -r requirements.txt --upgrade
python app.py
```

## 支持

如果遇到问题，请：

1. 查看本文档的故障排查部分
2. 查看 GitHub Issues
3. 提交新的 Issue，包含：
   - 问题描述
   - 错误日志
   - 环境信息
   - 复现步骤