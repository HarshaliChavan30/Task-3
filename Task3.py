import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('D://Task-3//householdtask3.csv')
a = data.head(10)
print(a)
print('**********************************************************')


#scatter plot with year against own 

plt.scatter(data["year"] , data ['own'])
print('**************************************************************')


# Adding title to the plot

plt.title("scatter plot")

#Setting x and y label

plt.xlabel ("year")
plt.ylabel ("own")

#Showing the plot
plt.show()
print('****************************************************************')

#line chart with year against own 

plt.plot(data['year'])
plt.plot(data['own'])

#Adding title to the plot 

plt.title("line chart")
#setting x and y labels

plt.xlabel('year')
plt.ylabel('own')

#Showning the chart

plt.show()
print("***************************************************************")

#Bar chart 
#Scatter plot with year against own 

plt.bar(data['year'] , data ['own'])

#Adding title to the plot

plt.title("Bar chart")

#Setting x and y labels

plt.xlabel('year')
plt.ylabel('own')

#Shownig the chart

plt.show()
print("************************************************************")

#Plotting Histogram 

plt.hist(data['income'])
plt.title('histogram')

plt.show()