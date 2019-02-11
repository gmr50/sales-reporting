import os
import pandas as pd 


filename = "sales-201710.csv"
data = pd.read_csv(filename)


totalSales = data["sales price"].sum()


def month_lookup(month):
	year_month={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return year_month[month]


month = month_lookup(filename[-6:-4]) # TODO: get from file name or date values
year = int(filename[6:10]) # TODO: get from file name or date values



#print(date)

print("SALES REPORT: " + str(month) + " " + str(year))
print("TOTAL SALES :" + str(totalSales))