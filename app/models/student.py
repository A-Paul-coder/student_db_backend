from sqlalchemy import String, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Student(Base):

    __tablename__ = "students"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    department: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    semester: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    age: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    cgpa: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )