from playhouse.pool import PooledMySQLDatabase

db = PooledMySQLDatabase('test',
                         user='root', password='test',
                         host='localhost', port=3306,
                         max_connections=16,
                         stale_timeout=300)
