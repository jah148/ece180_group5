import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# def label_point(x, y, val, ax):
#     a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
#     for i, point in a.iterrows():
#         ax.text(point['x'], point['y'], str(point['val']))

# s = pd.Series(np.array(['England','Norway','Austrilia','United States','Turkey','Finland','Chile','Italy','Switzerland']))
# ax = df.set_index('Percentage of students who benefit from public loans AND/OR scholarships/grants')['Average tuition fees charged by public institutions in USD'].plot(style = 'o')
# label_point(df['Percentage of students who benefit from public loans AND/OR scholarships/grants'],
# 			df['Average tuition fees charged by public institutions in USD'], s , ax)

df = pd.read_csv('Relationships between average tuition fees and Fin Aid.csv')
df = df.drop('Average tuition fees charged by private institutions in USD', 1)
df.set_index('Country') 

# ax = df.plot.scatter(x = 'Percentage of students who benefit from public loans AND/OR scholarships/grants',
# 					 y = 'Average tuition fees charged by public institutions in USD', 
# 					 color = 'DarkBlue', label = 'Group 1')

df.plot.scatter(x = 'Percentage of students who benefit from public loans AND/OR scholarships/grants',
				y = 'Average tuition fees charged by public institutions in USD')

plt.title('Average tuition fees vs. the percentage \n of students receiving public subsidies(2015/16)')

# Relabel axis:
plt.xlabel('Percentage of students who benefit from public loans \n AND/OR scholarships/grants ($)')
h = plt.ylabel('Average tuition fees\n charged by public \n institutions in USD($)', labelpad = 55)
h.set_rotation(0)

plt.xticks(range(0,101,5))
plt.yticks(range(0,8500,1000))

plt.show()
