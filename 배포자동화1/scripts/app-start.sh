#!/bin/bash

SERVICE_NAME="music-server"

echo "=== 서비스 시작 ==="
sudo systemctl start $SERVICE_NAME
echo "=== 완료! ==="