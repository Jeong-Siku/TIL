from kafka import KafkaProducer

# 브로커 목록을 정의
#  브로커가 한개만 있다 하더라도 리스트 형태로 정의하는 것이 좋다.
#  여러 개의 브로커가 띄워진 경우에도 한 개의 브로커만 입력해도 연결은 가능하나, 모두 적어주는 것이 좋다.
BROKER_SERVERS = ["15.152.234.229:9092"]
TOPIC_NAME = "sample_topic"

# 프로듀서 생성
producer = KafkaProducer(bootstrap_servers=BROKER_SERVERS)

# 메시지를 토픽에 전송
producer.send(TOPIC_NAME, b'Hello Kafka Python')

# 버퍼 스트림 제거(선택 사항이지만 하는 것이 좋다.)
producer.flush()