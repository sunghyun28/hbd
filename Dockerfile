# 작업 디렉터리 설정
WORKDIR /app

# 모든 파일 복사 (templates 포함)
COPY . /app

# Flask 설치
RUN pip install --no-cache-dir flask

# 환경 변수 설정
ENV FLASK_APP=api/index.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Flask 실행
CMD ["flask", "run"]
