FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=.env

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]