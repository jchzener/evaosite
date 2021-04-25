import math

# Expenses in USD
# USDtoCFA: 
buy_rate = 530 
sell_rate = 550 

# Product cost to the benin port
proCost = 85760 + 158

# Customs fee
customsCost = 5000000

# Monthly Security agency charges 
monthlySecuCost = 100000

# Monthly Storage warehouse cost
monthlyStorageCost = 80000

def totalCostusd(buy_rate, n1, n2):
	total =  proCost + customsCost/buy_rate + monthlySecuCost*n1/buy_rate + monthlyStorageCost*n2/buy_rate
	return math.ceil(total)


total_cost_cfa = totalCostusd(530, 8, 8)*sell_rate

unit_cost = math.ceil(total_cost_cfa/190)
unit_cost_cfa = math.ceil(unit_cost*sell_rate)

# Total revenue
def totalRevenue(unitPrice, quantity):
	return math.floor(unitPrice*quantity)

total_revenue = totalRevenue(430000, 190)
# Profit
def profit(total_revenue, total_cost):
	return math.floor(total_revenue - total_cost_cfa)

profit = profit(total_revenue, total_cost_cfa)

def ROI(profit, total_cost):
	return round(100*(profit/total_cost))

myReturn = ROI(profit, total_cost_cfa)

print("unit_cost: {} \nunit_cost_cfa: {} \ntotal_revenue_cfa: {} \nprofi_cfa: {} \nROI: {}".format(unit_cost, unit_cost_cfa, total_revenue, profit, myReturn))

#>>> unit_cost_cfa
#287815.0
#>>> unit_cost_cfa*1.75
#503676.25
#>>> unit_cost_cfa*1.5
#431722.5
#>>> unit_cost_cfa*1.5 - unit_cost_cfa
#143907.5
#>>> 150000*190
#28500000
#>>> 150000*190/550
#51818.181818181816
