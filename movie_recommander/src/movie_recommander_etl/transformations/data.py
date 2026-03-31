from pyspark import pipelines as dp
from pyspark.sql.functions import *


# This file defines a sample transformation.
# Edit the sample below or add new transformations
# using "+ Add" in the file browser.


@dp.table
def product():
    # Read from the "sample_trips" table, then sum all the fares
    return (
        spark.readStream.format("delta")
        .load("/Volumes/hk/bronze/product")
    )
