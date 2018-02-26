FROM python:2.7-slim
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
ENV NAME World
EXPOSE 80
CMD ["python", "app.py"]

