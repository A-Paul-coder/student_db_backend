from sqlalchemy.orm import Session

from app.repositories import student_repository
from app.schemas.student import (
    StudentCreate,
    StudentUpdate
)


def create_student(
    db: Session,
    data: StudentCreate
):
    return student_repository.create_student(
        db,
        data
    )


def get_students(db: Session):

    return student_repository.get_students(db)


def get_student(
    db: Session,
    student_id: int
):

    return student_repository.get_student(
        db,
        student_id
    )


def update_student(
    db: Session,
    student_id: int,
    data: StudentUpdate
):

    return student_repository.update_student(
        db,
        student_id,
        data
    )


def delete_student(
    db: Session,
    student_id: int
):

    return student_repository.delete_student(
        db,
        student_id
    )