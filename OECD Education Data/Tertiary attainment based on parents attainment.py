import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Tertiary attainment based on parents attainment.csv')
df = df[['Country','SEX','AGE','Measure','YEAR','ISCED-A 2011','Category','Value']]
df = df[df.SEX == 'T'] # Removes all M/F sex values
df = df[df.AGE == 'Y30T44']
df = df[df.Measure == 'Value'] # Removes all M/F sex values
df = df[df.YEAR == 2012] # Only includes YEAR == 2012
df = df[df['ISCED-A 2011'] == 'Tertiary-type B']

# df.to_csv("Test.csv")
# plt.text(x,y,'text')

test = df.pivot_table('Value','Country', 'Category') #value,index,columns
test.plot.bar()
plt.title("Tertiary Attainment Based on Parents Attainment (2014)")
plt.xlabel("Countries")
plt.ylabel("Population (%)")
plt.legend(bbox_to_anchor = (1.04,1), borderaxespad = 0)
plt.show()

