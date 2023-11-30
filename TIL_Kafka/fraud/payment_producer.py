from kafka import KafkaProducer
import datetime
import pytz
import time
import random
import json

# 결제 정보 토픽
TOPIC_NAME = "payments"
BROKERS=["15.152.234.229:9092"]

# Producer 생성
producer = KafkaProducer(bootstrap_servers=BROKERS)

# 현재 시간을 Asia/Seoul timezone에 맞춰서 생성하기
def get_seoul_datetime():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    kst_now = utc_now.astimezone(pytz.timezone("Asia/Seoul"))

    d = kst_now.strftime("%m/%d/%Y")
    t = kst_now.strftime("%H:%M:%S")

    return d, t

# 결제 정보 데이터 생성기. 랜덤하게 결제 정보를 만들어준다.
def generate_payment_data():
    # 데이터 소스로부터 데이터를 끌어오는 기능을 해주면 된다.
    # 크롤링이나 다른 데이터 레이크에서 데이터를 가져오면 된다.
    payment_type = random.choice(["롯데", "하나", "국민", "비트코인", "이더리움"])
    amount = random.randint(1000, 10000000)
    to = random.choice(["me", "mom", "dad", "stranger"])

    return payment_type, amount, to

# 데이터 발생 및 스트리밍
while True:
    # 현재 시간 데이터 얻기
    d, t = get_seoul_datetime()

    # 랜덤하게 만들어진 결제정보 얻기
    payment_type, amount, to = generate_payment_data()
    
    # 스트리밍 할 데이터를 조립 (json)
    row_data = {
        "DATE": d,
        "TIME": t,
        "PAYMENT_TYPE": payment_type,
        "AMOUNT": amount,
        "TO": to
    }

    # json 형식으로 바꿔주기
    row_json = json.dumps(row_data).encode("utf-8")

    # 데이터 스트리밍
    producer.send(TOPIC_NAME, row_json)
    print(row_data)
    time.sleep(1)