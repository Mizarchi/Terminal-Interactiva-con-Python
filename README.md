Opción 1: Sistema de Gestión de Biblioteca
Contexto: Desarrolla una aplicación de terminal para gestionar una biblioteca, que permita a los usuarios buscar, reservar y prestar libros. El sistema debe manejar información de libros, usuarios y préstamos.

Las funciones a implementar son:

Agregar Libro: Esta función recibe los datos del libro (título, autor). Si el libro ya existe en la biblioteca, aumenta su cantidad en uno. Si el libro no existe, lo agrega con una cantidad inicial de 1.

Mostrar Libros: Esta función muestra la lista de libros en la biblioteca junto con su autor, cantidad y disponibilidad (disponible o no disponible) en la consola.

Prestar Libro: Esta función permite prestar un libro a un usuario dado su título y nombre de usuario. Verifica si el libro está disponible y si el usuario está registrado. Si ambos criterios se cumplen, presta el libro al usuario y actualiza la disponibilidad del libro y la cantidad en la biblioteca.

Registrar Usuario: Agrega un usuario a la biblioteca.

Guardar Datos: Guarda los datos actuales de la biblioteca (libros y usuarios) en un archivo llamado datos_biblioteca.pkl utilizando el módulo pickle.

Cargar Datos: Intenta cargar los datos previos de la biblioteca desde el archivo 'datos_biblioteca.pkl' utilizando pickle. Si el archivo no existe inicializar la biblioteca como vacía.

Listar Usuarios: Muestra una lista de los usuarios registrados en la biblioteca en la consola.

Listar Libros de Usuarios: Muestra una lista de libros prestados a un usuario específico.

Devolver Libro: Permite a un usuario devolver un libro prestado. Si el usuario tiene el libro y lo devuelve correctamente, actualiza la disponibilidad y la cantidad del libro en la biblioteca.


Como fue creado:


Clase Transaccion:

Esta clase representa una transacción financiera con los siguientes atributos:
- monto: float, el monto de la transacción.
- fecha: str, la fecha de la transacción en formato 'YYYY-MM-DD'.
- descripcion: str, una descripción de la transacción.
- tipo: str, el tipo de transacción (ingreso o gasto).

Método __str__:
- Retorna una representación en forma de string de la transacción, incluyendo la fecha, tipo, monto y descripción.

Clase RegistroFinanciero:

Esta clase gestiona las transacciones financieras con los siguientes atributos:
- archivo: str, nombre del archivo donde se guardarán los datos.
- transacciones: list, lista de transacciones financieras.

Métodos:
- __init__(archivo='datos_financieros.pkl'): Inicializa la clase, cargando las transacciones desde el archivo especificado.
- agregar_transaccion(transaccion): Agrega una nueva transacción al registro financiero.
- listar_transacciones(): Lista las transacciones ordenadas por fecha.
- balance(): Calcula el balance financiero: ingresos totales, gastos totales y capacidad de ahorro.
- guardar_datos(): Guarda los datos en el archivo especificado.
- cargar_datos(): Carga los datos desde el archivo especificado.


Funciones del programa principal:

- validar_fecha(fecha): Valida que la fecha esté en formato 'YYYY-MM-DD'.
- solicitar_monto(): Solicita al usuario un monto válido.
- solicitar_fecha(): Solicita al usuario una fecha válida.
- menu(): Función principal del programa, que corre un menú donde el usuario puede seleccionar diferentes opciones, como registrar ingresos, registrar gastos, listar transacciones, mostrar balance y salir del programa.
