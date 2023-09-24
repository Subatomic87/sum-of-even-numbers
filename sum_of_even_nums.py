x=0
y=0
numbers=list()
while(x != "stop"):
 x=(input("enter a bunch of numbers and I will find the sum of the even ones; type 'stop' all lower case when done entering numbers "))
 if(x=="stop"):
     break
 x=int(x)
 numbers.append(x)
 y=y+1
# print(numbers)
b=0
even=list()
for i in range(y):
 z=numbers[b]
 b=b+1
 if (z%2==0):
     even.append(z)
#print(even)
print(sum(even))