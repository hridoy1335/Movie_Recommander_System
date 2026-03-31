from pyspark import pipelines as dp
from pyspark.sql.functions import *


# This file defines a sample transformation.
# Edit the sample below or add new transformations
# using "+ Add" in the file browser.


@dp.table
def bronze_movie():
    # Read from the "sample_trips" table, then sum all the fares
    return (
        spark.readStream.table("/Workspace/Users/rkhridoyinfo@gmail.com/Movie_Recommander_System/artifacts/movies_data.csv")
    )

@dp.table
def bonze_credit():
    return (
        spark.readStream.table("/Workspace/Users/rkhridoyinfo@gmail.com/Movie_Recommander_System/artifacts/tmdb_5000_credits.csv")
    )

@dp.table
def bronze_metadata():
    return (
        spark.readStream.table("/Workspace/Users/rkhridoyinfo@gmail.com/Movie_Recommander_System/artifacts/tmdb_5000_movies.csv")
    )
