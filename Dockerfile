FROM spider_actor:v1.0

RUN sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list
RUN sed -i 's/security.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list
RUN apt-get update && apt-get install --yes --no-install-recommends libjemalloc2 protobuf-compiler
ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.2 MALLOC_CONF='background_thread:true,dirty_decay_ms:0,muzzy_decay_ms:0'

WORKDIR /app
COPY . /app

RUN protoc -I. --python_out=. proto/**/*.proto

EXPOSE 3000

CMD ["gunicorn","-c","config.py","app:app", "-k","uvicorn.workers.UvicornWorker"]
