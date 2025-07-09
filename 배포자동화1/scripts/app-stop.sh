#!/bin/bash

SERVICE_NAME="music-server"

echo "=== 서비스 중지 ==="
sudo systemctl stop $SERVICE_NAME
echo "=== 완료! ==="