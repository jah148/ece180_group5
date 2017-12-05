import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
This code processes and plots a .cvs file with 4 columns and 9 countries. 

'''

string = 'Relationships between average tuition fees and Fin Aid.csv'

assert isinstance(string, str),"Input must be of type string"

df = pd.read_csv(string)
# Drop the following column:
df = df.drop('Average tuition fees charged by private institutions in USD', 1)
# Change index from 0,1...n to names of countries
df.set_index('Country') 

# Creates scatter plot
df.plot.scatter(x = 'Percentage of students who benefit from public loans AND/OR scholarships/grants',
				y = 'Average tuition fees charged by public institutions in USD')

plt.title('Average tuition fees vs. the percentage \n of students receiving public subsidies(2015/16)')

# Relabel axis:
plt.xlabel('Percentage of students who benefit from public loans \n AND/OR scholarships/grants ($)')

# Assign ylabel to object so that I can rotate it
h = plt.ylabel('Average tuition fees\n charged by public \n institutions in USD($)', labelpad = 55)
h.set_rotation(0)

# Add more ticks to improve readability
plt.xticks(range(0,101,5))
plt.yticks(range(0,8500,1000))

plt.show()
