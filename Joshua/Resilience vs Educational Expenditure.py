import pandas as pd
import matplotlib.pyplot as plt

'''
This py script generates a scatter plot of the percentage amount of each
country's poorest 25% of students who are considered resilient students vs. the percentage amount of each country's annual budget that is allocated to
public education.

Resilient students are those who are in the bottom 25% of their country in
terms of economic factors, but are in the top 25% of all students in all
countries in terms of academic performance.
'''

# csv files in local directory 
f_expenditure = "Public Expenditure by Country.csv"
f_resilient = "Resilient Students.csv"


# formatting dataframes
resilient_df = pd.read_csv(f_resilient)
resilient_df = resilient_df.set_index("Country")

expenditure_df = pd.read_csv(f_expenditure)
expenditure_df = expenditure_df.set_index("Country")

# joining df's
res_exp_df = expenditure_df.join(resilient_df)

# creating the scatter plot
ax = res_exp_df.plot.scatter(x = "(%)Public Expenditure", y = "(%)Resilient Disadvantaged Students")

# adding labels to data points
for k, v in res_exp_df.iterrows():
  ax.annotate(k, v, xytext=(5,5), textcoords="offset points", fontsize=8)
plt.title("(%)Resilient Students vs (%)Public Expenditure")
plt.show()

