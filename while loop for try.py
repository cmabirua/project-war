def ask():# if we dont need break then 
    #waiting =true
    while True:#while true
        try:
            n = int(input("input an interger :"))
             
        except:#it occure only error occure ..galat input de ge tho baar baar run hoga
            print("An error occured! Please try again !")
            continue
        else:
            print("Thank you, your number squared is :")
            break #waiting =false it will work same
    print(n**2)#squaring the number
ask()