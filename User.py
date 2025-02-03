from dataclasses import dataclass
from UserAddress import UserAddress

@dataclass
class User:
    name: str
    email: str
    address: UserAddress
    hiring_date: str
    job_title: str
