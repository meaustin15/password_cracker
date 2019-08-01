import hashlib #import hashlib

foundFlag = 0 #password found flag
found = [] #list of found passwords + hashes

pass_hash = input("MD5 List File: ") #f1

#Try to see if list of hashes file was found
try:
    pass_file = open(pass_hash, "r") #List of MD5 Hashes
except:
    print("No file found")
    quit()

wordlist = input("Word List File: " ) #f2

#Try to see if list of words file was found
try:
    word_file = open(wordlist, "r")
except:
    print("No file found")
    quit()

wordarr = []
hasharr = []

# word_file = open("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt", "r")
for word in word_file:
    word_file = open("wordlist.txt", "r")
    print("--------------------------------")
    print("Password: " + word)
    wordarr.append(word)
    # wordstrip = word.strip()
    # print(wordarr)
    word = word.strip('\r\n')
    for pas in pass_file:
        # hasharr.append(pas)
        # print(hasharr)
        pass_file = open("md5hashlist.txt", "r")
       # word_file = open("wordlist.txt", "r")
        wordstrip = word.strip()  # stripping the white spaces from word
        encodedword = wordstrip.encode('utf-8')  # encode the word ascii
        # print(encodedword) #see the encoded word
        md5hash = hashlib.md5(encodedword).hexdigest()  # creating the md5 hash


        print(str(md5hash).strip('\r\n')) #print hash of words
        print(str(pas).strip('\r\n')) #print hash for hash list
        print("\n") #spacer


        if str(md5hash).rstrip('\r\n') == str(pas).rstrip('\r\n'):
            foundFlag = 1
            print("Password(s) found")
            print("Password is " + word + "\n")
            found.append("Password: " + word + " = MD5 Hash: " + md5hash)


if foundFlag == 0: #if passwords are found
      print("Password is not in the list")

for password in found: #show array of found passwords
    print(password)
