import uuid

from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserInfoResponse(BaseModel):
    id: uuid.UUID
    email: EmailStr
    nickname: str

    model_config = ConfigDict(from_attributes=True)


class SignUpResponse(BaseModel):
    info: UserInfoResponse
    access_token: str = Field(...)
    refresh_token: str = Field(...)
