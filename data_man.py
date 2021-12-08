from read_data import df

from pyspark.sql.functions import isnan, when, count, col
df1 = df
def no_of_records():
    return df.distinct().count()

def col_names():
    return df.columns

def count_missing_values():
    df.select([count(when(isnan(c), c)).alias(c) for c in df.columns]).show()

def delete_cols(col):
    df1 = df.drop(col)
    return df1.columns


