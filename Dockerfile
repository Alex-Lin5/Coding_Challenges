FROM python:latest

WORKDIR /coding
RUN pip install -U pytest
# ENTRYPOINT ["tail"]
# CMD ["-f","/dev/null"]