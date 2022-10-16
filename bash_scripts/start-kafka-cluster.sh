~/data-apps/kafka/bin/zookeeper-server-start.sh -daemon ~/data-apps/kafka/config/zookeeper.properties
~/data-apps/kafka/bin/kafka-server-start.sh -daemon ~/data-apps/kafka/config/server.properties
~/data-apps/kafka-bk1/bin/kafka-server-start.sh -daemon ~/data-apps/kafka-bk1/config/server.properties
~/data-apps/kafka-bk2/bin/kafka-server-start.sh -daemon ~/data-apps/kafka-bk2/config/server.properties