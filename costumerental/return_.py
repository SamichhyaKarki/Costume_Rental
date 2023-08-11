import rent
from datetime import *

name = rent.name
id = rent.id
rent.cart = []
rent.cart_wordbook = {}


# date and time
year = str(datetime.now().year)
month = str(datetime.now().month)
day = str(datetime.now().day)
hour = str(datetime.now().hour)
minutes = str(datetime.now().minute)
date_today = year + " - " + month + " - " + day + " , " + hour + " : " + minutes 





def rtrn():
    try:
        #read the data that the customer has previously rented
        rented_items = open(name.upper()+" "+id+" rent cart"+".txt",'r')
        rented_items_lines = rented_items.readlines()
        book_rent = {} 

        #store the data in a wordbookionery
        for i in range(1,len(rented_items_lines) + 1):    
            book_rent[i] = rented_items_lines[i-1].split(",")      
        
        for i in range(1, len(rented_items_lines)):
            book_rent[i].pop(6)           
        
        print(book_rent)
        
       
        amount = float(book_rent[1][5])
        quantity = float(book_rent[1][3])

        # to remove $ from the price
        count = 0
        price1 = "" 
        for i in book_rent[1][4]:
            if count > 0:
                price1 = price1 + i 
            count = count + 1

        price = float(price1)
        number_of_days = (amount *5)/(quantity * price)

        # for rented date:
        date_data = open(name.upper()+" "+id+" rented"+".txt","r").readlines()
        date_data_date = date_data[3].split(",")[0].split("-")
        d0 = date(int(date_data_date[0]),int(date_data_date[1]),int(date_data_date[2]))
        d1 = date(int(year), int(month), int(day))
        difference = (d1 - d0).days

        #for total amount
        total = float(0)
        for i in range(1, len(book_rent)):
            total = total + float(book_rent[i][5])
        

        # for fine
        fine = 0
        if number_of_days < difference:
            overdue = difference - number_of_days
            for i in range(1, len(book_rent)):
                fine = fine + (price/5)*int(book_rent[i][3]) * overdue
        
        

        # printing the bill generated after returning
        print("The items you have rented previously are:")
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        print("  Number of days: ", int(number_of_days))
        print("  Rented on: ",date_data[3]," Returned on: ",date_today,"\n  Number of days passed: ", difference )
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        print("  Sno\t\tCostume ID\t\tCostume\t\t\tBrand\t\t\tQuantity\t\tPrice(5 days)\t\tAmount") 
        print("------------------------------------------------------------------------------------------------------------------------------------------------\n")
        for i in range(1, len(book_rent)):
            print("  {0}\t\t{1}\t\t\t{2}\t\t{3}\t\t{4}\t\t\t{5}\t\t\t${6}\n".format(i, book_rent[i][0],book_rent[i][1],book_rent[i][2],book_rent[i][3],book_rent[i][4],book_rent[i][5])) # prints uptop indexes 3 (because 4th is"\n" or "" ) of each list from each index of the wordbookionery 
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Total: $", "{:.2f}".format(total))
        print("Overdue Fine: $","{:.2f}".format(fine))
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Grand Total: $","{:.2f}".format(total + fine))
        print("------------------------------------------------------------------------------------------------------------------------------------------------")


        #updating wordbookionery containing tthe stock data
        wordbook = rent.read_cart()
        for i in range(1, len(book_rent)):
            wordbook[int(book_rent[i][0])][3] = str(int(wordbook[int(book_rent[i][0])][3]) + int(book_rent[i][3]))
        print(wordbook)

        #updating the stock.txt file
        write(wordbook)



        # keeping the record for the returned data
        invoice(name, id, number_of_days, date_today, difference, book_rent, total, fine, date_data)
        
        #record of returened items
        cart_rent = open(name.upper()+" "+id+" return cart"+".txt",'w')
        for i in range(1, len(book_rent)):            
            for j in range(6):         
                cart_rent.write(str(book_rent[i][j]))           
                cart_rent.write(',')    
            cart_rent.write("\n")  
        
        #for printing date and time of rent form the rent cart file
        cart_rent.write(book_rent[len(book_rent)][0]) 
        cart_rent.write(",")
        cart_rent.write(book_rent[len(book_rent)][1])
        cart_rent.close()
    except:
        print("==============================================")
        print(" NOT RENTED  ")
        print("==============================================")

def invoice(name, id, number_of_days, date_today, difference, book_rent, total, fine, date_data):
    invoice = open(name.upper()+" "+id+" returned"+".txt","w")
    invoice.write("Your bill")
    invoice.write("\n")
    invoice.write("------------------------------------------------------------------------------------------------------------------------------------------------")
    invoice.write("\n")
    invoice.write("  Number of days: "+ str(number_of_days))
    invoice.write("\n")
    invoice.write("  Rented on: "+str(date_data[3])+"  Returned on: "+str(date_today)+"\n  Number of days passed: "+ str(difference ))
    invoice.write("\n")
    invoice.write("------------------------------------------------------------------------------------------------------------------------------------------------")
    invoice.write("\n")
    invoice.write("  Sno\t\tCostume ID\t\tCostume\t\t\tBrand\t\t\tQuantity\t\tPrice(5 days)\t\tAmount") 
    invoice.write("\n")
    invoice.write("------------------------------------------------------------------------------------------------------------------------------------------------\n")
    invoice.write("\n")
    for i in range(1, len(book_rent)):
        invoice.write("  {0}\t\t{1}\t\t\t{2}\t\t{3}\t\t{4}\t\t\t{5}\t\t\t${6}\n".format(i, book_rent[i][0],book_rent[i][1],book_rent[i][2],book_rent[i][3],book_rent[i][4],book_rent[i][5])) # prints uptop indexes 3 (because 4th is"\n" or "" ) of each list from each index of the wordbookionery 
        invoice.write("\n")
    invoice.write("------------------------------------------------------------------------------------------------------------------------------------------------")
    invoice.write("\n")
    invoice.write("Total: $"+ str("{:.2f}".format(total)))
    invoice.write("\n")
    invoice.write("Fine: $"+str("{:.2f}".format(fine)))
    invoice.write("\n")
    invoice.write("------------------------------------------------------------------------------------------------------------------------------------------------")
    invoice.write("\n")
    invoice.write("Sum Total: $"+str("{:.2f}".format(total + fine)))
    invoice.write("\n")
    invoice.write("------------------------------------------------------------------------------------------------------------------------------------------------")

def write(wordbook):
    stock2 = open('data.txt','w')     
    for i in range(1, len(wordbook)+1):         
        for j in range(4):         
            stock2.write(wordbook[i][j])         
            stock2.write(',')       
        stock2.write("\n")     
    stock2.close()
