from tasks import Task 


def choices(i=0):

    print ("Puedes: 1 - Crear tarea; 2 - Dar tarea pro terminada: 3 - Eliminar una tarea; 4 - Salir")
    print ("¿Qué quiere hacer")
    choice = input()
    strikes = [f"No es ciencia de cohetes, {name}: 1,2,3 o 4",
            f"{choice} no es una opción {name}",
            f"Ok, como broma vale, {name}. Elije de una vez",
            f"Vale, vuelve a intentarlo cuando hayas descansado un poco, {name}"]
    match choice:
        case "1":
            print ("Crear tabla")
        case "2":
            print ("Terminar tarea")
        case "3":
            print ("Elininar tarea")
        case "4":
            print (f"Hasta otra, {name}")
            
        case _:
            print(strikes[i])
            ++i
            choices(i)
i = 0
tasks = Task("database.db")
print ("*********************")
print ("** LISTA DE TAREAS **")
print ("*********************")
print ("¿Como me dirijo a ti?")
name = input()
print (f"Hola {name} esta es tu lista de tareas: ")
tasks.read()
print ("")
choices()


