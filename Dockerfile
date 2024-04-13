FROM python:3.10-slim

WORKDIR DivarApp

COPY requirements.txt ./
RUN  apt-get update
RUN apt-get install -y libpq-dev
RUN apt-get install -y lsb-release
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY Divar .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]