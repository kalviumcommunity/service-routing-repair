FROM python:3.12-slim
WORKDIR /app
COPY app.py dashboard.py ./
EXPOSE 8080
CMD ["python", "app.py"]
