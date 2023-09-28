from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType, ArrayType
import pyspark.sql.functions as F

spark = SparkSession.builder.appName("Test").getOrCreate()

# Create a dataset
data = [('Milk',('Drink', 'Cold')),
         ('Cola',('Drink', 'Cold', 'Sweet')),
         ('Apple',('Eat',)),
         ('Chips',('Eat', 'Warm', 'Salty')),
         ('Phone', None)
]

schema = StructType().add("Product", StringType()).add("Category", ArrayType(StringType()))

df = spark.createDataFrame(data=data, schema=schema)
df.printSchema()

# In fact, calling this method is enough to fulfill the task condition 
# because the name of all products and their categories is returned
df.show()

# Lets return df for each Product
def ProductDF(ProductName: StringType):
  return df\
            .select("Product", "Category")\
            .filter(F.col("Product") == ProductName)

# Test list with product names
aProductList = df.select("Product").\
               rdd.flatMap(lambda x: x)\
               .collect()

# Return df for each product
for aProduct in aProductList:
  aNewDF = ProductDF(aProduct)
  aNewDF.show()