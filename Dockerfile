FROM python:3.11.1

WORKDIR /app

COPY . /app
ADD run.py .

RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install Flask==2.3.2 Werkzeug==2.3.6 Flask-WTF==1.2.1 Flask-SQLAlchemy==3.1.1 Flask-Migrate==4.0.1 Flask-Login==0.6.2 Flask-CKEDitor==0.4.6

# EXPOSE 80

# ENV FLASK_APP=run.py

CMD ["python", "./run.py", "--bind 0.0.0.0:5000"]