# print("hello"[4])
#tip calculator

print("welcome to tip calculator")

total_bill=float(input("what was the total bill"))

select_percent=int(input("what percentage of tip would you like to give? 10,12 or 15"))

if(select_percent==10):
 percent=10/100
elif(select_percent==12):
 percent=12/100
else :
 percent=15/100

total_bill+=percent



splitt=int(input("how many people to split the bill?"))

print("each person should pay :")
amt=total_bill/splitt
print(round(amt,2))
