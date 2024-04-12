FROM python:3.10-slim

WORKDIR DivarApp

COPY requirements.txt ./
RUN  apt-get update
RUN apt-get install -y lsb-release
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update

COPY . .

CMD ["python3", "./Divar/manage.py", "runserver"]