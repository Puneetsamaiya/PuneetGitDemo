mylist = ['Home', 'Loan', 'Car', 'Cloan', ]

print ('Mylist contains', len(mylist),' items')

print (mylist)

print ('I want to append one more item as "Furniture" in the list')

mylist.append('Furniture')

print ('Now my list contains', len(mylist),' items')

print (mylist)

print ('I want to remove "Cloan" from the list')

print (mylist[3])
mylist.sort()
print (mylist)
print ('After sorting',mylist[3])

mylist.reverse()

print (mylist)

mylist.insert(3,"A")
mylist.sort()
print(mylist)

mylist.pop()

print(mylist)
