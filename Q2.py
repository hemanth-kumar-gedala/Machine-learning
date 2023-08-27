# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11VjdW2yG7q8OFas6KTpqkpdq7c_wWEwi
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_excel(r"Lab Session1 Data.xlsx",sheet_name="IRCTC Stock Price")

mean = df["Price"].mean()
variance = df["Price"].var()

print('Meanof Column D : ', mean)
print('Variance of Column D :  ', variance)
price_list=df["Price"]

wednesday = price_list[df['Day'] == 'Wed']
print("Wednesday  : ", wednesday)

sample = np.mean(wednesday)

print('Sample mean:', sample)

april = price_list[df['Month'] == 'Apr']


aprilmean = np.mean(april)

print('April mean:', aprilmean)

chg = df['Chg%']

loss = np.where(chg > 0, False, True)

wednesday_data = df[df['Day'] == 'Wed']
profit_on_wednesday = np.mean(wednesday_data['Chg%'] > 0)

print('Probability of profit on Wednesday', profit_on_wednesday)

Wed_Probability= np.mean(df['Day'] == 'Wed')

conditional_probability = profit_on_wednesday / Wed_Probability

print('Conditional probability  :', conditional_probability)

loss_probability = np.mean(loss)

print('Probability of loss:', loss_probability)


plt.scatter(df['Day'], df['Chg%'])
plt.ylabel('Chg%')
plt.title('Chg% vs Day')
plt.xlabel('Day')
plt.show()