from os.path import join, abspath
import collections

from pyspark import StorageLevel
from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import functions
from pyspark.sql.types import *
from pyspark.sql.window import Window
import time


#스파크 세션을 사용하면 DataFrame 생성, DataFrame을 테이블로 등록, SQL 실행, 테이블 캐시, 패켓 파일 읽기 등을 할 수 있다. 
#다음은 스파크 세션을 생성한 빌드 패턴 예시이다. 

warehouse_location = abspath('spark-warehouse')


spark = SparkSession \
    .builder \                                                            #sparksession의 빌더
    .appName("sample") \                                                  #app의 이름
    .master("local[*]") \                                                 #로컬 시스템에 있는 코어 수만큼의 작업자 스레드를 사용하여 스파크를 실행.                                   
    .config("spark.sql.warehouse.dir", warehouse_location) \ #(configuration property의 key값, configuration property의 value값)
    .config("spark.driver.host", "172.30.1.60") \       #연결할 스파크 마스터 URL을 설정
    .getOrCreate()                                    #기존 스파크 세션을 가져오거나 기존 스파크 세션이 없는 경우 이 빌더에 설정된 옵션을 기반으로 새 스파크 세션을 만듦


sample_dataframe = spark.range(1000).toDF("number") 

#sample_dataframe의 number가 짝수인 로우들을 찾는 트렌스포메이션
sample_tf = sample_dataframe.where("number%2 =0")


#Dataframe 생성
df = spark.read.format("json").load("/Users/soyoon-yoon/Downloads/Spark-The-Definitive-Guide-master/data/flight-data/json/2015-summary.json")

#컬럼의 행/열 수 확인
print((df.count(), len(df.columns)))


df.select("DEST_COUNTRY_NAME").show(2)
df.selectExpr("DEST_COUNTRY_NAME as Country name", "DEST_COUNTRY_NAME").show(10)

