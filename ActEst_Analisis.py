# %%
import pandas as pd

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

# %%
import seaborn as sns
sns.set_theme(style="whitegrid")

# %%
df.head()

# %%
#Historiograma de la frecuencia de cada hora por dia de la semana
g = sns.histplot(data=df, x="hour", multiple="stack", hue="weekday")
for q in df.hour.quantile([.25, .5, .75]):
    g.axvline(q, linestyle=":")
    g.text(q, 5, q)

# %%
df["Drinks%_cat"]=pd.cut(df["Drinks%"], [-1,0,20,40,60,80,100],labels=['0','1-20','20-40','40-60','60-80','80-100'])
df.dropna()

# %%
sns.displot(data=df, x="Drinks%_cat", hue="weekday", palette="Blues")

# %%
sns.displot(data=df, x="hour")

# %%
df["discount%_cat"]=pd.cut(df["discount%"], [-70,-1,0,20,60,100],labels=['Aumento','0','1-20','21-60','61-100'])
sns.histplot(data=df, x="discount%_cat", multiple="stack", hue="weekday")

# %%
Aumentos=df[df["discount%_cat"]=='Aumento']
sns.displot(data=Aumentos, x="discount%_cat", multiple="stack", hue="weekday")

# %%
sns.boxplot(data=df, x="weekday", y="total_items")

# %%
sns.boxplot(data=df, x="discount%")

# %%
sns.boxplot(data=df, x="Drinks%")

# %%
df.head()

# %%
sns.displot(data=df, x="Drinks%_cat", y="total_items")

# %%
df_original=df.drop(columns=['Drinks%_cat','discount%_cat'])
sns.heatmap(df_original.corr())

# %%
