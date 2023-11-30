from kafka import KafkaConsumer
import json

FRAUD_TOPIC = "fraud_payments"
BROKERS = ["15.152.234.229:9092"]

consumer = KafkaConsumer(FRAUD_TOPIC, bootstrap_servers=BROKERS)
username = "소민호"

# pip install requests
def send_slack(msg):
    import requests
    WEBHOOK_URL = "https://hooks.slack.com/services/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"

    payloads = {
        "channel": "#기타자료",
        "username": username,
        "text": msg
    }

    requests.post(WEBHOOK_URL, json.dumps(payloads))

for message in consumer:
    msg = json.loads(message.value.decode())
    payment_type = msg["PAYMENT_TYPE"]
    payment_date = msg["DATE"]
    payment_time = msg["TIME"]
    amount = msg["AMOUNT"]
    to = msg["TO"]

    fraud_msg = f"이상거래 - [{payment_type}] {payment_date} {payment_time} << {to} - {amount} >>"
    send_slack(fraud_msg)
    print(fraud_msg)