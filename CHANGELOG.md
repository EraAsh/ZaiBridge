# ZaiBridge 更新日志

**作者**: EraAsh

## [2.0.0] - 2026-01-02

### 新增功能 ✨

- **完整支持 x-zai-darkknight 请求头**
  - 在 OAuth 登录流程中自动提取 `x-zai-darkknight` 值
  - 在所有 API 调用中自动添加 `x-zai-darkknight` 请求头
  - 支持从响应头、JSON 响应和 HTML 中提取 darkknight 值

- **代码混淆保护模块**
  - 新增 `obfuscator.py` 模块
  - 字符串混淆：使用 base64 + XOR 混淆敏感字符串
  - Token 脱敏：所有 token 在日志中自动脱敏显示
  - 哈希保护：敏感数据的哈希值用于日志记录

### 修复问题 🐛

- **修复 x-zai-darkknight 验证问题**
  - 之前版本因缺少 `x-zai-darkknight` 请求头导致 API 调用失败
  - 现已完整支持该验证机制

- **增强 Discord Token 认证**
  - 改进 OAuth 登录流程
  - 优化错误处理和重试机制
  - 添加更详细的日志输出

### 数据库变更 📊

- **Token 模型新增字段**
  - `zai_darkknight`: 存储 x-zai-darkknight 请求头的值
  - 自动迁移现有数据库，无需手动操作

### 安全性增强 🔒

- **敏感信息保护**
  - 所有 API 端点使用混淆字符串
  - 请求头名称使用混淆
  - Token 在日志中自动脱敏
  - Cookie 名称使用混淆

### 文档更新 📝

- 更新 README.md，添加详细的使用说明
- 添加技术实现说明
- 添加常见问题解答
- 添加数据库结构说明

### 改进 🚀

- 优化 token 刷新逻辑
- 改进错误处理和日志记录
- 增强代码可维护性
- 提升整体稳定性

## [1.0.0] - 初始版本

### 功能特性

- 多 Token 管理
- 自动保活
- OpenAI 兼容接口
- 负载均衡
- WebUI 管理面板
- Docker 部署支持