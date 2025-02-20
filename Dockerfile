FROM python:3.9

WORKDIR /app

# 필수 파일 복사 및 설치
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# 프로젝트 코드 복사 (static, templates 포함)
COPY static /app/static
COPY templates /app/templates
COPY api /app/api
COPY . /app/

# Flask 실행
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
