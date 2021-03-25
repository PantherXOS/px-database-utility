import json
import logging
import sys

import pkg_resources

from .classes import ConnectionDetails
from .cli import get_cl_arguments
from .db import dump_schema, get_all_database, select_database
from .log import *

version = pkg_resources.require("px_database_utility")[0].version


log = logging.getLogger(__name__)

def main():
    log.info('------')
    log.info('Welcome to PantherX Database Utility v{}'.format(version))
    log.info('v{}'.format(version))
    log.info('------')

    cl_arguments = get_cl_arguments()
    operation = cl_arguments['operation']
    database = cl_arguments['database']

    db = ConnectionDetails()
    merge = ['host', 'port', 'username', 'password']

    for prop in merge:
        if cl_arguments[prop] is not None:
            db[prop] = cl_arguments[prop]

    if operation == 'BACKUP':
        db_array = []

        if database == 'SELECT' or database == 'ALL' or database == None:
            all_database = get_all_database(db)
            if len(all_database) == 0:
                log.error('No database found.')
                sys.exit(0)
            if database == 'ALL':
                db_array = all_database
            else:
                selected_db = select_database(all_database)
                db_array.append(selected_db)
        else:
            db_array.append(database)

        database_backup_files = []

        for db_for_backup in db_array:
            db.dbname = db_for_backup
            backup_file = dump_schema(db)
            database_backup_files.append(backup_file)

        return json.dumps(database_backup_files)


if __name__ == '__main__':
    main()
