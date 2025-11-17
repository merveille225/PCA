FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir flask redis
ENV FLASK_ENV=production
EXPOSE 5000
CMD ["python", "app.py"]
