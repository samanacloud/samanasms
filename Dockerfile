FROM python:3.13

RUN <<EOF
mkdir -p /app
pip install slack-sdk flask
EOF
ENTRYPOINT [ "flask", "--app", "sms", "run", "--host", "0.0.0.0"]
COPY sms.py /app
WORKDIR /app
