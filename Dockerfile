FROM python:3.11

WORKDIR /src

COPY requirements.txt ./
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

COPY app/ ./app/
COPY config.py ./

COPY .vscode/ ./.vscode/
