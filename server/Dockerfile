FROM python:3.7.4

RUN mkdir -p /root/python/cquptpiper
RUN mkdir -p /root/.piper
ADD . /root/python/cquptpiper
WORKDIR /root/python/cquptpiper

RUN pip3 install -r requirements.txt

CMD ["gunicorn", "main:app", "-c", "./gunicorn.conf.py"]
