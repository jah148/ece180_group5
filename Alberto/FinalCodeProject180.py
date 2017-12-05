import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''CSV was created using data that was not downloadable as a .csv or .xls file. The European
countries' data was accesed from EuroStat
(http://ec.europa.eu/eurostat/statistics-explained/index.php
/File:Employment_rate_of_recent_graduates,_EU-28,_2006-2016.png)'''

'''US data was found at the US Bureau of
Labor Statistics (https://www.bls.gov/opub/ted/2017
/unemployment-rate-2-point-5-percent-for-college-grads-7-point-7-percent-
for-high-school-dropouts-january-2017.htm).'''

'''The socioeconomic status of those without tertiary education is extremely
hindered compared to those of having completed this level of education. One
way this is noteable is through employment percentage'''

filename = 'Employment_College_Graduates_1-3years_graduated.csv'
assert isinstance(filename, str)
df = pd.read_csv(filename, delimiter='\t')

filename1 = 'Employment_without_Tertiary_Education.csv'
assert isinstance(filename1, str)
df1 = pd.read_csv(filename1)

def tertiaryGraph(df):
    '''There are 5 countries in which to graph. Using one plot would be
    extremely messy and hard to read. With each country getting its own plot,
    we can see how its employment based on tertiary education changes over
    time.'''

    assert isinstance(df, pd.core.frame.DataFrame)
    
    fig, ax = plt.subplots()
    fit = np.polyfit(df.Years, df.EU, deg=1)
    ax.plot(df.Years, fit[0] * df.Years + fit[1], color='red',label='Linear Regression')
    ax.plot(df.Years, df.EU, 'ko--',label='Data Points')
    plt.title("Percent of Employment of Tertiary Education Graduates: EU", fontweight='bold')
    plt.xlabel("Years", fontweight='bold')
    plt.ylabel("Percent of Employment", fontweight='bold')
    ax.legend()
    
    fig, ax = plt.subplots()
    fit = np.polyfit(df.Years, df.Germany, deg=1)
    ax.plot(df.Years, fit[0] * df.Years + fit[1], color='red',label='Linear Regression')
    ax.plot(df.Years, df.Germany, 'ko--',label='Data Points')
    plt.title("Percent of Employment of Tertiary Education Graduates: Germany", fontweight='bold')
    plt.xlabel("Years", fontweight='bold')
    plt.ylabel("Percent of Employment", fontweight='bold')
    ax.legend()

    fig, ax = plt.subplots()
    fit = np.polyfit(df.Years, df.Turkey, deg=1)
    ax.plot(df.Years, fit[0] * df.Years + fit[1], color='red',label='Linear Regression')
    ax.plot(df.Years, df.Turkey, 'ko--',label='Data Points')
    plt.title("Percent of Employment of Tertiary Education Graduates: Turkey", fontweight='bold')
    plt.xlabel("Years", fontweight='bold')
    plt.ylabel("Percent of Employment", fontweight='bold')
    ax.legend()

    fig, ax = plt.subplots()
    fit = np.polyfit(df.Years, df.UK, deg=1)
    ax.plot(df.Years, fit[0] * df.Years + fit[1], color='red',label='Linear Regression')
    ax.plot(df.Years, df.UK, 'ko--',label='Data Points')
    plt.title("Percent of Employment of Tertiary Education Graduates: UK", fontweight='bold')
    plt.xlabel("Years", fontweight='bold')
    plt.ylabel("Percent of Employment", fontweight='bold')
    ax.legend()

    fig, ax = plt.subplots()
    fit = np.polyfit(df.Years, df.US, deg=1)
    ax.plot(df.Years, fit[0] * df.Years + fit[1], color='red',label='Linear Regression')
    ax.plot(df.Years, df.US, 'ko--',label='Data Points')
    plt.title("Percent of Employment of Tertiary Education Graduates: US", fontweight='bold')
    plt.xlabel("Years", fontweight='bold')
    plt.ylabel("Percent of Employment", fontweight='bold')
    ax.legend()

    plt.show()

def secondaryGraph(df1):
    '''There are 5 countries in which to graph. Using one plot would be
    extremely messy and hard to read. With each country getting its own plot,
    we can see how its employment based on tertiary education changes over
    time.'''
    
    assert isinstance(df1, pd.core.frame.DataFrame)
    
    fig, ax = plt.subplots()
    fit = np.polyfit(df1.Years, df1.EU, deg=1)
    ax.plot(df1.Years, fit[0] * df1.Years + fit[1], color='blue',label='Linear Regression')
    ax.plot(df1.Years, df1.EU, 'go--',label='Data Points')
    plt.title("Percent of Employment of Secondary Education Only: EU", fontweight='bold')
    plt.xlabel("Years", fontweight='bold')
    plt.ylabel("Percent of Employment", fontweight='bold')
    ax.legend()

    fig, ax = plt.subplots()
    fit = np.polyfit(df1.Years, df1.Germany, deg=1)
    ax.plot(df1.Years, fit[0] * df1.Years + fit[1], color='blue',label='Linear Regression')
    ax.plot(df1.Years, df1.Germany, 'go--',label='Data Points')
    plt.title("Percent of Employment of Secondary Education Only: Germany", fontweight='bold')
    plt.xlabel("Years", fontweight='bold')
    plt.ylabel("Percent of Employment", fontweight='bold')
    ax.legend()

    fig, ax = plt.subplots()
    fit = np.polyfit(df1.Years, df1.Turkey, deg=1)
    ax.plot(df1.Years, fit[0] * df1.Years + fit[1], color='blue',label='Linear Regression')
    ax.plot(df1.Years, df1.Turkey, 'go--',label='Data Points')
    plt.title("Percent of Employment of Secondary Education Only: Turkey", fontweight='bold')
    plt.xlabel("Years", fontweight='bold')
    plt.ylabel("Percent of Employment", fontweight='bold')
    ax.legend()

    fig, ax = plt.subplots()
    fit = np.polyfit(df1.Years, df1.UK, deg=1)
    ax.plot(df1.Years, fit[0] * df1.Years + fit[1], color='blue',label='Linear Regression')
    ax.plot(df1.Years, df1.UK, 'go--',label='Data Points')
    plt.title("Percent of Employment of Secondary Education Only: UK", fontweight='bold')
    plt.xlabel("Years", fontweight='bold')
    plt.ylabel("Percent of Employment", fontweight='bold')
    ax.legend()

    fig, ax = plt.subplots()
    fit = np.polyfit(df1.Years, df1.US, deg=1)
    ax.plot(df1.Years, fit[0] * df1.Years + fit[1], color='blue',label='Linear Regression')
    ax.plot(df1.Years, df1.US, 'go--',label='Data Points')
    plt.title("Percent of Employment of Secondary Education Only: US", fontweight='bold')
    plt.xlabel("Years", fontweight='bold')
    plt.ylabel("Percent of Employment", fontweight='bold')
    ax.legend()

    plt.show()

'''Resulting plots from called functions'''
tertiaryGraph(df)
secondaryGraph(df1)
