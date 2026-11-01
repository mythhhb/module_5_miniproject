import expence
import report 
while True:
    print("==EXPENCE TRACKER==")
    dics = expence.discription()
    cat = expence.catagory()
    amount = expence.amount()
    date = expence.date()

    ch = input("ADD ANOTHER EXPENCE?(y/n):").lower()
    if ch == "n":
        break


print("====MONTHLY REPORT====")
print("date: ",expence.now.date())
print("DISCRIPTION: " , dics)
print("CATAGORY: " , cat)
print("Amount: " ,amount)
print("REPORT MONTH",expence.now.date())

