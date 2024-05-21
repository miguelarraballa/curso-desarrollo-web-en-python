from tasks import Task 


tasks = Task("database.db")
print ("*********************")
print ("** LISTA DE TAREAS **")
print ("*********************")
print ("¿Como me dirijo a ti?")
name = input()
tasks.set_name(name)
print (f"Hola {tasks.user_name} esta es tu lista de tareas: ")
tasks.read()
print ("")
tasks.choices()