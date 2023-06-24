import hashlib
print("\t\t\tWelcome to Package hasher 1.0.0.0")
print("\t\t\tCreated by XIICODE")
print("\t\t\tHASH FILE IN DIFFERENT HASHES")

print("1.MD5\n2.SHA1\n3.SHA256\n4.SHA384\n5.SHA512\n6.SHA224\n7.ALL HASHES")
choice=input("Select a Category of hash : ")
path = str(input("Enter path to file : "))
if(int(choice)==1):
   with open(path, 'rb') as f:
        data = f.read()
        print(f"The MD5 hash sum  is :{hashlib.md5(data).hexdigest()}")

elif(int(choice)==2):
    with open(path, 'rb') as f:
        data = f.read()        
        print(f"The SHA1 hash sum  is :{hashlib.sha1(data).hexdigest()}")

elif(int(choice)==3):
    with open(path, 'rb') as f:
        data = f.read()        
        print(f"The SHA256 hash sum  is :{hashlib.sha256(data).hexdigest()}")

elif(int(choice)==4):
    with open(path, 'rb') as f:
        data = f.read()        
        print(f"The SHA384 hash sum  is :{hashlib.sha384(data).hexdigest()}")

elif(int(choice)==5):
    with open(path, 'rb') as f:
        data = f.read()        
        print(f"The SHA512 hash sum  is :{hashlib.sha512(data).hexdigest()}")

elif(int(choice)==6):
    with open(path, 'rb') as f:
        data = f.read()        
        print(f"The SHA224 hash sum  is :{hashlib.sha224(data).hexdigest()}")

elif(int(choice)==7):
    with open(path, 'rb') as f:
        data = f.read()
        print(f"The MD5 hash sum  is :{hashlib.md5(data).hexdigest()}")
        print(f"The SHA1 hash sum  is :{hashlib.sha1(data).hexdigest()}")
        print(f"The SHA256 hash sum  is :{hashlib.sha256(data).hexdigest()}")
        print(f"The SHA384 hash sum  is :{hashlib.sha384(data).hexdigest()}")
        print(f"The SHA512 hash sum  is :{hashlib.sha512(data).hexdigest()}")
        print(f"The SHA224 hash sum  is :{hashlib.sha224(data).hexdigest()}")
else:
    print("Error in selection")       

print("Completed Operation")
    
