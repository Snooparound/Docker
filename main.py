from fastapi import FastAPI
from courses import course_router
import uvicorn

app = FastAPI()

# APIRouter를 app에 연결함
app.include_router(course_router)

# 서버 직접 실행 구문
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)