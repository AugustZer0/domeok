from datetime import date

from pydantic import BaseModel, EmailStr, Field, model_validator


class SignUpRequest(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=8, max_length=20)
    checked_password: str = Field(..., min_length=8, max_length=20)
    nickname: str = Field(..., min_length=8, max_length=20)

    name: str | None = Field(None, min_length=2, max_length=20)
    birth: date | None = Field(None)
    phone_num: str | None = Field(None, pattern=r"^\d{10,11}$")

    @model_validator(mode="after")
    def verify_password_match(self):
        if self.password != self.checked_password:
            raise ValueError("비밀번호 확인이 일치하지 않습니다.")
        return self
