import models.database as database

class TaskModel:
    
    def __init__(self,name):
        self.table = "tasks" 
        self.db = database.Connection(name)
    
    def create(self,task):
        if (type(task) != str and type(task) != int):
            self.db.error(f"La tarea debe ser un texto, has introducido: {type(task)}")
        query = f"INSERT INTO {self.table} (task) VALUES ('{task}')"
        self.db.query(query) 
        self.db.commit()
    
    def read(self):
        query = f"SELECT * FROM  {self.table} ORDER BY ID ASC"
        results = self.db.query(query) 
        self.db.commit()
        tasks = results.fetchall()
        for task in tasks:
            if task[2] == 0: 
                state = "PENDIENTE"
            else:
                state = "TERMINADO"
                 
            print(f"{state} -> {task[0]: 2} - {task[1]}")
        
    
    def update(self,id,data):
        pass
    
    def delete(self,id):
        pass

