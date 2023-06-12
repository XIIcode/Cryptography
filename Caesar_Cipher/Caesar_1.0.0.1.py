# Python program to generate cryptography encoding based on key value of encoding(min 0 : max 25).
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n','o', 'p','q','r','s','t','u','v','w','x','y','z']
# Encoding Engine.
def encodeMessage(message , key):
    print("Message passed for encoding is : '{0}' with key-bit : '{1}'".format(message,key))
    temp_message = []

    for char in str(message):
        s_lowered = char.lower()
        s_index = 0
        if(s_lowered in alphabets):
            s_index = alphabets.index(s_lowered)
        else:
            pass
        temp_index = s_index + int(key)
        if(temp_index > len(alphabets) - 1):
            final_index = temp_index - (len(alphabets))
            temp_message.append(alphabets[final_index])
        elif(s_lowered == " "):
            temp_message.append(" ")
        else:
            temp_message.append(alphabets[temp_index])
            
    final_message = "".join(temp_message)
    print(f"Encoded message is : '{final_message}'")
    return final_message
# Decoding Engine.
def decoder(message,key):
    temp_message = []
    for char in str(message):
        s_lowered = char.lower()
        s_index = 0
        final_message = ""
        if(s_lowered in alphabets):
            s_index = alphabets.index(s_lowered)   
        temp_index = s_index - int(key)
        if(temp_index < 0):
            val = int(key) - (s_index + 1)
            final_index = (len(alphabets)-1) - val
            temp_message.append(alphabets[final_index])
        else:
            temp_message.append(alphabets[temp_index])
    final_message = "".join(temp_message)
    return final_message
# Interface to Decode.
def decodeMessage(message , key):
    print("Message passed for decoding is : '{0}' with key-bit : '{1}'".format(message,key))
    splitted_message = str(message).split(" ")
    final = ""
    for x in range(0, len(splitted_message)):
        test_string = decoder(splitted_message[x], key)
        final+=test_string
        if(x < len(splitted_message)-1):
            final += " "
    print("Decoded message is : '{0}'".format(final))

print("\t\t\t\t\tWelcome to Caesar Cypher 1.0.0.1")
print("\t\t\t\t\tUse keybit 0-25")
print("\t\t\t\t\tCreator XIICODE")
print("\t\t\t\t\tSpecial Characters not supported in this version.?$#@!&*()-_+={[]}|/,.")
print("\t\t\t\t\tOUTPUT IS IN LOWER CASE")
print("\n\n\n")
print("You can set a minimum of 0 key-bit and a maximum of 25 key-bit")
value = 12
encoded_mess = encodeMessage("I love Cryptography",value)
decodeMessage(encoded_mess,value)
print("\n\n\n")
choice =input("Do you wish to encode(e) or decode(d) message press any key to quit : ")
if(choice == "e"):
    user_value = input("Enter the key-bit to use (min : 0 no encryption, max : 25): ")
    user_message = input("Enter the message to encode : ")
    user_encoded_message = encodeMessage(user_message,int(user_value))
elif(choice == "d"):
    user_value = input("Enter the key-bit to use (min : 0 no encryption, max : 25): ")
    user_message = input("Enter the message to dencode : ")
    user_decoded_message = decodeMessage(user_message,int(user_value))




            


    