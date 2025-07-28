FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "uvicorn app_api:app --host 0.0.0.0 --port 8000 & streamlit run streamlit_app.py --server.address=0.0.0.0 --server.port=8501"]