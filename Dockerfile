FROM python:3.11

WORKDIR /app

RUN pip install -U pathway
RUN pip install -U requests
RUN pip install -U datetime
RUN pip install -U openai
RUN pip install -U python-dotenv
RUN pip install -U streamlit
RUN pip install -U feedparser

COPY . /app

EXPOSE 8080
EXPOSE 8501

# ENTRYPOINT ["python", "run_scripts.py"]
