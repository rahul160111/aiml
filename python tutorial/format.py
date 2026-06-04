s = "{} working in an Company and his salary is Salary"

x1  = s.format("Rahul")
print(x1)

# # mutlitple parameter 
# x2 = s.format(noun = "Rahul", Company = "TCS", Salary = 50000)
# print(x2)


#order of parameters
            #  0       1          2
# x3 = s.format("rahul", "TCS", "50000r")
# print(x3)

#alias within the string
# x4 = s.format(noun="Rahul", Company="TCS", Salary="50000")
# print(x4)

#f-string
a = int(input("enter the value:"))
b = int(input("enter the value:"))

addition = a+b
print(f"addition of {a} and {b} is {addition}")
