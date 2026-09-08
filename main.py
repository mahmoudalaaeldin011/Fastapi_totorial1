from fastapi import FastAPI
from pydantic import BaseModel
# انشاء تطبيق fastAPI 
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
)
 #تعريف نموذج بيانات باستخدام Paydantic 
class student(BaseModel):
     id: int 
     name: str
     grade: int 

#قائمه تخزين الاماكن ف الذاكره 
students = [
     student (id=1,name= "Mahmoud Alaa Eldin",grade=4),
     student(id=2,name="Abd Allah" ,grade=4 ),
]

#قراءه جميع العناصر  
@app.get("/students/")
def read_stydents():
     return students

#انشاء عنصر جديد 
@app.post("/student/")
def create_student(New_student: student):
     students.append(New_student)
     return students

@app.put("/students/{student_id}")
def update_syudent(student_id : int , update_student : student):
     #حلقه للبحث عن الطالب بعدين تحديث العنوان 
     for index , student in enumerate(students):
          if student.id == student_id :
               students[index]=update_student
               return update_student
     return{"error":"Stusent not found"}

@app.delete("/students/{student_id}")
def delete_syudent(student_id : int):
     for index , student in enumerate(students):
               if student.id == student_id :
                    del students[index]
                    return{"message":"student deleted"}
     return{"error":"Stusent not found"}