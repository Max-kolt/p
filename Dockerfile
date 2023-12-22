FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache --no-cache-dir -r requirements.txt

COPY . .
WORKDIR /app/app
EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
