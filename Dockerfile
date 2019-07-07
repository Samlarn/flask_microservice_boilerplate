FROM python:3.7-slim-stretch

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

# Was needed for Docker Toolbox (Windows 10)
#RUN chmod 644 app.py

CMD ["python", "app.py"]
