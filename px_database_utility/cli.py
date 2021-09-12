'''Command line interface'''

import argparse
import logging
import os
import sys

log = logging.getLogger(__name__)


def get_cl_arguments():
    '''Command line arguments'''
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--operation", type=str, required=True,
                        choices=['BACKUP', 'RESTORE', 'LIST'],
                        help="Primary operations."
                        )
    parser.add_argument("-d", "--database", type=str, default='SELECT',
                        help="Specify single DB or all with 'ALL' | Restore: Specify the DB name to restore to."
                        )
    parser.add_argument("-i", "--interface", type=str,
                        help="Specify database host"
                        )
    parser.add_argument("-p", "--port", type=str,
                        help="Specify database post"
                        )
    parser.add_argument("-u", "--username", type=str,
                        help="Specify database username"
                        )
    parser.add_argument("-pw", "--password", type=str,
                        help="Specify database password"
                        )
    parser.add_argument("-f", "--file", type=str,
                        help="RESTORE only: Restore from absolute file path."
                        )
    parser.add_argument("-k", "--keep", type=int, default=5,
                        help="Number of backups to keep"
                        )
    args = parser.parse_args()

    if args.operation == 'RESTORE':
        if args.database is None or args.database == 'SELECT':
            log.error(
                'You need to define a target name `--database DATABASE` for restore operations.')
            sys.exit(1)
        else:
            if args.database.endswith('.dmp'):
                log.error(
                    'Use the --file flag for the absolute path; use the --database flag for the target database name.')
                sys.exit(1)

        if args.file is not None:
            if args.file.endswith('.dmp') == False:
                log.error('Database backup files usually end with .dmp.')
                sys.exit(1)
            else:
                if os.path.isfile(args.file) == False:
                    log.error('File {} could not be found.'.format(args.file))
                    sys.exit(1)

    return {
        'operation': args.operation,
        'database': args.database,
        'host': args.interface,
        'port': args.port,
        'username': args.username,
        'password': args.password,
        'file': args.file,
        'keep': args.keep
    }
