import rent
import return_
print("---------------------------------------------")
print("    Welcome To Our Store          ")
print("-------------------------------------------\n\n\n")


def main():
    a = True
    while a == True:
        
        print("Select a desirable option \n(1) Press r to rent a costume \n(2) Press rn to return a costume\n(3) Press e to exit.\n")
        userInput = input("Enter an option:").lower()

        if userInput == "r":
            rent.rent()
        elif userInput == "rn":
            return_.rtrn()
        elif userInput == "e":
            a = False
        else:
            print("\n\n Invalid input\n Select value as per the provided options\n\n")

        

    
main()
