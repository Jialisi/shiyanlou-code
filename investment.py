#!/usr/bin/env python3
amount = float(input('Enter amount:'))
inrate = float(input('Enter Interest rate:'))
period = int(input('Enter period:'))
value = 0
year = 1
while year <= period:
    value = amount + (inrate * amount)
    print("Year {} Rs. {:.2f}".format(year,value))
    amount = value
    year = year + 1
#str.format()
#Year {} Rs. {:.2f}".format(year, value) 字符串格式化
