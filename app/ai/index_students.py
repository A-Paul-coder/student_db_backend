from langchain_core.documents import Document

from app.core.database import SessionLocal
from app.models.student import Student
from app.ai.vector_store import vector_store


def index_students():

    db = SessionLocal()

    try:
        students = db.query(Student).all()

        documents = []

        for student in students:

            text = f"""
Student ID: {student.id}
Name: {student.name}
Email: {student.email}
Department: {student.department}
Semester: {student.semester}
Age: {student.age}
CGPA: {student.cgpa}
"""

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "student_id": student.id,
                        "department": student.department
                    }
                )
            )

        if documents:
            vector_store.add_documents(documents)

        print(f"{len(documents)} students indexed successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    index_students()