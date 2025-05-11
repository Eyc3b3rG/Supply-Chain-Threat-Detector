@echo off
echo Stopping existing containers...
docker-compose down

echo.
echo Building and starting Docker containers...
docker-compose up --build

pause