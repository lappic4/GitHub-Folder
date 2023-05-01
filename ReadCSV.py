import pandas as pd
import matplotlib.pyplot as mt

Main = pd.read_csv(r"C:\Users\dimit\OneDrive\Desktop\AAPL.csv")

x = [1,6]
y = [2,7]

mt.scatter(x,y,color = 'r')
mt.show()
