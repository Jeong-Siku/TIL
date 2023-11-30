from kafka import KafkaConsumer
import json
from joblib import load
BROKER_SERVERS = ["15.152.234.229:9092"]
TOPIC_NAME = "naver_reviews"

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=BROKER_SERVERS)
tfidf_vectorizer = load("/home/ubuntu/working/kafka/movie_review/tfidf_vect.pkl")
model = load("/home/ubuntu/working/kafka/movie_review/korean_model.pkl")
print("Wait....")

for message in consumer:
    sentence = json.loads(message.value.decode())['sentence']
    test_vector = tfidf_vectorizer.transform([sentence])
    print(sentence, "===>", model.predict(test_vector)[0])

print("Done....")