FROM python

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py password_utils.py ./
COPY templates ./templates

EXPOSE 5000

CMD ["python", "app.py"]
