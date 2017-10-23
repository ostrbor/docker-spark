import pyspark
from blessings import Terminal

term = Terminal()
sc = pyspark.SparkContext()
rdd = sc.parallelize(range(0, 10))
result = str(rdd.count())
import pdb; pdb.set_trace()
print(term.green+result)
print(term.green+"HELLO FROM SPARK"+term.normal)