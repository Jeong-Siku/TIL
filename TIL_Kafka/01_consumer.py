from kafka import KafkaConsumer

BROKER_SERVERS = ["15.152.234.229:9092"]
TOPIC_NAME = "sample_topic"

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=BROKER_SERVERS)

# Consumer는 파이썬의 Generator로 구현됨
print("Wait....")

for message in consumer:
    print(message)

print("Done....")