# 博客


# 使用部署

1.git clone

```shell
git clone git@github.com:ScarecrowFu/AlanHome.git
```

2.安装虚拟环境

```shell
python3 -m venv AlanHome
source AlanHome/bin/activate
pip install -r requirements.txt
```

3.配置 system_configure.ini 文件

```shell
[MYSQL]
MYSQL_DB = alan_home
MYSQL_USER = alan
MYSQL_PASSWORD = PASSWORD
MYSQL_HOST = 127.0.0.1
MYSQL_PORT = 3306

[VERSION_INFO]
serial_number = AlanHome
version = V1
title = 程序员赛道
keywords = 扶妖-程序员赛道
description = 扶妖，程序员赛道, 技术文章，博客，文章，程序，Python, JavaScript, 副业，自媒体，短视频，电商
remark = 程序员赛道，分享各类技术文章，项目，工具，创业方向，以及利用程序解决遇到的问题。
```

4. 创建数据库

```shell
create database alan_home character set utf8;
```

5. 同步数据模型

```shell

```