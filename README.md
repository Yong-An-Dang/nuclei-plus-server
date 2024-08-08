# nuclei-plus-server

nuclei-plus辅助服务

> demo程序，简单粗暴的实现

## 功能

### TODO

- [x] 模板同步接口
- [x] 模板生成接口

### LLM

```shell
# %pip install langchain
# %pip install langchain-openai
# %pip install langchain-together
```

### 构建

```shell
# 安装构建工具
pip install poetry

# 修改版本号：`vi version.py`
__version__ = "1.0.0"

# 构建
poetry build
```

## 快速起步

### 安装配置

```shell
# 1. 源码安装
git clonehttps://github.com/Yong-An-Dang/nuclei-plus-server.git
cd nuclei-plus-server
pip install .

# 2. 生成配置
nuclei-plus-server config
# 或 指定参数生成配置
nuclei-plus-server config --config -u https://api.together.xyz/v1 -k xxxxxxxx -m Qwen/Qwen2-72B-Instruct

# 3. 手动修改配置
vim /path/to/config.yaml
```

### 运行服务

```shell
nuclei-plus-server start
```

### 查看当前版本

```shell
nuclei-plus-server version
```
