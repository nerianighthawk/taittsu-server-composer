FROM python:3.10-bookworm

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./
RUN echo "API_KEY=${API_KEY}" >> .env

RUN pip install gunicorn

EXPOSE 8080
CMD ["gunicorn", "run:app", "-b", "0.0.0.0:8080"]
