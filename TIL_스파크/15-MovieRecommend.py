from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.types import IntegerType

# 데이터가 매우 큰 경우 강제로 사용할 메모리의 용량을 설정
MAX_MEMORY = "4g"

spark = (
    SparkSession.builder.appName("movie-recommendation")
    .config("spark.executor.memory", MAX_MEMORY)
    .config("spark.driver.memory", MAX_MEMORY)
    .getOrCreate()
)

filepath = "/home/ubuntu/working/spark-examples/data/MovieLens/ratings.csv"
ratings_df = spark.read.csv(f"file://{filepath}", inferSchema=True, header=True)
ratings_df.show()

# timestamp는 뺴고 선택
ratings_df = ratings_df.select("userId", "movieId", "rating")
# ratings_df.printSchema()

# 통계 정보 확인
ratings_df.select("rating").describe().show()

# train_df, test_df 데이터 세트 분리
train_df, test_df = ratings_df.randomSplit([0.8, 0.2], seed=42)

# 모델 생성
als = ALS(
    maxIter=5,
    regParam=0.1,  # Learning Rate
    userCol="userId",  # 사용자 정보
    itemCol="movieId",  # 아이템 컬럼(여기서는 영화)
    ratingCol="rating",  # 평점 컬럼
    coldStartStrategy="drop",  # 학습하지 못한 데이터에 대한 처리(삭제)
)

# 모델 훈련
als_model = als.fit(train_df)

# print(type(als))
# print(type(als_model))

# 예측(test_df) , 자동으로 prediction 컬럼 생성
predictions = als_model.transform(test_df)
predictions.show()  # actions

# 평가
evaluator = RegressionEvaluator(
    metricName="rmse", labelCol="rating", predictionCol="prediction"
)

# 예측된 데이터 프레임 넣어주기
rmse = evaluator.evaluate(predictions)
print(rmse)


# 추천하기
# 1. 각 user에게 top 3 아이템을 추천
#       [{영화 id, 예상 평점}, {영화 id, 예상 평점}, {영화 id, 예상 평점}]
# als_model.recommendForAllUsers(3).show()

# 2. 각 영화에 어울리는 top 3 유저를 추천
# als_model.recommendForAllItems(3).show()

# 사용자 목록을 만들어서 추천
user_list = [276, 53, 393]
users_df = spark.createDataFrame(user_list, IntegerType()).toDF("userId") # 시리즈를 데이터프레임으로 만드는 방법 중 하나. toDF는 컬럼명을 정해준다.

user_recommend = als_model.recommendForUserSubset(users_df, 5)
user_recommend.show()

# 특정 user를 위한 추천
movies_list = user_recommend.filter("userId = 393").select("recommendations")
movies_list.show()

# 데이터프레임으로 조회해서 가져오는 것이 아닌, 셀제 데이터를 가져와야 하기 때문에 collect()같은 것들을 사용하는 것이 좋다.
movies_list = (
    movies_list.select("recommendations").collect()[0].recommendations 
)  # 로우값에서 일부분 추출, 뒤에 recommendation은 특정 컬럼명 지정하여 추출

recommend_df = spark.createDataFrame(movies_list)
recommend_df.show()

movie_filepath = "/home/ubuntu/working/spark-examples/data/MovieLens/movies.csv"
movies_df = spark.read.csv(f"file://{movie_filepath}", inferSchema=True, header=True)

# SQL 활용을 위해 TempView 등록
recommend_df.createOrReplaceTempView("rec")
movies_df.createOrReplaceTempView("movies")

query = """
select *
from movies
join rec on movies.movieId = rec.movieId
order by rating desc
"""

spark.sql(query).show()
