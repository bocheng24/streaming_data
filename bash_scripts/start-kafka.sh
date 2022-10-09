export KAFKA_HOME=~/data-apps/kafka
export PATH=$KAFKA_HOME/bin:$PATH

# Start Zookeeper
zookeeper-server-start.sh -daemon $KAFKA_HOME/config/zookeeper.properties

# Start Broker
kafka-server-start.sh -daemon $KAFKA_HOME/config/server.properties
