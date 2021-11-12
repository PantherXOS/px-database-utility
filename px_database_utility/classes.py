from dataclasses import dataclass

@dataclass
class ConnectionDetails:
    host: str = '127.0.0.1'
    port: str = '5432'
    dbname: str = ''
    username: str = 'postgres'
    password: str = 'postgres'
    no_owner: bool = False