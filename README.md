# simulacro_gestion_estudiantes

Sistema que me permite gestionar a estudiantes registrando, actualizando y eliminando su información académica y calculando su rendimiento a través de sus notas.

Desarrollo: El programa interactúa con el usuario a través de la consola, solicitando datos como:
- id del estudiante
- nombre del estudiante
- edad del estudiante
- calificación del estudiante
Este, a su vez tiene un menú intuitivo el cual permite que el usuario decida la opción que más se acomode a su necesidad.

Requerimientos: 
- El sistema debe comenzar con al menos 5 estudiantes iniciales en su base de datos.
- Deben realizarse validaciones de entradas para asegurar que el ID sea único, la nota esté dentro del rango permitido (0.0 - 5.0) y la edad sea positiva.
- En caso de que un estudiante no exista durante la búsqueda o actualización, el sistema debe mostrar mensajes claros que expliquen el error.
- Las notas deben estar en un rango entre 0.0 y 5.0, y se debe validar que la edad sea un número entero positivo.
- El sistema debe estar implementado utilizando funciones para realizar cada una de las operaciones solicitadas.
- Todo el código debe estar comentado y explicado en inglés.

Ejemplos de entrada y salida del sistema:
Bienvenido al sistema de notas. Ingresa la opción que deseas realizar
[1] Agregar estudiante
[2] Consultar estudiante
[3] Actualizar estudiante
[4] Eliminar estudiante
[5] Consultar promedio de calificaciones
[5] Consultar notas menores a 3.0
[6] Salir del sistema

Opción:  3

Ingrese el id del estudiante: 3
Advertencia: El estudiante no existe en la base de datos.

Explicación del código:
El código está dividido modularmente por funciones tanto como para agregar, eliminar, actualizar, entre otras, como para calcular el rendimiento de los estudiantes según las notas ingresadas en el sistema.
Funciones:
- add_students(): Busca en el sistema al estudiante, si existe manda un mensaje que el estudiante ya existe en la base de datos; si no existe lo agrega al diccionario students con su id, nombre, edad y nota respectivos. Valida que los datos ingresados sean válidos.
- search_student():  Busca en el sistema al estudiante, si no existe manda un mensaje que el estudiante no existe en la base de datos; si existe envía los datos pertenecientes al estudiante buscado.
- update_student(): Busca en el sistema al estudiante, si no existe manda un mensaje que el estudiante no existe en la base de datos; si existe entonces le pregunta cual dato desea cambiar (notas o edad del estudiante). Valida que los datos ingresados sean válidos y manda un mensaje si la operación es exitosa.
- def delete_students(): Busca en el sistema al estudiante, si no existe manda un mensaje que el estudiante no existe en la base de datos; si existe elimina el id del estudiante respectivo y envía un mensaje de operación exitosa.
- students_average(): calcula el promedio de todos los estudiantes iterando sobre students.items(), sumando las notas y después dividiendolas.
- lower_grades(): verifica en students.items cuales son las notas menores a 3.0 y devuelve una tupla de los estudiantes que cumplen con esta condición
- menu(): contiene las opciones del menú con el cual va a interactuar el usuario
- Por medio de un match, case, se asigna a cada opción una función para que sea funcional, si el usuario ingresa una opción no válida se enviará un mensaje de: Opción no válida

Link repositorio: https://github.com/angelicacvo/simulacro_gestion_estudiantes
