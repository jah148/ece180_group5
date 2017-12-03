import pandas as pd
import matplotlib.pyplot as plt

'''
This code processes and plots a .cvs file with 4 columns and 9 countries. 

'''

string = 'Distrib of fin aid to students at bachelors.csv'
assert isinstance(string, str),'Input must be of type string'

df = pd.read_csv(string)


# I thought changing the "country" column to index would make .plt plot the
# countries instead of the index, but it still plotted index values, therefore
# I commented it out and will manually set the names

# df.set_index('Country') 

# Makes a stacked bar graphs
df.plot.bar(stacked=True,color = ['Red','DarkOrange','DarkBlue','Green'])
plt.title('Distribution of Financial Support to Students at bachelors (2015/16)')
plt.text(9,65,'National students, based on full-time students',fontstyle='italic')
plt.ylabel("%")

# Adds ticks w/ countries as labels
plt.xticks(range(9) ,('England','Norway','Austrailia','United States',
						'Turkey','Finland','Chile','Italy','Switzerland'))

# Adds more ticks for increased readability
plt.yticks(range(0,100,10))

# Anchors the legend outside the plot for better readability
plt.legend(bbox_to_anchor = (1.04,1), borderaxespad = 0)
plt.show()

