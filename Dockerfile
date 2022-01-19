FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP /basicsite

#system requirements
# RUN apt-get update
# RUN apt-get -y install python-pip
# RUN apt-get update
# RUN pip install --upgrade pip
# RUN pip install psycopg2-binary
RUN mkdir $APP
WORKDIR $APP
COPY requirements.txt /$APP/
RUN pip install -r requirements.txt
ADD . /$APP/