# 예제 Dockerfile
FROM python:3.9

WORKDIR /app

# 필수 파일 복사
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# 프로젝트 코드 복사
COPY . /app/

# ❗ static 폴더가 안 복사되는 경우 추가해야 함
COPY static /app/static

# Flask 실행
CMD ["flask", "run", "--host=0.0.0.0"]
