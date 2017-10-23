from fabric.api import local, task


@task
def up():
    local("docker-compose up")


@task
def run():
    local("docker exec -it dockerspark_master_1 /bin/bash -c '$SPARK_HOME/bin/spark-submit $PROJECT_HOME/src/test.py'")


@task
def run():
    local("docker exec -it dockerspark_master_1 /bin/bash -c '$SPARK_HOME/bin/spark-submit $PROJECT_HOME/src/test.py'")


@task
def ch():
    local(
        "docker run -it --rm --link dockerspark_clickhouse_1:clickhouse-server yandex/clickhouse-client --host clickhouse")


@task
def pg():
    local("docker run -it --rm --link dockerspark_postgres_1:postgres postgres psql -h postgres -U postgres")
