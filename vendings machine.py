Vending_items=(
"___________________________________________________\n"
"|             Sanads Vending Machine              |\n"
"|-------------------------------------------------|\n"
"|                   Categories                    |\n"
"|-------------------------------------------------|\n"
"|1)   Drinks                                      |\n"
"|2)   Snacks                                      |\n"
"|3)   Beverages                                   |\n"
"|4)   Soft Drinks                                 |\n"
"|5)   Chocolates                                  |\n"
"|_________________________________________________|\n")
Vending_drinks=(
"_____________________________________________\n"
"|                 Drinks                    |\n"
"|-------------------------------------------|\n"
"| Code |          Item             | Price  |\n"
"|-------------------------------------------|\n"
"| 101  |          Water            |  1AED  |\n"
"| 102  |      Sparkling Water      |  3AED  |\n"
"| 103  |   Double Chocolate milk   |  4AED  |\n"
"| 104  |    Capri-Sun cocktail     |  2AED  |\n"
"| 105  |     Melco Mango Juice     |  3AED  |\n"
"|___________________________________________|\n")

Vending_snacks=(
"_____________________________________________\n"
"|                 Snacks                    |\n"
"|-------------------------------------------|\n"
"| Code |          Item             | Price  |\n"
"|-------------------------------------------|\n"
"| 201  |     Lays spicy chips      |  3AED  |\n"
"| 202  |    Lays French cheese     |  3AED  |\n"
"| 203  |      Chilli Peanuts       |  2AED  |\n"
"| 204  |       Chicken Puff        |  5AED  |\n"
"| 205  |         Veg Puff          |  4AED  |\n"
"| 206  |      Chicken Sandwich     |  6AED  |\n"
"| 207  |    Chocolate Croissant    |  2AED  |\n"
"|___________________________________________|\n")

Vending_beverage=(
"_____________________________________________\n"
"|               Beverages                   |\n"
"|-------------------------------------------|\n"
"| Code |          Item             | Price  |\n"
"|-------------------------------------------|\n"
"| 301  |          Chai             |  2AED  |\n"
"| 302  |         Coffee            |  3AED  |\n"
"| 303  |       Cappuccino          |  3AED  |\n"
"| 304  |      Hot Chocolate        |  3AED  |\n"
"|___________________________________________|\n"
)
vending_softd=(
"_____________________________________________\n"
"|              Soft Drinks                  |\n"
"|-------------------------------------------|\n"
"| Code |          Item             | Price  |\n"
"|-------------------------------------------|\n"
"| 401  |      Mountain Dew         |  3AED  |\n"
"| 402  |          7up              |  3AED  |\n"
"| 403  |     Barbican lemon        |  3AED  |\n"
"| 404  |         Pepsi             |  3AED  |\n"
"| 405  |       Coca-Cola           |  3AED  |\n"
"|___________________________________________|\n")

vending_choc=(
"_____________________________________________\n"
"|               Chocolates                  |\n"
"|-------------------------------------------|\n"
"| Code |          Item             | Price  |\n"
"|-------------------------------------------|\n"
"| 501  |      M&m chocolate        |  4AED  |\n"
"| 502  |       M&m peanuts         |  4AED  |\n"
"| 503  |        Snickers           |  4AED  |\n"
"| 504  |         KitKat            |  4AED  |\n"
"| 505  |    Reese choco cups       |  6AED  |\n"
"| 506  |      Diary Milk Bar       |  4AED  |\n"
"|___________________________________________|\n")

