# An automated Decoder that tries to decode a message in all 25 possible means to find the correct one.
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n','o', 'p','q','r','s','t','u','v','w','x','y','z']
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
    splitted_message = str(message).split(" ")
    final = ""
    for x in range(0, len(splitted_message)):
        test_string = decoder(splitted_message[x], key)
        final+=test_string
        if(x < len(splitted_message)-1):
            final += " "
    print("Decoded message is : '{0}' with Key-bit : '{1}'".format(final,key))

def AutomatedDecoder(message):
    for key in range(0,26):
        decodeMessage(message,key)

mess = input("Enter the message to perform automated Decoding : ")
AutomatedDecoder(mess)