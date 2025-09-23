import random

def test_random():
    #randomnumber 
    random_number = random.randint(1, 10)

    #inputnumber
    number = (input("Enter your number: "))
    number = int(number)
    if number == random_number:
        print("Good job ")
    
    elif random_number < number:
        print("Too much")

    elif random_number > number:
        print("Too low")
    
    print(random_number)

test_random()