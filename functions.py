def greetMe():
    print("Welcome Wole")
    print("Welcome Ope")
    print("Welcome Ore")


greetMe()

# Parameterized functions


def greetUser(i):
    print(f"Welcome {i}")


greetUser("Adewole")

def square(number):
    return print(number*number)

def emojis(message):
    words = message.split()
    emoji = {
        ":)": "😊",
        ":(": "😞",
        ";)": "😉"
    }
    output = ""
    for i in words:
        output += emoji.get(i, i) + " "
    return output
    

message = input(">")
print(emojis(message))




