#Python program to generate crptographic encoding and decoding functions for messages.
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n','o', 'p','q','r','s','t','u','v','w','x','y','z']
# print(alphabets[4])
def encodeMessage(message):
    print("Message passed for encoding is {0}".format(message))
    temp_message = []
    for char in str(message):
        s_lowered = char.lower()
        if(s_lowered in alphabets and s_lowered != 'z'):
            index = alphabets.index(s_lowered)
            temp_message.append(alphabets[index+1])
        elif(s_lowered == " "):
            temp_message.append(" ")
        elif(s_lowered == 'z'):
            temp_message.append(alphabets[0])
    final_message = "".join(temp_message)
    print(f"Encoded message is : {final_message}")
    return final_message

def decodeMessage(message):
    print("Message passed for decoding is : {0}".format(message))
    temp_message = []
    for char in str(message):
        s_lowered = char.lower()
        if(s_lowered in alphabets and s_lowered != 'a'):
            index = alphabets.index(s_lowered)
            temp_message.append(alphabets[index-1])
        elif(s_lowered == " "):
            temp_message.append(" ")
        elif(s_lowered == "a"):
            temp_message.append(alphabets[25])
    final_message = "".join(temp_message)
    print(f"Decoded message is : {final_message}")

enc_mess = encodeMessage("y")
decodeMessage(enc_mess)       
            