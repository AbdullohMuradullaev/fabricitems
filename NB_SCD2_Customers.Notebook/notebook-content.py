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

df = spark.read.format("csv").option("header","true").load("abfss://Week_3@onelake.dfs.fabric.microsoft.com/day13.Lakehouse/Files/customers_initial.csv")
# df now is a Spark DataFrame containing CSV data from "abfss://Week_3@onelake.dfs.fabric.microsoft.com/day13.Lakehouse/Files/customers_initial.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import col, current_timestamp, lit, to_date
df_scd=(df
.withColumn("effective_from", to_date(col("last_updated")))
.withColumn("effective_to", lit("9999-12-31").cast("date"))
.withColumn("is_current", lit(True))
.withColumn("version", lit(1))
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_scd.write.format("delta").mode("overwrite").saveAsTable("dim_customer")
spark.read.table("dim_customer").show(5)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_delta = spark.read.option("header", True).csv("Files/customers_delta.csv")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_current = spark.read.table("dim_customer").filter(col("is_current") == True)
# Find customer_ids in delta that already exist with different attribute values
tracked_cols = ["city", "country", "loyalty_tier", "credit_limit"]
from functools import reduce
change_conditions = reduce(lambda a, b: a | b, [
(df_delta[c] != df_current[c]) for c in tracked_cols
])
df_changed_keys = (df_delta.alias("d")
.join(df_current.alias("c"), "customer_id", "inner")
.where(change_conditions)
.select("d.customer_id"))
df_changed_keys.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from delta.tables import DeltaTable
delta_dim = DeltaTable.forName(spark, "dim_customer")
delta_dim.alias("target").merge(
df_changed_keys.alias("src"),
"target.customer_id = src.customer_id AND target.is_current = true"
).whenMatchedUpdate(set={
"effective_to": "current_date() - interval 1 day",
"is_current": "false"
}).execute()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# All delta rows become new "current" rows
df_new_versions = (df_delta
.withColumn("effective_from", to_date(col("last_updated")))
.withColumn("effective_to", lit("9999-12-31").cast("date"))
.withColumn("is_current", lit(True))
.withColumn("version", lit(2))   # bump version
)
df_new_versions.write.format("delta").mode("append").saveAsTable("dim_customer")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.read.table("dim_customer") \
.filter(col("customer_id") == "C001") \
.orderBy("version") \
.show(truncate=False)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM day13.dbo.dim_customer LIMIT 1000")
df.filter(
    (col("effective_from")<="2025-06-05") & (col("effective_to")>="2025-06-05") 
).show()

df.printSchema()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
