FROM python:3.7

RUN echo "deb http://repos.uclv.edu.cu/debian buster main non-free contrib\n \
deb http://repos.uclv.edu.cu/debian buster-updates main non-free contrib\n \
deb http://repos.uclv.edu.cu/debian-security buster/updates main non-free contrib\n \
deb http://repos.uclv.edu.cu/debian buster-proposed-updates main non-free contrib\n \
deb http://repos.uclv.edu.cu/debian buster-backports main non-free contrib \
" > /etc/apt/sources.list

ARG DEBIAN_FRONTEND=noninteractive

RUN  apt-get update && apt-get install -y --no-install-recommends \
    apt-utils \
    gettext \
    postgresql-client \
    libz-dev \
    libjpeg-dev \
    libfreetype6-dev \
    python-dev \
&& rm -rf /var/lib/apt/lists/*

ARG ENVIRONMENT

RUN mkdir -p /service_django
WORKDIR /service_django

RUN mkdir -p application
RUN mkdir -p volumes volumes/celery volumes/staticfiles volumes/mediafiles
RUN mkdir -p commands

COPY ./application application
COPY ./commands commands

WORKDIR /service_django/application
ADD pip.conf /etc/pip.conf
RUN pip3 install pip --upgrade
RUN pip3 install --no-cache-dir -r requirements/${ENVIRONMENT}.txt

# Set a custom entrypoint to let us provide custom initialization behavior
ENTRYPOINT ["/service_django/commands/entrypoint.sh"]
# Set the command to start uwsgi
CMD ["/service_django/commands/cmd.sh"]
