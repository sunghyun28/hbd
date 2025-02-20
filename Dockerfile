# 기본 이미지 설정
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일만 복사 (빌드 오류 방지)
COPY templates /app/templates
COPY api /app/api
COPY requirements.txt /app/requirements.txt

# 디버깅용 (복사된 파일 확인)
RUN ls -l /app/templates

# 패키지 설치
RUN pip install --no-cache-dir -r /app/requirements.txt

# 환경 변수 설정
ENV FLASK_APP=api/index.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# 컨테이너 실행 시 커맨드
CMD ["flask", "run"]
