# n = int(input("enter the number to print the table:"))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")


# l = ["Rahul","rat","sachon"]
# for r in l:
#     if r.startswith("r"):
#         print(r)
        

# n = int(input("inter the value"))
# while n>9

# n =  int(input("find the value "))
# x=1
# while x<11:
#     print(n,"x",x, "=",n*x)
#     x+=1 
n=1 
while n<11:
    print(n,"x",n,"=",n*n)
    n+=1 

if n==0 or n==1:
    print(f"{n}is not prime ")    

elif n>2:
    for i in range (20,n):
        if(n%i)==0:
            print("not prime")
            break
        else:
            print(f"{n}is prime number")
            # print(f"{n}is not prime number")
# x = 0

# while x<11:
#     if x%2==1:
#         print(x)
#     x+=1