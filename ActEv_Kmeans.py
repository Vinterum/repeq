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

# ======================================
# Ya con el k calculamos los clusters
# ======================================
kmeans = KMeans(n_clusters=k).fit(df[["total_items","discount%","weekday","hour","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]])

# Generar el scatterplot con la organización de los clusters
#sns.scatterplot(data=df, x="Annual_Income_(k$)", y="Spending_Score", hue=kmeans.labels_)
#plt.show()

# %%
#sns.scatterplot(data=df, x="Annual_Income_(k$)", y="Spending_Score", hue="Age")

# %%
df["Beauty%_range"]=pd.cut(df["Beauty%"], [-1,0,20,40,60,80,100],labels=['0','1-20','21-40','41-60','61-80','81-100'])
#cluster0['Beauty%_range'].cat.categories=[1,2,3,4,5,6]

# %%
df["Health%_range"]=pd.cut(df["Health%"], [-1,0,20,40,60,80,100],labels=['0','1-20','21-40','41-60','61-80','81-100'])

# %%
df["Baby%_range"]=pd.cut(df["Baby%"], [-1,0,20,40,60,80,100],labels=['0','1-20','21-40','41-60','61-80','81-100'])

# %%
df["Pets%_range"]=pd.cut(df["Pets%"], [-1,0,20,40,60,80,100],labels=['0','1-20','21-40','41-60','61-80','81-100'])

# %%
cluster0=df[kmeans.labels_ == 0]
cluster1=df[kmeans.labels_ == 1]
cluster2=df[kmeans.labels_ == 2]
cluster3=df[kmeans.labels_ == 3]

# %%
sns.boxplot(data=cluster0, x="Beauty%_range", y="total_items", hue="Health%_range")

# %%
sns.boxplot(data=cluster0, x="Baby%_range", y="total_items", hue="Beauty%_range")

# %%
