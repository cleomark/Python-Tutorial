def computepay(h, r):
    if h <= 40:
        return (r * h)
    else:
        base = r * 40
        overtime = ((h - 40) * r) * 1.5
        totalpay = base + overtime
        return round(totalpay,2)


hrs = input("Enter Hours:")
rate = input("Input rate per hour:")

hours = float(hrs)
pay_per_hour = float(rate)

p = computepay(hours, pay_per_hour)
print("Pay", p)