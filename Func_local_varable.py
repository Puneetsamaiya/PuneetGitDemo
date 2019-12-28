a =5
print ('outside', a)

def check_local(a):
    print ('inside func ')
    a=2
    print (a)

check_local(10)
print (a)
