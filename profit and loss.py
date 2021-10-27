def Profit(costPrice, sellingPrice) :

    profit = (sellingPrice - costPrice)

    return profit

def Loss(costPrice, sellingPrice) :

    loss =(costPrice - sellingPrice)

    return loss

if __name__ == "__main__" :
    costPrice = int(input("Please enter the cost price (CP)"))
    sellingPrice= int(input("Please enter the selling price (SP)"))

    if sellingPrice == costPrice :
        print("no profit or loss")
    
    elif sellingPrice > costPrice :
        print("$" ,Profit (costPrice, sellingPrice), "Profit")
    
    else:
        print("$" ,Loss (costPrice, sellingPrice), "Loss")