# my-scripts

- [my-scripts](#my-scripts)
  - [1. 概述](#1-概述)
  - [2. 脚本](#2-脚本)
    - [2.1 Python](#21-python)
    - [2.2 Docker](#22-docker)
    - [2.3 PHP](#23-php)
    - [2.4 Unix](#24-unix)
  - [3. 关键实现](#3-关键实现)
  - [4. 说明](#4-说明)

## 1. 概述

该项目保存一些个人脚本

## 2. 脚本

以实现方式和用途区分

### 2.1 Python

* `./py/BlackHat/` 仿netcat实现
* `./py/php_env.py` 同步执行nginx重启和phpfpm
* `./py/TestUpdateAuditRemark.py` 检查一个项目中的所有的审核页面的“audit_remark”字段是必选项
* `./py/dos2unix.py` 将文本换行符从CRLF转换成LF的脚本

### 2.2 Docker

* `./docker/clean_logs.sh` 批量清楚docker输出日志
* `./docker/command.txt` 几条docker命令

### 2.3 PHP

* `./php/opencaiprocess.php` **swoole**多进程执行实例

### 2.4 Unix

* `./unix/command.txt` Unix下常用命令

## 3. 关键实现

`command.txt` 比较特殊一些，用来记录各种命令

## 4. 说明

暂不是完善，努力改进中
