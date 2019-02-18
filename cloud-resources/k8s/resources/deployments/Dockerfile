FROM goddy/python:3.6xp
RUN pip install requests
ADD app.py /code/
WORKDIR /code/
ENTRYPOINT ["python", "app.py"]