age = int(input("What is your age: "))
if age <= 17:
    print('You are a minor')
elif age >= 18 and age <= 36:
    print ('You are a youth')
else:
    print ('You are an elder')