vending_list=[
    {'code':101,'name':'Water','price':1,'stock':10},
    {'code':102,'name':'Sparkling Water','price':3,'stock':1},
    {'code':103,'name':'Double Chocolate milk','price':4,'stock':3},
    {'code':104,'name':'Capri-sun cocktail','price':2,'stock':0},
    {'code':105,'name':'Melco mango juice','price':3,'stock':10},
    {'code':201,'name':'Lays spicy chips','price':3,'stock':5},
    {'code':202,'name':'Lays French cheese','price':3,'stock':6},
    {'code':203,'name':'Chilli Peanuts','price':2,'stock':6},
    {'code':204,'name':'Chicken Puff','price':5,'stock':0},
    {'code':205,'name':'Veg Puff','price':4,'stock':4},
    {'code':206,'name':'Chicken Sandwich','price':6,'stock':10},
    {'code':207,'name':'Chocolate Croissant','price':2,'stock':10},
    {'code':301,'name':'Chai','price':2,'stock':7},
    {'code':302,'name':'Coffee','price':3,'stock':10},
    {'code':304,'name':'Hot Chocolate','price':3,'stock':8},
    {'code':401,'name':'Mountain Dew','price':3,'stock':10},
    {'code':402,'name':'7up','price':3,'stock':10},
    {'code':403,'name':'Barbican lemon','price':5,'stock':10},
    {'code':404,'name':'Pepsi','price':3,'stock':10},
    {'code':405,'name':'Coca-Cola','price':3,'stock':10},
    {'code':501,'name':'M&m chocolate','price':4,'stock':1},
    {'code':502,'name':'M&m peanuts','price':4,'stock':2},
    {'code':503,'name':'Snickers','price':4,'stock':10},
    {'code':504,'name':'KitKat','price':4,'stock':0},
    {'code':505,'name':'Reese choco cups','price':6,'stock':10},
    {'code':506,'name':'Diary Milk Bar','price':7,'stock':10},
]
def vending():
    a=0
    m=0
    total=0
    balance=0
    while a==0:
        print(Vending_items)
        print("Welcome To Sanads vending machine")
        money=int(input("Please input the amount of money you would like to deposit to make a purchase-\nand make sure you account for 5% VAT"))
        if money<=0:
            print("Invalid Amount!")
            vending()
        else:
            m=m+money
        choice=int(input("Enter the code of your desired category-"))
        if choice>5 or choice<0:
            print("Invalid option!")
            vending()

        if choice==1:
            print(Vending_drinks)
            choice_1=int(input("Please enter the desired item to purchase")) 
            for i in vending_list:
                if choice_1==i['code'] and i['stock']==0:
                    print("Sorry no stock available")
                    a=1

                if choice_1==i['code'] and m<(i['price']*1.05):
                    print("Insufficient Funds! your money has been returned, please try again")
                    a=1
                if choice_1==i['code'] and m>(i['price']*1.05) and i['stock']>0:
                    print(
                        "________________________________\n"
                        "you have selected",i["name"],'\n'
                        "________________________________\n")
                    total=(total+i['price'])*1.05
                    balance=money-total
                    if m==total:
                        balance=0
                    print("_______________________________")
                    print("------------Reciept------------")
                    print("-",i['name'],'       ',i['price'],'AED')
                    print("-------------------------------")
                    print("Total-", total,'AED')
                    print("Balance-",balance,'AED')
                    print("VAT-",total-i['price'])
                    print("----Thank you for shopping!----")
                    print("_______________________________")
                    a=1
        if choice==2:
            print(Vending_snacks)
            choice_1=int(input("Please enter the desired item to purchase")) 
            for i in vending_list:
                if choice_1==i['code'] and i['stock']==0:
                    print("Sorry no stock available")
                    a=1

                if choice_1==i['code'] and m<(i['price']*1.05):
                    print("Insufficient Funds! your money has been returned, please try again")
                    a=1
                if choice_1==i['code'] and m>(i['price']*1.05) and i['stock']>0:
                    print(
                        "________________________________\n"
                        "you have selected",i["name"],'\n'
                        "________________________________\n")
                    total=(total+i['price'])*1.05
                    balance=money-total
                    if m==total:
                        balance=0
                    print("_______________________________")
                    print("------------Reciept------------")
                    print("-",i['name'],'       ',i['price'],'AED')
                    print("-------------------------------")
                    print("Total-", total,'AED')
                    print("Balance-",balance,'AED')
                    print("VAT-",total-i['price'])
                    print("----Thank you for shopping!----")
                    print("_______________________________")
                    a=1
        if choice==3:
            print(Vending_beverage)
            choice_1=int(input("Please enter the desired item to purchase")) 
            for i in vending_list:
                if choice_1==i['code'] and i['stock']==0:
                    print("Sorry no stock available")
                    a=1

                if choice_1==i['code'] and m<(i['price']*1.05):
                    print("Insufficient Funds! your money has been returned, please try again")
                    a=1
                if choice_1==i['code'] and m>(i['price']*1.05) and i['stock']>0:
                    print(
                        "________________________________\n"
                        "you have selected",i["name"],'\n'
                        "________________________________\n")
                    total=(total+i['price'])*1.05
                    balance=money-total
                    if m==total:
                        balance=0
                    print("_______________________________")
                    print("------------Reciept------------")
                    print("-",i['name'],'       ',i['price'],'AED')
                    print("-------------------------------")
                    print("Total-", total,'AED')
                    print("Balance-",balance,'AED')
                    print("VAT-",total-i['price'])
                    print("----Thank you for shopping!----")
                    print("_______________________________")
                    a=1
        if choice==4:
            print(vending_softd)
            choice_1=int(input("Please enter the desired item to purchase")) 
            for i in vending_list:
                if choice_1==i['code'] and i['stock']==0:
                    print("Sorry no stock available")
                    a=1

                if choice_1==i['code'] and m<(i['price']*1.05):
                    print("Insufficient Funds! your money has been returned, please try again")
                    a=1
                if choice_1==i['code'] and m>(i['price']*1.05) and i['stock']>0:
                    print(
                        "________________________________\n"
                        "you have selected",i["name"],'\n'
                        "________________________________\n")
                    total=(total+i['price'])*1.05
                    balance=money-total
                    if m==total:
                        balance=0
                    print("_______________________________")
                    print("------------Reciept------------")
                    print("-",i['name'],'       ',i['price'],'AED')
                    print("-------------------------------")
                    print("Total-", total,'AED')
                    print("Balance-",balance,'AED')
                    print("VAT-",total-i['price'])
                    print("----Thank you for shopping!----")
                    print("_______________________________")
                    a=1
        if choice==5:
            print(vending_choc)
            choice_1=int(input("Please enter the desired item to purchase")) 
            for i in vending_list:
                if choice_1==i['code'] and i['stock']==0:
                    print("Sorry no stock available")
                    a=1

                if choice_1==i['code'] and m<(i['price']*1.05):
                    print("Insufficient Funds! your money has been returned, please try again")
                    a=1
                if choice_1==i['code'] and m>(i['price']*1.05) and i['stock']>0:
                    print(
                        "________________________________\n"
                        "you have selected",i["name"],'\n'
                        "________________________________\n")
                    total=(total+i['price'])*1.05
                    balance=money-total
                    if m==total:
                        balance=0
                    print("_______________________________")
                    print("------------Reciept------------")
                    print("-",i['name'],'       ',i['price'],'AED')
                    print("-------------------------------")
                    print("Total-", total,'AED')
                    print("Balance-",balance,'AED')
                    print("VAT-",total-i['price'])
                    print("----Thank you for shopping!----")
                    print("_______________________________")
                    a=1
def reorder():
    print("Do you want to buy more items?")
    choice_2=int(input("1-yes\n2-no\n-"))
    if choice_2==1:
        vending()
    elif choice_2==2:
        print("Thank you for shopping, have a great day")
    else:
        print("invalid option")
        reorder()
vending()
reorder()