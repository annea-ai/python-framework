FROM python:3.10-slim

WORKDIR /apps/annea_baz

COPY apps/annea_baz .
COPY libs /libs

RUN pip3 install -e .

RUN rm -rf /libs

ENTRYPOINT ["annea_baz"]