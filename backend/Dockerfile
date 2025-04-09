FROM python:3.11

RUN mkdir -p /opt/app

COPY ./requirements.txt /opt/app/requirements.txt
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --progress-bar off -r /opt/app/requirements.txt

COPY app /opt/app
COPY Makefile /opt/app/Makefile

WORKDIR /opt/app

RUN apt-get -y update && apt-get install -y --no-install-recommends \
    libusb-1.0-0-dev \
    libudev-dev \
    build-essential \
    ca-certificates && \
    rm -fr /var/lib/apt/lists/*

# Keep python from buffering the stdout - so the logs flushed quickly
ENV PYTHONUNBUFFERED=TRUE

# Don't compile bytecode
ENV PYTHONDONTWRITEBYTECODE=TRUE

ENV PATH="/opt/app:${PATH}"

ENV PYTHONPATH=.

EXPOSE 8000

ENTRYPOINT ["make", "run_all"]