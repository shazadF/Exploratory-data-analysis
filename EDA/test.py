import pandas as pd
import matplotlib.pyplot as plt

data  = {'managers':['mike1','mike2','mike3','mike4','mike5','mike6','mike7'],
'profit':[110,60,40,30,10,5,5],
}

df = pd.DataFrame(data)

df = df.sort_values(by = 'profit', ascending = False)
print(df)
top_5 = df.iloc[:5] 
print(top_5)
others = df.iloc[5:]['profit'].sum()

df2 = pd.DataFrame([['others',others]], columns = ['managers','profit'])
print(df2)
all_data = top_5.append(df2, ignore_index=True)
print(all_data)

all_data.index = all_data['managers']
print(all_data)
#func to lable the pieces
def auto_func(val):
    return(round(val)) 

all_data.plot.pie(y = 'profit', autopct = auto_func)

# ax = plt.gca()

plt.show()