from pydantic import BaseModel
from typing import Optional


class EventBase(BaseModel):
    id: str
    organizationNames: str
    organizationNames: str
    name: str
    description: str
    categoryNames: str
    location: str
    startsOn: str
    endsOn: str
    theme: str
    benefitNames: str
    institutionId: str
    organizationId: str
    organizationIds: str
    OrganizationProfilePicture: str
    branchId: str
    imagePath: str
    visibility: str
    status: str
    searchScore: str


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: str

    class Config:
        orm_mode = True


class EventUpdate(EventBase):
    id: Optional[str]
    organizationNames: Optional[str]
    organizationNames: Optional[str]
    name: Optional[str]
    description: Optional[str]
    categoryNames: Optional[str]
    location: Optional[str]
    startsOn: Optional[str]
    endsOn: Optional[str]
    theme: Optional[str]
    benefitNames: Optional[str]
    institutionId: Optional[str]
    organizationId: Optional[str]
    organizationIds: Optional[str]
    OrganizationProfilePicture: Optional[str]
    branchId: Optional[str]
    imagePath: Optional[str]
    visibility: Optional[str]
    status: Optional[str]
    searchScore: Optional[str]


class StudentBase(BaseModel):
    StudentID: int
    Name: str
    Email: str
    Password: str

    class Config:
        orm_mode = True


class StudentCreate(BaseModel):
    #StudentID: Optional[int]
    Name: Optional[str]
    Email: Optional[str]
    Password: Optional[str]

    class Config:
        orm_mode = True


class StudentReg(BaseModel):
    StudentID: int
    Email: str

    # Email: str
    # pass

    class Config:
        orm_mode = True


class StudentEmail(StudentBase):
    Email: str

    class Config:
        orm_mode = True


class StudentUpdate(StudentBase):
    StudentID: Optional[int]
    Name: Optional[str]
    Email: Optional[str]
    Password: Optional[str]

    class Config:
        orm_mode = True


class RegistrationBase(BaseModel):
    StudentID: int
    EventID: str
    RegistrationID: int

    class Config:
        orm_mode = True
