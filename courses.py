from fastapi import APIRouter
from model import Course
import json

# APIRouter 생성
course_router = APIRouter()

@course_router.get("/courses")
async def get_courses():
    with open("courses.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

@course_router.post("/courses")
async def add_course(course: Course):
    with open("courses.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # 전달받은 Pydantic 모델 데이터를 딕셔너리로 변환하여 추가
    new_course = course.model_dump()
    data.append(new_course)
    
    with open("courses.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    return {"msg": "course added successfully", "added_course": new_course}