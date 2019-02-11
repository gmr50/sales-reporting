import pandas as pd 


data = pd.read_csv('sales-201710.csv')


totalSales = data["sales price"].sum()



print("TOTAL SALES REPORT:" + str(totalSales))