FROM python:3.9

WORKDIR /app

# 필수 파일 복사
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# 프로젝트 코드 복사 (static 포함)
COPY . .  

# Flask 실행
CMD ["flask", "run", "--host=0.0.0.0"]
