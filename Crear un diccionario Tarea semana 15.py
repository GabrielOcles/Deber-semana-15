informacion_personal = {
    "nombre": "gabriel ocles",
    "edad": 32,
    "ciudad": "quito",
    "profesion": "estudiante"
}

# Realizar todas las modificaciones en un solo bloque de código
informacion_personal["ciudad"] = "quito"  # Modificar valor de "ciudad"
informacion_personal["profesion"] = "estudiante"  # Modificar valor de "profesion"

if "telefono" not in informacion_personal:  # Verificar y agregar "telefono"
    informacion_personal["telefono"] = "0990553711"

del informacion_personal["edad"]  # Eliminar clave "edad"

# Imprimir el diccionario final
print(informacion_personal)