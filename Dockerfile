FROM python:3.9

WORKDIR /app

# 필수 파일 복사
COPY requirements.txt ./
RUN pip install -r requirements.txt

# 전체 프로젝트 복사
COPY . .  

# Flask 실행
CMD ["flask", "run", "--host=0.0.0.0"]
