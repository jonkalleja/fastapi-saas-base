from datetime import datetime
from typing import List

from pydantic import BaseModel


class AccountBase(BaseModel):
    email: str
    first_name: str
    last_name: str


class AccountCreate(AccountBase):
    password: str
    is_system_admin: bool


class Account(AccountBase):
    id: int
    is_system_admin: bool

    class Config:
        orm_mode = True


class EmailAddressBase(BaseModel):
    email: str
    primary: bool
    verified: bool
    verified_on: datetime = None


class EmailAddressCreate(EmailAddressBase):
    pass


class EmailAddress(EmailAddressBase):
    id: int

    class Config:
        orm_mode = True
