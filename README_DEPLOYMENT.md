# Agno Finance App 公网部署指南

## 🎯 部署目标
将本地Finance Agent应用部署到公网，供领导和团队访问使用。

## 📋 部署选项

### 选项1：云服务器部署（推荐）

#### 1.1 购买云服务器
- **阿里云/腾讯云/AWS** - 选择2核4G以上配置
- **操作系统**: Ubuntu 20.04 LTS
- **带宽**: 至少5Mbps

#### 1.2 服务器配置
```bash
# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# 安装Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

#### 1.3 部署应用
```bash
# 上传代码到服务器
git clone <your-repo-url>
cd agent-app-aws-main

# 设置环境变量
export OPENAI_API_KEY=your_api_key_here

# 运行部署脚本
chmod +x deploy.sh
./deploy.sh
```

### 选项2：Railway部署（简单快速）

#### 2.1 注册Railway账号
- 访问 https://railway.app
- 使用GitHub账号注册

#### 2.2 连接GitHub仓库
- 在Railway中创建新项目
- 选择GitHub仓库
- 设置环境变量：`OPENAI_API_KEY`

#### 2.3 自动部署
- Railway会自动检测Dockerfile
- 自动构建和部署应用
- 提供公网访问地址

### 选项3：Render部署

#### 3.1 注册Render账号
- 访问 https://render.com
- 使用GitHub账号注册

#### 3.2 创建Web Service
- 选择GitHub仓库
- 设置构建命令：`pip install -r requirements.txt`
- 设置启动命令：`streamlit run ui/Home.py --server.port=$PORT --server.address=0.0.0.0`
- 设置环境变量：`OPENAI_API_KEY`

## 🔧 环境变量配置

### 必需环境变量
```bash
OPENAI_API_KEY=sk-proj-your-api-key-here
```

### 可选环境变量
```bash
# 应用配置
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0

# 代理设置（如果需要）
HTTP_PROXY=http://your-proxy:port
HTTPS_PROXY=http://your-proxy:port
```

## 🌐 域名和SSL配置

### 域名配置
1. 购买域名（如：agno-finance.com）
2. 在DNS提供商处添加A记录
3. 指向服务器IP地址

### SSL证书配置
```bash
# 使用Let's Encrypt免费SSL证书
sudo apt install certbot
sudo certbot --nginx -d your-domain.com
```

## 📊 监控和维护

### 日志查看
```bash
# Docker容器日志
docker logs agno-app

# 实时日志
docker logs -f agno-app
```

### 应用重启
```bash
# 重启容器
docker restart agno-app

# 重新部署
docker stop agno-app
docker rm agno-app
./deploy.sh
```

### 性能监控
- 使用htop监控服务器资源
- 设置日志轮转防止磁盘满
- 配置监控告警

## 🔒 安全配置

### 防火墙设置
```bash
# 只开放必要端口
sudo ufw allow 22    # SSH
sudo ufw allow 80    # HTTP
sudo ufw allow 443   # HTTPS
sudo ufw enable
```

### 访问控制
- 设置强密码
- 禁用root登录
- 使用SSH密钥认证

## 💰 成本估算

### 云服务器（月费用）
- **阿里云**: 2核4G ≈ 100元/月
- **腾讯云**: 2核4G ≈ 80元/月
- **AWS**: t3.medium ≈ 150元/月

### 域名费用
- 域名注册：50-100元/年
- SSL证书：免费（Let's Encrypt）

## 🚀 快速部署命令

```bash
# 一键部署到云服务器
wget -O - https://raw.githubusercontent.com/your-repo/deploy.sh | bash

# 或者使用Docker Compose
docker-compose up -d
```

## 📞 技术支持

如果遇到部署问题，请检查：
1. 环境变量是否正确设置
2. 网络连接是否正常
3. 服务器资源是否充足
4. 防火墙是否开放端口

---

**部署完成后，你的领导就可以通过公网地址访问Finance Agent了！** 🎉 