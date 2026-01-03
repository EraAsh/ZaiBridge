# ZaiBridge 快速开始指南

## 项目简介

ZaiBridge 是一个 Discord Token 转 zai.is API Token 的自动化网关服务。

**作者**: EraAsh

## 核心功能

✅ **自动转换**：输入 Discord Token，自动获取 zai.is 的 API Token  
✅ **完整支持**：支持 zai.is 的 `x-zai-darkknight` 请求头验证  
✅ **自动刷新**：Token 过期前自动刷新  
✅ **负载均衡**：多个 Token 自动轮询使用  
✅ **OpenAI 兼容**：提供标准的 `/v1/chat/completions` 和 `/v1/models` 接口  
✅ **WebUI 管理**：可视化的管理面板  

## 5 分钟快速部署

### 方式一：Docker 部署（推荐）

```bash
# 1. 克隆项目
git clone https://github.com/EraAsh/zai-bridge.git
cd zai-bridge

# 2. 启动服务
docker-compose up -d

# 3. 访问管理面板
# 浏览器打开: http://localhost:5000
# 默认账号: admin
# 默认密码: admin
```

### 方式二：源码部署

```bash
# 1. 克隆项目
git clone https://github.com/EraAsh/zai-bridge.git
cd zai-bridge

# 2. 安装依赖
pip install -r requirements.txt

# 3. 启动服务
python app.py

# 4. 访问管理面板
# 浏览器打开: http://localhost:5000
# 默认账号: admin
# 默认密码: admin
```

## 获取 Discord Token

### 方法一：浏览器开发者工具（推荐）

1. 打开 Discord 网页版或客户端
2. 按 `F12` 打开开发者工具
3. 切换到 `Network`（网络）标签
4. 在任意群组发送一条消息
5. 在网络请求中找到该消息的请求
6. 在 `Request Headers`（请求标头）中找到 `Authorization` 字段
7. 复制该值（格式类似：`MTE...`）

### 方法二：Discord 客户端

1. 打开 Discord 客户端
2. 按 `Ctrl+Shift+I`（Windows）或 `Cmd+Option+I`（Mac）打开开发者工具
3. 按照上述方法获取 Token

## 添加 Token

1. 登录管理面板（http://localhost:5000）
2. 点击"新增 Token"按钮
3. 粘贴 Discord Token
4. （可选）填写备注信息
5. 点击"添加"

系统将自动：
- 使用 Discord Token 登录 zai.is
- 提取 API Token
- 提取 x-zai-darkknight 值
- 显示 Token 状态

## 调用 API

### 示例 1：聊天补全

```bash
curl -X POST http://localhost:5000/v1/chat/completions \
  -H "Authorization: Bearer your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {"role": "user", "content": "你好！"}
    ]
  }'
```

### 示例 2：获取模型列表

```bash
curl http://localhost:5000/v1/models \
  -H "Authorization: Bearer your-api-key"
```

### 示例 3：Python 调用

```python
import requests

url = "http://localhost:5000/v1/chat/completions"
headers = {
    "Authorization": "Bearer your-api-key",
    "Content-Type": "application/json"
}
data = {
    "model": "gpt-4",
    "messages": [
        {"role": "user", "content": "你好！"}
    ]
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

## 配置 API Key

1. 登录管理面板
2. 切换到"系统配置"标签
3. 找到"API 密钥配置"
4. 输入新的 API Key
5. 点击"更新 API Key"

## 管理 Token

### 查看状态
- 在 Token 列表中查看每个 Token 的状态
- 查看剩余刷新时间
- 查看错误次数

### 刷新 Token
- **单个刷新**：点击 Token 行的"更新"按钮
- **批量刷新**：点击"一键刷新 ZaiToken"按钮

### 启用/禁用 Token
- 点击 Token 行的"启用"或"禁用"按钮

### 删除 Token
- 点击 Token 行的"删除"按钮

## 常见问题

### Q: Token 刷新失败怎么办？

A: 请检查：
1. Discord Token 是否有效
2. 网络连接是否正常
3. 是否需要配置代理
4. 查看 Token 列表中的错误信息

### Q: 如何提高稳定性？

A: 建议：
1. 添加多个 Discord Token
2. 设置合理的刷新间隔
3. 配置错误重试次数
4. 使用代理（如果网络不稳定）

### Q: API 调用返回 401？

A: 请检查：
1. API Key 是否正确
2. Token 是否已启用
3. Token 是否已过期

### Q: 如何查看日志？

A: 在管理面板的"请求日志"标签中查看所有 API 调用记录。

## 安全建议

1. **修改默认密码**：首次登录后立即修改管理员密码
2. **使用强密码**：使用复杂的密码保护管理面板
3. **定期更换 Token**：定期更换 Discord Token
4. **配置 HTTPS**：在生产环境中使用 HTTPS
5. **限制访问**：使用防火墙限制管理面板的访问

## 技术支持

- GitHub: https://github.com/EraAsh/zai-bridge
- Issues: https://github.com/EraAsh/zai-bridge/issues

## 免责声明

本项目仅供学习和研究使用。使用者应自行承担使用本工具产生的所有风险和责任。请遵守相关服务条款。