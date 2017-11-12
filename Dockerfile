FROM python:3
MAINTAINER Pierre de LESPINAY <gprod.net+github@gmail.com>

WORKDIR /usr/src/app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]
