from LISTA import alphabet
def caesar(msg,shift_number,d):
    if d == 'encode':
        cipher_text = ""

        for letter in msg:
            shifted_position = alphabet.index(letter) + shift_number
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        print(f"The encode result is {cipher_text}")
    else:
        cipher_text = ""

        for letter in msg:
            shifted_position = alphabet.index(letter) - shift_number
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        print(f"The decode result is {cipher_text}")

fim = False
while fim == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    caesar(text,shift,direction)
    choose = input("Do you wanna go again, type 'yes or 'no': \n")
    if choose == 'no':
        fim = True
        print("Goodbye!")