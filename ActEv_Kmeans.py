# %%
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from kneed import KneeLocator

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

# ================================
# Determina el numero k óptimo
# ================================
dfp = df[["total_items","discount%","weekday","hour","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]]

ssd = []
ks = range(1,11)
for k in range(1,11):
    km = KMeans(n_clusters=k)
    km = km.fit(dfp)
    ssd.append(km.inertia_)

kneedle = KneeLocator(ks, ssd, S=1.0, curve="convex", direction="decreasing")
kneedle.plot_knee()
plt.show()

k = round(kneedle.knee) # Número óptimo para k

print(f"Number of clusters suggested by knee method: {k}")

# ============================================
# Ya con el valor de k calculamos los clusters
# ============================================
kmeans = KMeans(n_clusters=k).fit(df[["total_items","discount%","weekday","hour","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]])

# Generar el scatterplot con la organización de los clusters

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
cluster0=df[kmeans.labels_ == 0]
cluster1=df[kmeans.labels_ == 1]
cluster2=df[kmeans.labels_ == 2]
cluster3=df[kmeans.labels_ == 3]

# %%
cluster0[["Food%","Fresh%","Drinks%",x=]].sum().plot.bar()
plt.show()

# %%
cluster1[["Food%","Fresh%","Drinks%"]].sum().plot.bar()
plt.show()

# %%
cluster2[["Food%","Fresh%","Drinks%"]].sum().plot.bar()
plt.show()

# %%
cluster3[["Food%","Fresh%","Drinks%"]].sum().plot.bar()
plt.show()


# %%
#A partir de aquí es el cluster 0
sns.histplot(data=cluster0, x="Baby%_range", multiple="stack", hue="Pets%_range")

# %%
sns.histplot(data=cluster0, x="Food%_range", multiple="stack", hue="Fresh%_range")
#sns.boxplot(data=cluster0, x="Pets%_range", y="total_items", hue="Home%_range")

# %%
sns.histplot(data=cluster0, x="Home%_range", multiple="stack", hue="Beauty%_range")

# %%
sns.histplot(data=cluster0, x="Drinks%_range")

# %%
# A partir de aquí es el cluster 1
sns.histplot(data=cluster1, x="Baby%_range", multiple="stack", hue="Pets%_range")

# %%
sns.histplot(data=cluster1, x="Food%_range", multiple="stack", hue="Fresh%_range")

# %%
sns.histplot(data=cluster1, x="Home%_range", multiple="stack", hue="Beauty%_range")

# %%
sns.histplot(data=cluster1, x="Drinks%_range")

# %%
# A partir de aquí es el cluster 2
sns.histplot(data=cluster2, x="Baby%_range", multiple="stack", hue="Pets%_range")

# %%
sns.histplot(data=cluster2, x="Baby%_range", multiple="stack", hue="Home%_range")

# %%
sns.histplot(data=cluster2, x="Baby%_range", multiple="stack", hue="Beauty%_range")

# %%
sns.histplot(data=cluster2, x="Drinks%_range")

# %%
# A partir de aquí es el cluster 3
sns.histplot(data=cluster3, x="Baby%_range", multiple="stack", hue="Pets%_range")

# %%
sns.histplot(data=cluster3, x="Food%_range", multiple="stack", hue="Fresh%_range")

# %%
sns.histplot(data=cluster3, x="Home%_range", multiple="stack", hue="Beauty%_range")

# %%
sns.histplot(data=cluster3, x="Drinks%_range")

# %%
