import random
from tkinter import *
from tkinter import messagebox
from winsound import *
import os #Se usa solo para el botón Ayuda del menu para abrir el manual de usuario

posc=() #Ayuda a seleccionar un label
creado="No" #Se usa para saber si existe un juego creado
juego={} #Contiene al juego actual
listo="No" #Se usa para saber si el usuario escribio un nombre
repetidos=[] #Acumula los juegos que van saliendo para que no salgan repetidos
count=0 #Se usa para el cronometro y timer
pausado="No" #Para saber si el juego esta pausado o no (cronometro y timer)
tipo="Timer" #Ayuda cuando el timer tiene que pasar a cronometro
dific='' #Contiene el nivel de dificultad
jugadas = []
btn = 0
def cargarArchivo(archivo):
    strResultado = leer(archivo)
    if strResultado != "":
        return eval(strResultado)
    else:
        return []

def leer(archivo):
    fo = open(archivo, "r")
    resultado = fo.read()
    fo.close()
    return resultado

def guardar(archivo, strLista):
    fo = open(archivo, "w")
    fo.write(strLista)
    fo.close()

plantilla_top10 = ['','',0,0,0]

def obtenerPlantillaTop10 ():
    global plantilla_top10
    return plantilla_top10[:]

def jugarKenken(ventana): #Recibe la ventana del menu y la destruye
    ventana.destroy()
    ventana= Tk()
    ventana.title("Jugar Kenken")
    ventana.geometry("1366x700")
    ventana.config(bg= '#4682b4')

    global posc,juego,listo,creado,repetidos,count,pausado,jugadas,btn
    #Siempre se inicializan de esta forma
    posc=()
    repetidos=[]
    creado="No"
    listo="No"
    juego={}
    count=0
    pausado="No"
    tipo="Timer"

    #Se usa para colocar la operacion que le corresponde a cada celda
    dic={(1,1):(350,60),(1,2):(398,60),(1,3):(446,60),(1,4):(494,60),(1,5):(542,60),(1,6):(590,60),(2,1):(350,130),(2,2):(398,130),(2,3):(446,130),\
    (2,4):(494,130),(2,5):(542,130),(2,6):(590,130),(3,1):(350,200),(3,2):(398,200),(3,3):(446,200),(3,4):(494,200),(3,5):(542,200),(3,6):(590,200),\
    (4,1):(350,270),(4,2):(398,270),(4,3):(446,270),(4,4):(494,270),(4,5):(542,270),(4,6):(590,270),(5,1):(350,340),(5,2):(398,340),(5,3):(446,340),\
    (5,4):(494,340),(5,5):(542,340),(5,6):(590,340),(6,1):(350,410),(6,2):(398,410),(6,3):(446,410),(6,4):(494,410),(6,5):(542,410),(6,6):(590,410)}

    #Contiene una lista de colores para diferenciar las celdas
    colores=["greenyellow","#83689a","yellow","orange","#0dd0e1","bisque","pink","indianred","lightgreen","slateblue1","khaki","thistle","#227ca2","#f77e78","#40e7b9",\
    "green2","#c98686",'#518251','#f6c348','#f9ccbb','#e7aebf','#b980ff','#9b775d','#c91b20','#ffb2f2','#5fcc9c','#ee6c4d','#ffe19c','#fecc0c','#5ec4ec','#dabe96','#cdffe6']

    #Se coloca una cuadricula con los tiempos, solo aparece cuando se usa timer o cronometro
    horas=Label(ventana,text=" HORAS ",bg="yellow",font=("Helvetica",12)).place(x=850,y=60)
    minutos=Label(ventana,text="  MINUTOS ",bg="yellow",font=("Helvetica",12)).place(x=921,y=60)
    segundos=Label(ventana,text="SEGUNDOS",bg="yellow",font=("Helvetica",12)).place(x=1010,y=60)

    hours=Label(ventana,text=0,width=7,bg="white",font=("Helvetica",12))
    hours.place(x=851,y=85)
    minuts=Label(ventana,text=0,width=9,bg="white",font=("Helvetica",12))
    minuts.place(x=921,y=85)
    seconds=Label(ventana,width=10,text=0,bg="white",font=("Helvetica",12))
    seconds.place(x=1010,y=85)
    
    cortina=Label(ventana,width=28,heigh=3,bg="#4682b4",font=("Helvetica",12)) #Ayuda a ocultar la cuadricula
    cortina.place(x=850,y=60)

    def guardarJugador(): #Guarda el nombre del jugador
        global listo
        if len(nombre.get())<3:
            return messagebox.showinfo("ERROR","EL NOMBRE DEBE SER DE MINIMO 3 CARACTERES")
        elif len(nombre.get())>30:
            return messagebox.showinfo("ERROR","EL NOMBRE DEBE SER DE MAXIMO 30 CARACTERES")
        else:
            listo="Si" #Ponemos que ya exxisste un nombre
            entryName.config(state = DISABLED) #Se deshablita el entry
            name.destroy() #Destruimos el boton
            

    def crearCeldas(posicion,color): #Recibe un par ordenado para saber cual label se tiene que configurar con un color
        if posicion==(1,1):
            uno.config(bg=color)
        elif posicion==(1,2):
            dos.config(bg=color)
        elif posicion==(1,3):
            tres.config(bg=color)
        elif posicion==(1,4):
            cuatro.config(bg=color)
        elif posicion==(1,5):
            cinco.config(bg=color)
        elif posicion==(1,6):
            seis.config(bg=color)
        elif posicion==(2,1):
            siete.config(bg=color)
        elif posicion==(2,2):
            ocho.config(bg=color)
        elif posicion==(2,3):
            nueve.config(bg=color)
        elif posicion==(2,4):
            diez.config(bg=color)
        elif posicion==(2,5):
            once.config(bg=color)
        elif posicion==(2,6):
            doce.config(bg=color)
        elif posicion==(3,1):
            trece.config(bg=color)
        elif posicion==(3,2):
            catorce.config(bg=color)
        elif posicion==(3,3):
            quince.config(bg=color)
        elif posicion==(3,4):
            dieciseis.config(bg=color)
        elif posicion==(3,5):
            diecisiete.config(bg=color)
        elif posicion==(3,6):
            dieciocho.config(bg=color)
        elif posicion==(4,1):
            diecinueve.config(bg=color)
        elif posicion==(4,2):
            veinte.config(bg=color)
        elif posicion==(4,3):
            veintiuno.config(bg=color)
        elif posicion==(4,4):
            veintidos.config(bg=color)
        elif posicion==(4,5):
            veintitres.config(bg=color)
        elif posicion==(4,6):
            veinticuatro.config(bg=color)
        elif posicion==(5,1):
            veinticinco.config(bg=color)
        elif posicion==(5,2):
            veintiseis.config(bg=color)
        elif posicion==(5,3):
            veintisiete.config(bg=color)
        elif posicion==(5,4):
            veintiocho.config(bg=color)
        elif posicion==(5,5):
            veintinueve.config(bg=color)
        elif posicion==(5,6):
            treinta.config(bg=color)
        elif posicion==(6,1):
            treintauno.config(bg=color)
        elif posicion==(6,2):
            treintados.config(bg=color)
        elif posicion==(6,3):
            treintatres.config(bg=color)
        elif posicion==(6,4):
            treintacuatro.config(bg=color)
        elif posicion==(6,5):
            treintacinco.config(bg=color)
        else:
            treintaseis.config(bg=color)
            
    def guardarTop10():
        global dific
        configuracion=open("kenken_configuración.dat").readlines()
        if configuracion[1]=="relojSi\n":
            try:
                archivo10 = eval(str(cargarArchivo('kenken_top10.dat')))
                plantilla = obtenerPlantillaTop10()
                plantilla[0] = dific
                plantilla[1] = nombre.get()
                plantilla[2] = hours['text']
                plantilla[3] = minuts['text']
                plantilla[4] = seconds['text']
                tempo = []
                tempo+=[plantilla]
                archivo10+= tempo
                print('tempo',tempo,'archivo',archivo10)
                guardar('kenken_top10.dat',str(archivo10))
                print(cargarArchivo('kenken_top10.dat'))
            except:
                top10 = open('kenken_top10.dat','w')
                guardar('kenken_top10.dat','[]')
                return guardarTop10()               

                
    def partidasGuardadas(): #Pone en un diccionario las partidas de acuerdo a su dificultad
        partidas=open('kenken_juegos.dat')
        dic={"F":[],"I":[],"D":[]}
        while True:
            juego=partidas.readline()
            if juego=="":
                break
            elif juego[0]=="F":
                dic["F"]+=[eval(juego[2:-1])]
            elif juego[0]=="I":
                dic["I"]+=[eval(juego[2:-1])]
            else:
                dic["D"]+=[eval(juego[2:-1])]
        return dic

    def pasarSegundos(lista): #cambia las horas, los minutos y segundos a segundos
        lista = lista[2:]
        resultado = 0
        resultado += lista[0]*3600 + lista[1]*60 + lista[2]
        return resultado

    def invertirLlaves(diccionario): #Hace un diccionario invirtiendo las llaves y valores
        inverso={}
        for llave in diccionario:
            inverso[diccionario[llave]]=llave
        return inverso
    def leerArchivo10(): #retorna los nombres de los primeros 10
        global dific
        configuracion=open("kenken_configuración.dat").readlines() #Lista con la configuracion del juego
        dific=configuracion[0][0] #Contiene el nivel de dificultad
        top10 = cargarArchivo('kenken_top10.dat') #abre el archivo
        temporal = {}
        for i in range(len(top10)):
            for j in range(len(top10)):
                if top10[i][0] == dific:
                    temporal[top10[i][1]] = pasarSegundos(top10[i]) 
        valores = list(temporal.values()) #segundos
        valores.sort() #ordena los segundos
        resultado = [] 
        dic = invertirLlaves(temporal) #segundos se vuelven las llaves y los nombres los valores
        for i in valores:
            resultado += [[dic[i],i]] #nombres,valores
        resultado = resultado[:10]
        nombres = []
        for i in range(len(resultado)):
           nombres += [resultado[i][0]]
        return nombres

    def mejoresValoresTop10(): #retorna los mejores 10 números
        lista = leerArchivo10()
        top10 = eval(str(cargarArchivo('kenken_top10.dat')))
        mejores10 = []
        for i in range(len(top10)):
            if top10[i][1] in lista:
                mejores10 += [top10[i][2:]]
        mejores10.sort()
        return mejores10

    def top10():
        root = Tk()
        root.geometry('500x300')
        root.title('TOP 10')

 #Contiene el nivel de dificultad
        def listbox(): #crea los listboxs
            col1 = leerArchivo10() #nombres
            col2 = mejoresValoresTop10() #valores
            print(col1,col2)
            lb1 = Listbox(root) #crea un listbox para los nombres
            lb1.place(x=100,y=100)
            lb2 = Listbox(root)  #crea un listbox para los valores
            lb2.place(x=250,y=100)
            contador = 0 #se necesita un contador para el listbox
            for i in col1:
                    lb1.insert(contador,i)
                    contador+=1
            contador = 0
            for j in col2:
                    lb2.insert(contador,j)
                    contador+=1

        listbox()
        jugadores = Label(root,text="JUGADORES",bd = 1, relief = 'solid', heigh = 2, width = 12,bg="yellow",font=("Helvetica",12,'bold')).place(x=100,y=50)
        tiempo = Label(root,text= 'TIEMPO', bd = 1, relief = 'solid',bg = 'yellow', heigh = 2, width = 12,font = ('Helvetica',12,'bold')).place(x=250,y=50)

        root.mainloop()
        
        
    def crear_juego_aux(juego): #Recibe un juego al azar dependiendo de la dificultad, esta funcion lee como debe verse el juego graficamente
        color=0 #Ayuda a dar color a los labels, permite usar un color de la lista de colores
        for indice in juego: #Ingresamos al diccionario del juego
            operacion=juego[indice][0] #Vemos el resultado que deben dar las celdas correspondientes
            contador=1 #Eviatamos la operacion
            while contador<len(juego[indice]):
                for posicion in dic: #Usamos el diccionario que posee las ubicaciones de cada par ordenado
                    if contador==1 and posicion==juego[indice][contador]: #El primer par ordenado es que el tendra la operacion
                        Label(ventana,text=operacion,width=3,bg=colores[color],font=("Arial",10)).place(x=dic[posicion][0]+3,y=dic[posicion][1]+3) #Colocamos la operacon
                        crearCeldas(posicion,colores[color]) #Configuramos la casilla con color
                        break
                    elif posicion==juego[indice][contador]:
                        Label(ventana,width=3,bg=colores[color],font=("Arial",10)).place(x=dic[posicion][0]+3,y=dic[posicion][1]+3)
                        crearCeldas(posicion,colores[color]) #Configuramos la casilla con color                      
                        break
                contador+=1 #Aumentamos el contador para configurar la celda
            color+=1 #Se aumenta el contador de color

    def crear_juego(created,opcion): #Recibe un parametro que le permite saber si ya hay un juego iniciado y si ya existe un cronometro (caso especial)
        global listo,juego,repetidos,dific
        if listo=="Si": #Verificamos que el usuario haya puesto el nombre
            if created=="No": #Verificamos que no exista un juego creado (caso para iniciar juego)
                global creado,count
                configuracion=open("kenken_configuración.dat").readlines() #Lista con la configuracion del juego
                dificultad=configuracion[0][0] #Contiene el nivel de dificultad
                dific = dificultad
                tiempo=configuracion[1] #Vemos si el juego es con reloj, timer o ninguno
                lista=partidasGuardadas() #Obtiene un diccionario con los niveles(llaves) y una lista con los diccionarios respectivos(valores)
                partidas=0 #Almacena las partidas de acuerdo a la dificultades
                
                for nivel in lista: #Vemos las llaves del diccionario
                    if nivel==dificultad: #Comparamos la llave del diccionario con la dificultad de la configuracion
                        partidas=lista[nivel] #Colocamos la lista de partidas del diccionario en la variable partidas
                try: #Se intenta escoger un juego al azar
                    juego=partidas[random.randint(0,len(partidas))-1]
                except: #En caso de que no hayan partidas de ese nivel
                    return  messagebox.showinfo("ERROR","NO EXISTEN PARTIDAS PARA ESTE NIVEL")
                if len(partidas)==len(repetidos): #Vemos si ya hemos seleccionado todos los juegos de la dificultad para volverlos a poner
                    repetidos=[] 
                while (juego in repetidos)==True: #Escogemos un juego que no este repetido
                    juego=partidas[random.randint(0,len(partidas))-1]
                repetidos+=[juego] #Ponemos ese juego en repetidos
                crear_juego_aux(juego)
                creado="Si" #Ponemos que ya existe un juego creado
                if tiempo=="relojSi\n": #Vemos si la configuracion posee un cronometro
                    cortina.destroy() #Se destruye el label
                    count=0 #Ponemos el contador en 0
                    if opcion=="Si": #Verificamos que no exista otro cronometro (caso que dificultaba el uso de otro juego)
                        cronometro()
                elif tiempo=="timer\n": #Vemos si la configuracion es un timer
                    cortina.destroy() #Se destruye el label
                    #Se ponen los valores adecuados a cada tiempo
                    hours['text']=int(configuracion[3][:1])
                    minuts['text']=int(configuracion[3][1:3])
                    seconds['text']=int(configuracion[3][3:5])
                    count=seconds['text']
                    if opcion=="Si":
                        timer()
            else:
                return messagebox.showinfo("ERROR","YA HAY UN JUEGO INICIADO")
        else:
            return messagebox.showinfo("ERROR","EL JUGADOR NO HA DADO SU NOMBRE")

    def otroJuego(opcion): #Crea otro juego
        global creado,listo,tipo
        if listo=="Si": #Vericamos que el usuari haya puesto su nombre
            if creado=="Si": #Vemos si ya hay un juego creado
                configuracion=open("kenken_configuración.dat").readlines()
                #Detenemos el tiempo del timer o cronometro
                if configuracion[1]=="timer\n":
                    detenerTimer()
                elif configuracion[1]=="relojSi\n":
                    detenerCronometro()

                if opcion=="No":
                    opcion=messagebox.askquestion("OTRO JUEGO", "¿ESTA SEGURO DE TERMINAR ESTE JUEGO Y EMPEZAR CON OTRO?", icon='warning')
                if opcion=="yes": #En caso de que desee otro juego, ademas se reinicia el timer o cronometro si estan configurados
                    reiniciar("yes")
                    crear_juego("No","No")
                else: #En caso de que no sea asi, continuamos con el cronometro o timer si es que hay
                    if configuracion[1]=="timer\n" and tipo=="Timer":
                        timer()
                    elif configuracion[1]=="relojSi\n" or tipo=="Cronometro":
                        cronometro()
            else:
                return messagebox.showinfo("ERROR","NO HA INICIADO NINGUN JUEGO")
        else:
            return messagebox.showinfo("ERROR","EL JUGADOR NO HA DADO SU NOMBRE")

    def terminar(): #Permite regresar al menu
        global creado,tipo
        configuracion=open("kenken_configuración.dat").readlines()
        if creado=="Si": #Vemos si ya existe un juego creado
            #En caso de que exista vemos si el juego es un timer o cronometro y lo pausamos
            if configuracion[1]=="timer\n":
                detenerTimer()
            elif configuracion[1]=="relojSi\n":
                detenerCronometro()

        salir=messagebox.askquestion("SALIR", "¿ESTA SEGURO DE TERMINAR EL JUEGO?", icon='warning') #Preguntamos si quiere salir del juego
        if salir=="yes": #Si responde si regresamos al menu
            menu("Si",ventana)
        else: #En caso de que no quiera terminar el juego vemos si existe un juego creado y reiniciamos el cronometro o timer
            if creado=="Si":
                if configuracion[1]=="timer\n" and tipo=="Timer":
                    timer()
                elif configuracion[1]=="relojSi\n" or tipo=="Cronometro":
                    cronometro()
        
        
    def validarCeldas(): #Verifica que el juego este correcto
        global listo,creado
        if listo=="Si":
            if creado=="Si":
                if verVacios()==True:
                    return messagebox.showinfo("ERROR","NO DEBEN HABER CASILLAS VACIAS")
                elif verFilas()==True:
                    return messagebox.showinfo("ERROR","NO DEBEN HABER NUMEROS REPETIDOS EN UNA MISMA FILA")
                elif verColumnas()==True:
                    return messagebox.showinfo("ERROR","NO DEBEN HABER NUMEROS REPETIDOS EN UNA MISMA COLUMNA")
                elif verOperaciones() == False:
                    return messagebox.showinfo("ERROR","EXISTEN CASILLAS QUE NO DAN LA OPERACION CORRESPONDIENTE")
                else:
                    configuracion=open("kenken_configuración.dat").readlines()
                    guardarTop10()
                    if configuracion[1]=="timer\n":
                        detenerTimer()
                    elif configuracion[1]=="relojSi\n":
                        detenerCronometro()
                    if configuracion[2]=="sonidoSi\n":
                        PlaySound('congratulations.wav', SND_FILENAME)
                    messagebox.showinfo("FELICIDADES","FELICIDADES, HAS GANADO")
                    opcion=messagebox.askquestion("CONTINUAR", "¿DESEA SEGUIR JUGANDO?", icon='warning')
                    if opcion=="yes":
                        otroJuego("yes")
                    else:
                        menu("Si",ventana)
                    
            else:
                return messagebox.showinfo("ERROR","NO HA INICIADO NINGUN JUEGO")
        else:
            return messagebox.showinfo("ERROR","EL JUGADOR NO HA DADO SU NOMBRE")

    def verOperaciones(): #Se usa para validar la respuesta del jugador
        global juego
        for indice in juego:
            if len(juego[indice][0]) > 1: #cuando tiene una operación
                resultado = int(juego[indice][0][:-1]) #el número
                operacion = juego[indice][0][-1] #la operación
            else: #cuando no
                resultado = int(juego[indice][0])
                operacion = ' '

            if operacion == "x" or operacion == "X":
                operacion ='*'
            lista = [] #donde van los números relacionados
            pares=[]
            contador = 1 #ayuda a tomar en cuenta solo los pares ordenados 
            while contador < len(juego[indice]):
                lista+=[retornarLabel(juego[indice][contador])[0]] #la lista con los valores relacionados
                pares+=[retornarLabel(juego[indice][contador])[1]]
                contador+=1
                
            lista.sort() 
            lista.reverse()
                
            temporal='' #donde se va agregando el resultado
            for numero in lista:
                temporal+= str(numero)+operacion
            try:
                result= int(eval(temporal[:-1]))
            except:
                return False
            if result!=resultado:
                for par in pares: #Se hace un ciclo para marcar la celda que no da el resultado correcto
                    par['text']=str(par['text'])+"X"
                return False
        return True

    def retornarLabel(tupla): #Ayuda a retornar el valor de cada label
        if tupla==(1,1):
            return [uno['text'],uno]
        elif tupla==(1,2):
            return [dos['text'],dos]
        elif tupla==(1,3):
            return  [tres['text'],tres]
        elif tupla==(1,4):
            return [cuatro['text'],cuatro]
        elif tupla==(1,5):
            return [cinco['text'],cinco]
        elif tupla==(1,6):
            return [seis['text'],cinco]
        elif tupla==(2,1):
            return [siete['text'],siete]
        elif tupla==(2,2):
            return [ocho['text'],ocho]
        elif tupla==(2,3):
            return [nueve['text'],nueve]
        elif tupla==(2,4):
            return [diez['text'],diez]
        elif tupla==(2,5):
            return [once['text'],once]
        elif tupla==(2,6):
            return [doce['text'],doce]
        elif tupla==(3,1):
            return [trece['text'],trece]
        elif tupla==(3,2):
            return [catorce['text'],catorce]
        elif tupla==(3,3):
            return [quince['text'],quince]
        elif tupla==(3,4):
            return [dieciseis['text'],dieciseis]
        elif tupla==(3,5):
            return [diecisiete['text'],diecisiete]
        elif tupla==(3,6):
            return [dieciocho['text'],dieciocho]
        elif tupla==(4,1):
            return [diecinueve['text'],diecinueve]
        elif tupla==(4,2):
            return [veinte['text'],veinte]
        elif tupla==(4,3):
            return [veintiuno['text'],veintiuno]
        elif tupla==(4,4):
            return [veintidos['text'],veintidos]
        elif tupla==(4,5):
            return [veintitres['text'],veintitres]
        elif tupla==(4,6):
            return [veinticuatro['text'],veinticuatro]
        elif tupla==(5,1):
            return [veinticinco['text'],veinticinco]
        elif tupla==(5,2):
            return  [veintiseis['text'],veintiseis]
        elif tupla==(5,3):
            return [veintisiete['text'],veintisiete]
        elif tupla==(5,4):
            return [veintiocho['text'],veintiocho]
        elif tupla==(5,5):
            return [veintinueve['text'],veintinueve]
        elif tupla==(5,6):
            return [treinta['text'],treinta]
        elif tupla==(6,1):
            return [treintauno['text'],treintauno]
        elif tupla==(6,2):
            return [treintados['text'],treintados]
        elif tupla==(6,3):
            return [treintatres['text'],treintatres]
        elif tupla==(6,4):
            return [treintacuatro['text'],treintacuatro]
        elif tupla==(6,5):
            return [treintacinco['text'],treintacinco]
        elif tupla==(6,6):
            return [treintaseis['text'],treintaseis]

    def verVacios(): #Veriicamos que el label no este vacio
        valores=[uno['text'],dos['text'],tres['text'],cuatro['text'],cinco['text'],seis['text'],siete['text'],ocho['text'],nueve['text'],diez['text'],once['text'],\
        doce['text'],trece['text'],catorce['text'],quince['text'],dieciseis['text'],diecisiete['text'],dieciocho['text'],diecinueve['text'],veinte['text'],\
        veintiuno['text'],veintidos['text'],veintitres['text'],veinticuatro['text'],veinticinco['text'],veintiseis['text'],veintisiete['text'],veintiocho['text'],\
        veintinueve['text'],treinta['text'],treintauno['text'],treintados['text'],treintatres['text'],treintacuatro['text'],treintacinco['text'],treintaseis['text']]
        for valor in valores:
            if valor=="":
                return True
        return False

    def verFilas(): #Verificamos que no existan los mismos numeros en una fila
        filas=[[uno['text'],dos['text'],tres['text'],cuatro['text'],cinco['text'],seis['text']],[siete['text'],ocho['text'],nueve['text'],diez['text'],once['text'],\
        doce['text']],[trece['text'],catorce['text'],quince['text'],dieciseis['text'],diecisiete['text'],dieciocho['text']],[diecinueve['text'],veinte['text'],\
        veintiuno['text'],veintidos['text'],veintitres['text'],veinticuatro['text']],[veinticinco['text'],veintiseis['text'],veintisiete['text'],veintiocho['text'],\
        veintinueve['text'],treinta['text']],[treintauno['text'],treintados['text'],treintatres['text'],treintacuatro['text'],treintacinco['text'],treintaseis['text']]]
        for fila in filas:
            for numero in fila:
                cantidad=0
                for copia in fila:
                    if numero==copia:
                        cantidad+=1
                if cantidad>1:
                    return True
        return False

    def verColumnas(): #Verificamos que no existan los mismos numeros en una columna
        columnas=[[uno['text'],siete['text'],trece['text'],diecinueve['text'],veinticinco['text'],treintauno['text']],[dos['text'],ocho['text'],catorce['text'],\
        veinte['text'],veintiseis['text'],treintados['text']],[tres['text'],nueve['text'],quince['text'],veintiuno['text'],veintisiete['text'],treintatres['text']],\
        [cuatro['text'],diez['text'],dieciseis['text'],veintidos['text'],veintiocho['text'],treintacuatro['text']],[cinco['text'],once['text'],diecisiete['text'],\
        veintitres['text'],veintinueve['text'],treintacinco['text']],[seis['text'],doce['text'],dieciocho['text'],veinticuatro['text'],treinta['text'],\
        treintaseis['text']]]
        for columna in columnas:
            for numero in columna:
                cantidad=0
                for copia in columna:
                    if numero==copia:
                        cantidad+=1
                if cantidad>1:
                    return True
        return False

    def reiniciar(opcion): #Pone en blanco cada label, tambien reinicia el cronometro y timer si estan presentes
        valores=[uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,diez,once,doce,trece,catorce,quince,dieciseis,diecisiete,dieciocho,diecinueve,veinte,veintiuno,\
        veintidos,veintitres,veinticuatro,veinticinco,veintiseis,veintisiete,veintiocho,veintinueve,treinta,treintauno,treintados,treintatres,treintacuatro,\
        treintacinco,treintaseis]
        global creado,listo,tipo
        if listo=="Si":
            if creado=="Si":
                configuracion=open("kenken_configuración.dat").readlines()
                if configuracion[1]=="timer\n":
                    detenerTimer()
                elif configuracion[1]=="relojSi\n":
                    detenerCronometro()
                    
                if opcion=="No":
                    opcion=messagebox.askquestion("REINICIAR", "¿ESTA SEGURO DE EMPEZAR NUEVAMENTE ESTE MISMO JUEGO?", icon='warning')
                if opcion=="yes":
                    global count
                    
                    for label in valores:
                        label['text']=""

                    if configuracion[1]=="relojSi\n":
                        hours['text']=0
                        minuts['text']=0
                        seconds['text']=0
                        count=0
                        cronometro()
                    elif configuracion[1]=="timer\n":
                        hours['text']=int(configuracion[3][:1])
                        minuts['text']=int(configuracion[3][1:3])
                        seconds['text']=int(configuracion[3][3:5])
                        count=seconds['text']
                        timer()
                else:
                    if configuracion[1]=="timer\n" and tipo=="Timer":
                        timer()
                    elif configuracion[1]=="relojSi\n" or tipo=="Cronometro":
                        cronometro()
            else:
                return messagebox.showinfo("ERROR","NO HA INICIADO NINGUN JUEGO")
        else:
            return messagebox.showinfo("ERROR","EL JUGADOR NO HA DADO SU NOMBRE")    

    #Funciones del cronometro
    def cronometro():
        global count,pausado
        pausado="No"
        pausar=Button(ventana,text="  Pausar ",command=lambda:detenerCronometro(),bg="lightgreen",font=("Helvetica",12))
        pausar.place(x=851,y=113)
        cronometro_aux(count)

    def cronometro_aux(contador):
        global proceso,count
        count=contador
        if minuts['text']==59 and contador==60:
            hours['text']+=1
            minuts['text']=0
            seconds['text']=0
            proceso=seconds.after(1000, cronometro_aux, (1))
        elif contador==60:
            minuts['text']+=1
            seconds['text']=0
            proceso=seconds.after(1000, cronometro_aux, (1))
        else:
            seconds['text'] = contador
            proceso=seconds.after(1000, cronometro_aux, (contador+1))

    def detenerCronometro():
        global proceso,pausado
        pausado="Si"
        reiniciar=Button(ventana,text="Reiniciar",command=lambda:cronometro(),bg="lightgreen",font=("Helvetica",12))
        reiniciar.place(x=851,y=113)
        seconds.after_cancel(proceso)

    #Funciones del timer
    def timer():
        global count,pausado
        pausado="No"
        pausar=Button(ventana,text="  Pausar ",command=lambda:detenerTimer(),bg="lightgreen",font=("Helvetica",12))
        pausar.place(x=851,y=113)
        timer_aux(count)

    def timer_aux(contador):
        global proceso,count,tipo
        count=contador
        seconds['text'] = contador
        if hours['text']==0 and minuts['text']==0 and contador==0: #En caso de que expire el tiempo tenemos ue preguntarle al usuario si desea continuar
            detenerTimer()
            opcion=messagebox.askquestion("TIEMPO EXPIRADO","¿DESEA CONTINUAR EL MISMO JUEGO?")
            if opcion=="yes":
                configuracion=open("kenken_configuración.dat").readlines()
                hours['text']=int(configuracion[3][:1])
                minuts['text']=int(configuracion[3][1:3])
                seconds['text']=int(configuracion[3][3:5])
                count=seconds['text']
                tipo="Cronometro"
                cronometro()
            else:
                return menu("Si",ventana)
        elif minuts['text']==0 and contador==59:
            hours['text']-=1
            minuts['text']=59
            proceso=seconds.after(1000, timer_aux, (contador-1))
        elif contador==59:
            minuts['text']-=1
            proceso=seconds.after(1000, timer_aux, (contador-1))
        elif contador==0:
            proceso=seconds.after(1000, timer_aux, (59))
        else:
            proceso=seconds.after(1000, timer_aux, (contador-1))

    def detenerTimer():
        global proceso,pausado
        pausado="Si"
        reiniciar=Button(ventana,text="Reiniciar",command=lambda:timer(),bg="lightgreen",font=("Helvetica",12))
        reiniciar.place(x=851,y=113)
        seconds.after_cancel(proceso)
   
    def pos(event,tupla): #Ayuda a seleccionar un label
        global posc
        posc = tupla

    #36 labels del juego
    uno=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    uno.place(x=350,y=60)
    uno.bind('<Button-1>',  lambda event: pos(event,(1,1)))
    
    dos=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    dos.place(x=398,y=60)
    dos.bind('<Button-1>',  lambda event:pos(event,(1,2)))
    
    tres=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    tres.place(x=446,y=60)
    tres.bind('<Button-1>',  lambda  event:pos(event,(1,3)))
    
    cuatro=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    cuatro.place(x=494,y=60)
    cuatro.bind('<Button-1>',  lambda event:pos(event,(1,4)))
    
    cinco=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    cinco.place(x=542,y=60)
    cinco.bind('<Button-1>',  lambda  event:pos(event,(1,5)))
    
    seis=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    seis.place(x=590,y=60)
    seis.bind('<Button-1>',  lambda  event:pos(event,(1,6)))
    
    siete=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    siete.place(x=350,y=130)
    siete.bind('<Button-1>',  lambda  event:pos(event,(2,1)))
    
    ocho=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    ocho.place(x=398,y=130)
    ocho.bind('<Button-1>',  lambda  event:pos(event,(2,2)))
    
    nueve=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    nueve.place(x=446,y=130)
    nueve.bind('<Button-1>',  lambda  event:pos(event,(2,3)))
    
    diez=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    diez.place(x=494,y=130)
    diez.bind('<Button-1>',  lambda  event:pos(event,(2,4)))
    
    once=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    once.place(x=542,y=130)
    once.bind('<Button-1>',  lambda  event:pos(event,(2,5)))
    
    doce=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    doce.place(x=590,y=130)
    doce.bind('<Button-1>',  lambda  event:pos(event,(2,6)))
    
    trece=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    trece.place(x=350,y=200)
    trece.bind('<Button-1>',  lambda  event:pos(event,(3,1)))
    
    catorce=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    catorce.place(x=398,y=200)
    catorce.bind('<Button-1>',  lambda  event:pos(event,(3,2)))
    
    quince=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    quince.place(x=446,y=200)
    quince.bind('<Button-1>',  lambda  event:pos(event,(3,3)))
    
    dieciseis=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    dieciseis.place(x=494,y=200)
    dieciseis.bind('<Button-1>',  lambda  event:pos(event,(3,4)))
    
    diecisiete=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    diecisiete.place(x=542,y=200)
    diecisiete.bind('<Button-1>',  lambda  event:pos(event,(3,5)))
    
    dieciocho=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    dieciocho.place(x=590,y=200)
    dieciocho.bind('<Button-1>',  lambda  event:pos(event,(3,6)))
    
    diecinueve=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    diecinueve.place(x=350,y=270)
    diecinueve.bind('<Button-1>',  lambda event:pos(event,(4,1)))
    
    veinte=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    veinte.place(x=398,y=270)
    veinte.bind('<Button-1>',  lambda event:pos(event,(4,2)))
    
    veintiuno=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    veintiuno.place(x=446,y=270)
    veintiuno.bind('<Button-1>',  lambda event:pos(event,(4,3)))
    
    veintidos=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    veintidos.place(x=494,y=270)
    veintidos.bind('<Button-1>',  lambda event:pos(event,(4,4)))
    
    veintitres=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    veintitres.place(x=542,y=270)
    veintitres.bind('<Button-1>',  lambda event:pos(event,(4,5)))
    
    veinticuatro=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    veinticuatro.place(x=590,y=270)
    veinticuatro.bind('<Button-1>',  lambda event:pos(event,(4,6)))
    
    veinticinco=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    veinticinco.place(x=350,y=340)
    veinticinco.bind('<Button-1>', lambda event:pos(event,(5,1)))
    
    veintiseis=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    veintiseis.place(x=398,y=340)
    veintiseis.bind('<Button-1>',  lambda event:pos(event,(5,2)))
    
    veintisiete=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    veintisiete.place(x=446,y=340)
    veintisiete.bind('<Button-1>', lambda event:pos(event,(5,3)))
    
    veintiocho=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    veintiocho.place(x=494,y=340)
    veintiocho.bind('<Button-1>',  lambda event:pos(event,(5,4)))
    
    veintinueve=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    veintinueve.place(x=542,y=340)
    veintinueve.bind('<Button-1>', lambda event:pos(event,(5,5)))
    
    treinta=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    treinta.place(x=590,y=340)
    treinta.bind('<Button-1>', lambda event:pos(event,(5,6)))
    
    treintauno=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    treintauno.place(x=350,y=410)
    treintauno.bind('<Button-1>', lambda event:pos(event,(6,1)))
    
    treintados=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    treintados.place(x=398,y=410)
    treintados.bind('<Button-1>',  lambda event:pos(event,(6,2)))
    
    treintatres=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    treintatres.place(x=446,y=410)
    treintatres.bind('<Button-1>', lambda event:pos(event,(6,3)))
    
    treintacuatro=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    treintacuatro.place(x=494,y=410)
    treintacuatro.bind('<Button-1>',  lambda event:pos(event,(6,4)))
    
    treintacinco=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    treintacinco.place(x=542,y=410)
    treintacinco.bind('<Button-1>',  lambda event:pos(event,(6,5)))
    
    treintaseis=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
    treintaseis.place(x=590,y=410)
    treintaseis.bind('<Button-1>', lambda event:pos(event,(6,6)))

    #Nombre del jugador
    nombre=StringVar()
    Label(ventana,text="Nombre del jugador",bg="yellow",font=("Helvetica",14)).place(x=200,y=600)
    entryName = Entry(ventana,textvariable=nombre,font=("Helvetica",14))
    entryName.place(x=375,y=600)
    name=Button(ventana,text="Guardar",command=lambda:guardarJugador(),bg="white",font=("Helvetica",12))
    name.place(x=375,y=630)

    def guardarJugada(var):
        global jugadas, posc
        if var == "si":
            jugadas.append([btn,posc])
            print(jugadas)

    def deshacerJugadas():
        global jugadas #[[num puesto, label], [num puesto,label]]
        copia = jugadas
        copia.reverse()
        copia[1:]
        for i in range(len(copia)):
            if copia[i][1] == posc:
                boton(copia[i][0],"no")
            
                
        
        
    #Botones principales del juego
    Button(ventana,text="Iniciar\nJuego",command=lambda:crear_juego(creado,"Si"),bg="red",font=("Helvetica",14)).place(x=200,y=500)
    Button(ventana,text="Validar\nJuego",command=lambda:validarCeldas(),bg="green2",font=("Helvetica",14)).place(x=350,y=500)
    Button(ventana,text="Otro\nJuego",command=lambda:otroJuego("No"),bg="lightblue",font=("Helvetica",14)).place(x=500,y=500)
    Button(ventana,text="Reiniciar\nJuego",command=lambda:reiniciar("No"),bg="orange",font=("Helvetica",14)).place(x=650,y=500)
    Button(ventana,text="Terminar\nJuego",command=lambda:terminar(),bg="pink",font=("Helvetica",14)).place(x=800,y=500)
    Button(ventana,text="TOP\n10",command=lambda:top10(),bg="#518251",font=("Helvetica",14)).place(x=800,y=600)
    Button(ventana,text="Deshacer\nJugada",command=deshacerJugadas,bg="lightblue",font=("Helvetica",14)).place(x=850,y=600)
    #Button(ventana,text="Rehacer\nJugada",command=lambda:top10(),bg="#518251",font=("Helvetica",14)).place(x=800,y=600)

        
        
    def rehacerJugadas():
        pass

        
    borrador = PhotoImage(file="borrador.png")
    Button(ventana,text="Borrar",image = borrador,command=lambda:boton("",""),bg="#4682b4",fg="white",font=("Helvetica",14)).place(x=800,y=380)
    def boton(num,var): #Aca se coloca los valores cada label
        global posc,listo,creado,pausado,btn
        btn = num
        if listo=="Si": #Verificamos que el usuario haya puesto su nombre
            if creado=="Si": #Vemos que exissta un juego creado
                if pausado=="No": #Vemos que el juego no este pausado
                    if posc==():
                        return messagebox.showinfo("ERROR","PRIMERO DEBE SELECCIONAR UNA CASILLA")
                    elif posc==(1,1):
                        uno['text']=num
                        guardarJugada(var)
                    elif posc==(1,2):
                        dos['text']=num
                        guardarJugada(var)
                    elif posc==(1,3):
                        tres['text']=num
                        guardarJugada(var)
                    elif posc==(1,4):
                        cuatro['text']=num
                        guardarJugada(var)
                    elif posc==(1,5):
                        cinco['text']=num
                        guardarJugada(var)
                    elif posc==(1,6):
                        seis['text']=num
                        guardarJugada(var)
                    elif posc==(2,1):
                        siete['text']=num
                        guardarJugada(var)
                    elif posc==(2,2):
                        ocho['text']=num
                        guardarJugada(var)
                    elif posc==(2,3):
                        nueve['text']=num
                        guardarJugada(var)
                    elif posc==(2,4):
                        diez['text']=num
                        guardarJugada(var)
                    elif posc==(2,5):
                        once['text']=num
                        guardarJugada(var)
                    elif posc==(2,6):
                        doce['text']=num
                        guardarJugada(var)
                    elif posc==(3,1):
                        trece['text']=num
                        guardarJugada(var)
                    elif posc==(3,2):
                        catorce['text']=num
                        guardarJugada(var)
                    elif posc==(3,3):
                        quince['text']=num
                        guardarJugada(var)
                    elif posc==(3,4):
                        dieciseis['text']=num
                        guardarJugada(var)
                    elif posc==(3,5):
                        diecisiete['text']=num
                        guardarJugada(var)
                    elif posc==(3,6):
                        dieciocho['text']=num
                        guardarJugada(var)
                    elif posc==(4,1):
                        diecinueve['text']=num
                        guardarJugada(var)
                    elif posc==(4,2):
                        veinte['text']=num
                        guardarJugada(var)
                    elif posc==(4,3):
                        veintiuno['text']=num
                        guardarJugada(var)
                    elif posc==(4,4):
                        veintidos['text']=num
                        guardarJugada(var)
                    elif posc==(4,5):
                        veintitres['text']=num
                        guardarJugada(var)
                    elif posc==(4,6):
                        veinticuatro['text']=num
                        guardarJugada(var)
                    elif posc==(5,1):
                        veinticinco['text']=num
                        guardarJugada(var)
                    elif posc==(5,2):
                        veintiseis['text']=num
                        guardarJugada(var)
                    elif posc==(5,3):
                        veintisiete['text']=num
                        guardarJugada(var)
                    elif posc==(5,4):
                        veintiocho['text']=num
                        guardarJugada(var)
                    elif posc==(5,5):
                        veintinueve['text']=num
                        guardarJugada(var)
                    elif posc==(5,6):
                        treinta['text']=num
                        guardarJugada(var)
                    elif posc==(6,1):
                        treintauno['text']=num
                        guardarJugada(var)
                    elif posc==(6,2):
                        treintados['text']=num
                        guardarJugada(var)
                    elif posc==(6,3):
                        treintatres['text']=num
                        guardarJugada(var)
                    elif posc==(6,4):
                        treintacuatro['text']=num
                        guardarJugada(var)
                    elif posc==(6,5):
                        treintacinco['text']=num
                        guardarJugada(var)
                    elif posc==(6,6):
                        treintaseis['text']=num
                        guardarJugada(var)
                else:
                    return messagebox.showinfo("ERROR","EL JUEGO ESTA PAUSADO")
            else:
                return messagebox.showinfo("ERROR","NO HA INICIADO NINGUN JUEGO")
        else:
            return messagebox.showinfo("ERROR","EL JUGADOR NO HA DADO SU NOMBRE")
        
    #Teclado numerico
    Button(ventana,text=1,command=lambda:boton(1,"si"),bg="black",fg="white",font=("Helvetica",14)).place(x=700,y=75)
    Button(ventana,text=2,command=lambda:boton(2,"si"),bg="black",fg="white",font=("Helvetica",14)).place(x=700,y=145)
    Button(ventana,text=3,command=lambda:boton(3,"si"),bg="black",fg="white",font=("Helvetica",14)).place(x=700,y=215)
    Button(ventana,text=4,command=lambda:boton(4,"si"),bg="black",fg="white",font=("Helvetica",14)).place(x=700,y=285)
    Button(ventana,text=5,command=lambda:boton(5,"si"),bg="black",fg="white",font=("Helvetica",14)).place(x=700,y=355)
    Button(ventana,text=6,command=lambda:boton(6,"si"),bg="black",fg="white",font=("Helvetica",14)).place(x=700,y=425)
    
    mainloop()

