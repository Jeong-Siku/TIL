from kafka import KafkaConsumer

BROKER_SERVERS = ["13.208.235.178:9092"]
TOPIC_NAME = "sample_topic"

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=BROKER_SERVERS)

# Consumer는 파이썬의 Generator로 구현됨. next 실행 전까지는 block 상태
print("Wait...")

# 컨슈머는 항상 LISTEN(대기) 상태. Generator와 같이 topic에 정보가 들어오기 전까지 block 상태
for message in consumer:  # topic에 정보가 들어오면 실행한다.
    print(message)

print("Done...")  # 종료하기 전까지 이 부분은 뜨지 않는다.
