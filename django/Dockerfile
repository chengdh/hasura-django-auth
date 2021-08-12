FROM python:3
ENV PIP_NO_CACHE_DIR=1

WORKDIR /code
ADD ./entrypoint.sh /entrypoint.sh
ADD ./requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install -r /requirements.txt 

RUN chmod a+x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]