import streamlit as st #as es una alias

menu_opciones=["Inicio","Saludo","Suma de dos números","Área de un triangulo","Calculadora de descuento","Suma de una lista de numeros","Funciones con valores predeterminados","Numeros pares e impares","Mutiplicación con *args","Información de una persona con **kwargs","Calculadora flexible"]
st.subheader("Tarea funciones")

seleccionar=st.sidebar.selectbox("Opciones",menu_opciones)

match seleccionar:
    case "Inicio":
        st.markdown("### ¿Qué es esta pagina?")
        st.markdown("Esta es una pagina la cual puede realizar distintas funciones, checa la barra de seleccion a la izquierda para verlas\n")

    case "Saludo":
        def saludar(lol):
            if st.button("Mostrar saludos"):
                st.text(f"Hola {lol}, buen día")
        st.markdown("### ¿Qué realiza esta función?")
        st.markdown("Da saludos personalisados a tu nombre")
        saludar(st.text_input("Ingresa tu nombre"))

    case "Suma de dos números":
        def sumar(a:int,b:int):
            if st.button("Mostrar suma"):
                st.text(f"La suma de los dos numeros es {a+b}")
        st.markdown("### ¿Qué realiza esta función?")
        st.markdown("Da la suma de dos numeros ingresados por ti")
        sumar(st.number_input("Ingresa un número"),st.number_input("Ingresa otro número"))

    case "Área de un triangulo":
        def calcular_area_triangulo(base,altura):
            if st.button("Mostrar area del triengulo"):
                st.text(f"El área del triángulo es {(base*altura)*0.5}")
        st.markdown("### ¿Qué realiza esta función?")
        st.markdown("Calcula el área de un triángulo, debes darle la medicion de la base y altura del triángulo")
        calcular_area_triangulo(st.number_input("Ingresa la base"),st.number_input("Ingresa la altura"))

    case "Calculadora de descuento":
        def calcular_precio_final(precio,descuento,impuesto):
            imp=st.checkbox("No incluir descuento")
            if imp==True:
                descuento=0
            des=st.checkbox("No incluir impuestos")
            if des==True:
                impuesto=0
            if st.button("Mostrar precio final"):
                st.text(f"El precio final el {precio-(precio*(descuento/100))+(precio*(impuesto/100))}")
        st.markdown("### ¿Qué realiza esta función?")
        st.markdown("Checa el precio final añadiendo descuento e impuestos, puedes elegir si incluir o no el descuento y los impuestos")
        calcular_precio_final(st.number_input("Ingresa el precio"),st.number_input("Ingresa descuento en procentaje",min_value=10),st.number_input("Ingresa impuesto en porcentaje",min_value=16))

    case "Suma de una lista de numeros":
        def sumar_lista(elementos):
            milista=[]
            suma=0
            for i in range(elementos):
                elemento=st.number_input(f"Ingresa el número {i+1}")
                milista.append(elemento)
            for i in range(elementos):
                suma+=milista[i]
            if st.button("Mostrar suma de numeros de la lista"):
                st.text(f"{suma}")
        st.markdown("### ¿Qué realiza esta función?")
        st.markdown("Esta funcion suma los números de una lista ingresada")
        sumar_lista(int(st.number_input("¿Cuantos numeros quieres ingresar en la lista?",step=1)))

    case "Funciones con valores predeterminados":
        def producto(nombre,cantidad=1,precio=10):
            st.markdown("Valores predeterminados: cantidad=1, precio=10")
            lol=st.checkbox("Cambiar valores predeterminados")
            if lol==True:
                cantidad=int(st.number_input("Ingresa cantidad"))
                precio=st.number_input("Ingresa precio")
            if st.button("Mostrar precio total"):
                st.text(f"{int(cantidad)} de {nombre} vale {precio*cantidad}")
        st.markdown("### ¿Qué realiza esta función?")
        st.markdown("Calcula cuanto cuesta una cantidad de un producto, puedes cambiar los valores predeterminados de la cantidad de producto y el precio")
        producto(st.text_input("Ingresa el nombre"))

    case "Numeros pares e impares":
        def numeros_pares_impares(lista):
            lista_pares=[]
            lista_impares=[]
            for i in range(len(lista)):
                if lista[i]%2==0:
                    lista_pares.append(lista[i])
                else:
                    lista_impares.append(lista[i])
            if st.button("Mostrar numeros pares e impares"):
                st.text(f"Numeros pares {lista_pares}, numeros impares {lista_impares}")
        st.markdown("### ¿Qué realiza esta función?")
        st.markdown("Esta función muestra cuales numeros son pares e impares de una lista ingresada")
        listaNumeros=[]
        numeros=int(st.number_input("¿Cuantos numeros para la lista?",step=1))
        for i in range(numeros):
            numero=int(st.number_input(f"Ingresa el numero {i+1}"))
            listaNumeros.append(numero)
        numeros_pares_impares(listaNumeros)

    case "Mutiplicación con *args":
        def multiplicar_todos(*args):
            mul=1
            for i in range(len (args)):
                mul=mul*args[i]
            if st.button("Mostrar multiplicacón"):
                st.text(f"La multiplicacion de los numeros ingresados es {mul}")
        st.markdown("### ¿Qué realiza esta función?")
        st.markdown("Realiza la multilicación de los numeros ingresados")
        manolo=[]
        a=int(st.number_input("¿Cuantos numeros quieres multiplicar?",step=1))
        for i in range(a):
            e=st.number_input(f"Ingresa el numero {i+1}")
            manolo.append(e)   
        multiplicar_todos(*manolo)

    case "Información de una persona con **kwargs":
        def informacion_personal(**datos):
            if st.button("Mostrar datos"):
                for key,value in datos.items():
                    st.text(f"{key}:{value}")
        st.markdown("### ¿Qué realiza esta función?")
        st.markdown("Muestra x cantidad de datos personales ingresados por el usuario")
        datos={}
        ejem=int(st.number_input("¿Cuantos datos personales?",step=1))
        for i in range(ejem):
            st.markdown(f"Dato numero {i+1}")
            nombre=st.text_input(f"Ingrese nombre del dato {i+1}")
            valor=st.text_input(f"Ingrese valor del dato {i+1}")
            datos[nombre]=valor
        informacion_personal(**datos)
    
    case "Calculadora flexible":
        def calculadora_flexible(num1,num2,operacion):
            if st.button("Mostrar resultado de la operación"):
                match operacion:
                    case "Suma":
                        st.text(f"La suma de los numeros es {num1+num2}")
                    case "Resta":
                        st.text(f"La resta de los numeros es {num1-num2}")
                    case "Multiplicación":
                        st.text(f"La multiplicación de los numeros es {num1*num2}")
                    case "División":
                        st.text(f"La división de los numeros es {num1/num2}")
        st.markdown("### ¿Qué realiza esta función?")
        st.markdown("Esta es una calculadora la cual acepta dos numeros y eliges el tipo de operación (mira a la izquierda para selecionar el tipo de operación)")
        tipo_de_operacion=["Suma","Resta","Multiplicación","División"]
        calculadora_flexible(st.number_input("Ingresa el primer numero"),st.number_input("Ingresa el segundo numero"),st.sidebar.selectbox("Opciones de operecion",tipo_de_operacion))
