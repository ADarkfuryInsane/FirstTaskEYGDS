from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

import sqlite3
 
app = FastAPI()
 
# ------------------- Database Connection -------------------
 
def get_db_connection():

    conn = sqlite3.connect("C:\\MiniProject\\e_learning.db")  # Update path if needed

    conn.row_factory = sqlite3.Row

    return conn
 
# ------------------- Models -------------------
 
class Course(BaseModel):

    CourseID: str

    Title: str

    Category: str

    Duration: int
 
class Student(BaseModel):

    StudentID: str

    Name: str

    Email: str

    Country: str
 
# ------------------- Root Endpoint -------------------
 
@app.get("/")

def root():

    return {"message": "🎉 FastAPI is running!"}
 
# ------------------- Courses Endpoints -------------------
 
@app.get("/courses")

def list_courses():

    conn = get_db_connection()

    courses = conn.execute("SELECT * FROM courses").fetchall()

    conn.close()

    return [dict(row) for row in courses]
 
@app.post("/courses")

def add_course(course: Course):

    conn = get_db_connection()

    try:

        conn.execute("INSERT INTO courses VALUES (?, ?, ?, ?)",

                     (course.CourseID, course.Title, course.Category, course.Duration))

        conn.commit()

    except sqlite3.IntegrityError:

        raise HTTPException(status_code=400, detail="Course already exists")

    finally:

        conn.close()

    return {"message": "Course added successfully"}
 
@app.put("/courses/{course_id}")

def update_course(course_id: str, course: Course):

    conn = get_db_connection()

    cursor = conn.execute("UPDATE courses SET Title=?, Category=?, Duration=? WHERE CourseID=?",

                          (course.Title, course.Category, course.Duration, course_id))

    conn.commit()

    conn.close()

    if cursor.rowcount == 0:

        raise HTTPException(status_code=404, detail="Course not found")

    return {"message": "Course updated successfully"}
 
@app.delete("/courses/{course_id}")

def delete_course(course_id: str):

    conn = get_db_connection()

    cursor = conn.execute("DELETE FROM courses WHERE CourseID=?", (course_id,))

    conn.commit()

    conn.close()

    if cursor.rowcount == 0:

        raise HTTPException(status_code=404, detail="Course not found")

    return {"message": "Course deleted successfully"}
 
# ------------------- Students Endpoints -------------------
 
@app.get("/students")

def list_students():

    conn = get_db_connection()

    students = conn.execute("SELECT * FROM students").fetchall()

    conn.close()

    return [dict(row) for row in students]
 
@app.post("/students")

def add_student(student: Student):

    conn = get_db_connection()

    try:

        conn.execute("INSERT INTO students VALUES (?, ?, ?, ?)",

                     (student.StudentID, student.Name, student.Email, student.Country))

        conn.commit()

    except sqlite3.IntegrityError:

        raise HTTPException(status_code=400, detail="Student already exists")

    finally:

        conn.close()

    return {"message": "Student added successfully"}
 
@app.put("/students/{student_id}")

def update_student(student_id: str, student: Student):

    conn = get_db_connection()

    cursor = conn.execute("UPDATE students SET Name=?, Email=?, Country=? WHERE StudentID=?",

                          (student.Name, student.Email, student.Country, student_id))

    conn.commit()

    conn.close()

    if cursor.rowcount == 0:

        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "Student updated successfully"}
 
@app.delete("/students/{student_id}")

def delete_student(student_id: str):

    conn = get_db_connection()

    cursor = conn.execute("DELETE FROM students WHERE StudentID=?", (student_id,))

    conn.commit()

    conn.close()

    if cursor.rowcount == 0:

        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "Student deleted successfully"}
 