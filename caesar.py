from sys import stdin
# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "  #cipher 1,2
#ALPHABET = " -,;:!?/.'\"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ"                 #cipher 3
n = len(ALPHABET)		
DICTIONARY_FILE = "dictionary-01.txt"

# read in the dictionary
f=open(DICTIONARY_FILE,"r")
dic=f.read().rstrip("\n").split("\n")
f.close()

# performs decryption codes
def decrypt(key, message):  
    result = ""
    for letter in message:
        new_key = (ALPHABET.find(letter)-key)%n
        if letter in ALPHABET:
            result = result + ALPHABET[new_key]   
        else:
            result = result + letter
    return result


ciphertext = stdin.read().rstrip("\n")              
ciphertext_f10 = "\n".join(ciphertext.split("\n")[:10])

 
counts = {}   # {index:value}, index is the shift
maxCount,maxIndex=0,0

for i in range(0,n):                                 
    plaintext = decrypt(i,ciphertext_f10)
    words = plaintext.split()    
    res=[] 
    for word in words:                
        word=word.strip('\",.?!;')
        res.append(word)
    words=res

# sperate plaintext in a list , change each word to lower case and strip unnecessary symbols
    count=0                                                             
    for word in words:                    
        if word in dic:
            count += 1
    counts[i]=count
    
    if counts[i]>maxCount:
        maxCount=counts[i]
        maxIndex=i

# choose the corresponding the index of max count as shift
bestShift = maxIndex

bestPlaintext = decrypt(maxIndex,ciphertext)

print("Shift="+str(bestShift)+":")
print(bestPlaintext)
      
#  python a1_correction.py < 01ciphertext-1.txt
                                                   
         
                    


 





