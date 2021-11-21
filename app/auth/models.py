from dataclasses import dataclass

@dataclass
class SignInModel:
    username: str
    password: str

@dataclass
class SignUpModel:
    firstName: str
    lastName: str
    username: str
    password: str
