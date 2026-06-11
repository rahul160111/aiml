# Area of triangle 
# def aot(b,h):
#     return 0.5 *b*h
# print(aot(5,6))


# # print number 
# def is_prime(n):
#     if n == 0 or n == 1:
#         print(f"{n} is not prime")
#     elif n > 1:
#         for i in range(2, n):
#             if (n % i) == 0:
#                 print(f"{n} is not prime")
#                 break
#         else:
#             print(f"{n} is a prime number")
#     else:
#         print(f"{n} is not prime")

# is_prime(17)
        
# # revers a string 
# def reverse_string(s):
#     return s[::-1]
# entered_string = input("enter a string ")
# print (reverse_string(entered_string ))

#greatest  of four 
def greatest04(n1,n2,n3,n4):
    if n1>n2:
        f1=n1
    else:
        f1=n2
    if n3>n4:
        f2=n3
    else:
        f2=n4
    
    if f1>f2:
        print (f"{f1} is greatest ")
    else:
        print (F"{f2} is greatest")

greatest04(43,56,78,99)

# area of circle 
def aoc(r):
    return 3.45*r*r
print(aoc(2))



