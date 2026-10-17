# ------------------------------------------------------
#        Name: (Winta Kebede)
#       Peers: (add any collaborators)
#  References: (I used the slides and also I used geekforgreek for function on finding a specific word)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ take input sentence from user and find secret word, dog, dog and print sentence associated with all the words. if the specific word is not found the loop continues."""
    b= "dog" #to assign the word to a variable 
    c= "Dog"
    
    while True:
        a= input("Give me a sentence: ")
        if a. find(secret_word) != -1: #in string a find the secret word and if you find it then print the string. when it doesn't find it it will return -1. That is why not equal to -1 is used
            print("You used the secret word!")
            break
        elif a. find(b) !=-1:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break
        elif a. find(c) !=-1:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break 
        else:
            print("Try again")


# Task 2
def check_greater():
    """ take two integer input from the user and print of one is greater than the other. But of the two are equal the loop continues. """
    while True:
        g= int(input("Give me 1st integer: "))
        h= int(input("Give me 2nd integer: "))
        if g>h:
            print("First is Greater")
            break # go to the next code outside of the loop
        elif h>g:
            print("Second is Greater")
            break
        elif g==h:
            print("Try again")
               
               
           



# Task 3
def get_special_numbers():
    """ in the range of 1-40 print the numbers that are a multiple of 3, but not multiple of 2 and 5 """
    for a in range(1,40): 
        if a%2!=0 and a%3==0 and a%5!=0: # if the number, when divided by 2 or 5 has remainder diffrent from 0 and when divided by 3 has a remainder 0, then print the number
            print(a)
          
        


# Task 4.a
def my_for_loop():
    """ take a string input from the user and if it meets the criteria, then write whether each letter in the string is vowel or consonant"""    
    
    vowel =("A", "a", "E", "e","I","i","O","o","U","u")# list of upper case and lower case vowel
    j = input("Give me a string: ")
    k= len(j)
    h=" "
    my_range = range(2,6)
    if  k in my_range and h not in j: # if the length is in my range and if there is no space then go through every letter assigning vowel and consonant
        for i in j:
            if i in vowel:
                print(f"letter {i} is a vowel")
            else:
                print(f"letter {i} is a consonant")
    else:
        print("bad word")
            
            
        
# Task 4.b
def my_while_loop():
    """ take a string input from the user and print something, continue the loop or exit the program """
    a = "a" # a varible is equal to string a
    b = "b"
    c = "c"
    while True:
        n=input("choose one option:a, b, or c: ") # is the input of the user
        if n==a: # if the input is equal to a then continue the loop
            continue
        elif n==b:
            print("Goodbye")
            break
        elif n==c:
            sys.exit() # to exit the program
        else:
            print("try again")
# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
