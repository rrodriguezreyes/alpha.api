import psycopg2
from typing import List, Dict, Any


class Database:
    def __init__(self, connection_params: Dict[str, str]):
        self.connection_params = connection_params
        self._connection: psycopg2.extensions.connection = None

    @property
    def connection(self):
        if self._connection is None:
            self.connect()
        return self._connection

    def connect(self):
        self._connection = psycopg2.connect(**self.connection_params)

    def disconnect(self):
        if self._connection:
            self._connection.close()

    def fetch_all(self, query: str, *args) -> List[Dict[str, Any]]:
        with self.connection.cursor() as cursor:
            cursor.execute(query, args)
            columns = [desc[0] for desc in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def fetch_one(self, query: str, *args) -> Dict[str, Any]:
        with self.connection.cursor() as cursor:
            cursor.execute(query, args)
            columns = [desc[0] for desc in cursor.description]
            row = cursor.fetchone()
            return dict(zip(columns, row)) if row else None

    def fetch_val(self, query: str, *args) -> Any:
        result = self.fetch_one(query, *args)
        return result[0] if result else None

    def execute(self, query: str, values: List[Any] = None) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            self.connection.commit()


connection_params = {
    'user': 'alpha',
    'password': 'P@$$w0rd',
    'host': 'alpha-dbserver.postgres.database.azure.com',
    'port': '5432',
    'database': 'postgres',
    'sslmode': 'require'
}

database = Database(connection_params)
