FROM python:3.11.4-alpine
LABEL authors="Denis"
COPY .. /app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


