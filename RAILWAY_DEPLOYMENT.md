# Railway部署指南

## 🚀 部署步骤

### 1. 准备GitHub仓库
确保您的代码已经推送到GitHub仓库：`Sebbb320/Agno-Finance-Data-Agent`

### 2. 访问Railway
1. 打开浏览器访问：https://railway.app
2. 使用GitHub账号登录

### 3. 创建新项目
1. 点击 "Start a New Project"
2. 选择 "Deploy from GitHub repo"
3. 选择仓库：`Sebbb320/Agno-Finance-Data-Agent`
4. 点击 "Deploy Now"

### 4. 等待构建
Railway会自动：
- 检测Dockerfile
- 构建Docker镜像
- 部署应用
- 构建过程大约需要2-3分钟

### 5. 配置环境变量
部署完成后，在Railway控制台中：
1. 进入项目设置
2. 找到 "Variables" 标签
3. 添加以下环境变量：

#### 必需的环境变量：
```
OPENAI_API_KEY=your_openai_api_key_here
```

#### 数据库配置（可选，如果不配置会使用内存存储）：
```
DB_HOST=your_db_host
DB_PORT=5432
DB_USER=your_db_user
DB_PASS=your_db_password
DB_DATABASE=your_db_name
```

#### 其他可选环境变量：
```
RUNTIME_ENV=production
MIGRATE_DB=false
```

### 6. 访问应用
部署完成后，Railway会提供一个公网URL，类似：
`https://your-app-name.railway.app`

## 📋 部署检查清单

- [ ] GitHub仓库已更新
- [ ] Dockerfile配置正确
- [ ] requirements.txt包含所有依赖
- [ ] 环境变量已配置
- [ ] 应用可以正常访问

## 🔧 故障排除

### 常见问题

1. **构建失败**
   - 检查Dockerfile语法
   - 确认requirements.txt格式正确
   - 查看Railway构建日志

2. **应用无法启动**
   - 检查环境变量配置
   - 确认端口设置正确
   - 查看应用日志

3. **功能异常**
   - 确认OPENAI_API_KEY已设置
   - 检查网络连接
   - 查看浏览器控制台错误

4. **数据库连接问题**
   - 如果不配置数据库，应用会使用内存存储
   - 如果需要持久化存储，请配置PostgreSQL数据库
   - 可以使用Railway的PostgreSQL插件

## 📞 支持

如果遇到问题，请检查：
1. Railway构建日志
2. 应用运行日志
3. 环境变量配置
4. 网络连接状态 