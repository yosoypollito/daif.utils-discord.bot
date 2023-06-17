FROM python:latest

WORKDIR /app/utils/

COPY . .

RUN python -m venv env

RUN pip install -r requirements.txt

CMD ["python", "./bot.py"]