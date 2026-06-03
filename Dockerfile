# Dockerfile
FROM python:3.10
WORKDIR /app

# 패키지 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

# 소스코드 복사
COPY . .

# 내부 포트 명시 (Notion 예시 기준)
EXPOSE 8000

# FastAPI 실행 (uvicorn을 main.py 안에서 실행한다고 가정)
# 만약 터미널에서 uvicorn으로 실행했다면 CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 로 수정하세요.
CMD ["python", "main.py"]
