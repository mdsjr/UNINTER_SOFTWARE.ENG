--Atividade Pratica Big Data

from google.colab import drive
drive.mount('/content/drive')
!cp /content/drive/MyDrive/BIGDATA\
/imdb-reviews-pt-br.csv /content

!pip install pyspark

from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
cam_arq ='/content/drive/MyDrive\
/BIGDATA/imdb-reviews-pt-br.csv'

imdbDf = spark.read.csv\
(cam_arq, header=True, inferSchema=True)

from pyspark.sql.functions import sum
RU = "3539252"
neg_imdbDf = imdbDf.filter\
       (imdbDf.sentiment == "neg")
soma = neg_imdbDf.select\
         (sum("id")).collect()[0][0]
print(soma)





from pyspark.sql.functions\
import explode, split, col
neg_imdbDf = imdbDf.filter\
(imdbDf.sentiment == "neg")
palsPtDf = neg_imdbDf.select\
(explode(split\
(neg_imdbDf.text_pt, "\\W+"))\
.alias("pals_pt"))
palsEnDf = neg_imdbDf.select\
(explode(split\
(neg_imdbDf.text_en, "\\W+"))\
.alias("pals_en"))
contPalsPtDf = palsPtDf.groupBy\
("pals_pt").count()
contPalsEnDf = palsEnDf.groupBy\
("pals_en").count()

totalPt = contPalsPtDf.agg(\
{"count": "sum"}).collect()[0][0]
RU = "3539252"
totalEn = contPalsEnDf.agg(\
{"count": "sum"}).collect()[0][0]

diferencaPalavras = totalPt - totalEn
print(diferencaPalavras)
