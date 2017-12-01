import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Distrib of fin aid to students at bachelors.csv')

# I thought changing the "country" column to index would make .plt plot the
# countries instead of the index, but it still plotted index values, therefore
# I commented it out and will manually set the names

# df.set_index('Country') 

df.plot.bar(stacked=True,color = ['Red','DarkOrange','DarkBlue','Green'])
plt.title('Distribution of Financial Support to Students at bachelors (2015/16)')
plt.text(9,65,'National students, based on full-time students',fontstyle='italic')
plt.ylabel("%")
plt.xticks(range(9) ,('England','Norway','Austrailia','United States',
						'Turkey','Finland','Chile','Italy','Switzerland'))
plt.yticks(range(0,100,10))
plt.legend(bbox_to_anchor = (1.04,1), borderaxespad = 0)
plt.show()

