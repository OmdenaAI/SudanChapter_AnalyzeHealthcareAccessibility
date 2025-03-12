# assign base image
FROM python:3.9-slim

# setting the directory
WORKDIR /app

# install and copy
COPY requirements.txt requirements.txt
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# # open port
# EXPOSE 5000

# run application
#CMD ["python", "app.py"]
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]