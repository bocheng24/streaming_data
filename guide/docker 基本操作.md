# Kafka 与 Spark Streaming
## 本项目使用 docker 容器环境搭建与代码测试，所有使用到的镜像都记录在 docker-compose.yml 中
### 在 docker-compose 文件中，用到了以下几个镜像文件
1. wurstmeister/zookeeper
1. wurstmeister/kafka
1. jupyter/all-spark-notebook
1. postgres
### 使用以下命令启动所有容器
* 由于添加 -d 参数，启动完成后，所有的镜像将以容器的形式在后台运行
* 去掉 -d 参数，容器将在前台运行
```
docker-compose up -d
```
### 运行以下命令查看是否所有的服务都运行起来
```
docker ps
```
命令输出主要关注container id，这个值在每一次重新启动后，会随机生成新的值

### 查看服务日志
如果是后台运行，需要使用以下命令查看
```
docker logs <container id 前四位>
```
通过这个命令可以查看所有的服务是否运行正常

### 关闭所有容器
#### 1. 如果是在前端运行，则使用 ctrl + c 关闭
注：这种方式会停止服务，但是容器还是会在后台保留，可以通过以下命令查看
```
docker ps -a
```
如果想将容器删除节省系统资源，需要运行以下命令
```
docker rm <container1 id 前四位> <container2 id 前四位> <container3 id 前四位> ...
```
#### 2. 如果是在后台运行，则可以使用以下命令，这个命令会自动将容器也删除
```
docker-compose down
```


