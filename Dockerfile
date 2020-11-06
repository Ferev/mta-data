FROM python:3.8
WORKDIR /app
ADD . /app
RUN python setup.py install
RUN useradd appuser && chown -R appuser /app
USER appuser
ENV MTA_DATA_API_KEY=""
ENV IN_CONTAINER=True
VOLUME "/app/data"
ENTRYPOINT ["python", "-m", "mta_data"]