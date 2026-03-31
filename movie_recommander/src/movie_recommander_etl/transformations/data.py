from pyspark import pipelines as dp
from pyspark.sql.functions import *


# This file defines a sample transformation.
# Edit the sample below or add new transformations
# using "+ Add" in the file browser.


@dp.table()
def bronze_movie():
    # Ingest movie data from volume using Auto Loader
    return (
        spark.readStream.format("delta")
        .load("/Volumes/hk/bronze/product")
    )
