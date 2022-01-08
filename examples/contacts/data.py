from dataclasses import dataclass


@dataclass
class Contact:
    name: str
    gender: int
    blog: str
    placeholder: bool = False


contacts = [
    Contact("Jay Chou", 1, ""),
    Contact("Hello Kitty", 0, "https://www.google.com"),
    Contact("JJ", 1, "invalid")
]
