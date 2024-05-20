import sqlite3


class Connection:
    
    def __init__(self,name):
        """Constructor

        Args:
            name (string): database's name
        """
        #table name
        self.name = name
        self.conn = ""

        #initialize tables
        self.create_tables()

    def create_tables(self):
        """ Create the tables if they don`t exists yet
        """
        queries = []
        
        #List of tables, one crete query for each item in the list
        queries.append (""" CREATE TABLE IF NOT EXISTS tasks (
            ID              INTEGER PRIMARY KEY AUTOINCREMENT,
            task            TEXT NOT NULL,
            active          INTEGER NOT NULL DEFAULT 0) """)
 
        try:
            # Open connection
            self.open() 
            cursor = self.conn.cursor()
            
            #Execute queries
            for query in queries:
                self.query(query)
            #Commit queries
            self.commit()
                        
        except sqlite3.Error as e:
            print(e)

    def open(self):
        """Open the connection to sqllite3 database and assign it to conn parameter. 
        """
        self.conn = sqlite3.connect(self.name)
        
    def query(self,query):
        """execute a query and returns the results

        Args:
            query (string): SQL Query for SQLITE3

        Returns:
            _type_: query's result
        """
        cursor = self.conn.cursor()  
        cursor.execute(query)
        return cursor
        
    def commit(self):
        """Commit the actual executed queries
        """
        self.conn.commit()
    
    def error(self,message):
        """Return a error of type sqlite3
        """
        raise sqlite3.IntegrityError(message)
        
    def close(self):
        """ Close the connection open
        """
        self.conn.close()
