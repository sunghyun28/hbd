# Python 3.9 기반 이미지 사용
FROM python:3.9

# 작업 디렉터리 설정
WORKDIR /app

# 필요한 파일 복사 후 종속성 설치
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# 프로젝트 코드 전체 복사
COPY . /app/

# Gunicorn을 이용해 WSGI 서버 실행
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "index:app"]
