# PantherX Database Utilities

Designed to make working with local databases more convenient.

For now, we only support PostgreSQL.


## Setup

**Requirements**

- `postgresql` (with `pg_dump`)

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

### Misc

Development

```
guix environment \
--pure python \
--ad-hoc python-exitstatus-2.0.1 python-setuptools
```