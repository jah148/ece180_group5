import pandas as pd
import matplotlib.pyplot as plt

'''
This py script generates a scatter plot of the percentage amount of each
country's poorest 25% of students who are considered low-achieving students vs. the percentage amount of each country's annual budget that is allocated to
public education.

Low-achieving students are those who are in the bottom 25% of their country in
terms of economic factors, and are in the bottom 25% of all students in all
countries in terms of academic performance.
'''

# csv files in local directory 
f_expenditure = "Public Expenditure by Country.csv"
f_low = "Low Achieving Students.csv"


# formatting dataframes
low_df = pd.read_csv(f_low)
low_df = low_df.set_index("Country")

expenditure_df = pd.read_csv(f_expenditure)
expenditure_df = expenditure_df.set_index("Country")

# joining df's
low_exp_df = expenditure_df.join(low_df)

# creating the scatter plot
ax = low_exp_df.plot.scatter(x = "(%)Public Expenditure", y = "(%)Low-achieving Disadvantaged Students")

# adding labels to data points
for k, v in low_exp_df.iterrows():
  ax.annotate(k, v, xytext=(5,5), textcoords="offset points", fontsize=8)
plt.title("(%)Low-achieving Students vs (%)Public Expenditure")
plt.show()
