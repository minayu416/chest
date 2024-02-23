# Import any settings of db connection tool (engine or driver)
# from sqlalchemy import create_engine, event
# from sqlalchemy.pool import QueuePool


# Init one SQL connection pool
class DatabasePool(object):
    """Create DB connection with pretent singleton design pattern
    
    Use:
        >>> db_pool = DatabasePool("<db_url>").get()
    """

    def __init__(self, db_url):
        self.db_url = db_url
        self.engine = None

    def get(self):
        if not self.engine:
            # If not existing connection, init one, you can use any connection method to instead this line.
            self.engine = create_engine(self.db_url, poolclass=QueuePool)
        return self.engine


# TODO can use with syntax to write function.
class DBOperator(object):
    """The operator of database, CRUD with DB.
    
    Use:
        >>> db_operator = DBOperator(<connection>)
        >>> db_operator.get(sql_statement)
        >>> db_operator.execute(...)
        >>> db_operator.update(...)
    """

    def __init__(self, engine):
        self.engine = engine

    def get(self, stmt):
        conn = self.engine.connect()
        try:
            result = conn.execute(stmt)
            result = [r for r in result]
            return result
        except Exception as e:
            print(str(e))
            # TODO logger().error("Error Msg: " + str(e))

        finally:
            conn.close()

    def execute(self, sql, params):
        conn = self.engine.connect()
        try:
            for param in params:
                add_sql = sql % param
                conn.execute(add_sql)

        except Exception as e:
            print(str(e))
            # TODO logger().error("Error Msg: " + str(e))

        finally:
            conn.close()

    def update(self, params):
        conn = self.engine.connect()
        try:
            # TODO
            # result = conn.execute("SELECT * FROM table")
            # result = [r for r in result]
            return result
        except Exception as e:
            print(str(e))
            # TODO logger().error("Error Msg: " + str(e))

        finally:
            conn.close()