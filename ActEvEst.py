#%%
import pandas as pd
import numpy as np
# %%
df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

# %%
df.index

# %%
df.size

# %%
df.colums

# %%
df.min()

#%%
df.max()

# %%
df.mean()


# %%
df[["customer","total_items","discount%","weekday",
"hour","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]].mode()


# %%
df.median()

# %%
df.std()

# %%
df.quantile([.25,.5,.75])

# %%
df.quantile(0.5)

# %%
df.quantile(0.75)

#%%
df.info()

# %%
df.describe()