def configuracion(ventana): #Ventana de la configuracion, recibe la ventana del menu
    ventana.destroy() #Se destruye la ventana del menu
    config = Tk()
    config.title("Configuracion")
    config.geometry('500x600')
    config.resizable(False,False)
    config.config(bg="CadetBlue")

    def guardar(): #Se guarda la informacion
        archivo=open('kenken_configuración.dat','w')
        try:
            archivo.write(opcionDificultad.get()+opcionReloj.get()+opcionSonido.get()+str(int(h.get())*10000+int(m.get())*100+int(s.get())))
        except:
            archivo.write(opcionDificultad.get()+opcionReloj.get()+opcionSonido.get())
        archivo.close()
        verCronometro()

    h=StringVar() #Se usa para poner las horas en caso de seleccionar timer
    m=StringVar() #Se usa para poner los minutos en caso de seleccionar timer
    s=StringVar() #Se usa para poner los segundos en caso de seleccionar timer

    def validar(): #Valida los elementos de los entries en caso de haber seleccionado timer
        try: #Se pone dentro de un try en caso de que no pueda convertir los elementos a numeros
            horas=int(h.get()) #Se convierte las horas a enteros
            minutos=int(m.get()) #Se convierte los minutos a enteros
            segundos=int(s.get()) #Se convierte los segundos a enteros
            if horas<0 or horas>3: #Se validan las horas
                return messagebox.showinfo("ERROR","LAS HORAS DEBEN ESTAR ENTRE 0 Y 3")
            elif minutos<0 or minutos>59: #Se validan los minutos
                messagebox.showinfo("ERROR","LOS MINUTOS DEBEN ESTAR ENTRE 0 Y 59")
            elif segundos<0 or segundos>59: #Se validan segundos
                return messagebox.showinfo("ERROR","LOS SEGUNDOS DEBEN ESTAR ENTRE 0 Y 59")
            elif horas==0 and minutos==0 and segundos==0: #Los valores de los tiempos no pueden iniciar en 0
                return messagebox.showinfo("ERROR","EL TIMER NO DEBE EMPEZAR EN 0")
            elif horas==0 and minutos==0: #Caso especial
                archivo=open('kenken_configuración.dat','w')
                archivo.write(opcionDificultad.get()+opcionReloj.get()+opcionSonido.get()+"000"+str(segundos))
                archivo.close()
            elif horas==0: #Caso especial
                if minutos>9:
                    archivo=open('kenken_configuración.dat','w')
                    archivo.write(opcionDificultad.get()+opcionReloj.get()+opcionSonido.get()+"0"+str(minutos*100+segundos))
                    archivo.close()
                else:
                    archivo=open('kenken_configuración.dat','w')
                    archivo.write(opcionDificultad.get()+opcionReloj.get()+opcionSonido.get()+"00"+str(minutos*100+segundos))
                    archivo.close()
            else:
                archivo=open('kenken_configuración.dat','w')
                archivo.write(opcionDificultad.get()+opcionReloj.get()+opcionSonido.get()+str(horas*10000+minutos*100+segundos))
                archivo.close()
        except: #Mensaje de error ya que los elementos no eran numeros
            messagebox.showinfo("ERROR","LOS VALORES DEL TIMER DEBEN SER NUMEROS ENTEROS")

    def verCronometro(): #Se usa para timer
        archivo=open("kenken_configuración.dat").readlines()
        if archivo[1]=="timer\n":
            try: #Vemos si ya habia un tiempo configurado
                h.set(int(archivo[3][:1]))
                m.set(int(archivo[3][1:3]))
                s.set(int(archivo[3][3:5]))
            except:
                pass
            #Aparecen los entries
            Label(config,text="     Horas    ",bg="yellow",font=("Helvetica",12)).place(x=200,y=250)
            Entry(config,textvariable=h,width=9,font=("Helvetica",12)).place(x=199,y=275)
    
            Label(config,text="   Minutos   ",bg="yellow",font=("Helvetica",12)).place(x=286,y=250)
            Entry(config,textvariable=m,width=9,font=("Helvetica",12)).place(x=285,y=275)
            
            Label(config,text=" Segundos ",bg="yellow",font=("Helvetica",12)).place(x=372,y=250)
            Entry(config,textvariable=s,width=9,font=("Helvetica",12)).place(x=371,y=275)

            Button(config,text="Guardar",command=lambda:validar(),bg="lightgreen",font=("Helvetica",12)).place(x=200,y=299)
        else:
            Label(config,width=36,heigh=5,bg="CadetBlue").place(x=199,y=250)
        
    opcionDificultad = StringVar() #Contiene la dificultad
    opcionReloj = StringVar() #Contiene el tipo de juego (reloj,timer o ninguno)
    opcionSonido = StringVar() #En caso de que desee un sonido
    
    try: #Se trata de leer el archivo
        guardado=open("kenken_configuración.dat").readlines() #Se obtiene una lista con los datos guardados de la configuracion
        opcionDificultad.set(guardado[0])
        opcionReloj.set(guardado[1])
        opcionSonido.set(guardado[2])
        verCronometro()        
    except: #Por defecto
        opcionDificultad.set("F\n")
        opcionReloj.set("relojSi\n")
        opcionSonido.set("sonidoNo\n")
        guardar()


    #Nivel
    Label(config, text = "1. Nivel",bg="lightgreen",font=("Helvetica",12)).place(x=20,y= 50)
    Radiobutton(config,text="Fácil",bg="CadetBlue",variable = opcionDificultad, value = "F\n",command = guardar,font=("Helvetica",11)).place(x= 100,y=50)
    Radiobutton(config,text="Intermedio",bg="CadetBlue",variable = opcionDificultad, value = "I\n",command = guardar,font=("Helvetica",11)).place(x=100,y=100)
    Radiobutton(config,text="Difícil",bg="CadetBlue",variable = opcionDificultad, value = "D\n",command = guardar,font=("Helvetica",11)).place(x= 100,y=150)
    #Reloj
    Label(config, text = "2. Reloj",bg="lightgreen",font=("Helvetica",12)).place(x=20,y= 250)
    Radiobutton(config,text="Sí",bg="CadetBlue",variable = opcionReloj, value = "relojSi\n",command = guardar,font=("Helvetica",11)).place(x=100,y=250)
    Radiobutton(config,text="No",bg="CadetBlue",variable = opcionReloj, value = "relojNo\n",command = guardar,font=("Helvetica",11)).place(x=100,y=300)
    Radiobutton(config,text="Timer",bg="CadetBlue",variable = opcionReloj, value = "timer\n",command = guardar,font=("Helvetica",11)).place(x=100,y=350)
    #Sonido
    Label(config, text = "3. Sonido cuando termina el juego exitosamente",bg="lightgreen",font=("Helvetica",12)).place(x=20,y= 420)
    Radiobutton(config,text="No",bg="CadetBlue",variable = opcionSonido, value = "sonidoNo\n",command = guardar,font=("Helvetica",11)).place(x=100,y=450)
    Radiobutton(config,text="Sí",bg="CadetBlue",variable = opcionSonido, value = "sonidoSi\n",command = guardar,font=("Helvetica",11)).place(x=100,y=500)

    regresar=Button(config,text="Regresar",command=lambda:menu("Si",config),bg="lightgreen",font=("Helvetica",12)).place(x=20,y=550)

    mainloop()


