import random

def main():
    """Generates the password based on user-inputs"""

    list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    length,upcase,number = settings()
    #generator
    for _ in range(length) :
        if number == True :
            ranchar = list[random.randint(0,len(list) - 1)]
        else :
            ranchar = list[random.randint(0,len(list) - 11)]

        if upcase == True :
            print(ranchar, end="")
        else :
            print(ranchar.lower(), end="")


def settings():
    """Takes user-input to length,uppercase,number options and returns them"""

    # length equality of number
    while True :
        try :
            length = int(input("Length? : "))
            break
        except ValueError :
            print("Invalid number")

    #uppercase true/false
    while True :
            upcaseq = input("Uppercase ? Y/N\n")

            if upcaseq.upper() in ["Y", "YES"] : 
                upcase = True
                break
            elif upcaseq.upper() in ["N", "NO"] :
                upcase = False
                break
            else :
                print("Invalid answer")

    #number true/false
    while True :
        numberq = input("Number ? Y/N\n")

        if numberq.upper() in ["Y", "YES"] : 
            number = True
            break
        elif numberq.upper() in ["N", "NO"] :
            number = False
            break
        else :
            print("Invalid answer")
    
    return length,upcase,number


main()
