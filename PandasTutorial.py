import pandas as pd

data={'Range':[1,2,3,4,'','',''],"Value":[5,6,7,8,'','','']}

dataDisplay=pd.DataFrame(data,index=['index1','index2','index3','index4'])

dataDisplay=pd.DataFrame(data)

print(dataDisplay)
print(dataDisplay.loc['index2'])
print(dataDisplay.shape)

datadisplay_temp=dataDisplay.append(dataDisplay)

print("Data Temp Display Temp : {0}".format(datadisplay_temp.shape))
print(datadisplay_temp)
#datadisplay_temp_Remove_Duplicates = datadisplay_temp.drop_duplicates()
datadisplay_temp.drop_duplicates(inplace=True)
print(datadisplay_temp)
print(dataDisplay.columns)

dataDisplay.rename(columns={
        'Range': 'Range_Rename', 
        'Value': 'value_Rename'
    }, inplace=True)


print(dataDisplay.columns)

dataDisplay.columns = [col.lower() for col in dataDisplay]
print(dataDisplay.columns)

print(dataDisplay)
print(dataDisplay.isnull())
print(dataDisplay.isnull().sum())

dataDisplay.dropna(axis=1)
dataDisplay.fillna(revenue_mean, inplace=True)

dataDisplay['genre'].describe()
movies_df['genre'].value_counts().head(10)
movies_df.corr()


