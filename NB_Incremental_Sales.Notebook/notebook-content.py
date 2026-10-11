# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "53eeac01-8da3-4225-819e-591fe39448f7",
# META       "default_lakehouse_name": "day13",
# META       "default_lakehouse_workspace_id": "a838cac6-6d38-4f79-add6-6988f69ec709",
# META       "known_lakehouses": [
# META         {
# META           "id": "53eeac01-8da3-4225-819e-591fe39448f7"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import col
df_day1 = spark.read.option("header", True).csv("Files/sales_day1.csv")
df_day1 = df_day1.withColumn("sale_date", col("sale_date").cast("timestamp"))
print(df_day1.count())
df_day1.write.format("delta").mode("overwrite").saveAsTable("fact_sales")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

max_date = df_day1.agg({"sale_date": "max"}).collect()[0][0]
from pyspark.sql import Row
control_df = spark.createDataFrame([
Row(table_name="fact_sales", last_loaded_timestamp=max_date)
])
control_df.write.format("delta").mode("overwrite").saveAsTable("load_control")
print(f"Day 1 watermark: {max_date}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

watermark = (spark.read.table("load_control")
.filter(col("table_name") == "fact_sales")
.select("last_loaded_timestamp")
.collect()[0][0])
print(f"Reading rows newer than {watermark}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import lit
df_day2 = (spark.read.option("header", True).csv("Files/sales_day2.csv")
.withColumn("sale_date", col("sale_date").cast("timestamp"))
.filter(col("sale_date") > lit(watermark)))
print(f"New rows to load: {df_day2.count()}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_day2.write.format("delta").mode("append").saveAsTable("fact_sales")
new_max = df_day2.agg({"sale_date": "max"}).collect()[0][0]
spark.sql(f"""
UPDATE load_control
SET last_loaded_timestamp = '{new_max}'
WHERE table_name = 'fact_sales'
""")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

print(spark.read.table("fact_sales").count())
spark.read.table("load_control").show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
