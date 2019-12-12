# HPC 
> Web application for the HPC.

First in the folders ***service_nginx/volumes/ssl/*** and ***service_pgadmin/volumes/ssl/*** you must create the files:
+ ***certificate.crt***
+ ***certificate_key.key***

Also you must create the file .env in the project root:
+ ***.env***

The ***.env*** file must have the environment variables:
```
# APPLICATION
APPLICATION=hpc
ENVIRONMENT=development
VERSION=latest

# SERVICE_POSTGRES
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=hpc
POSTGRES_USER=hpc
POSTGRES_PASSWORD=12345*abc
PGDATA=/var/lib/postgresql/data

# SERVICE_PGADMIN
PGADMIN_HOST=pgadmin
PGADMIN_PORT=444
PGADMIN_DEFAULT_EMAIL=user@domain.com
PGADMIN_DEFAULT_PASSWORD=SuperSecret
PGADMIN_ENABLE_TLS=True
PGADMIN_SERVER_NAME=pgadmin.hpc.uclv.cu

# SERVICE_RABBITMQ
RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672
RABBITMQ_DEFAULT_USER=hpc
RABBITMQ_DEFAULT_PASS=12345*abc

# SERVICE_DJANGO
DJANGO_HOST=django
DJANGO_HTTP_SOCKET_HOST=0.0.0.0
DJANGO_PORT=8080
DJANGO_SECRET_KEY='d^1v!34h_+0jjl%yh5))vb2j0j=)=&jygpym$%u$+ja6i14@ge'

# SERVICE_DJANGO_EMAILS
DJANGO_EMAIL_HOST=10.12.1.5
DJANGO_EMAIL_PORT=25
DJANGO_EMAIL_USER_NOREPLY=noreply@uclv.edu.cu

# SERVICE_DJANGO_LDAP
DJANGO_LDAP_SERVER_HOST=10.12.31.4
DJANGO_LDAP_SERVER_PORT=389
DJANGO_LDAP_SERVER_USER=cn=admin,dc=hpc,dc=cu
DJANGO_LDAP_SERVER_PASSWORD='7H\_VJBP>)hP{xZ}C'
DJANGO_LDAP_SERVER_GROUPS_SEARCH_BASE=ou=Groups,dc=hpc,dc=cu
DJANGO_LDAP_SERVER_GROUPS_LIST='UCLV UCI UO'
DJANGO_LDAP_SERVER_GROUPS_GROUP_CN=UCLV
DJANGO_LDAP_SERVER_GROUPS_GROUP_GIDNUMBER=5001
DJANGO_LDAP_SERVER_USERS_SEARCH_BASE=ou=AllPeople,dc=hpc,dc=cu
DJANGO_LDAP_SERVER_USERS_HPC_SEARCH_BASE=ou=People,dc=hpc,dc=cu
DJANGO_LDAP_SERVER_USERS_HOMEDIRECTORY=/home/CLUSTER/

# SERVICE_DJANGO_CLUSTER
DJANGO_CLUSTER_SERVER_HOST=10.12.31.20
DJANGO_CLUSTER_SERVER_PORT=22

# SERVICE_DJANGO_CELERY_RESULTS
DJANGO_CELERY_RESULTS_HOST=service_django_celery_results

# SERVICE_DJANGO_CELERY_BEAT
DJANGO_CELERY_BEAT_HOST=service_django_celery_beat

# SERVICE_NGINX
NGINX_HOST=nginx
NGINX_PORT_HTTP=80
NGINX_PORT_HTTPS=443
NGINX_SERVER_NAME=hpc.uclv.cu

```

The application works in two modes, you must specify one of the following modes in the ***ENVIRONMENT*** variable in the ***.env*** file:
+ ***development***
+ ***production***

To work you must go to the root of the project and write depending on the way you want the application to work:
``` [bash]
sudo ./docker-compose.sh --build
```
