FROM python:3.10
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 80
CMD ["python", "app.py"]