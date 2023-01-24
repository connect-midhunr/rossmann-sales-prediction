FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=app.py
ENV FLASK_ENV=ross
CMD ["flask", "run", "--host=0.0.0.0"]