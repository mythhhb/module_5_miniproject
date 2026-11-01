import datetime
now = datetime.datetime.now()


def discription():
    dis = input("enter discription: ")
    return dis
def catagory():
    cat  =  input("enter catagory: ")
    return cat
def amount():
    am = float(input("enter amount:"))
    return am
def date(date = now.date()):
    return date
