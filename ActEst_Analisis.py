# %%
import pandas as pd

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

# %%
import seaborn as sns
sns.set_theme(style="whitegrid")

# %%
#Historiograma de la frecuencia de cada hora por dia de la semana
g = sns.histplot(data=df, x="hour", multiple="stack", hue="weekday")
for q in df.hour.quantile([.25, .5, .75]):
    g.axvline(q, linestyle=":")
    g.text(q, 5, q)

# %%
df["Food%_range"]=pd.cut(df["Food%"], [-1,0,20,40,60,80,100],labels=['0','1-20','21-40','41-60','61-80','81-100'])
df["Fresh%_range"]=pd.cut(df["Fresh%"], [-1,0,20,40,60,80,100],labels=['0','1-20','21-40','41-60','61-80','81-100'])
df["Drinks%_range"]=pd.cut(df["Drinks%"], [-1,0,20,40,60,80,100],labels=['0','1-20','21-40','41-60','61-80','81-100'])
df["Home%_range"]=pd.cut(df["Home%"], [-1,0,20,40,60,80,100],labels=['0','1-20','21-40','41-60','61-80','81-100'])
df["Beauty%_range"]=pd.cut(df["Beauty%"], [-1,0,20,40,60,80,100],labels=['0','1-20','21-40','41-60','61-80','81-100'])
df["Health%_range"]=pd.cut(df["Health%"], [-1,0,20,40,60,80,100],labels=['0','1-20','21-40','41-60','61-80','81-100'])
df["Baby%_range"]=pd.cut(df["Baby%"], [-1,0,20,40,60,80,100],labels=['0','1-20','21-40','41-60','61-80','81-100'])
df["Pets%_range"]=pd.cut(df["Pets%"], [-1,0,20,40,60,80,100],labels=['0','1-20','21-40','41-60','61-80','81-100'])

# %%
sns.displot(data=df, x="Drinks%_range", multiple="stack", hue="weekday", palette="rainbow")

# %%
df["discount%_cat"]=pd.cut(df["discount%"], [-70,-1,0,20,60,100],labels=['Aumento','0','1-20','21-60','61-100'])
sns.histplot(data=df, x="discount%_cat", multiple="stack", hue="weekday")

# %%
sns.histplot(data=df, x="discount%_cat", multiple="stack", hue="weekday")

# %%
Aumentos=df[df["discount%_cat"]=='Aumento']
sns.histplot(data=Aumentos, x="discount%_cat", multiple="stack", hue="weekday")

# %%
sns.boxplot(data=df, x="weekday", y="total_items")

# %%
sns.boxplot(data=df, x="discount%")

# %%
sns.boxplot(data=df, x="Pets%")

# %%
sns.boxplot(data=df, x="Fresh%")

# %%
sns.boxplot(data=df, x="Beauty%")

# %%
sns.histplot(data=df, x="Baby%_range", multiple="stack", hue="Pets%_range")

# %%
sns.displot(data=df, x="Drinks%_range", y="total_items")

# %%
df_original=df.drop(columns=['Food%_range', 'Fresh%_range','Drinks%_range', 'Home%_range', 'Beauty%_range', 'Health%_range','Baby%_range', 'Pets%_range','discount%_cat'])
sns.heatmap(df_original.corr())

# %%
df_original.describe()

# %%
