FROM library/python:3.9-slim

WORKDIR /app/

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
RUN pip install uvicorn

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /app

RUN chmod +x start.sh

CMD ["./start.sh"]
