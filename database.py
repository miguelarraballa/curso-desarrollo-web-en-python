import sqlite3

class Connection:
    """
        Clase que abre una conexión SQLite3, crea las tablas necesarias sino existen y métodos para usar la conexión. 
    """    
    def __init__(self,name):
        """Constructor

        Args:
            name (string): nombre de la base de dato
        """
        #Nombre de la tabla
        self.name = name
        self.conn = ""

        #Inicializa las tablas
        self.create_tables()

    def create_tables(self):
        """ Crea las tablas si aún no existen
        """
        queries = []
        
        #lista de tablas. Un item por tabla que haya que crear.
        queries.append (""" CREATE TABLE IF NOT EXISTS tasks (
            ID              INTEGER PRIMARY KEY AUTOINCREMENT,
            taLk            TEXT NOT NULL,
            finish          INTEGER NOT NULL DEFAULT 0) """)
 
        try:
            # Abre la conexión
            self.open() 
            cursor = self.conn.cursor()
            
            #Ejecuta las queries de la lista
            for query in queries:
                self.query(query)
            #hace los cambios
            self.commit()
                        
        except sqlite3.Error as e:
            print(e)

    def open(self):
        """Abre una conexión SQLite3 en un archivo indicado al instanciar la clase. 
        """
        self.conn = sqlite3.connect(self.name)
        
    def query(self,query):
        """Ejecuta una query y devuelve el resultado
        Args:
            query (string): SQL Query de SQLITE3

        Returns:
            _type_: Resultado de la query
        """
        cursor = self.conn.cursor()  
        cursor.execute(query)
        return cursor
        
    def commit(self):
        """ Fija los cambios en la conexion abierta 
        """
        self.conn.commit()
    
    def error(self,message):
        """ Fuerza un error de tipo SQLite3 para que pueda ser capturado por la excepción. 
        """
        raise sqlite3.IntegrityError(message)
        
    def close(self):
        """ Cierra la conexión que se ha abierto al instanciar.  
        """
        self.conn.close()
