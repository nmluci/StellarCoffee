from app.baseModel import db
from app.userdata.models import User
from app.auth.models import SignInModel, SignUpModel

def uniquify(plaintext: str, maxLen: int=8) -> str:
    hashed = str()
    val = 0
    
    for i, c in enumerate(plaintext):
        hashed += str(ord(c)*10 + i + 1 if i+1 < 10 else ord(c)*100+i+1)
    hashNum = int(hashed)
    hashNum = int(pow(hashNum, 2))

    return hashNum%(10**maxLen)

def verifyUserCredentials(metadata: SignInModel) -> bool:
    plaintext = f"{metadata.username}:{metadata.password}"
    usr = isUsernameUsed(metadata.username)
    if not usr: 
        return False
    else: 
        return (usr.username != metadata.username) or (usr.password != uniquify(metadata.password, 20))

def registerUser(metadata: SignUpModel):
    plaintext = f"{metadata.username}:{metadata.password}"
    if isUsernameUsed(metadata.username):
        raise Exception("username has taken")
    
    uid = uniquify(plaintext)
    if db.session.query(User).filter(User.uid==uid).all():
        raise Exception("username has taken")

    if not metadata.firstName:
        raise Exception("firstname cannot be empty")
    
    if not metadata.lastName:
        raise Exception("lastname cannot be empty")
    
    newUser = User(
        uid=uid,
        firstname=metadata.firstName,
        lastname=metadata.lastName,
        username=metadata.username,
        password=uniquify(metadata.password, 10)
    )

    newUser.insert()

def isUsernameUsed(uname: str) -> SignInModel:
    usernames = db.session.query(User).all()
    for usr in usernames:
        if usr.username == uname:
            print(f"u:{usr.username} == c:{uname}")
            return usr
    return None