def menu(opcion,window): #Recibe Si para eliminar la ventana de configuracion o de jugarKenken
    global dific
    if opcion=="Si": #Se usa para destruir la ventana anterior
        window.destroy()
    ventana= Tk()
    ventana.title("Menu")
    ventana.geometry("590x200")
    ventana.resizable(False,False)
    ventana.config(bg="CadetBlue")

    #Boton de jugar
    jugar=Button(ventana,text="Jugar",command=lambda:jugarKenken(ventana),bg="white",font=("Helvetica",14)).place(x=40,y=80)

    #Boton para configurar el juego
    config=Button(ventana,text="Configurar",command=lambda:configuracion(ventana),bg="white",font=("Helvetica",14)).place(x=130,y=80)

    #Despliega una ventana con el manual de usuario 
    helps=Button(ventana,text="Ayuda",command=lambda:os.startfile("manual_de_usuario_kenken.pdf"),bg="white",font=("Helvetica",14)).place(x=262,y=80)

    #Permite conocer un poco sobre la tarea
    acerca=Button(ventana,text="Acerca de",command=lambda:messagebox.showinfo("Acerca de","Nombre del programa: Kenken \nVersión: 1.0 \nCreacion: 01/10/2018 \nAutores: Mariela Murillo Artavia\n                Mauricio Gamboa Godínez"),bg="white",font=("Helvetica",14))
    acerca.place(x=360,y=80)

    #Boton salir
    salir=Button(ventana,text="Salir",command=lambda:ventana.destroy(),bg="white",font=("Helvetica",14)).place(x=495,y=80)

    mainloop()

menu("No",0) #Se llama a la funcion para iniciar la ejecucion
