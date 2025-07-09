#!/bin/bash

set -e

APP_DIR="/home/$(whoami)/music-server"
SERVICE_NAME="music-server"

echo "=== 배포 시작 ==="

# 1. 서비스 중지 
sudo systemctl stop $SERVICE_NAME || true 

# 2. jar 파일 복사 
JAR_FILE=$(find $APP_DIR/target -name "*.jar" -type f | head -1 )
cp "$JAR_FILE" "$APP_DIR/app.jar" 

# 3. 로그 디렉토리 생성 
mkdir -p "$APP_DIR/logs"

# 4. 서비스 파일 삭제 후 다시 생성한다. 
sudo rm -rf /etc/systemd/system/$SERVICE_NAME.service
sudo ./scripts/setup-service.sh 


# 5. 서비스 시작
sudo systemctl daemon-reload
sudo systemctl start $SERVICE_NAME
sudo systemctl enable $SERVICE_NAME

echo "=== 배포 완료 ==="