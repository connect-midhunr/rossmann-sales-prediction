FROM python:3.10.9
ADD . /app
WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 3000
CMD ["python", "app.py"]