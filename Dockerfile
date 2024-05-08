FROM python:3.10

WORKDIR /code
COPY ./requirments.txt ./
#RUN pip install --no-cache-dir -r requirments.txt
COPY ./src ./src
CMD ["python", "src/game.py"]