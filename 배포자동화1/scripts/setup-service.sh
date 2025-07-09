#!/bin/bash

SERVICE_NAME="music-server"
APP_DIR="/home/ec2-user/music-server"
USER="ec2-user"

echo "=== 서비스 설정 ==="

yum update && yum install -y java-17-amazon-corretto-headless


# 서비스 파일 생성
cat > /etc/systemd/system/$SERVICE_NAME.service << EOF
[Unit]
Description=Spring Boot API Server
After=network.target

[Service]
Type=simple
User=$USER
Environment="JAVA_HOME=/usr/lib/jvm/java-17-amazon-corretto"
WorkingDirectory=$APP_DIR
ExecStart=/usr/bin/java -jar $APP_DIR/app.jar
Restart=always
RestartSec=10
StandardOutput=$APP_DIR/logs/app.log
StandardError=$APP_DIR/logs/app.log

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable $SERVICE_NAME

echo "=== 완료! ==="