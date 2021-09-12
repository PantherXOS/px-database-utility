import json
import logging
import sys

import pkg_resources

from .classes import ConnectionDetails
from .cli import get_cl_arguments
from .config import DEFAULT_DATABASE_DUMP_PATH
from .db import (dump_schema, get_all_backup_database, get_all_database,
                 restore_schema, select_database, select_database_backup)
from .log import *
from .util import check_dependencies, remove_old_backups

version = pkg_resources.require("px_database_utility")[0].version


log = logging.getLogger(__name__)


def main():
    log.info('------')
    log.info('Welcome to PantherX Database Utility v{}'.format(version))
    log.info('v{}'.format(version))
    log.info('------')

    pg_dump_is_installed = check_dependencies()
    if pg_dump_is_installed is False:
        return 'False'

    cl_arguments = get_cl_arguments()
    operation = cl_arguments['operation']
    database = cl_arguments['database']
    number_of_backups_to_keep = cl_arguments['keep']
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

            remove_old_backups(db_for_backup, number_of_backups_to_keep)
            # Remove old backups

        log.info('--- Enable backup for this database on Central Management ---')
        log.info('1. Ensure you have added a Device Backup Destination')
        log.info('2. Add the database name(s) to the database backup scope')
        log.info('---')

        return json.dumps(database_backup_files)

    elif operation == 'RESTORE':
        db.dbname = database
        if file is None:
            all_database = get_all_backup_database()
            if len(all_database) == 0:
                log.error('No database backup found at {}'.format(
                    DEFAULT_DATABASE_DUMP_PATH
                ))
                return 'NONE'
            selected_db = select_database_backup(all_database)
            print(selected_db)
            restore_schema(db, selected_db)
        else:
            restore_schema(db, file)

    elif operation == 'LIST':
        all_database = get_all_database(db)
        if len(all_database) > 0:
            print("Found {} database:".format(len(all_database)))
            for item in all_database:
                print("- {}".format(item))
        else:
            log.warn("No database found.")
        return json.dumps(all_database)


if __name__ == '__main__':
    main()
