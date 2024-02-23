from redis import Redis, ConnectionPool

from config import config
from log import logger


def if_not_else(value1, value2):
    """According if-else condition to detect None/Null/0 value.

    Args:
        value1:
        value2:

    Returns:
        value1 or value2:

    """
    return value1 if value1 else value2


class RedisPool():
    """Open Redis connection pool

    Other Information:
        To monitor redis command, please refer below url
        https://gist.github.com/sripathikrishnan/2604537, or
        https://stackoverflow.com/questions/10458146/how-can-i-mimic-the-redis-monitor-command-in-a-python-script-using-redis-py

    """

    __pool = None

    def __init__(self, name: str, host: str, port: int, db: int = 0, password: str = None):
        self.__pool = ConnectionPool(host=host, port=port, db=db, password=password)

    def get_conn(self):
        conn = Redis(connection_pool=self.__pool)
        return conn


__redis_list = {}
__all_redis = config.get_value('redis')

if __all_redis:
    __db = 0
    __default = __all_redis.get('default')

    if __default:
        __db = if_not_else(__default.get('db'), __db)
    else:
        logger.warning('No default redis configuration')

    for redis_name in __all_redis:
        if redis_name == 'default':
            continue
        redis = __all_redis[redis_name]
        redis_host = redis['host']
        redis_port = redis['port']
        redis_db = if_not_else(redis.get('pool_size'), __db)
        password = redis.get("password")

        logger.info(f'Create redis pool for {redis_name}')
        redis_pool = RedisPool(name=redis_name, host=redis_host, port=redis_port, db=redis_db, password=password)
        __redis_list[redis_name] = redis_pool

else:
    logger.warning('No redis configuration')


def get_conn(redis_name: str):
    return __redis_list[redis_name].get_conn()


class RedisOperator(object):
    """Redis Operator: operate Redis, set key, get key, delete key and others operation action.

    Description:
        set_one_json(p: conn, key: str, value: [str, list, dict]): to set single key and data.
        set_multiple_json(p: conn, data: dict): to set multiple key and data.
                data value: dict: [{key: value, key: value, ...}]
        get_one(key:str): return data of specific key.
        get_multiple_keys(key_prefix: str): get multiple keys that with specific key_prefix.
        get_multiple_value(keys: list): get multiple value of multiple keys.
        delete_multiple_keys(keys: list): delete multiple keys.

    Notice:
        illegal format: tuple, can not be json.

    """

    def __init__(self, conn):
        self.conn = conn

    def __set(self, p, key: str, value: str):
        value = value.encode(encoding="utf-8")
        p.set(key, value)
        logger.debug(f"Load Data into Redis: {key} = {value}")

    def set_one_json(self, key: str, value: str) -> None:
        try:
            with self.conn as p:
                self.__set(p, key, value)
                logger.debug("Completed set data!")

        except Exception as e:
            logger.exception(f"Failed to write data into redis, {str(e)}")
            raise

    def set_multiple_json(self, data: dict) -> None:
        try:
            with self.conn.pipeline() as p:
                if isinstance(data, dict):
                    for key, value in data.items():
                        self.__set(p, key, value)

                p.execute()
                logger.debug("Completed set data!")

        except Exception as e:
            logger.exception(f"Failed to write data into redis, {str(e)}")
            raise

    def get_one_json(self, key: str) -> str:
        try:
            with self.conn as p:
                value = p.get(key)
                return value.decode(encoding="utf-8")

        except Exception as e:
            logger.exception(f"Failed to get data from redis, {str(e)}")
            raise

    def get_multiple_keys(self, namespace: str) -> list:
        try:
            with self.conn as p:
                multi_keys = p.keys(pattern=f"{namespace}:*")
                multi_keys = [key.decode(encoding="utf-8") for key in multi_keys]
                return multi_keys

        except Exception as e:
            logger.exception(f"Failed to get data from redis, {str(e)}")

    def get_multiple_value(self, keys: list) -> list:
        try:
            with self.conn as p:
                multi_value = p.mget(keys)
                multi_value = [value.decode(encoding="utf-8") for value in multi_value]
                return multi_value

        except Exception as e:
            logger.exception(f"Failed to get data from redis, {str(e)}")

    def delete_multiple_keys(self, keys: list) -> None:
        try:
            with self.conn as p:
                p.delete(*keys)
                logger.debug(f"Deleted keys in redis, {str(keys)}")

        except Exception as e:
            logger.exception(f"Failed to delete data in redis, {str(e)}")
