from datetime import datetime
cart = []                              
cart_wordbook ={}                             
name = input("Enter full name: ")     
id = input("Enter CitizenShip number: ") 

def read_cart():
    stock = open('data.txt','r')               
    stock_lines = stock.readlines()             
    wordbook = {}                          

    for i in range(1,len(stock_lines) + 1): 
        wordbook[i] = stock_lines[i-1].split(",")     
    
    for i in range(1, len(wordbook) + 1):  
        wordbook[i].pop(-1)                 

    return wordbook



    



# date and time
year = str(datetime.now().year)
month = str(datetime.now().month)
day = str(datetime.now().day)
hour = str(datetime.now().hour)
minutes = str(datetime.now().minute)
date_today = year + " - " + month + " - " + day + " , " + hour + " : " + minutes 



while True: 
    try:
        days = int(input("Enter the number of days you want to rent the costume for: "))
        break
    except:
        print("Enter valid data")


wordbook = read_cart()
def rent():

    try:
        
        print("--------------------------------------------------------------------------------------------------")
        print("  ID\t\tCostume\t\t\tCostume Brand\t\tPrice\t\tQuantity") 
        print("--------------------------------------------------------------------------------------------------\n")
    
        for i in range(1, len(wordbook)+1):
            print("  {0}\t\t{1}\t\t{2}\t\t{3}\t\t\t{4}\n".format(i, wordbook[i][0],wordbook[i][1],wordbook[i][2],wordbook[i][3])) 
        print("--------------------------------------------------------------------------------------------------")

        user = int(input("Enter the ID of the costume you want to rent: "))    
        present = False 

        for i in range(1, len(wordbook) + 1):       
            if user == i:
                present = True      
                break
    
        if present == False: 
            print("\n\n")
            print("*******************************************")
            print("Please Enter a valid ID !!! ")
            print("*****************************************\n\n")
            rent()
        else:
         
            if int(wordbook[user][3]) == 0:
                print("\n\n")
                print("**************************************")
                print("Costume out of stock !!! ")
                print("**************************************\n\n")
                rent()
            else: 
                print("Costume ID is {0}\n\n".format(user))
                print("***********************")    
                print("Costume is available")
                print("***********************\n\n")

                user_req = int(input("Enter the Quantity of the costume: ")) 

                if int(wordbook[user][3]) < user_req:     
                    print("***********************************************************")
                    print("Quantity provided is greater than what we have in stock!!!")     
                    print("*************************************************************")
                    print(wordbook, "\n\n")
                    rent()
                else:

                    # remove $ from the price
                    count = 0
                    price = "" 

                    for i in wordbook[user][2]:
                        if count > 0: 
                            price = price + i 
                        count = count + 1
                    
                    
                    actual_price = "{:.2f}".format((int(price)/5) *user_req * days) 
           

                    cart.append([user,wordbook[user][0], wordbook[user][1], str(user_req), wordbook[user][2], actual_price ]) 
                    for i in range(1,len(cart)+1):
                        cart_wordbook[i] = cart[i-1]

                    print("Your cart:\n {0}".format(cart_wordbook))


                    wordbook[user][3]= str(int(wordbook[user][3]) - user_req)     

                    recheck_validation = False 

                    while recheck_validation == False:
                        recheck = input("Do you want to rent any thing else? (Y/N): ")
                        if recheck.upper() == "Y": 
                            rent()
                            recheck_validation = True
                        elif recheck.upper() == "N": 
                            recheck_validation = True
                            bill(name, id, days, date_today, cart_wordbook) 
                            print(wordbook)        
                            update_stock(wordbook) 
                            invoice(name, id, days, date_today, cart_wordbook) 
                            cart_(name, id, cart_wordbook, date_today) 
                            clear_() 
                            
                        else:
                            print("***********************")
                            print("  Enter either Y or N  ")
                            print("************************")
    except:
        print("*****************************")
        print("  Invalid input  ")
        print("******************************")
    
        


