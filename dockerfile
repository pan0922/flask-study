FROM python:3.7
COPY . /app
WORKDIR /app/myproject
RUN pip install -r requirements.txt
ENV FLASK_APP "pybo"
ENV FLASK_DEBUG "true"
CMD ["-m","flask","run","--host=0.0.0.0"]
EXPOSE 5000
