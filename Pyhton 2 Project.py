#year = int(input("What year do you want to check?"))

#if year % 4 == 0:
    #print(str(year) + " is a leap year")
#else:
        #print(str(year) + " is not a leap year")





answer = "y"
my_list = input("Insert a list of 4 names : ").split(", ")

while answer == "y":
    name = input("Enter a name from your contact:")
    my_list.append(name)
    answer = input("Anything you want to add? (y/n):")
my_list.sort()
print(my_list)


    






