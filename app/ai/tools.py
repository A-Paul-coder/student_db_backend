from typing import Optional

from sqlalchemy.orm import Session
from langchain_core.tools import tool

from app.core.database import SessionLocal
from app.models.student import Student


@tool
def count_students(department: Optional[str] = None) -> str:
    """
    Count students in the database.

    If department is provided, count only students
    from that department.
    """

    db: Session = SessionLocal()

    try:
        query = db.query(Student)

        if department:
            query = query.filter(
                Student.department.ilike(department)
            )

        count = query.count()

        if department:
            return (
                f"There are {count} students "
                f"in the {department} department."
            )

        return f"There are {count} students in total."

    finally:
        db.close()


@tool
def find_student(student_id: int) -> str:
    """
    Find a student using their student ID.
    """

    db: Session = SessionLocal()

    try:

        student = db.query(Student).filter(
            Student.id == student_id
        ).first()

        if not student:
            return f"No student found with ID {student_id}."

        return (
            f"Student ID: {student.id}\n"
            f"Name: {student.name}\n"
            f"Email: {student.email}\n"
            f"Department: {student.department}\n"
            f"Semester: {student.semester}\n"
            f"Age: {student.age}\n"
            f"CGPA: {student.cgpa}"
        )

    finally:
        db.close()


@tool
def get_students_by_department(
    department: str
) -> str:
    """
    Get students belonging to a specific department.
    """

    db: Session = SessionLocal()

    try:

        students = db.query(Student).filter(
            Student.department.ilike(department)
        ).all()

        if not students:
            return (
                f"No students found in "
                f"the {department} department."
            )

        result = []

        for student in students:

            result.append(
                f"ID: {student.id}, "
                f"Name: {student.name}, "
                f"Semester: {student.semester}, "
                f"CGPA: {student.cgpa}"
            )

        return "\n".join(result)

    finally:
        db.close()