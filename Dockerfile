FROM python:2

WORKDIR /app
ADD /requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD / /app
EXPOSE 8000
CMD ["/app/run.sh"]