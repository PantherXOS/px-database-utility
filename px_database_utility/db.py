import logging
import os
import subprocess
from datetime import datetime

import psycopg2
from psycopg2 import OperationalError, connect

from .config import DEFAULT_DATABASE_DUMP_PATH

log = logging.getLogger(__name__)


def get_connection_string(db: 'ConnectionDetails'):
    conn_string = 'postgres://{}:{}@{}:{}'.format(
        db.username, db.password, db.host, db.port
    )
    return conn_string


def create_dump_path_if_does_not_exist(path: str):
    '''Create the backup path if it does not exist'''
    if not os.path.isdir(path):
        os.makedirs(path)


def dump_schema(db: 'ConnectionDetails'):
    '''Dump selected database to file'''
    filename = "{}_{}.dmp".format(db.dbname, int(datetime.utcnow().timestamp()*1e3))
    create_dump_path_if_does_not_exist(DEFAULT_DATABASE_DUMP_PATH)
    file = '{}/{}'.format(DEFAULT_DATABASE_DUMP_PATH, filename)
    log.info('=> Dumping database to {}'.format(file))
    command = f'pg_dump --host={db.host} ' \
        f'--port={db.port} ' \
        f'--dbname={db.dbname} ' \
        f'--username={db.username} ' \
        f'--no-password ' \
        f'--format=c ' \
        f'--file={file}'

    os.environ["PGPASSWORD"] = db.password

    proc = subprocess.run(command, shell=True, capture_output=True)

    if proc.returncode == 0:
        log.debug('Success')
    else:
        log.error(proc.stderr)
        raise Exception(proc.stderr)

    os.environ["PGPASSWORD"] = ''

    return file


def get_all_database(db: 'ConnectionDetails'):
    '''Get a list of all available database'''
    connection_string = get_connection_string(db)
    database_list_cleaned = []

    try:
        conn = psycopg2.connect(connection_string)

        cursor = conn.cursor()
        s = ""
        s += "SELECT datname FROM pg_database"
        s += " WHERE datistemplate = false;"

        cursor.execute(s)
        database_list = cursor.fetchall()

        database_list_cleaned = []

        for item in database_list:
            database_list_cleaned.append(item[0])

    except OperationalError as err:
        log.error(err)

    return database_list_cleaned


def select_database(database_list):
    '''Prompt the user to select from a list of database'''

    print('Found {} database. Select the one you would like to interact with.'.format(len(database_list)))
    count = 0
    for db in database_list:
        print('{} {}'.format(count, db))
        count += 1

    selected_database = input('Which database do you want to work with?: (number) ')
    return database_list[int(selected_database)]
