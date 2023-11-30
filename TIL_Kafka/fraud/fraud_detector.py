# payment_producer에서 데이터를 Consume
# 정상 데이터 -> legit_processor로 프로듀싱
# 이상 데이터 -> fraud_processor로 프로듀싱

from kafka import KafkaConsumer, KafkaProducer
import json

PAYMENT_TOPIC = "payments"
FRAUD_TOPIC = "fraud_payments"
LEGIT_TOPIC = "legit_payments"

BROKERS = ["15.152.234.229:9092"]

consumer = KafkaConsumer(PAYMENT_TOPIC, bootstrap_servers=BROKERS)
producer = KafkaProducer(bootstrap_servers=BROKERS)

# 이상 결제 기준 정의
def _is_suspicious(message):
    # stranger가 결제 or 결제금액이 500만원 이상.. 기준은 여러분들 마음대로..
    #  message를 feature로 받는 머신러닝 모델의 predict
    if message["TO"] == 'stranger' or message["AMOUNT"] >= 5000000:
        return True
    else:
        return False

for message in consumer:
    # json.loads -> Byte JSON을 문자열 JSON으로
    msg = json.loads(message.value.decode())

    if _is_suspicious(msg):
        producer.send(FRAUD_TOPIC, json.dumps(msg).encode("utf-8"))
    else:
        producer.send(LEGIT_TOPIC, json.dumps(msg).encode("utf-8"))
    
    producer.flush()
    print(_is_suspicious(msg), msg["TO"], msg["AMOUNT"])