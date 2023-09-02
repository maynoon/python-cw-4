def my_name(name):
    print (f"Hi my name is {name}")

the_name = input("whats your name ")

my_name(the_name)



def my_meal():
    food = input("enter a food")
    drink = input("enter a drink")

    print(f"I like to eat  {food}  and to drink  {drink}")

my_meal()

    
def cube (number):
    return number*number*number

cubed_num = int(input("enter the number to be cubed"))
result = cube (cubed_num)
print(result)

def odd_or_even(number):
    if number %3==0 :
        print("True")
    else:
        print("False")

num = int(input("Whats the number"))
odd_or_even(num)
