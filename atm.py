amount = 1000
while True:
    p = input("Enter the process type: ")
    if p == "Q":
        break
    elif p == "1":
        print("You have {}$ currently...".format(amount))
    elif p == "2":
        while True:
            if amount > 0:
                print("You have {}$ currently...".format(amount))
                am_rec = float(input("Amount of money: "))
                if am_rec <= amount:
                    amount -= am_rec
                    print("Pull your cash money!\nRest money amount: {}".format(amount))
                    break
                else:
                    print("Please enter a valid amount!")
                    continue
            else:
                print("Process invalid! No money left in your account!")
                break
    elif p == "3":
        pass
    else:
        print("Please enter a valid process!")
