t= ( '10',20,True, "Hello" ,3.45)
print(type(t))

for i in t:
    if i== True:
        print (i)

print(t.index(3.45))
print(t.count(20))

k = list (t)
k.append(40)
t = tuple(k)
print(t)





 