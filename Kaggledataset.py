import pandas as pd
df=pd.read_csv("titanic.csv")
print(df.head())
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 200)
print("▂" * 200)
#subset
subset=df[['PassengerId','Pclass','Name']]
print(subset)
print("▂" * 200)
#head(10)-prints top 10  line
print(df.head(10))


