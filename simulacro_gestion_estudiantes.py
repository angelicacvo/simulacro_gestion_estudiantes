DANGER = "\033[91m"
WARNING = "\033[93m"
SUCCESS = "\033[92m"
RESET = "\033[0m"
# Students dictionary which it's principal key is the id of the student
students = {
     "123" : {
        "name" : "Valeria Martinez",
        "age": "20",
        "grade": 4.0
    },
      "456" : {        
        "name" : "Sofia Lopez",
        "age": "21",
        "grade": 4.5        
    },
      "789": {
        "name" : "Gabriela Perez",
        "age": "21",
        "grade": 3.2
    },
      "135": {
        "name" : "Tatiana Higuita",
        "age": "18",
        "grade": 2.8       
    },
      "246": {
        "name" : "Juliana Alvarez",
        "age": "19",
        "grade": 2.9
    }
}

# Functions:
# function add student: to the dictionary if the student doesn't exist
def add_students():
  new_student = input("Ingrese id del nuevo estudiante ")
  # validation if the student exists in the dict
  if new_student in students:
    print(WARNING + "Advertencia: Estudiante ya se encuentra registrado." + RESET)
  else:
    student = input("Ingrese el nombre del estudiante ")
    age = input("Ingrese la edad del nuevo estudiante ")
    # validation if the age is not a number and is greater than 0
    if age.isdigit() and int(age) > 0:
      grade = input("Ingrese la nota del nuevo estudiante")
      if grade.isdigit() and float(grade) > 0 and float(grade) < 5 :
        students[new_student] = {"name" : student, "age": age, "grade" : grade}
        print(students)
        print(SUCCESS + "Operación exitosa." + RESET)
      else:
        print(WARNING + "Advertencia: Debes ingresar un valor entre 0 y 5.0." + RESET)
    else:
      print(WARNING + "Advertencia: Ingresa una edad válida." + RESET)

# function search student: searchs if the student exists in the dictionary and prints the student's data
def search_student():
  choice = input("Ingrese el id del estudiante ")
  if not choice in students:
    print(WARNING + "Advertencia: El estudiante no existe en la base de datos." + RESET)
  else:
    print(SUCCESS + "Operación exitosa." + RESET)
    print(f"El estudiante con identificación {choice}")
    print("Nombre: ", students[choice]["name"])
    print("Edad: ", students[choice]["age"])
    print("Calificación: ", students[choice]["grade"])


# function update student: search the student in the dictionary and asks the user which option they want to change (n = grade, e = age)
def update_student():
  choice = input("Ingrese el id del estudiante ")
  if not choice in students:
    print(WARNING + "Advertencia: El estudiante no existe en la base de datos." + RESET)
  else:
    change = input("¿Qué desea cambiar? [n] nota, [e] edad")
    match change:
      case "n" | "nota":
        change_grade = input("¿Cual es la nota? ")
        if change_grade.isdigit() and int(change_grade) > 0:
          students[choice]["grade"] = change_grade
          print(students)
          print(SUCCESS + "Operación exitosa." + RESET)
        else:
          print(WARNING + "Advertencia: Debes ingresar un valor entre 0 y 5.0." + RESET)
      case "e" | "edad":
        change_age = input("¿Cuál es la edad? ")
        if change_age.isdigit() and int(change_age) > 0:
          students[choice]["age"] = change_age
          print(students)
          print(SUCCESS + "Operación exitosa." + RESET)
        else:
          print(WARNING + "Advertencia: Debes ingresar un valor entre 0 y 5.0." + RESET)
    
# function delete students: searchs for the student in the dictionary and with the method .pop deletes the student searched
def delete_students():
  choice = input("Ingrese el id del estudiante ")
  if not choice in students:
    print(WARNING + "Advertencia: El estudiante no existe en la base de datos." + RESET)
  else:
    students.pop(choice)
    print(SUCCESS + "Operación exitosa." + RESET)
    print(students)

# function students average: searchs for every grade, sums and divides the result
def students_average():
  students_grades = 0
  for i, grade in students.items():
    students_grades += float(grade["grade"])
  mult_grades = students_grades/len(students)
  print(SUCCESS + "Operación exitosa." + RESET)
  print(mult_grades)

# function lower grades: searchs for the lowest grades in the dictionary and prints the results
def lower_grades():
  for i, grade in students.items():
    if grade["grade"] < 3.0:
      student = grade["name"], grade["grade"]
      print(SUCCESS + "Operación exitosa." + RESET)
      print(student)

# function menu: contains the options which the user will interact
def menu():
  option = input("""
  Bienvenido al sistema de notas. Ingresa la opción que deseas realizar
  \n[1] Agregar estudiante
  \n[2] Consultar estudiante
  \n[3] Actualizar estudiante
  \n[4] Eliminar estudiante
  \n[5] Consultar promedio de calificaciones
  \n[5] Consultar notas menores a 3.0
  \n[6] Salir del sistema

  """)
  return option

# functions settlement for each option
flag = True
while flag != 6:
  match menu():
    case "1": add_students()
    case "2": search_student()
    case "3": update_student()
    case "4": delete_students()
    case "5": students_average()
    case "6": students_average()
    case "7":
      break
    case _:
      print("Opción no válida")