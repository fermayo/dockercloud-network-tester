FROM python:2

WORKDIR /app
ADD /requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Wait this number of seconds between checks
ENV POLLING_PERIOD 5

ADD / /app
CMD ["python", "/app/test.py"]
