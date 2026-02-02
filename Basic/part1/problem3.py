''' Read n numbers from input, and print the average of the numbers excluding the highest and lowest number.
If there are less than 3 numbers, print 0.
[1,2,3,4,100] → 3
[1,1,5,5,10,8,7] → 5
[-10,-4,-2,-4,-2,0] → -3'''

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

total = sum(arr) - max(arr) - min(arr)
remain = n - 2
if n < 3:
    print(0)
else:
    print(total // remain)