def bill(name, id, days, date_today, cart_wordbook):  
    print("Your bill:\n")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("  Name: "+name+"\t\t" + "ID: "+id +"\t\t"+ "For: "+ str(days) + " Day/s" +"\n  "+ date_today)
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("  Sno.\t\tCostume ID\t\tCostume Name\t\tBrand\t\tQuantity\trate\t\tTotal  ")
    print("-----------------------------------------------------------------------------------------------------------------------")
    for i in range(1, len(cart_wordbook) + 1): 
        print("  {0}\t\t{1}\t\t\t{2}\t\t{3}\t{4}\t\t{5}\t\t{6}  ".format(i,cart_wordbook[i][0], cart_wordbook[i][1], cart_wordbook[i][2], cart_wordbook[i][3],cart_wordbook[i][4], "$" + str(cart_wordbook[i][5])  )) # i-1 because i starts form 1 and list index starts from 0
    print("-----------------------------------------------------------------------------------------------------------------------")
    total_amount = float(0) 
    for i in range(1, len(cart_wordbook)+1):
        total_amount = total_amount + float(cart_wordbook[i][5])
                    
    print("Total Amount:","$" + str("{:.2f}".format(total_amount)))
    print("-----------------------------------------------------------------------------------------------------------------------")


def update_stock(wordbook):
    stock2 = open('data.txt','w')    
    for i in range(1, len(wordbook)+1):
        for j in range(4):          
            stock2.write(wordbook[i][j])           
            stock2.write(',')           
        stock2.write("\n")      
    stock2.close()
    

def invoice(name, id, days, date_today, cart_wordbook):
    invoice = open(name.upper()+" "+id+" rented"+".txt","w")
    invoice.write("Your bill:\n")
    invoice.write("-----------------------------------------------------------------------------------------------------------------------")
    invoice.write("\n")
    invoice.write("  Name: "+name+"\t\t" + "ID: "+id +"\t\t"+ "For: "+ str(days) + " Day/s" +"\n  "+ date_today)
    invoice.write("\n")
    invoice.write("-----------------------------------------------------------------------------------------------------------------------")
    invoice.write("\n")
    invoice.write("  Sno.\t\tCostume ID\t\tCostume Name\t\tBrand\t\tQuantity\trate\t\tTotal  ")
    invoice.write("\n")
    invoice.write("-----------------------------------------------------------------------------------------------------------------------")
    invoice.write("\n")
    for i in range(1, len(cart_wordbook) + 1): # i+1 becaust Sno starts form 1
        invoice.write("  {0}\t\t{1}\t\t\t{2}\t\t{3}\t{4}\t\t{5}\t\t{6}  ".format(i,cart_wordbook[i][0], cart_wordbook[i][1], cart_wordbook[i][2], cart_wordbook[i][3],cart_wordbook[i][4], "$" + str(cart_wordbook[i][5])  )) # i-1 because i starts form 1 and list index starts from 0
        invoice.write("\n")
    invoice.write("-----------------------------------------------------------------------------------------------------------------------")
    invoice.write("\n")
    total_amount = float(0) # local variable to store total amount
    for i in range(1, len(cart_wordbook)+1): # adds the prices in the cart and stores in total_amount
        total_amount = total_amount + float(cart_wordbook[i][5])
                    
    invoice.write("Total Amount: "+"$" + str("{:.2f}".format(total_amount)))# total as float with 2 digits after decimal
    invoice.write("\n")
    invoice.write("-----------------------------------------------------------------------------------------------------------------------")
    invoice.close()



def cart_(name, id, cart_wordbook, date_today):
    cart_p = open(name.upper()+" "+id+" rent cart"+".txt",'w')      
    for i in range(1, len(cart_wordbook)+1):            
        for j in range(6):        
            cart_p.write(str(cart_wordbook[i][j]))
            cart_p.write(',')           
        cart_p.write("\n")     
    cart_p.write(date_today)
    cart_p.write("\n")
    cart_p.close()
    return cart_p




def clear_():
    is_empty = False
    while is_empty == False:
        try:
            cart.pop() 
            cart_wordbook.popitem() 
        except:
            is_empty = True 
    
    return is_empty
    
