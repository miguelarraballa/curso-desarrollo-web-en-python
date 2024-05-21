import database as database

class Task:
    
    def __init__(self,name):
        self.table = "tasks" 
        self.user_name = 'Anonymous'
        self.db = database.Connection(name)
    
    def create(self,task):
        if (type(task) != str and type(task) != int):
            self.db.error(f"La tarea debe ser un texto, has introducido: {type(task)}")
        query = f"INSERT INTO {self.table} (task) VALUES ('{task}')"
        self.db.query(query) 
        self.db.commit()
        print("Tarea guardada")
        
    
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
        
    
    def update(self,id):
        if (self.is_task_in_table(id)):
            query = f"UPDATE {self.table} SET finish = 1 WHERE id = {id}"
            results = self.db.query(query) 
            self.db.commit()
            print(f"Tarea {id} finalizada")
        else:
            print(f"Con {id} no me viene nada")
    
    def delete(self,id):
        if (self.is_task_in_table(id)):
            query = f"DELETE FROM {self.table} WHERE id = {id}"
            results = self.db.query(query) 
            self.db.commit()
            print(f"Tarea {id} eliminada")
        else:
            print(f"Con {id} no me viene nada")
    
    def set_name(self,name):
        if name.strip() != "":
            self.user_name = str(name)
    
    def get_name(self):
        return self.user_name
    
    def is_task_in_table(self,id):
        query = f"SELECT * FROM {self.table} WHERE id = {id}"
        results = self.db.query(query) 
        self.db.commit()
        tasks = results.fetchone()
        if (tasks == None):
            return False
        else:
            return True
        
        
    def confirm(self):
        confirm = input("¿Estás segur@? (s/N)")
        if confirm.lower() == "s":
            return True
        else:
            return False 
            
        
    def choices(self):
        print ("Puedes: 1 - Listar de nuevo; 2 - Crear tarea; 3 - Dar tarea por terminada; 4 - Eliminar una tarea; 5 - Salir")
        print ("¿Qué quieres hacer?")
        choice = input()
        match choice:
            case "1": 
                self.read()
                self.choices()
            case "2":
                print ("¿Cuál es la nueva tarea?")
                task = input()
                self.create(task)
                self.choices()
            case "3":
                print("¿Cuál es el número de la tarea que quieres terminar?")
                try:
                    id = int(input()) 
                    if self.confirm():
                        self.update(id)   
                except ValueError: 
                    print("Debe ser un número entero, no inventes")

                self.choices() 
            case "4":
                print("¿Cuál es el número de la tarea que quieres eliminar?")
                try:
                    id = int(input())
                    if self.confirm():
                        self.delete(id) 
                except ValueError: 
                    print("Debe ser un número entero, no inventes")  
                self.choices() 
            case "5":
                print (f"Hasta otra, {self.user_name}")
                
            case _:
                print(f"Ok,{self.user_name}, no es cienca de cohetes:  {choice} no es una opción. Elige: 1,2,3,4 o 5")
                self.choices()
