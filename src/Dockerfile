
FROM python:latest

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

WORKDIR /app/src

EXPOSE 5000

# execute command to run app.py
CMD ["python", "app.py"]