FROM python:3.9

WORKDIR /app

# 필수 파일 복사
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# 프로젝트 코드 복사 (static 포함)
COPY . /app/
COPY static /app/static  # ✅ static 폴더를 강제로 복사

# Flask 실행
CMD ["flask", "run", "--host=0.0.0.0"]
