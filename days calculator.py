age = int(input("What is your current age? "))
age_end=int(input("what is the age you want to live till? "))
age_left=int(age_end-age)
d=int(age_left*365)
w=int(age_left*52)
m=int(age_left*12)
print(f"You have {d} days, {w} weeks, and {m} months left.")  #use {} inside print function to print value of variable
