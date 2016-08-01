list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)
for num in list1:
    new = num * 3
    if new % 2 ==0:
        print(new)
    else:
        print("No")


