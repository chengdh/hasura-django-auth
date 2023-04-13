FROM python:3
ENV PIP_NO_CACHE_DIR=1

WORKDIR /code
ADD ./entrypoint.sh /entrypoint.sh
ADD ./requirements.txt /requirements.txt
# RUN pip install --upgrade pip 
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /requirements.txt 
# RUN pip install -r /requirements.txt 

# RUN chmod a+x /entrypoint.sh
# ENTRYPOINT ["/entrypoint.sh"]