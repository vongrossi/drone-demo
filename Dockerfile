FROM python:2.7-slim
WORKDIR /app
ADD app.py requirements.txt ./
RUN pip install -r requirements.txt
ENV NAME World
EXPOSE 4000
CMD ["python", "app.py"]

