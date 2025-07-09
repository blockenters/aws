#!/bin/bash

# 프로젝트 디렉토리로 이동.
cd /home/ec2-user/fast-music-server

# 가상환경 실행
source /home/ec2-user/miniconda3/etc/profile.d/conda.sh
conda activate music

# 라이브러리 설치
pip install -r requirements.txt

# 서버실행 
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 2

