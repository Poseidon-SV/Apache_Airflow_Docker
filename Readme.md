# Airflow Docker 
`> bash`

Download `docker-compose.yaml` file with
`$ curl -Lfo 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'`

for windows: ``$ curl -L 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'``


```bash
$ mkdir ./dags ./plugins ./logs ./config
$ echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
```
Airflow initializing in docker
`$ docker-compose up airflow-init`


```bash
shubham@Verma:/mnt/d/My Computer (Shubham)/AI/Apache_Airflow/Docker_airflow$ docker-compose up airflow-init
[+] Running 36/3
 ⠏ airflow-init 19 layers [⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿] 189.4MB/219MB   Pulling                                                          91.0s 
 ✔ redis 6 layers [⣿⣿⣿⣿⣿⣿]      0B/0B      Pulled                                                                                     23.3s 
 ⠏ postgres 12 layers [⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿] 55.62MB/102MB   Pulling                                                                        91.0s 
```

Last thing is to execute the command
`docker-compose up`

To check docker is running(in new terminal) run
`docker ps`
```
CONTAINER ID   IMAGE                  COMMAND                  CREATED              STATUS                        PORTS                    NAMES
6e3bc26d7a85   apache/airflow:2.6.2   "/usr/bin/dumb-init …"   About a minute ago   Up About a minute (healthy)   8080/tcp                 docker_airflow-airflow-scheduler-1
0b1fe8c6bc96   apache/airflow:2.6.2   "/usr/bin/dumb-init …"   About a minute ago   Up About a minute (healthy)   0.0.0.0:8080->8080/tcp   docker_airflow-airflow-webserver-1
c96651ba7bd7   apache/airflow:2.6.2   "/usr/bin/dumb-init …"   About a minute ago   Up About a minute (healthy)   8080/tcp                 docker_airflow-airflow-triggerer-1
520301ba153d   apache/airflow:2.6.2   "/usr/bin/dumb-init …"   About a minute ago   Up About a minute (healthy)   8080/tcp                 docker_airflow-airflow-worker-1
061aa3afd884   postgres:13            "docker-entrypoint.s…"   5 minutes ago        Up 4 minutes (healthy)        5432/tcp                 docker_airflow-postgres-1
42143729da5f   redis:latest           "docker-entrypoint.s…"   5 minutes ago        Up 4 minutes (healthy)        6379/tcp                 docker_airflow-redis-1

```

## Very Very important
### Use: `http://localhost:8080/`

to run your airflow if it shows server not able to connect in `http://0.0.0.0:8080/`


## Project
open docker desktop
`> docker-compose up -d`
`> docker-compose up`
Username - pass
`docker-compose.yaml`
```yaml
256| _AIRFLOW_WWW_USER_USERNAME: ${_AIRFLOW_WWW_USER_USERNAME:-airflow}
257| _AIRFLOW_WWW_USER_PASSWORD: ${_AIRFLOW_WWW_USER_PASSWORD:-airflow}
```
Delete all exmmple Dags to create own
`docker-compose down -v` (shutdown and remove vol in dok compose yaml file)

Change in `docker-compose.yaml`
```yaml
65|   AIRFLOW__CORE__LOAD_EXAMPLES: 'false' # true
```
init
`> docker-compose up airflow-init`
launch
`> docker-compose up -d`
Now all exp will be removed

Now start coding
dags> my_fst_dag.py

