# LabpythonD34
INTEGRANTES (Com isiD 1.4k)

  Alejandro Sebastian Barboza,
  Lisandro Samuel Iturri,
  Rolon Dilan Cesar Alfredo,
  Baez Jorge Matias,
  Renzo Nicolas Benitez,
  
******************************************************************

Escenario 7. Sistema de biblioteca

"El sistema deberá gestionar préstamos y devoluciones dentro de una biblioteca. La solución podrá incluir registro de usuarios, préstamos de libros, devoluciones, control de disponibilidad y cálculo de multas simples por demora.
Asimismo, podrá incorporar estadísticas relacionadas con libros más solicitados o cantidad de préstamos realizados."

******************************************************************
Todo sobre la creación y evolución de este proyecto.
Contiene:
	>>DOCUMENTACIÓN
	>>HISTORIA
	>>SOLUCIÓN DE PROBLEMAS
******************************************************************
>>DOCUMENTACIÓN
I. RESUMEN
II. REQUISITOS
III. INSTALACIÓN
IV. USO
V. ESTRUCTURA
VI. CREDITOS
******************************************************************
I. RESUMEN
	Programa que permite realizar un seguimiento del estado de un producto:(libros),y estado de Cuenta de clientes:(usuarios)
  ,permitiendo la obtencion de un prestamo (el cual consta de una multa por morosidad por atrazo de devolucion), permite ver:
  1.datos de clientes (ACTIVOS/BAJA)
  2.Libros disponibles/reservado/reintegrado(devuelto), con sus respectivos motos
II. REQUISITOS
	Requiere:
		Python 3.14.6
  /no requiere de uso de internet, no requiere de dependencias ni programas externos.
III.  INSTALACIÓN
	Este programa es portable, no requiere de alguna instalación en particular, para sus librerías:
	consulta REQUISITOS (.II)
IV. USO
	Abre el programa desde su ejecutable, agrega los usuarios a gestionar
	desde el menú de Solicitudes o editando usuarios.txt, luego para agregar pedidos
  dirigete al apartado de reservas(puedes reservar mas de uno), al momento de realizar dicha reserva se actualizara
  prestamos.txt y veras los libros en obtencion.
  Para devolver un libro dirigete a Ingresar Libros y cargalos manualmente o todos de una vez, cobrandote o no morosidad.
  Y listo esto es todo el progama de Gestion de Biblioteca.
VI. CREDITOS
	Programa hecho en Python 3.14.6
	Integrantes :
		Alejandro Sebastian Barboza
    Lisandro Samuel Iturri
    Rolon Dilan Cesar Alfredo
    Baez Jorge Matias
    Renzo Nicolas Benitez
	2026
  ******************************************************************
>>HISTORIA
I. INICIOS
II. ESTRUCTURA Y FUNDAMENTOS
III. TRABAJO
IV. FUTURO
******************************************************************
I. INICIOS
  El programa surgio como modelo de gestion de datos para usuarios bibliotecarios
  pudiendo controlar datos entrega y devolucion de libros, manejo de interes por morosidad
  creacion y baja de usuarios.

II. ESTRUCTURA Y FUNDAMENTOS
	La estructura: optamos por un 1 carpeta con todas las funciones necesarios, 1 carpeta con todos los registros.txt necesarios, y un main.py
  que dirige todo el programa.
III. TRABAJO
	El trabajo se dividio por modulos, cada integrante trabajo en modulos individuales, teniendo asi
  una fluctuacion de feedback por ambas partes iguales, mejorando asi el programa
IV. FUTURO
	Las próximas actualizaciones incluirá:
		soporte para input de mouse.
		estadísticas avanzadas.
		calendario
		,etc.

******************************************************************
>>SOLUCIÓN DE PROBLEMAS:
q. preguntas frecuentes
a. respuestas
	q. "no puedo abrir el programa"
    asegurate de que ninguna aplicacion intervenga con la descarga , para que asi puedan descargarse los archivos necesarios
	q. "no me figura ninguna cuenta"
	  puedes agregarla manualmente desde el bloc de notas usuarios.txt o desde la opcion SOLICITUDES/AGREGAR USUARIO.
		1. Incluye el programa por medio de configuración o por el usuario.txt

******************************************************************
>>USO DE LA IA.

Se utilizó Claude (Anthropic) como herramienta de apoyo durante el desarrollo, específicamente para:

1	Revisar el código ya escrito por el grupo y detectar errores puntuales (por ejemplo, una inconsistencia entre el texto de una opción de menú y la función que realmente ejecutaba).
2	Recibir sugerencias de corrección, que el equipo analizó y aplicó de forma consciente antes de incorporarlas.
3	Ordenar el proceso de subida del proyecto a GitHub en commits progresivos, agrupando el trabajo por módulo/funcionalidad en lugar de subir todo el código de una sola vez.

Todas las decisiones de diseño (estructura de módulos, validaciones, cálculo de multas, manejo de errores) fueron discutidas y comprendidas por el equipo, que puede justificar cada una de ellas.
