a=['suya','malar','thowfiya','abdullah','alfi']
b=[3000,7000,5000,6000,2000]

sender = input("enter the sender name:")
receiver = input("enter the receiver name:")
amount = int(input("enter amount"))

for i in a:
    if i==sender:
        print("sender is available")
        x=(a.index(i))
        print("sender balance amount:",b[x]-amount)

    elif i==receiver:
        print("receiver is available")
        y=(a.index(i))
        print("receiver full amount:",b[y]+amount)
        break
