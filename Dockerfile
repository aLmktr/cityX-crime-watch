FROM python:3.13-slim

WORKDIR /app

# add non root user 
RUN useradd -m streamlituser

# copy requirement file 
COPY requirements.txt .

# install dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# copy the project files to the container 
COPY . .

# allow non-root to run files 
RUN chown -R streamlituser:streamlituser /app

# swtich to non-root user 
USER streamlituser

# expose streamlit default port
EXPOSE 8501

# run the app 
CMD ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
