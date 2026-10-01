from pydantic import BaseModel, EmailStr, Field


class StudentCreate(BaseModel):

    name: str = Field(min_length=2, max_length=100)

    email: EmailStr

    department: str

    semester: int = Field(ge=1, le=8)

    age: int = Field(ge=15, le=100)

    cgpa: float = Field(ge=0, le=10)


class StudentUpdate(BaseModel):

    name: str | None = None

    email: EmailStr | None = None

    department: str | None = None

    semester: int | None = Field(
        default=None,
        ge=1,
        le=8
    )

    age: int | None = None

    cgpa: float | None = Field(
        default=None,
        ge=0,
        le=10
    )


class StudentResponse(StudentCreate):

    id: int

    class Config:
        from_attributes = True