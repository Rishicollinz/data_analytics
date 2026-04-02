# Polars

- Written in rust, so fast and memory efficient.
- Supports lazy loading

- For dataset always use ipynb, because it is generally better because it only loads the dataset once.

- [Reference - Playlist](https://www.youtube.com/playlist?list=PLo9Vi5B84_dfAuwJqNYG4XhZMrGTF3sBx)

---

**Methods:**

- read_csv()
- read_parquet()
- scan_csv()
- scan_parquet()
- select()
- pl.col('col_name')
- df.shape
- df.head()
- with_columns()
- alias()
- lazy()
- collect()
- group_by()
- filter()
- sort()
- agg()

- [polar_basic](./polar_learn.ipynb)
- [polar_lazy](./lazy_loading.ipynb)
