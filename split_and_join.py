#Denver Wydermyer
#Computer Prgramming
#1/25/18

def split():# splits the string by spaces 
    string = "My name is Jose"
    split = string.split(' ')
    print(split)
split()

def split2(): # splits string by the ; 
    string = "user1;user2;user3"
    split = string.split(";")
    print(split)
split2()

def join(): # joins the list by the " " 
    thelist = ['this','is','a','sentence']
    glue = " "
    mylist = glue.join(thelist)
    print(mylist)
join()

