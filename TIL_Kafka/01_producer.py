from kafka import KafkaProducer

# 데이터를 보낼 브로커 목록을 정의.
#   브로커가 한개만 있다 하더라도 리스트 형태로 정의하는 것이 좋다.
#   여러 개의 브로커가 띄워진 경우에도 한개의 브로커만 입력해도 연결은 가능하나, 모두 적어주는 것이 좋다.
#   장애 대응을 위해서!
BROKER_SERVERS = ["13.208.235.178:9092"]
TOPIC_NAME = "sample_topic"

# 프로듀서 생성
producer = KafkaProducer(bootstrap_servers=BROKER_SERVERS)
print(producer)

# 메시지를 토픽에 전송
producer.send(TOPIC_NAME, b"Hello Kafka Python")  # 용량을 줄이기 위해 바이트 문자열로 전송 b

# 버퍼 스트림 제거(선택 사항이지만 하는 것이 좋다.)
# 버퍼 스트림을 사용하면 마지막에 찌꺼기가 남는 경우가 생김. 이 경우를 예방하기 위해 사용
producer.flush()
