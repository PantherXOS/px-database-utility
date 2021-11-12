# PantherX Database Utilities

Designed to make working with local databases more convenient.

At the moment only PostgreSQL is supported.

- By default only the 5 latest backups for each database (by name) are stored.
- Backups are stored at `/var/opt/px-database-utility`
- Supported database names may include `_` or `-`. For ex. `primaryDatabase`, `primary_database`, `primary-database`

## Setup

**Requirements**

- `postgresql` (with `pg_dump`, `pg_restore`, `createdb`)

### Install on PantherX OS

```bash
guix package -i px-database-utility
```

### Install with pip package manager

```bash
pip3 install https://source-git-pantherx-org.s3.eu-central-1.amazonaws.com/px-database-utility_latest.tgz
```

_This might fail since we dropped using binary psycopg2. Here's the last release with binary:_

```bash
pip3 install https://source-git-pantherx-org.s3.eu-central-1.amazonaws.com/px-database-utility_v0.1.1.tgz
```

## Run

### Backup

There's two ways to run this:

```bash
px-database-utility
px-db-util
```

Run with defaults, it will prompt for your desired DB:

```bash
$ px-database-utility -o BACKUP
INFO: ------
INFO: Welcome to PantherX Database Utility v0.1.1
INFO: v0.1.1
INFO: ------
pg_dump (PostgreSQL) 12.7
Found 2 database. Select the one you would like to interact with.
0 postgres
1 primaryDatabase
Which database do you want to work with?: (number) 1
INFO: => Dumping database to /var/opt/px-database-utility/1635677798_primaryDatabase.dmp
INFO: --- Enable backup for this database on Central Management ---
INFO: 1. Ensure you have added a Device Backup Destination
INFO: 2. Add the database name(s) to the database backup scope
INFO: ---
["/var/opt/px-database-utility/1635677798_primaryDatabase.dmp"]
```

Specify a DB to backup:

```bash
px-db-util --operation BACKUP --database dev
```

Backup all DB:

```bash
px-db-util --operation BACKUP --database ALL
```

**Default backup location**: `/var/opt/px-database-utility/DBNAME_UNIXTIMESTAMP.dmp` (timestamp is in seconds)

For non-default database:

```bash
px-db-util --operation BACKUP \
--database DATABASE \
--interface 127.0.0.1 \
--port 5432 \
--username USER \
--password PASSWORD
```

_This only works for `root` users._

To backup to a specific file-path, use `--file`:

```bash
px-db-util --operation BACKUP \
--database DATABASE \
--interface 127.0.0.1 \
--port 5432 \
--username USER \
--password PASSWORD \
--file /some/path.dmp
```

### Restore

To restore a database (creates new database if it does not exist):

_This assumes that a backup is available at `/var/opt/px-database-utility/*`_

```bash
px-database-utility --operation RESTORE --database production
```

To restore a specific file (creates new database if does not exist):

```bash
px-database-utility --operation RESTORE --database production --file `ABSOLUTE_PATH.dmp`
```

**To ignore ownership**

```
--no-owner
```

### List

To list all tables:

```bash
px-db-util -o LIST
```

### Misc

Development

```bash
guix environment \
--pure python \
--ad-hoc python-psycopg2 python-setuptools
```

and

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install .
```
