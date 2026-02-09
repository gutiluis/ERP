FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# -m fixes everything. treat app as a package. add /app to sys.path resolve imports correctly
CMD ["python", "-m", "app.main"] # available under docker ps -a command
