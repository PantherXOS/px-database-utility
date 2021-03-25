'''Command line interface'''

import argparse
import logging

log = logging.getLogger(__name__)


def get_cl_arguments():
    '''Command line arguments'''
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--operation", type=str, required=True,
                        choices=['BACKUP'],
                        help="Primary operations."
                       )
    parser.add_argument("-d", "--database", type=str, default='SELECT',
                        help="Backup a specific database, or all databse with 'ALL'"
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
    args = parser.parse_args()

    return {
        'operation': args.operation,
        'database': args.database,
        'host': args.interface,
        'port': args.port,
        'username': args.username,
        'password': args.password
    }
