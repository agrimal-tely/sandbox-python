# 1. Use a tiny version of Python 3.12 as our base
FROM python:3.12-slim

# 2. Set the 'home' folder inside the container
WORKDIR /app

# 3. Copy our requirements first (for faster builds)
COPY requirements.txt .

# 4. Install the libraries (like 'requests') inside the box
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your app.py script into the box
COPY app.py .
COPY weather.py .

# 6. Tell the box to run the Streamlit server on a specific port
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]