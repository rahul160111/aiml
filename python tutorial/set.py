d = set()
s = { 1,2,3,4,5,6,7,8,9,9,4,3,55,6,3,3 }
print (s)
t = {1,2,3,4,5,6,7,}
print(t)
# t = set([1,2,3,4,5,6,7,8,9,]) #inmutable 
# print(t)
# t=[6] = 50 
# print(t)

f = s.intersection(t)
print(f)

s = s.union(t)
print(s)

# l = s.difference(t)
# print(l)


# o = t.difference(s)
# print(o)
# s.add(100)
# print(s)    

# s.remove(100)
# print(s)

# s.pop()
# s.pop()
# s.pop()
# print(s)
# # s.clear()
# # print(s)

# k = s.copy()
# print(k)

L = {i for i in range(-20,20) if i%2==0}
print("L:", L)



