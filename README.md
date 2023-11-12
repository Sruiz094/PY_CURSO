Generador de Contraseñas
Este script en Python genera contraseñas seguras y aleatorias utilizando caracteres numéricos, mayúsculas y minúsculas. 

Requerimientos
Asegúrate de tener instalado Python en tu sistema. La version de python utilizada en el script es la 3.10.12

Instalación
No es necesario instalar ninguna biblioteca externa para ejecutar este script.

Uso
Abre una terminal o línea de comandos en tu sistema.
Navega al directorio que contiene el script.
Ejecuta el script usando el comando python nombre_del_script.py.

Explicación del Script
El script sigue los siguientes pasos para generar una contraseña:

Definición de Caracteres:

Se definen tres listas de caracteres: números, minúsculas y mayúsculas.
Generación de Contraseña:

Se inicializa una lista vacía llamada contraseña.
Se utiliza un bucle para agregar un número, una mayúscula y una minúscula a la lista, repitiendo este proceso 9 veces.
Mezcla de Contraseña:

Se utiliza la función random.sample para mezclar aleatoriamente los elementos de la lista de contraseñas.
Creación de la Contraseña Final:

Se convierte la lista de contraseñas en una cadena utilizando el método "".join().
Impresión de la Contraseña:

La contraseña final se imprime en la consola.
