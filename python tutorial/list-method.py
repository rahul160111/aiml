l =[10,20,30,40,50,"apple"]
j =[ 60 , 70 , 80 , 90 , 100]

print (j.count(30))

# for adding any object at the end of list 
l.append(40)
print(l)

# at particular index number 
l.insert(2, 100)
print(l)
 

#  remove any object from list
l.pop()
print(l)

# particular object 
l.remove(50)
l.remove("apple")
print(l)

# empty
l.reverse()
print(l)
l.sort(reverse=True)
print(l)

# reverse 
l.reverse()
print(l)
  
#  sort method
l.sort()
print(l)
l.sort(reverse=True)
print(l) 

# extend method 
j. extend(l)
print(l)
