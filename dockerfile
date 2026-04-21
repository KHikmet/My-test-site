FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# debug üçün port açıq qalıb (real vibe)
EXPOSE 5000

ENV FLASK_ENV=development

CMD ["python", "app.py"]
