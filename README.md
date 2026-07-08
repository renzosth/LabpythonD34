# LabpythonD34 — Sistema de Gestión de Biblioteca

Link video demo: https://drive.google.com/file/d/10ONRsJrT3neg3S8WYBRX8P_jlTX7CF69/view?usp=drive_link
Link Repositorio: https://github.com/renzosth/LabpythonD34

**Escenario 7 | Comisión isiD 1.4k**

Integrantes:
- Alejandro Sebastian Barboza
- Lisandro Samuel Iturri
- Rolon Dilan Cesar Alfredo
- Baez Jorge Matias
- Renzo Nicolas Benitez

---

## Descripcion

Sistema de biblioteca que gestiona prestamos y devoluciones de libros, registro de usuarios, control de disponibilidad y calculo de multas por demora. Incluye modulo de estadisticas sobre los libros mas solicitados y cantidad de prestamos realizados.

---

## Requisitos

- Python 3.x
- Sin dependencias externas ni conexion a internet

---

## Instalacion

El programa es portable. No requiere instalacion. Solo necesitas tener Python instalado.

---

## Uso

1. Ejecuta `main.py` con Python.
2. Desde el menu **Solicitudes**, agrega usuarios o editá directamente `data/usuarios.txt`.
3. Ve al apartado de **Reservas** para registrar prestamos (podés hacer mas de uno).
   - Al confirmar, se actualiza `data/prestamos.txt` y el libro queda registrado como prestado.
4. Para devolver un libro, usá la opcion **Ingresar Libros**.
   - Podés devolver de a uno o todos juntos. El sistema calculara la multa si corresponde.

---

## Estructura del proyecto

```
LabpythonD34/
├── main.py               # Punto de entrada del programa
├── complement/
│   ├── usuarios.py       # Gestion de usuarios (alta/baja)
│   ├── libros.py         # Gestion del catalogo de libros
│   ├── prestamos.py      # Prestamos y devoluciones
│   ├── estadisticas.py   # Estadisticas de uso
│   └── menu.py           # Interfaz de menus
└── data/
    ├── usuarios.txt      # Registro de usuarios
    ├── libros.txt        # Catalogo de libros
    └── prestamos.txt     # Registro de prestamos activos
```

---

## Solucion de problemas

**"No puedo abrir el programa"**
Asegurate de tener Python instalado y ejecutar el archivo `main.py` directamente desde la terminal o un IDE.

**"No me figura ninguna cuenta"**
Podés agregar usuarios desde el menu **Solicitudes > Agregar Usuario**, o editando manualmente `data/usuarios.txt`.

---

## Historia del proyecto

El proyecto surgio como ejercicio de gestion de datos para un sistema bibliotecario, con foco en el control de entregas, devoluciones y morosidad de usuarios.

El trabajo se dividio por modulos: cada integrante fue responsable de un modulo individual, con revision cruzada entre el equipo para mantener coherencia en el conjunto.

**Posibles mejoras futuras:**
- Soporte para input de mouse
- Estadisticas avanzadas
- Calendario de vencimientos

---

## Creditos

Desarrollado en Python — 2026

---

## Uso de IA

Se utilizo Claude (Anthropic) como herramienta de apoyo durante el desarrollo, especificamente para:

1. Revisar el codigo escrito por el grupo y detectar errores puntuales.
2. Recibir sugerencias de correccion, que el equipo analizo y aplico de forma consciente.
3. Organizar los commits de GitHub de manera progresiva, agrupando el trabajo por modulo.

Todas las decisiones de diseno (estructura de modulos, validaciones, calculo de multas, manejo de errores) fueron discutidas y comprendidas por el equipo.
