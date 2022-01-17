FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP /basicsite

#system requirements
RUN mkdir $APP
WORKDIR $APP
COPY requirements.txt /$APP/
RUN pip install -r requirements.txt
ADD . /$APP/