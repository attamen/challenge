a=int(input("시작값>"))
b=int(input("끝값>"))
even=0
odd=0
sum=0

for i in range(a,b+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
    sum+=i
    
print(even)
print(odd)
print(sum)
print(sum/b-a+1)



        