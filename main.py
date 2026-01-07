
import random

mot = 'salut'
key = 'azertyuiop'
entropy = random.randint(0, 9999)

# cryptage
def crypt_with_key( word, mykey, entropy) :
    
	res = []
	index = 0
 
	for letter in word :
		crypted_letter = ord(letter.lower()) + ord(mykey[index].lower()) + entropy
		res.append(chr(crypted_letter).lower())
		index += 1
  
	return ''.join(res)

def is_same(crypted, word, mykey, entropy) : 
    success = False
    if crypt_with_key(word, mykey, entropy) == crypted :
        success = True
    
    return success

crypted = crypt_with_key( mot, key, entropy )

new_word = "salut"
is_same_word = is_same( crypted, new_word, key, entropy )

print(crypted)
print(is_same_word)



     

    
    
    
    
