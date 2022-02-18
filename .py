import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline


df=pd.read_csv('zomato.csv',encoding='latin-1')
df.info()


df.columns


df.isnull().sum()


[col for col in df.columns if df[col].isnull().sum()>0]


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


df1=pd.read_excel("Country-Code.xlsx")

df2=df.merge(df1,on="Country Code",how='left')


a=df2["Country"].value_counts().index
b=df2["Country"].value_counts().values

plt.pie(b[:3],labels=a[:3],autopct='%1.2f%%')



z=df2.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:"rating ct"})


plt.rcParams['figure.figsize']=(20,6)
sns.barplot(x='Aggregate rating',y='rating ct',data=z,palette=["white","red","orange","yellow","green","green"],hue='Rating color')


sns.countplot(x='Rating color',data=z,palette=["white","red","orange","yellow","green","green"])


df2[df2["Aggregate rating"]==0]
df3["Country"].value_counts()

df2[["Country","Currency"]].groupby(["Country","Currency"]).size().reset_index()

df2[df2["Has Online delivery"]=='Yes'].Country.value_counts()



a=df2["City"].value_counts().index
b=df2["City"].value_counts().values
plt.pie(b[:5],labels=a[:5],autopct='%1.2f%%')


df2["Cuisines"].value_counts().reset_index().head(10)
