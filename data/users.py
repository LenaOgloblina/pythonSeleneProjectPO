import dataclasses

from attr import dataclass


@dataclasses.dataclass
class User:
    full_name: str
    email: str
    currentAddress: str
    permanentAddress: str