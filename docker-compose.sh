#!/bin/bash

# Variables defined will be exported into this script's environment:
set -a
source .env

# Give permission to execute.
sudo chmod +x ./service_django/commands/cmd.sh
sudo chmod +x ./service_django/commands/entrypoint.sh
sudo chmod +x ./service_django/commands/celery.sh

if [ "$1" == '--build' ]
then
    # Create network
    docker network create ${APPLICATION}

    docker-compose build
    docker-compose up -d --force-recreate

    # Necessary for the pgadmin volume to work.
    docker exec ${APPLICATION}_${PGADMIN_HOST} chown apache:1000 -R /var/lib/pgadmin/

elif [ "$1" == '--bash' ]
then
    docker exec -i -t ${APPLICATION}_${DJANGO_HOST} /bin/bash

else
    echo "[options]"
    echo "--build"
    echo "--bash"
fi