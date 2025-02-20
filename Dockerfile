# 🚨 기본 이미지 추가 (Python 3.9)
FROM python:3.9

# 작업 디렉터리 설정
WORKDIR /app

# 모든 파일 복사 (templates 포함)
COPY . /app

# Flask 실행 시 templates 폴더가 있는지 확인하는 코드 추가 가능
RUN ls -l /app/templates

# Flask 및 관련 패키지 설치
RUN pip install --no-cache-dir flask

# 환경 변수 설정
ENV FLASK_APP=api/index.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Flask 실행
CMD ["flask", "run"]
