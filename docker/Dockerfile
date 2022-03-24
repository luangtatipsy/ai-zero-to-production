FROM arm64v8/python:3.9 
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt 
COPY ./src ./src
COPY ./models ./models
COPY ./logs ./logs
EXPOSE 8000:80

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "80"] 