FROM python:3.8-slim
WORKDIR /app/
ADD requirements.txt /app/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ADD . /app/
RUN cd /app/
CMD ["python3", "main.py"]

