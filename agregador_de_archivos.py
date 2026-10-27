ids = []
nombres = []
tipos = []
extensiones = []
tamanos = []
ubicaciones = []
descripciones = []
#------------------------------------------#
#--|menu_principal_agregador_de_archivos|--#
#------------------------------------------#
while True:
    print("menu principal agregador de archivos")
    print("1) crear archivo")
    print("2) editar archivo")
    print("3) eliminar archivo")
    print("4) buscar archivo")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-------------------#
    #--|crear_archivo|--#
    #-------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_archivo = 1
        else:
            id_archivo = ids[-1] + 1
        nombre = input("nombre del archivo: ")
        tipo = input("tipo de archivo: ")
        extension = input("extensión: ")
        tamano = float(input("tamaño (MB): "))
        ubicacion = input("ubicación: ")
        descripcion = input("descripción: ")
        ids.append(id_archivo)
        nombres.append(nombre)
        tipos.append(tipo)
        extensiones.append(extension)
        tamanos.append(tamano)
        ubicaciones.append(ubicacion)
        descripciones.append(descripcion)
        print("archivo registrado correctamente.")
        print("id:", id_archivo)
    #--------------------#
    #--|editar_archivo|--#
    #--------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar archivo")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {tipos[i]} | {extensiones[i]} | {tamanos[i]} MB | {ubicaciones[i]} | {descripciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | {tipos[posicion]} | {extensiones[posicion]} | {tamanos[posicion]} MB | {ubicaciones[posicion]} | {descripciones[posicion]}")
                nombres[posicion] = input("nuevo nombre del archivo: ")
                tipos[posicion] = input("nuevo tipo de archivo: ")
                extensiones[posicion] = input("nueva extensión: ")
                tamanos[posicion] = float(input("nuevo tamaño (MB): "))
                ubicaciones[posicion] = input("nueva ubicación: ")
                descripciones[posicion] = input("nueva descripción: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #----------------------#
    #--|eliminar_archivo|--#
    #----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar archivo")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {tipos[i]} | {extensiones[i]} | {tamanos[i]} MB | {ubicaciones[i]} | {descripciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {tipos[posicion]} | {extensiones[posicion]} | {tamanos[posicion]} MB | {ubicaciones[posicion]} | {descripciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    tipos.pop(posicion)
                    extensiones.pop(posicion)
                    tamanos.pop(posicion)
                    ubicaciones.pop(posicion)
                    descripciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #--------------------#
    #--|buscar_archivo|--#
    #--------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar archivo")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {tipos[posicion]} | {extensiones[posicion]} | {tamanos[posicion]} MB | {ubicaciones[posicion]} | {descripciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            suma = 0
            mayor = tamanos[0]
            menor = tamanos[0]
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {tipos[i]} | {extensiones[i]} | {tamanos[i]} MB | {ubicaciones[i]} | {descripciones[i]}")
                suma += tamanos[i]
                if tamanos[i] > mayor:
                    mayor = tamanos[i]
                if tamanos[i] < menor:
                    menor = tamanos[i]
            promedio = suma / len(ids)
            print("estadísticas agregador de archivos")
            print("cantidad de archivos:", len(ids))
            print("espacio total utilizado:", round(suma, 2), "MB")
            print("tamaño promedio:", round(promedio, 2), "MB")
            print("archivo más grande:", round(mayor, 2), "MB")
            print("archivo más pequeño:", round(menor, 2), "MB")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el agregador de archivos.")
        break
    else:
        print("opción no válida.")