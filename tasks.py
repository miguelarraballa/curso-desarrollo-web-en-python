import database as database

class Task:
    """Clase que sirve de modelo y controlador de "tareas"
    """
    
    def __init__(self,name):
        """Constructor

        Args:
            name (string): Nombre de la base de datos que se va a usar.
        """
        #Nombre de la tabla que se va a usar
        self.table = "tasks" 
        #Por defecto si el usuario no escribe nada al inicio su nombre sera Anonymous.
        self.user_name = 'Anonymous'
        #Instancia una conexión SQLite3
        self.db = database.Connection(name)
    
    def create(self,task):
        """Inserta una tarea

        Args:
            task (string): Nombre de la tarea
        """
        #Debe ser de typo string o int o informa de un error. Por defecto input debe traer una string.
        if (type(task) != str and type(task) != int):
            self.db.error(f"La tarea debe ser un texto, has introducido: {type(task)}")
        #Inserta la tarea en la tabla
        query = f"INSERT INTO {self.table} (task) VALUES ('{task}')"
        self.db.query(query) 
        self.db.commit()
        print("Tarea guardada")
        
    
    def read(self):
        """Imprime una lista formateada con todas las tareas
        """
        try:
            #Hace una select a la tabla
            query = f"SELECT * FROM  {self.table} ORDER BY ID ASC"
            results = self.db.query(query) 
            self.db.commit()
            #Devolvemos todos los resultados en una lista. 
            tasks = results.fetchall()

            #si no hay tareas, pues no hay tareas
            if not tasks:
                print("Sin tareas aún")
            else: 
            #hay tareas, así que recorre la lista y formatea cada línea.
                for task in tasks:
                    #Si el tercer item (que es "finish") es o está pendiente si es 1 está finalizada. 
                    if task[2] == 0: 
                        state = "PENDIENTE"
                    else:
                        state = "TERMINADO"
                        
                    #imprime una linea formateada. 
                    print(f"{state} -> {task[0]: 2} - {task[1]}")
        except:
            print("Error en la  ejecución")
            
    
    def update(self,id):
        """Marca una tarea como terminada

        Args:
            id (int): La id de la tarea.
        """
        try:
            #Comprueba si la id está en la tabla y si lo está actualiza el campo. 
            if (self.is_task_in_table(id)):
                query = f"UPDATE {self.table} SET finish = 1 WHERE id = {id}"
                results = self.db.query(query) 
                self.db.commit()
                print(f"Tarea {id} finalizada")
            else:
                #Si no aparece, pues lo dice
                print(f"Con {id} no me viene nada")
        except:
            print("Error en la  ejecución")
    
    def delete(self,id):
        """Elimina una tarea de la tabla

        Args:
            id (int): Id de la tarea en la tabla. 
        """
        try:
            #Comprueba si hay una tarea con esa id, si la hay la elimina, si no la hay lo dice. 
            if (self.is_task_in_table(id)):
                query = f"DELETE FROM {self.table} WHERE id = {id}"
                results = self.db.query(query) 
                self.db.commit()
                print(f"Tarea {id} eliminada")
            else:
                print(f"Con {id} no me viene nada")
        except:
            print("Error en la  ejecución")
    
    def set_name(self,name):
        """Da valor al nombre de usuario (user_name)

        Args:
            name (string): Nombre del usuario, que debería ser la cadena que se le ha pedido al usuario. 
        """
        if name.strip() != "":
            self.user_name = str(name)
    
    def get_name(self):
        """Devuelve el valor que tenga user_name 

        Returns:
            string: El valor de la variable user_name
        """
        return self.user_name
    
    def is_task_in_table(self,id):
        """Compruba si la tarea, por su id, está en la tabla

        Args:
            id (int): id de la tarea

        Returns:
            boolean: True or False
        """
        try:
            #Ejecuta una consulta a la base de datos
            query = f"SELECT * FROM {self.table} WHERE id = {id}"
            results = self.db.query(query) 
            self.db.commit()
            tasks = results.fetchone()
            #Si no hay líneas es False, si la hay es True
            if (tasks == None):
                return False
            else:
                return True
        except:
            return False
        
        
    def confirm(self):
        """Pregunta si el usuario está seguro o no de hacer la acción

        Returns:
            boolean: True or False
        """
        confirm = input("¿Estás segur@? (s/N)")
        #cualquier valor introducido distinto de "s" o "S" es False. 
        if confirm.lower() == "s":
            return True
        else:
            return False 
            
        
    def choices(self):
        """Devuelve las opciones que presenta la app
        """
        #Te ada opciones y te pide que elijas una
        print ("Puedes: 1 - Listar de nuevo; 2 - Crear tarea; 3 - Dar tarea por terminada; 4 - Eliminar una tarea; 5 - Salir")
        print ("¿Qué quieres hacer?")
        choice = input()
        #En función d elo que elijas realizará un acción
        match choice:
            case "1": 
                #listar
                self.read()
                self.choices()
            case "2":
                #Create
                print ("¿Cuál es la nueva tarea?")
                task = input()
                self.create(task)
                self.choices()
            case "3":
                #Update
                print("¿Cuál es el número de la tarea que quieres terminar?")
                try:
                    id = int(input()) 
                    if self.confirm():
                        self.update(id)   
                except ValueError: 
                    print("Debe ser un número entero, no inventes")

                self.choices() 
            case "4":
                #Delete
                print("¿Cuál es el número de la tarea que quieres eliminar?")
                try:
                    id = int(input())
                    if self.confirm():
                        self.delete(id) 
                except ValueError: 
                    print("Debe ser un número entero, no inventes")  
                self.choices() 
            case "5":
                #Sale de la app y de python
                print (f"Hasta otra, {self.user_name}")
                exit()
            case _:
                #si ha peusto otra cosa que no sea un nçumero de 1 a 5 se lo decimos, a nosotros no nos chulea nadie. 
                print(f"Ok,{self.user_name}, no es cienca de cohetes:  {choice} no es una opción. Elige: 1,2,3,4 o 5")
                self.choices()
