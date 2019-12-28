global a
a =5
print ('outside', a)

def check_local():
    #global a
    print ('inside func ')
    a=2
    print (a)

check_local()
print (a)
