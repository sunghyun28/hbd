# 베이스 이미지로 Python 3.9 사용
FROM python:3.9

# 작업 디렉터리 설정
WORKDIR /app

# 현재 디렉터리의 모든 파일을 컨테이너 내부의 /app 디렉터리로 복사
COPY . /app

# 필요한 패키지 설치
RUN pip install --no-cache-dir flask

# 환경 변수 설정 (Flask 실행 시 필요한 설정)
ENV FLASK_APP=api/index.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# 컨테이너에서 Flask 실행
CMD ["flask", "run"]
