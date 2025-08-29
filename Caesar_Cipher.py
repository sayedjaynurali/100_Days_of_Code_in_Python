alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']

should_run = True

while should_run == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt and 'exit' to STOP:\n").lower().strip()
    output_text = []
    if direction == "encode" or direction =="decode": 
        def encrypt():
            original_text = input("Type your message:\n").lower()
            shift_number = int(input("Type the shift number:\n"))
            for word in original_text:
                if word in alphabet:
                    if direction == "encode":
                        output_text.append(alphabet[(alphabet.index(word) + shift_number) % len(alphabet)])
                    elif direction == "decode":
                        output_text.append(alphabet[(alphabet.index(word) - shift_number) % len(alphabet)])
                else:
                    output_text.append(word)
            print(f'Here is your {direction}d result: {"".join(output_text)}')
        encrypt()

    elif direction == "exit":
        break

    else:
        print("Enter a valid input!")
