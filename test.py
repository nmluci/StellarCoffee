import base64

def passwordHashing(plain: str) -> str:
    hashed = str()
    val = 0
    
    for i, c in enumerate(plain):
        hashed += str(ord(c)*10 + i + 1 if i+1 < 10 else ord(c)*100+i+1)
    hashNum = int(hashed)
    hashNum = int(pow(hashNum, 2))


    while len(str(hashNum)) > 16:
        val += hashNum%10
        hashNum = hashNum/10
    
    hashed = str(hashNum)
    return base64.b64encode(hashed.encode("utf-8"))

def generateUserToken(username: str, password: str) -> str:
    token = f"{username}:{password}"
    if len(token) < 255:
        token += "###"
        token += "$" * (252-len(token))

    return base64.b64encode(token.encode("utf-8"))

print(passwordHashing("dgshgjdkshjk:jkdhgjksgkshdgs"))