sleep 1

echo
echo start add topics
echo
#/opt/kafka/bin/kafka-topics.sh --create --topic $TOPIC_NAME --partitions $PARTITIONS --replication-factor $REPLICATION_FACTOR --bootstrap-server kafka:9092

docker compose exec kafka kafka-topics --create --topic auth --bootstrap-server localhost:19092 --partitions 5 --replication-factor 1 &

sleep 1
echo
echo Huesos_kafka
echo finish add topics
echo
sleep 1