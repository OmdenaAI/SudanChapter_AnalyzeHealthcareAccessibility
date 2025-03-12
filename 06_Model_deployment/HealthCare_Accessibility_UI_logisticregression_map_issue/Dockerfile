# assign base image
FROM python:3.9-slim

# setting the directory
WORKDIR /app2

# install and copy
COPY requirements.txt requirements.txt
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# # open port
EXPOSE 8501

# run application
#CMD ["python", "app.py"]
CMD ["streamlit", "run", "app2.py", "--server.port=8501", "--server.address=0.0.0.0"]