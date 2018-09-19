print(" ")
print(" ")
print("##################################################")
print("#                                                #")
print("#   Magic: The Gathering Decklist Creation Tool  #")
print("#                                                #")
print("#               v0.0.1                           #")
print("##################################################")
print(" ")
print(" ")
print(" ")

def main():
    menu = {}
    menu['1']="Create Decklist" 
    menu['2']="Load Decklist"
    menu['3']="Exit"
    mBool = True 
    while mBool == True: 
        options=menu.keys()
        for entry in options: 
            print (entry, menu[entry])
 
        selection=input("Please select the number of the option you would like: ") 
        if selection =='1': 
            deckcreate() 
            mBool = False
        elif selection == '2': 
            print ("delete") 
        elif selection == '3':
            mBool = False
            print(" ")
            print("Exiting program.")
            break  
        else: 
            print ("Unknown Option Selected!")
         

def deckcreate():
        print("Deck creation (placeholder)")
        filename = input ("filename: ")
        with open (filename, "w") as f:
            f.write (input ())
        selection=input("Please select the number of the dank option you would like: ") 
        print (selection)
main()
#deckcreate() 