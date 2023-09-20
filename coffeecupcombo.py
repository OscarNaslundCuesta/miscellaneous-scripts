with open("input.txt", "r") as input:
    strings = input.readlines()

lectures = strings[1]
coffee = 0
awake_lectures = 0

def refill_coffee(coffee):
    coffee = 2
    return coffee

for lecture in lectures:
    if lecture == "1":
        awake_lectures += 1
        coffee = refill_coffee(coffee)

    if lecture == "0":
        if coffee > 0:
            coffee -= 1
            awake_lectures += 1
        else:
            pass

print(awake_lectures)
