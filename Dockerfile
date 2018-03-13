FROM python:2.7-alpine

WORKDIR /app
ADD requirements.txt ./
RUN pip install -r requirements.txt

ADD app.py ./

ENV PORT 4000
ENV NAME World

EXPOSE $PORT
CMD ["python", "app.py"]

