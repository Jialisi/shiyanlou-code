N = 10
sum = 0
count = 0
print("please input 10 numbers:")
while count < N:
    number = float(input())
    sum = sum + number
    count =  count + 1
print('count:{}'.format(count))
average = sum / count
print('N = {}, Sum = {}'.format(N, sum))
print('Average = {:.2f}'.format(average))

