from tasks import Task 

#Instancia la clase task
tasks = Task("database.db")
#título
print ("*********************")
print ("** LISTA DE TAREAS **")
print ("*********************")
#Pide al usuario introducir un nombre o alias o algo, sino escribe nada sera "Anonymous"
print ("¿Como me dirijo a ti?")
name = input()
#Guarda el nombre introducido como parámetro
tasks.set_name(name)
#saludo
print (f"Hola {tasks.user_name} esta es tu lista de tareas: ")
#Imprime la lista de tareas
tasks.read()
print ("")
#Imprime las opciones (menu)
tasks.choices()

