def ask_for_int():
    while True:
        try:
            result = int(input("please provide a number: "))
        except:
            print("whoops! that is not a number")
            continue
        else:
            print("yes, thank you")
            break
        finally:
            print("end of try/except/finally")
            print("I will always run at the end!")
ask_for_int()