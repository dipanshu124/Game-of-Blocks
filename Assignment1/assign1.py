import hashlib
import random
var = input("Provide a string\n")
target = 0x0000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
it = 0
#Randomly check for possible nonce value
while it < 10000000 :
    x = random.randint(1,2**256)
    str1 = var + str(x)
    new_result = hashlib.sha256(str1.encode()).hexdigest()
    val = int(new_result,16)
    if val < target :
        print('Value to be appended')
        print(x)
        print('number of iterations:')
        print(it)
        break
    it += 1
