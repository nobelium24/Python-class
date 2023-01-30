import converter
from converter import kgToLbs

message = input(">")
words = message.split(" ")
emojis = {
    ":)": "😊",
    ":(": "😞",
    ";)": "😉"
}
def moji ():
    output = ""
    for i in words:
       output += emojis.get(i, i) + " "
    print(output)
moji()

print(kgToLbs(100))