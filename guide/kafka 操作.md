# Kafka 操作
## 服务状态确认
kafka 的运行要基于 zookeeper，在 docker-compose 文件中，已经写明 zookeer 先于 kafka 启动，这样可以确保 kafka 正常启动，如果 kafka 与 zookeeper运行正常，系统将新开两个端口
```
2181 - zookeeper 的端口
```
```
9092 - kafka 的端口
```
使用以下命令确认上面两个端口是否是 listen 状态

A. linux 或 mac
```
netstat -an | grep 2181
netstat -an | grep 9092
```
B. Windows
```
netstat -an | findstr 2181
netstat -an | findstr 9092
```
## Kafka 基本操作

### 进入容器
#### 首先需要进入容器才能操作 kafka 的命令，运行一下命令进入 kafka 容器

```
docker exec -it <kafka container id 前四位> bash
```
####  进入容器之后，运行以下命令进入 kafka 根目录
```
cd /opt/kafka
```
#### 所有命令集都在 bin/ 中

### topic 操作

#### 查看现有 topic 
```
bin/kafka-topics.sh --list \
                  --bootstrap-server localhost:9092     # 即 kafka 的服务器名与端口
```

#### 创建 topic
```
bin/kafka-topics.sh --create \
                    --bootstrap-server localhost:9092 \
                    --topic <topic 名> \
                    --partitions <分区数量> \
                    --replication-factor <在多少个 broker 上进行备份>
```

#### 查看 topic 的描述信息
```
bin/kafka-topics.sh --describe \
                  --bootstrap-server localhost:9092
```

### 制造数据
```
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 \
                              --topic <topic 名>
```

### 消费数据

```
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 \
                              --topic <topic 名>
```