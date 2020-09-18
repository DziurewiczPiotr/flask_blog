FROM python:3.8-slim
WORKDIR /flask_blog
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY / .
CMD [ "python", "./blog.py" ]
