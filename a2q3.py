largest = None
smallest = None
while True:
        num = input("Enter a number: ")
        if num == "done":
            break
        print (num)
        n = int(num)
        if largest is None or largest<n:
            largest = n
        elif smallest is None or smallest>n:
             smallest = n
    
print ("Maximum", largest)
print ("Minimum", smallest)
