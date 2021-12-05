import base64

def uniquify(plaintext: str, maxLen: int=16) -> str:
    print(f"plaintext: {plaintext.split()}")
    hashed = int()
    val = 0
    
    for i, c in enumerate(plaintext):
        hashed += ord(c)*10 + i + 1 if i+1 < 10 else ord(c)*100+i+1
    hashNum = int(hashed)
    hashNum = int(pow(hashNum, 2))

    while len(str(hashNum)) > maxLen:
        val += hashNum%10
        hashNum = hashNum/10
    
    return hashNum

plaintext = input("Plaintext: ")
print(str(uniquify(plaintext)))
