#print("Hello World")


#string1 = "Paragliding is"
#string2 = "daring"
#string3 = string1 + string2

#print(string3) #outputs "Paragliding isdaring"


#fries = 30
#fries = str(30)
#print(fries)




#animals = ["lion", "elephant", "giraffe" , "cheetah"] 

#for x in animals:
# print(x)



#var1 = int(input("Insert a number"))
#var2 = int(input("Insert a number"))

#for x in range(var1 + var2 ):
    #print(x)


##my_list = [int(n) for n in input("Input a list of numbers").split()]
###count the numbers that have zero
##for x in my_list:
##    if x == 0 : 
##        print(x)
##    else :
##        print("Unavaible")


##
##flowers = [int(n) for n in input("How many blossoms are on each tree?").split()]
##
##def orchard(flowers):
##    if len(flowers) == 1:
##        print(flowers[0] + flowers[1])
##
##    else:
##        mid = len(flowers) // 2
##        first_half = flowers[:mid]
##        second_half = flowers[mid:]
##        
##        
##        orchard(first_half)
##        orchard(second_half)
##
##
##orchard(flowers)
##
##
##
##answer = int(input("Insert 4 numbers "))).split()
##def add_list(my_list):
##	if n <= 1:
##		return my_list[0]
##	else:
##		return my_list[0] + add_list(my_list[1:])
##
##print(add_list(answer))
##    


##def bubbleSort(arr):
##    for num in arr:
##        if arr[num] > arr[num+1]:
##            arr[num], arr[num+1] = arr[num+1], arr[num]
##    return arr
##    
##arr1 = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
##bubbleSort(arr1)


##def selection_list(sort_list):
##    for i in range(1, len(sort_list)):
##        key = sort_list[i]
##    j = i-1
##    while j >= 0 and key < sort_list[j] :
##            sort_list[j + 1] = sort_list[j]
##            j -= 1
##            sort_list[j + 1] = key
##
##arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
##
##number = int(input("Enter a number: "))
##
##arr.append(number)
##
##selection_list(arr)
##
##print(arr)


##answer = int(input("Enter a number 0-100: "))
##
##arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
##
##arr.append(answer)
##
##
##def mergeSort(sort_list):
##    if len(sort_list) > 1:
## 
##        mid = len(sort_list)//2
##        L = sort_list[:mid]
##        R = sort_list[mid:]
##        mergeSort(L)
##        mergeSort(R)
##
##        i = j = k = 0 
##        
##        while i < len(L) and j < len(R):
##            if L[i] < R[j]:
##                sort_list[k] = L[i]
##                i += 1
##            else:
##                sort_list[k] = R[j]
##                j += 1
##            k += 1
##                    
##        while i < len(L):
##                sort_list[k] = L[i]
##                i += 1
##                k += 1
##
##        while j < len(R):
##                sort_list[k] = R[j]
##                j += 1
##                k += 1
##
##mergeSort(arr)
##print(arr)


