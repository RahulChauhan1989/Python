import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

data=pd.read_csv("Logistic.csv",header=0)
print(data.shape)
print(list(data.columns))
print(data.head())
print(data['education'].unique())
data['education']=np.where(data['education'] =='basic.9y', 'Basic', data['education'])
data['education']=np.where(data['education'] =='basic.6y', 'Basic', data['education'])
data['education']=np.where(data['education'] =='basic.4y', 'Basic', data['education'])
print(data['education'].unique())
print(data['y'].value_counts())

#count_no_sub = len(data[data['y']==0])
#count_sub = len(data[data['y']==1])
#pct_of_no_sub = count_no_sub/(count_no_sub+count_sub)
#print("percentage of no subscription is", pct_of_no_sub*100)
#pct_of_sub = count_sub/(count_no_sub+count_sub)
#print("percentage of subscription", pct_of_sub*100)

#print(data.groupby('job').mean())
#print(data.groupby('marital').mean())
#print(data.groupby('education').mean())

pd.crosstab(data.job,data.y).plot(kind='bar')
plt.title('Purchase Frequency for Job Title')
plt.xlabel('Job')
plt.ylabel('Frequency of Purchase')
plt.savefig('purchase_fre_job')