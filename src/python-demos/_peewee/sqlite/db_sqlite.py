from playhouse.pool import PooledSqliteDatabase

db = PooledSqliteDatabase('test.db',
                          max_connections=16,
                          stale_timeout=300)
