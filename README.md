*LEER ANTES DE UTILIZAR*

El siguiente archivo fue pensado para ser corrido desde la consola del VS Code, lo cual se recomienda.
El código se encuentra compuesto por un módulo 'main.py', el cual es el principal, y desde donde DEBE correrse el script.
A su vez posee la carpeta 'packages' que contiene los módulos:
  - interface.py: Contiene la lógica de la interfaz grafica que se ve por consola y en el cual convergen el resto de los módulos de packages para su funcionamiento.
  
  - menu.py: Contiene la lógica para el display del menu.
  
  - project_paths.py: Contiene los paths para el guardado y carga del registro de usuarios (hay 3 opciones: TXT, JSON o CSV. Para elegir una, simplemente reemplazar
  en la constante "FILE_PATH" por la ruta deseada. SOLAMENTE ALLí SE PUEDE ESTABLECER.
  
  - users.py: Contiene las funciones relativas a los usuarios (tendrá mayor utilidad y será más claro cuando se pase a trabajar con POO)
  
  - utils.py: Contiene un conjunto de funciones 'herramientas' para evitar recargar el código innecesariamente y facilitar su lectura.
