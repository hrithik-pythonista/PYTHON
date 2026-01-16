import pandas as pd
data={
    'Name':['hrithik','vijaya','suba','anu'],
    'Age':[20,48,40,16],
    'Salary':[100000,190000,80000,70000]
    }
df=pd.DataFrame(data)
daf=df.set_index('Name')
print(daf)
print("\n")
print("----------------------------------------------------------------")
df_sorted=df.sort_values(by='Salary',ascending=False)
print(df_sorted)
print("----------------------------------------------------------------")
#loc (Label-based indexing)- Used to access rows and columns by labels (names).
print(daf.loc['hrithik'])
print("----------------------------------------------------------------")
#iloc (Integer-based indexing)- Used to access rows and columns by position (numbers).
print(daf.iloc[1])
print("----------------------------------------------------------------")

#indexing in pandas
print(daf[['Salary','Age']])
print("----------------------------------------------------------------")

#high salary filtering
highest_salary=df[df['Salary']>100000]
print(highest_salary)
print("----------------------------------------------------------------")


#reset
df_reset=df.reset_index()
print(df_reset)
print("----------------------------------------------------------------")

#groupby
grouped=df_reset.groupby('Age').sum()
print(grouped)
print("----------------------------------------------------------------")
print(df_reset.groupby('Age').agg({'Salary':['mean','sum','max']}))





