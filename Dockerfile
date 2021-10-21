FROM python:3.9.5

#make a directory for our application
WORKDIR /task1

#install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

#copy the source code
COPY hello.py .


CMD ["python", "hello.py"]
