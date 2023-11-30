from kafka import KafkaProducer
import pandas as pd
import urllib.request
import time
import json

BROKER_SERVERS = ["15.152.234.229:9092"]
TOPIC_NAME = "naver_reviews"

producer = KafkaProducer(bootstrap_servers=BROKER_SERVERS)
urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt", filename="ratings_test.txt")
df_test  = pd.read_table('ratings_test.txt')


for sentence in df_test['document']:

    msg = {
        "sentence": sentence
    }
    
    producer.send(TOPIC_NAME, json.dumps(msg).encode("utf-8"))
    print(msg)
    time.sleep(1)

producer.flush()