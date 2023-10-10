FROM python:3.8.17-alpine3.18
RUN apk --update add bash nano less git make gcc musl-dv tzdata
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./ /var/www/
RUN pip install -r /var/www/requirements.txt
WORKDIR /var/www
RUN sed -i 's/\r$//' ./shell/gunicorn.sh  && \  
    chmod +x ./shell/gunicorn.sh
ENTRYPOINT [ "./shell/gunicorn.sh" ]