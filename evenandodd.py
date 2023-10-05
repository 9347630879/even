
number = int(input(" enter a value "))
if number % 2 != 0:
    print( " this is an even number")
else:
    print( " this is not even number ")


#even number
number = 123
if number % 2  == 0:
    print( " this is an even number")
else:
    print( " this is an odd number ")

#paildromne
a = input(" enter a value  ")
return_a=a[::-1]
if a==return_a:
    print("value is paildromne")
else:
    print("value is not paildromne")

#address

sai = input("enter a address")
if  not sai.isnumeric():
    print("address is valid")
else:
    print("address is not valid")

city = input(" entry a city")
if city.isalpha():
    print(" city is valid should be a string")
else:
    print(" city should not be a valid")

state = input(" entry a  state")
if state.isalpha():
    print("state is a valid")
else:
    print(" state should not be a valid")


placeholder = "enter a value "
a = input(placeholder)
b = input(placeholder)
if(a.isnumeric())and b.isnumeric():
    print(int(a)*int(b))


sai = "enter a value"
a = input(sai)
b = input(sai)
if(a.isnumeric())and b.isnumeric():
    print(int(a)/int(b))

sai = "enter a value"
a = input(sai)
b = input(sai)
if(a.isnumeric())and b.isnumeric():
    print(int(a)-int(b))


sai = "enter a value"
a = input(sai)
b = input(sai)
if(a.isnumeric())and b.isnumeric():
    print(int(a)%int(b))
