def abrirCrearArchivo():
  """Intenta abrir un archivo inexistente y si no existe crearlo, manejando FileNotFoundError."""
  nombreArchivo = input("\n Ingrese el nombre del archivo ")
  try:
    with open(nombreArchivo, "r") as archivo: #Apertura de archivo solo lectura
      contenido = archivo.read()
      print(f" Contenido del archivo: {contenido}")
  except FileNotFoundError:
    print(f"\n Error: El archivo '{nombreArchivo}' no se encontró. Intentando crearlo.\n") 
    try:
      with open(nombreArchivo, "w") as archivoCreado: #Apertura de archivo para escritura
        archivoCreado.write(" Este es un nuevo archivo creado.") #Escritura en el archivo
      print(f" El archivo '{nombreArchivo}' ha sido creado.\n")
    except Exception as e:
      print(f" Error al crear el archivo \n'{nombreArchivo}': {e}") #error de creacion de archivo
    finally nombreArchivo.close() 
      
abrirCrearArchivo()
