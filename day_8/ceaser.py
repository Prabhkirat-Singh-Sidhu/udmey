from art import *
tprint("Ceaser Cipher")
conti= True
while conti:

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']

    direction = input('Type encode to encrypt or decode to decrypt:\n').lower()
    text = input('Type ur msg\n').lower()
    shift = int(input("Type the shift no:\n"))


    def cipher(orignal_text,shift_amount,direction1):

        if direction1== "decode":
            shift_amount *= -1
        
        cipher_text= ""

        for letter in orignal_text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                orignal_index = alphabet.index(letter)
                shifted_index = orignal_index + shift_amount
                shifted_index %= len(alphabet)
                cipher_text += alphabet[shifted_index]

        print(cipher_text,end="")


    cipher(text,shift,direction1=direction)

    decision= input("Type any key to restart or 'no' to close the program:\n").lower()
    if decision == "no":
        conti= False
        print("Program closed")
    else:
        print("Program is restarted.")