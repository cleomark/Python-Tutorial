largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        number = int(num)
        if largest == None or number > largest: 
            largest = number
        elif smallest == None or number < smallest:
            smallest = number
    except:
        print("That's not an integer! Try again...")
        continue

print("Maximum", largest)
print("Minimum is", smallest)