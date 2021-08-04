import math

# Expenses in USD
# USDtoCFA:
cfa2usd = 530                #buy_rate
usd2cfa = 555                #sell_rate

# Product cost to the benin port
proCost = 85760 + 158 + 2618.21 + 1528.29

# Customs fee + moto
customsCost = 5384784 + 100000 + 350000

# Monthly Security agency charges
monthlySecuCost = 100000*0

# Monthly Storage warehouse cost
monthlyStorageCost = 50000

# Monthly salary cost
monthlySalaryCost = 1*30000 + 70000

def totalCostusd(cfa2usd, n1, n2):
	total =  proCost + (customsCost + monthlySalaryCost*n1
	         + monthlySecuCost*n1 + monthlyStorageCost*n2)/cfa2usd
	return math.ceil(total)

total_cost_cfa = totalCostusd(cfa2usd, 12, 12)*usd2cfa

unit_cost_cfa = math.ceil(total_cost_cfa/190)
unit_cost = math.ceil(unit_cost_cfa/cfa2usd)

# Total revenue
def totalRevenue(unitPrice, quantity):
	return math.floor(unitPrice*quantity)

total_revenue = totalRevenue(415000, 40) + totalRevenue(455000, 150)

# Profit
def profit(total_revenue, total_cost):
	return math.floor(total_revenue - total_cost_cfa)

profit = profit(total_revenue, total_cost_cfa)

def ROI(profit, total_cost):
	return round(100*(profit/total_cost))

myReturn = ROI(profit, total_cost_cfa)

print("unit_cost: {} \nunit_cost_cfa: {} \ntotal_revenue_cfa: {} \nprofi_cfa: {} \nROI: {}".format(unit_cost, unit_cost_cfa, total_revenue, profit, myReturn))

# >>> unit_cost_cfa
# 287815.0
# >>> unit_cost_cfa*1.75
# 503676.25
# >>> unit_cost_cfa*1.5
# 431722.5
# >>> unit_cost_cfa*1.5 - unit_cost_cfa
#143907.5
#>>> 150000*190
#28500000
#>>> 150000*190/550
#51818.18181818181
