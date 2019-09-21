
import findspark
findspark.init()

from pyspark import SparkConf, SparkContext
from pyspark import SQLContext
from pyspark import SparkConf
from pyspark import StorageLevel
from termcolor import colored


conf = SparkConf().setMaster('local').setAppName('PySparkShell')
sc = SparkContext(conf=conf)

#设置log级别
sc.setLogLevel("WARN")
# spark = SQLContext(sc)

#创建一个lines的RDD
inputRDD = sc.textFile('log.txt')

# 遍历结果
errorsRDD = inputRDD.filter(lambda line: "error" in line)

# print(colored('把RDD持久化到内存中', 'red'))
# pandaslines.persist( StorageLevel.MEMORY_AND_DISK_2 )
# print('getStorageLevel=', pandaslines.getStorageLevel())

for i in errorsRDD.collect():
    print(colored('i==>', 'red'), i)