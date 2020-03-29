import eandom
def hangman():
    word = random.choice(["pugger" , "littlepugger" , "tiger" , "superman" , "thor" , "pokemon" , "avengers" , "savewater" , "earth" , "annable" ])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns =10
    guessmade=''
    while len(word)>0:
        main = ''
        missed=0

name = input("Enter Your Name : ")
print("Welcome", name)
print("----------------------------")
print("Try to guess the word in less then 10 attempts")
