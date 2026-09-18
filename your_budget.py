#AL, Your Budget

income = float(input("What is your monthly income: "))
rent = float(input("What is your monthly rent: "))
utilities = float(input("What is are monthly utilities: "))
groceries = float(input("What are your monthly groceries: "))
transportation = float(input("What is your monthly transportation: "))

rent_1 = int(round((rent / income) * 100))
utilities_1 = int(round((utilities / income) * 100)) 
groceries_1 = int(round((groceries / income) * 100)) 
transportation_1 = int(round((transportation / income) * 100)) 

savings = income * 0.10
savings_1 = 10 


spending_money = income - rent - utilities - groceries - transportation - savings

print(f"You rent is ${rent} and is {rent_1} percent of your income")
print(f"You utilities are ${utilities} and is {utilities_1} percent of your income")
print(f"You groceries are ${groceries} and is {groceries_1} percent of your income")
print(f"You transportation is ${transportation} and is {transportation_1} percent of your income")

print(f"You should save ${savings} and is {savings_1} percent of your income")
print(f"You have ${spending_money} of spending money each month")
