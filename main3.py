#find the sum of a list
l=[2,7,8,0,9,12,45]
print("Original list:",l)
#var to store the sum
count=0
for i in l:
    count+=i
#find the avg of the list
avg=count/len(l)
print(f"The sum of the list is {count}")
print(f"The average of the list is {avg}")
#sort the list
l.sort()
print("The smallest element is",l[0])
print("The largest element is:",l[-1])