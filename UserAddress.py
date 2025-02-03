from dataclasses import dataclass

@dataclass
class UserAddress:
    address1: str
    address2: str
    city: str
    zip_code: str