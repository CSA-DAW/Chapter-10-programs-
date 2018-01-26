#Denver Wydermyer
#Computer Prgramming
#1/24/18


mylist = ["James","Gloria","Sara","Dante","Mahima"]#My list with the five names

def thelist(mylist):# function that will add in the new names and passed in mylist to the function 
    name = input("What name would you like to use: ")
    newlist = mylist.append(name)
    print(mylist)
    name2 = input("Would you like to add anymore names: ")
    if name2 == "yes": # if they want to continue then they van but if not they can just see the new name list 
        thelist(mylist)
    else:
        print(mylist)
thelist(mylist)
    
    



