import polars as pl

df: pl.DataFrame = pl.read_csv("./ecommerce_dataset/2019-Nov.csv")

# print(df.shape)

# print(df.filter(pl.col('price')> 400 | pl.col('brand').is_in(['xiaomi'])).head())

df.select(pl.col('price').max())