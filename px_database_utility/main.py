import json
import logging
import sys

import pkg_resources

from .classes import ConnectionDetails
from .cli import get_cl_arguments
from .db import dump_schema, restore_schema, get_all_database, select_database, get_all_backup_database, select_database_backup
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
    file = cl_arguments['file']

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
    
    elif operation == 'RESTORE':
        db.dbname = database
        if file is None:
            all_database = get_all_backup_database()
            if len(all_database) == 0:
                log.error('No database backup found at {}'.format('----------- put something'))
                sys.exit(1)
            selected_db = select_database_backup(all_database)
            print(selected_db)
            restore_schema(db, selected_db)
        else:
            restore_schema(db, file)

    elif operation == 'LIST':
        all_database = get_all_database(db)
        return json.dumps(all_database)


if __name__ == '__main__':
    main()
