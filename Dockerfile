FROM python:3.8-slim
WORKDIR /app/
ADD . /app/
RUN pip3 install --upgrade pip
RUN pip3 install pipenv
RUN pipenv install --system --ignore-pipfile
RUN cd /app/
CMD ["python3", "main.py"]

