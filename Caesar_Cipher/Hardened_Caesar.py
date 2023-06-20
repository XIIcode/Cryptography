import random as rnd

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n','o', 'p','q','r','s','t','u','v','w','x','y','z']
En_Keys = []

def encodeMessage(message , key):
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
    return final_message

def hardenedEncoder(message):
    # Flush existing items in the list.
    En_Keys.clear()
    print(f"Message passed for Encoding is : {message}")
    splitted_message = str(message).split(" ")
    temp_mess = []
    for split in range(len(splitted_message)):
        random_Key = rnd.randint(1,25)
        En_Keys.append(random_Key)
        val = encodeMessage(splitted_message[split],random_Key)
        temp_mess.append(val)
        temp_mess.append(" ")
    Hardened_Message = "".join(temp_mess)
    print(f"Hardened Caesar Cipher Message is : {Hardened_Message}")
    print(f"Keys used in Encoding keep safe ! : {En_Keys}")
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
# Interface to Decode Hardened Message.
def hardenedDecoder(message):
    print("Message passed for decoding is : '{0}'".format(message))
    splitted_message = str(message).split(" ")
    final = ""
    for x in range(0, len(En_Keys)):
        test_string = decoder(splitted_message[x],En_Keys[x])
        final+=test_string
        if(x < len(splitted_message)-1):
            final += " "
    print("Decoded message is : '{0}'".format(final))
print("\t\t\t\t\tWelcome to Hardened Caesar Cypher 1.0.0.1")
print("\t\t\t\t\tCreator XIICODE")
print("\t\t\t\t\tSpecial Characters not supported in this version.?$#@!&*()-_+={[]}|/,.")
print("\t\t\t\t\tOUTPUT IS IN LOWER CASE")
print("\n\n\n")
def startCipher():
    choice =input("Do you wish to encode(e) or decode(d) message press any key to quit : ")
    if(choice.lower() == "e"):
        user_message = input("Enter the message to Cipher : ")
        hardenedEncoder(user_message)
        print("\n\n")
        cont_choice = input("Do you wish to continue (y/n) : ")
        if(cont_choice.lower() == "y"):
            startCipher()
        else:
            pass
    elif(choice.lower() == "d"):
        user_message = input("Enter the message to decode : ")
        key_count = input("Enter the number of Keys used during ENCRYPTION : ")
        # Flush Existing Keys in the EN list
        En_Keys.clear()
        # New Entries for EN list
        for count in range(0, int(key_count)):
            key = input(f"Enter KEY {count+1} : ")
            En_Keys.append(key)
        hardenedDecoder(user_message)
        print("\n\n")
        cont_choice = input("Do you wish to continue (y/n) : ")
        if(cont_choice.lower() == "y"):
            startCipher()
        else:
            pass
if __name__ == "__main__":
    startCipher()
