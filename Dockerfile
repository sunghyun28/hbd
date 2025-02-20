FROM python:3.9

WORKDIR /app

# 필수 파일 복사
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# static, templates 폴더를 명확하게 복사
COPY static /app/static
COPY templates /app/templates

# 프로젝트 코드 복사
COPY . /app/

# Flask 실행
CMD ["flask", "run", "--host=0.0.0.0"]

