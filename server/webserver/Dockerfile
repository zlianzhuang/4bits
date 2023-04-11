# Build container
FROM python:3.10-slim

ENV TZ=Asia/Shanghai
RUN mkdir -pv /src

WORKDIR /src

COPY web /src/web
COPY config.json /src/config.json

WORKDIR /src/web

RUN python -m pip install --trusted-host mirrors.aliyun.com --upgrade pip \
		-i http://mirrors.aliyun.com/pypi/simple/
RUN python -m pip install --trusted-host mirrors.aliyun.com --no-cache-dir \
		nicegui \
		-i http://mirrors.aliyun.com/pypi/simple/

ENTRYPOINT ["python"]
CMD ["main.py"]
