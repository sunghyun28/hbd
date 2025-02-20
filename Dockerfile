FROM python:3.9

WORKDIR /app

# 필수 파일 복사
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# 프로젝트 코드 복사
COPY . /app/

# (중요!) static 폴더 강제 생성
RUN mkdir -p /app/static

# Flask 실행
CMD ["flask", "run", "--host=0.0.0.0"]
