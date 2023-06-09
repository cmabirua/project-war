#finally key word
try:
    f=open('testfile','w')#if 'r' we write here then we get os error but still printing finally block
    f.write("write a test line")
except TypeError:
    print("there was a type error")
except OSError:
    print('hey you have an OS error')
finally:
    print("i always run")
