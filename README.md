# PantherX Database Utilities

Designed to make working with local databases more convenient.

For now, we only support PostgreSQL.


## Setup

**Requirements**

- `postgresql` (with `pg_dump`, `pg_restore`, `createdb`)

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install .
```

### Install with pip package manager

```bash
pip3 install https://source-git-pantherx-org.s3.eu-central-1.amazonaws.com/px-database-utility_latest.tgz
```

## Run

### Backup

Run with defaults, it will prompt for your desired DB:

```bash
px-database-utility --operation BACKUP
```

Specify a DB to backup:

```bash
px-db-util --operation BACKUP --database dev
```

Backup all DB:

```bash
px-db-util --operation BACKUP --database ALL
```

**Default backup location**: `/var/opt/px-database-utility/DBNAME_UNIXTIMESTAMP.dmp`

For non-default database location:

```bash
px-db-util --operation BACKUP \
--database DATABASE \
--interface 127.0.0.1 \
--port 5432
--username USER
--password PASSWORD
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

### List

To list all tables:

```bash
px-db-util -o LIST
```

### Misc

Development

```
guix environment \
--pure python \
--ad-hoc python-exitstatus-2.0.1 python-setuptools
```