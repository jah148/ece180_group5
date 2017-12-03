import pandas as pd
import matplotlib.pyplot as plt

'''
This code processes and plots a .cvs file with 19 columns and 289 rows 

'''

string = 'Tertiary attainment based on parents attainment.csv'

assert isinstance(string,str),'Input must be of type string'

df = pd.read_csv('Tertiary attainment based on parents attainment.csv')
# Obtain following columns:
df = df[['Country','SEX','AGE','Measure','YEAR','ISCED-A 2011','Category','Value']]
df = df[df.SEX == 'T'] # Removes all M/F sex values, I only want total
df = df[df.AGE == 'Y30T44'] # Want ages 30 to 44 only
df = df[df.Measure == 'Value'] # Only want value and not SE
df = df[df.YEAR == 2012] # Only include YEAR == 2012
df = df[df['ISCED-A 2011'] == 'Tertiary-type B'] # Only include this type of education

# df.to_csv("Test.csv")
# plt.text(x,y,'text')

# Organize to better fit plot 
test = df.pivot_table('Value','Country', 'Category') #(value,index,columns)
test.plot.bar()
plt.title("Tertiary Attainment Based on Parents Attainment (2014)")
plt.xlabel("Countries")
plt.ylabel("Population (%)")
plt.legend(bbox_to_anchor = (1.04,1), borderaxespad = 0)
plt.show()

