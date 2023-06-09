try:
    x = 5
    y = 0
    z = x/y
except:
    print("Error!")# it will give error call divided by zero error but still it will print finally block
finally:
    print("All done")