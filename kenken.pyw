#Mauricio Gamboa
#Maariela Artavia

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
proceso=0 #Ayuda en la parte de cronometro y timer
cargado="No" #Ayuda cuando se carga un juego
rehacer = [] #Acumula jugadas para rehacer
jugadas = [] #Acumula las jugadas que se van haciendo
#Variables para colocar las cuadriculas
l1=l2=l3=l4=l5=l6=l7=l8=l9=l10=l11=l12=l13=l14=l15=l16=l17=l18=l19=l20=l21=l22=l23=l24=l25=l26=l27=l28=l29=l30=l31=l32=l33=l34=l35=l36=l37=l38=l39=l40=l41=l42=\
l43=l44=l45=l46=l47=l48=l49=l50=l51=l52=l53=l54=l55=l56=l57=l58=l59=l60=l61=l62=l63=l64=l65=l66=l67=l68=l69=l70=l71=l72=l73=l74=l75=l76=l77=l78=l79=l80=l81=0

def jugarKenken(ventana): #Recibe la ventana del menu y la destruye
    ventana.destroy()
    ventana= Tk()
    ventana.title("Jugar Kenken")
    ventana.geometry("1366x700")
    ventana.config(bg="#4682b4")

    global posc,juego,listo,creado,repetidos,count,pausado,proceso,rehacer,jugadas,cargado
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26,l27,l28,l29,l30,l31,l32,l33,l34,l35,l36,l37,l38,l39,l40,l41,\
    l42,l43,l44,l45,l46,l47,l48,l49,l50,l51,l52,l53,l54,l55,l56,l57,l58,l59,l60,l61,l62,l63,l64,l65,l66,l67,l68,l69,l70,l71,l72,l73,l74,l75,l76,l77,l78,l79,l80,l81

    #Siempre se inicializan de esta forma
    posc=()
    repetidos=[]
    creado="No"
    listo="No"
    juego={}
    count=0
    pausado="No"
    tipo="Timer"
    proceso=0
    rehacer = []
    jugadas = []
    l1=l2=l3=l4=l5=l6=l7=l8=l9=l10=l11=l12=l13=l14=l15=l16=l17=l18=l19=l20=l21=l22=l23=l24=l25=l26=l27=l28=l29=l30=l31=l32=l33=l34=l35=l36=l37=l38=l39=l40=l41=l42=\
    l43=l44=l45=l46=l47=l48=l49=l50=l51=l52=l53=l54=l55=l56=l57=l58=l59=l60=l61=l62=l63=l64=l65=l66=l67=l68=l69=l70=l71=l72=l73=l74=l75=l76=l77=l78=l79=l80=l81=0

    #Se usa para colocar la operacion que le corresponde a cada celda
    dic={(1,1):(353,63),(1,2):(401,63),(1,3):(449,63),(1,4):(497,63),(1,5):(545,63),(1,6):(593,63),(1,7):(641,63),(1,8):(689,63),(1,9):(737,63),\
    (2,1):(353,133),(2,2):(401,133),(2,3):(449,133),(2,4):(497,133),(2,5):(545,133),(2,6):(593,133),(2,7):(641,133),(2,8):(689,133),(2,9):(737,133),\
    (3,1):(353,203),(3,2):(401,203),(3,3):(449,203),(3,4):(497,203),(3,5):(545,203),(3,6):(593,203),(3,7):(641,203),(3,8):(689,203),(3,9):(737,203),\
    (4,1):(353,273),(4,2):(401,273),(4,3):(449,273),(4,4):(497,273),(4,5):(545,273),(4,6):(593,273),(4,7):(641,273),(4,8):(689,273),(4,9):(737,273),\
    (5,1):(353,343),(5,2):(401,343),(5,3):(449,343),(5,4):(497,343),(5,5):(545,343),(5,6):(593,343),(5,7):(641,343),(5,8):(689,343),(5,9):(737,343),\
    (6,1):(353,413),(6,2):(401,413),(6,3):(449,413),(6,4):(497,413),(6,5):(545,413),(6,6):(593,413),(6,7):(641,413),(6,8):(689,413),(6,9):(737,413),\
    (7,1):(353,483),(7,2):(401,483),(7,3):(449,483),(7,4):(497,483),(7,5):(545,483),(7,6):(593,483),(7,7):(641,483),(7,8):(689,483),(7,9):(737,483),\
    (8,1):(353,553),(8,2):(401,553),(8,3):(449,553),(8,4):(497,553),(8,5):(545,553),(8,6):(593,553),(8,7):(641,553),(8,8):(689,553),(8,9):(737,553),\
    (9,1):(353,623),(9,2):(401,623),(9,3):(449,623),(9,4):(497,623),(9,5):(545,623),(9,6):(593,623),(9,7):(641,623),(9,8):(689,623),(9,9):(737,623)}

    #Contiene una lista de colores para diferenciar las celdas
    colores=["greenyellow","#83689a","yellow","orange","#0dd0e1","red","pink","indianred","lightgreen","slateblue1","khaki","thistle","#227ca2","#f77e78","#40e7b9",\
    "green2","#c98686",'#518251','#f6c348','gray','#e7aebf','#b980ff','#9b775d','#c91b20','#ffb2f2','#5fcc9c','#ee6c4d','#ffe19c','#fecc0c','#5ec4ec','#dabe96','#cdffe6']

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
            listo="Si" #Ponemos que ya existe un nombre
            #Label(ventana,bg="purple1",width=57,height=5).place(x=200,y=600)
            entryName.config(state = DISABLED) #Se deshablita el entry
            name.destroy() #Destruimos el boton            

    def crearCeldas(posicion,color): #Recibe un par ordenado para saber cual label se tiene que configurar con un color
         #Diccionario con los labels
        etiquetas={(1,1):l1,(1,2):l2,(1,3):l3,(1,4):l10,(1,5):l17,(1,6):l26,(1,7):l37,(1,8):l50,(1,9):l65,\
        (2,1):l4,(2,2):l5,(2,3):l6,(2,4):l11,(2,5):l18,(2,6):l27,(2,7):l38,(2,8):l51,(2,9):l66,\
        (3,1):l7,(3,2):l8,(3,3):l9,(3,4):l12,(3,5):l19,(3,6):l28,(3,7):l39,(3,8):l52,(3,9):l67,\
        (4,1):l13,(4,2):l14,(4,3):l15,(4,4):l16,(4,5):l20,(4,6):l29,(4,7):l40,(4,8):l53,(4,9):l68,\
        (5,1):l21,(5,2):l22,(5,3):l23,(5,4):l24,(5,5):l25,(5,6):l30,(5,7):l41,(5,8):l54,(5,9):l69,\
        (6,1):l31,(6,2):l32,(6,3):l33,(6,4):l34,(6,5):l35,(6,6):l36,(6,7):l42,(6,8):l55,(6,9):l70,\
        (7,1):l43,(7,2):l44,(7,3):l45,(7,4):l46,(7,5):l47,(7,6):l48,(7,7):l49,(7,8):l56,(7,9):l71,\
        (8,1):l57,(8,2):l58,(8,3):l59,(8,4):l60,(8,5):l61,(8,6):l62,(8,7):l63,(8,8):l64,(8,9):l72,\
        (9,1):l73,(9,2):l74,(9,3):l75,(9,4):l76,(9,5):l77,(9,6):l78,(9,7):l79,(9,8):l80,(9,9):l81}

        etiquetas[posicion].config(bg=color) #Se configura un label gracias al diccionario
        
    def partidasGuardadas(): #Pone en un diccionario las partidas de acuerdo a su dificultad y tamaño
        partidas=open('kenken_juegos.dat')
        nivel=open("kenken_configuración.dat").readlines()[3][0] #Contiene el tipo de cuadricula de la configuracion
        dic={"F":[],"I":[],"D":[]} #Guarda las partidas que correspondan a la cuadricula configurada en diccionarios segun su dificultad
        while True:
            juego=partidas.readline()
            if juego=="":
                break
            elif juego[0]=="F" and juego[1]==nivel:
                dic["F"]+=[eval(juego[2:-1])]
            elif juego[0]=="I" and juego[1]==nivel:
                dic["I"]+=[eval(juego[2:-1])]
            elif juego[0]=="D" and juego[1]==nivel:
                dic["D"]+=[eval(juego[2:-1])]
        return dic

    def crear_juego_aux(juego): #Recibe un juego al azar dependiendo de la dificultad, esta funcion lee como debe verse el juego graficamente
        color=0 #Ayuda a dar color a los labels, permite usar un color de la lista de colores
        for indice in juego: #Ingresamos al diccionario del juego
            operacion=juego[indice][0] #Vemos el resultado que deben dar las celdas correspondientes
            contador=1 #Eviatamos la operacion
            while contador<len(juego[indice]):
                for posicion in dic: #Usamos el diccionario que posee las ubicaciones de cada par ordenado
                    if contador==1 and posicion==juego[indice][contador]: #El primer par ordenado es que el tendra la operacion
                        Label(ventana,text=operacion,width=3,bg=colores[color],font=("Arial",10)).place(x=dic[posicion][0],y=dic[posicion][1]) #Colocamos la operacon
                        crearCeldas(posicion,colores[color]) #Configuramos la casilla con color
                        break
                    elif posicion==juego[indice][contador]:
                        Label(ventana,width=3,bg=colores[color],font=("Arial",10)).place(x=dic[posicion][0],y=dic[posicion][1])
                        crearCeldas(posicion,colores[color]) #Configuramos la casilla con color                      
                        break
                contador+=1 #Aumentamos el contador para configurar la celda
            color+=1 #Se aumenta el contador de color

    def crear_juego(created,opcion): #Recibe un parametro que le permite saber si ya hay un juego iniciado y si ya existe un cronometro (caso especial)
        global listo,juego,repetidos
        if listo=="Si": #Verificamos que el usuario haya puesto el nombre
            if created=="No": #Verificamos que no exista un juego creado (caso para iniciar juego)
                global creado,count
                configuracion=open("kenken_configuración.dat").readlines() #Lista con la configuracion del juego
                dificultad=configuracion[0][0] #Contiene el nivel de dificultad
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
                if tiempo=="relojSi\n": #Vemos si la configuracion posee un cronometro
                    cortina.destroy() #Se destruye el label
                    count=0 #Ponemos el contador en 0
                    if opcion=="Si": #Verificamos que no exista otro cronometro (caso que dificultaba el uso de otro juego)
                        cronometro()
                elif tiempo=="timer\n" and configuracion[3][1]!="M": #Vemos si la configuracion es un timer
                    cortina.destroy() #Se destruye el label
                    #Se ponen los valores adecuados a cada tiempo
                    hours['text']=int(configuracion[4][:1])
                    minuts['text']=int(configuracion[4][1:3])
                    seconds['text']=int(configuracion[4][3:5])
                    count=seconds['text']
                    if opcion=="Si":
                        timer()
                elif tiempo=="timer\n" and configuracion[3][1]=="M" and creado=="No":
                    cortina.destroy() #Se destruye el label
                    #Se ponen los valores adecuados a cada tiempo
                    hours['text']=2
                    minuts['text']=0
                    seconds['text']=0
                    count=seconds['text']
                    if opcion=="Si":
                        timer()
                creado="Si" #Ponemos que ya existe un juego creado
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
                    if tipo=="Cronometro":
                        tipo="Timer"
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
        global listo,creado,tipo
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
                    if configuracion[1]=="timer\n":
                        detenerTimer()
                    elif configuracion[1]=="relojSi\n":
                        detenerCronometro()
                    if configuracion[2]=="sonidoSi\n":
                        PlaySound('congratulations.wav', SND_FILENAME)
                    messagebox.showinfo("ERROR","FELICIDADES, HAS GANADO")
                    opcion=messagebox.askquestion("CONTINUAR", "¿DESEA CONTINUAR JUGANDO?", icon='warning')
                    if opcion=="yes":
                        if configuracion[3][1]=="M" and configuracion[3][0]!="9":
                            archivo=open('kenken_configuración.dat','w')
                            try:
                                archivo.write(configuracion[0]+configuracion[1]+configuracion[2]+str(int(configuracion[3][0])+1)+"M\n"+configuracion[4])
                            except:
                                archivo.write(configuracion[0]+configuracion[1]+configuracion[2]+str(int(configuracion[3][0])+1)+"M\n")
                            archivo.close()
                            labels()
                        elif configuracion[3][1]=="M" and configuracion[3][0]=="9":
                            cortina=Label(ventana,width=28,heigh=5,bg="#4682b4",font=("Helvetica",12)) #Ayuda a ocultar la cuadricula
                            cortina.place(x=850,y=60)
                            tipo="Nada"
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
                result=eval(temporal[:-1])
            except:
                return False
            if result!=resultado:
                for par in pares: #Se hace un ciclo para marcar la celda que no da el resultado correcto
                    par['text']=str(par['text'])+"X"
                return False
        return True

    def retornarLabel(tupla): #Ayuda a retornar el valor de cada label, ademas contiene el label para identificarlo en caso de que haya un error en la operacion

        #Diccionario con los labels
        etiquetas={(1,1):l1,(1,2):l2,(1,3):l3,(1,4):l10,(1,5):l17,(1,6):l26,(1,7):l37,(1,8):l50,(1,9):l65,\
        (2,1):l4,(2,2):l5,(2,3):l6,(2,4):l11,(2,5):l18,(2,6):l27,(2,7):l38,(2,8):l51,(2,9):l66,\
        (3,1):l7,(3,2):l8,(3,3):l9,(3,4):l12,(3,5):l19,(3,6):l28,(3,7):l39,(3,8):l52,(3,9):l67,\
        (4,1):l13,(4,2):l14,(4,3):l15,(4,4):l16,(4,5):l20,(4,6):l29,(4,7):l40,(4,8):l53,(4,9):l68,\
        (5,1):l21,(5,2):l22,(5,3):l23,(5,4):l24,(5,5):l25,(5,6):l30,(5,7):l41,(5,8):l54,(5,9):l69,\
        (6,1):l31,(6,2):l32,(6,3):l33,(6,4):l34,(6,5):l35,(6,6):l36,(6,7):l42,(6,8):l55,(6,9):l70,\
        (7,1):l43,(7,2):l44,(7,3):l45,(7,4):l46,(7,5):l47,(7,6):l48,(7,7):l49,(7,8):l56,(7,9):l71,\
        (8,1):l57,(8,2):l58,(8,3):l59,(8,4):l60,(8,5):l61,(8,6):l62,(8,7):l63,(8,8):l64,(8,9):l72,\
        (9,1):l73,(9,2):l74,(9,3):l75,(9,4):l76,(9,5):l77,(9,6):l78,(9,7):l79,(9,8):l80,(9,9):l81}

        return [etiquetas[tupla]['text'],etiquetas[tupla]]

    def verVacios(): #Veriicamos que el label no este vacio
        labels=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26,l27,l28,l29,l30,l31,l32,l33,l34,l35,l36,l37,l38,l39,\
        l40,l41,l42,l43,l44,l45,l46,l47,l48,l49,l50,l51,l52,l53,l54,l55,l56,l57,l58,l59,l60,l61,l62,l63,l64,l65,l66,l67,l68,l69,l70,l71,l72,l73,l74,l75,l76,l77,l78,\
        l79,l80,l81]
        try:
            for label in labels:
                if label['text']=="":
                    return True
        except:
            pass
        return False

    def verFilas(): #Verificamos que no existan los mismos numeros en una fila
        filas=[[l1,l2,l3,l10,l17,l26,l37,l50,l65],[l4,l5,l6,l11,l18,l27,l38,l51,l66],[l7,l8,l9,l12,l19,l28,l39,l52,l67],[l13,l14,l15,l16,l20,l29,l40,l53,l68],\
        [l21,l22,l23,l24,l25,l30,l41,l54,l69],[l31,l32,l33,l34,l35,l36,l42,l55,l70],[l43,l44,l45,l46,l47,l48,l49,l56,l71],[l57,l58,l59,l60,l61,l62,l63,l64,l72],\
        [l73,l74,l75,l76,l77,l78,l79,l80,l81]]
        nivel=int(open("kenken_configuración.dat").readlines()[3][0])

        #Se aggaran los labels necesarios dependiendo de la cuadricula
        filas=filas[:nivel]
        copia_filas=[]
        for fila in filas:
            copia_filas+=[fila[:nivel]]
            
        filas=copia_filas
        for fila in filas:
            for numero in fila:
                cantidad=0
                for copia in fila:
                    if numero['text']==copia['text']:
                        cantidad+=1
                if cantidad>1:
                    return True
        return False

    def verColumnas(): #Verificamos que no existan los mismos numeros en una columna
        columnas=[[l1,l4,l7,l13,l21,l31,l43,l57,l73],[l2,l5,l8,l14,l22,l32,l44,l58,l74],[l3,l6,l9,l15,l23,l33,l45,l59,l75],[l10,l11,l12,l16,l24,l34,l46,l60,l76],\
        [l17,l18,l19,l20,l25,l35,l47,l61,l77],[l26,l27,l28,l29,l30,l36,l48,l62,l78],[l37,l38,l39,l40,l41,l42,l49,l63,l79],[l50,l51,l52,l53,l54,l55,l56,l64,l80],\
        [l65,l66,l67,l68,l69,l70,l71,l72,l81]]
        nivel=int(open("kenken_configuración.dat").readlines()[3][0])

        #Se aggaran los labels necesarios dependiendo de la cuadricula
        columnas=columnas[:nivel]
        copia_columnas=[]
        for columna in columnas:
            copia_columnas+=[columna[:nivel]]

        columnas=copia_columnas
        for columna in columnas:
            for numero in columna:
                cantidad=0
                for copia in columna:
                    if numero['text']==copia['text']:
                        cantidad+=1
                if cantidad>1:
                    return True
        return False

    def reiniciar(opcion): #Pone en blanco cada label, tambien reinicia el cronometro y timer si estan presentes
        labels=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26,l27,l28,l29,l30,l31,l32,l33,l34,l35,l36,l37,l38,l39,\
        l40,l41,l42,l43,l44,l45,l46,l47,l48,l49,l50,l51,l52,l53,l54,l55,l56,l57,l58,l59,l60,l61,l62,l63,l64,l65,l66,l67,l68,l69,l70,l71,l72,l73,l74,l75,l76,l77,l78,\
        l79,l80,l81]
        global creado,listo,tipo,jugadas,rehacer
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
                    try:
                        for label in labels:
                            label['text']=""
                    except:
                        pass
                    rehacer = []
                    jugadas = []
                    if configuracion[1]=="relojSi\n":
                        hours['text']=0
                        minuts['text']=0
                        seconds['text']=0
                        count=0
                        cronometro()
                    elif configuracion[1]=="timer\n" and configuracion[3][1]!="M":
                        tipo="Timer"
                        hours['text']=int(configuracion[4][:1])
                        minuts['text']=int(configuracion[4][1:3])
                        seconds['text']=int(configuracion[4][3:5])
                        count=seconds['text']
                        timer()
                    elif configuracion[1]=="timer\n" and configuracion[3][1]=="M" and tipo=="Timer":
                        timer()
                    Label(ventana,width=28,heigh=19,bg="#4682b4",font=("Helvetica",12)).place(x=850,y=200)
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
                hours['text']=int(configuracion[4][:1])
                minuts['text']=int(configuracion[4][1:3])
                seconds['text']=int(configuracion[4][3:5])
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
        global proceso,pausado,tipo
        pausado="Si"
        if tipo!="Nada":
            reiniciar=Button(ventana,text="Reiniciar",command=lambda:timer(),bg="lightgreen",font=("Helvetica",12))
            reiniciar.place(x=851,y=113)
        seconds.after_cancel(proceso)
   
    def pos(event,tupla): #Ayuda a seleccionar un label
        global posc
        posc = tupla
        posiblesJugadas()

    def labels(): #Funcion que permite realizar un cuadricula de nxn
        global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26,l27,l28,l29,l30,l31,l32,l33,l34,l35,l36,l37,l38,l39,l40,l41,\
        l42,l43,l44,l45,l46,l47,l48,l49,l50,l51,l52,l53,l54,l55,l56,l57,l58,l59,l60,l61,l62,l63,l64,l65,l66,l67,l68,l69,l70,l71,l72,l73,l74,l75,l76,l77,l78,l79,l80,l81

        archivo=open("kenken_configuración.dat").readlines()
        size=int(archivo[3][0])
        if size>=3:
            l1=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l1.place(x=350,y=60)
            l1.bind('<Button-1>', lambda event:pos(event,(1,1)))
            
            l2=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l2.place(x=398,y=60)
            l2.bind('<Button-1>', lambda event:pos(event,(1,2)))
            
            l3=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l3.place(x=446,y=60)
            l3.bind('<Button-1>', lambda event:pos(event,(1,3)))
            
            l4=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l4.place(x=350,y=130)
            l4.bind('<Button-1>', lambda event:pos(event,(2,1)))

            l5=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l5.place(x=398,y=130)
            l5.bind('<Button-1>', lambda event:pos(event,(2,2)))

            l6=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l6.place(x=446,y=130)
            l6.bind('<Button-1>', lambda event:pos(event,(2,3)))

            l7=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l7.place(x=350,y=200)
            l7.bind('<Button-1>', lambda event:pos(event,(3,1)))

            l8=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l8.place(x=398,y=200)
            l8.bind('<Button-1>', lambda event:pos(event,(3,2)))

            l9=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l9.place(x=446,y=200)
            l9.bind('<Button-1>', lambda event:pos(event,(3,3)))

            Button(ventana,text=1,command=lambda:boton(1,"si"),bg="black",fg="white",font=("Helvetica",14)).place(x=300,y=75)
            Button(ventana,text=2,command=lambda:boton(2,"si"),bg="black",fg="white",font=("Helvetica",14)).place(x=300,y=145)
            Button(ventana,text=3,command=lambda:boton(3,"si"),bg="black",fg="white",font=("Helvetica",14)).place(x=300,y=215)
        if size>=4:
            l10=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l10.place(x=494,y=60)
            l10.bind('<Button-1>', lambda event:pos(event,(1,4)))

            l11=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l11.place(x=494,y=130)
            l11.bind('<Button-1>', lambda event:pos(event,(2,4)))

            l12=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l12.place(x=494,y=200)
            l12.bind('<Button-1>', lambda event:pos(event,(3,4)))

            l13=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l13.place(x=350,y=270)
            l13.bind('<Button-1>', lambda event:pos(event,(4,1)))

            l14=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l14.place(x=398,y=270)
            l14.bind('<Button-1>', lambda event:pos(event,(4,2)))

            l15=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l15.place(x=446,y=270)
            l15.bind('<Button-1>', lambda event:pos(event,(4,3)))

            l16=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l16.place(x=494,y=270)
            l16.bind('<Button-1>', lambda event:pos(event,(4,4)))

            Button(ventana,text=4,command=lambda:boton(4,"si"),bg="black",fg="white",font=("Helvetica",14)).place(x=300,y=285)
        if size>=5:
            l17=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l17.place(x=542,y=60)
            l17.bind('<Button-1>', lambda event:pos(event,(1,5)))

            l18=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l18.place(x=542,y=130)
            l18.bind('<Button-1>', lambda event:pos(event,(2,5)))

            l19=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l19.place(x=542,y=200)
            l19.bind('<Button-1>', lambda event:pos(event,(3,5)))

            l20=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l20.place(x=542,y=270)
            l20.bind('<Button-1>', lambda event:pos(event,(4,5)))

            l21=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l21.place(x=350,y=340)
            l21.bind('<Button-1>', lambda event:pos(event,(5,1)))

            l22=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l22.place(x=398,y=340)
            l22.bind('<Button-1>', lambda event:pos(event,(5,2)))

            l23=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l23.place(x=446,y=340)
            l23.bind('<Button-1>', lambda event:pos(event,(5,3)))

            l24=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l24.place(x=494,y=340)
            l24.bind('<Button-1>', lambda event:pos(event,(5,4)))

            l25=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l25.place(x=542,y=340)
            l25.bind('<Button-1>', lambda event:pos(event,(5,5)))

            Button(ventana,text=5,command=lambda:boton(5,"si"),bg="black",fg="white",font=("Helvetica",14)).place(x=300,y=355)
        if size>=6:
            l26=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l26.place(x=590,y=60)
            l26.bind('<Button-1>', lambda event:pos(event,(1,6)))

            l27=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l27.place(x=590,y=130)
            l27.bind('<Button-1>', lambda event:pos(event,(2,6)))

            l28=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l28.place(x=590,y=200)
            l28.bind('<Button-1>', lambda event:pos(event,(3,6)))

            l29=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l29.place(x=590,y=270)
            l29.bind('<Button-1>', lambda event:pos(event,(4,6)))

            l30=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l30.place(x=590,y=340)
            l30.bind('<Button-1>', lambda event:pos(event,(5,6)))

            l31=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l31.place(x=350,y=410)
            l31.bind('<Button-1>', lambda event:pos(event,(6,1)))

            l32=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l32.place(x=398,y=410)
            l32.bind('<Button-1>', lambda event:pos(event,(6,2)))

            l33=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l33.place(x=446,y=410)
            l33.bind('<Button-1>', lambda event:pos(event,(6,3)))

            l34=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l34.place(x=494,y=410)
            l34.bind('<Button-1>', lambda event:pos(event,(6,4)))

            l35=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l35.place(x=542,y=410)
            l35.bind('<Button-1>', lambda event:pos(event,(6,5)))

            l36=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l36.place(x=590,y=410)
            l36.bind('<Button-1>', lambda event:pos(event,(6,6)))

            Button(ventana,text=6,command=lambda:boton(6,"si"),bg="black",fg="white",font=("Helvetica",14)).place(x=300,y=425)
        if size>=7:
            l37=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l37.place(x=638,y=60)
            l37.bind('<Button-1>', lambda event:pos(event,(1,7)))

            l38=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l38.place(x=638,y=130)
            l38.bind('<Button-1>', lambda event:pos(event,(2,7)))

            l39=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l39.place(x=638,y=200)
            l39.bind('<Button-1>', lambda event:pos(event,(3,7)))

            l40=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l40.place(x=638,y=270)
            l40.bind('<Button-1>', lambda event:pos(event,(4,7)))

            l41=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l41.place(x=638,y=340)
            l41.bind('<Button-1>', lambda event:pos(event,(5,7)))

            l42=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l42.place(x=638,y=410)
            l42.bind('<Button-1>', lambda event:pos(event,(6,7)))

            l43=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l43.place(x=350,y=480)
            l43.bind('<Button-1>', lambda event:pos(event,(7,1)))

            l44=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l44.place(x=398,y=480)
            l44.bind('<Button-1>', lambda event:pos(event,(7,2)))

            l45=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l45.place(x=446,y=480)
            l45.bind('<Button-1>', lambda event:pos(event,(7,3)))

            l46=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l46.place(x=494,y=480)
            l46.bind('<Button-1>', lambda event:pos(event,(7,4)))

            l47=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l47.place(x=542,y=480)
            l47.bind('<Button-1>', lambda event:pos(event,(7,5)))

            l48=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l48.place(x=590,y=480)
            l48.bind('<Button-1>', lambda event:pos(event,(7,6)))

            l49=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l49.place(x=638,y=480)
            l49.bind('<Button-1>', lambda event:pos(event,(7,7)))

            Button(ventana,text=7,command=lambda:boton(7,"si"),bg="black",fg="white",font=("Helvetica",14)).place(x=300,y=495)
        if size>=8:
            l50=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l50.place(x=686,y=60)
            l50.bind('<Button-1>', lambda event:pos(event,(1,8)))

            l51=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l51.place(x=686,y=130)
            l51.bind('<Button-1>', lambda event:pos(event,(2,8)))

            l52=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l52.place(x=686,y=200)
            l52.bind('<Button-1>', lambda event:pos(event,(3,8)))

            l53=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l53.place(x=686,y=270)
            l53.bind('<Button-1>', lambda event:pos(event,(4,8)))

            l54=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l54.place(x=686,y=340)
            l54.bind('<Button-1>', lambda event:pos(event,(5,8)))

            l55=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l55.place(x=686,y=410)
            l55.bind('<Button-1>', lambda event:pos(event,(6,8)))

            l56=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l56.place(x=686,y=480)
            l56.bind('<Button-1>', lambda event:pos(event,(7,8)))

            l57=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l57.place(x=350,y=550)
            l57.bind('<Button-1>', lambda event:pos(event,(8,1)))

            l58=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l58.place(x=398,y=550)
            l58.bind('<Button-1>', lambda event:pos(event,(8,2)))

            l59=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l59.place(x=446,y=550)
            l59.bind('<Button-1>', lambda event:pos(event,(8,3)))

            l60=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l60.place(x=494,y=550)
            l60.bind('<Button-1>', lambda event:pos(event,(8,4)))

            l61=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l61.place(x=542,y=550)
            l61.bind('<Button-1>', lambda event:pos(event,(8,5)))

            l62=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l62.place(x=590,y=550)
            l62.bind('<Button-1>', lambda event:pos(event,(8,6)))

            l63=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l63.place(x=638,y=550)
            l63.bind('<Button-1>', lambda event:pos(event,(8,7)))

            l64=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l64.place(x=686,y=550)
            l64.bind('<Button-1>', lambda event:pos(event,(8,8)))

            Button(ventana,text=8,command=lambda:boton(8,"si"),bg="black",fg="white",font=("Helvetica",14)).place(x=300,y=565)
        if size==9:
            l65=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l65.place(x=734,y=60)
            l65.bind('<Button-1>', lambda event:pos(event,(1,9)))

            l66=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l66.place(x=734,y=130)
            l66.bind('<Button-1>', lambda event:pos(event,(2,9)))

            l67=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l67.place(x=734,y=200)
            l67.bind('<Button-1>', lambda event:pos(event,(3,9)))

            l68=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l68.place(x=734,y=270)
            l68.bind('<Button-1>', lambda event:pos(event,(4,9)))

            l69=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l69.place(x=734,y=340)
            l69.bind('<Button-1>', lambda event:pos(event,(5,9)))

            l70=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l70.place(x=734,y=410)
            l70.bind('<Button-1>', lambda event:pos(event,(6,9)))

            l71=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l71.place(x=734,y=480)
            l71.bind('<Button-1>', lambda event:pos(event,(7,9)))

            l72=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l72.place(x=734,y=550)
            l72.bind('<Button-1>', lambda event:pos(event,(8,9)))

            l73=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l73.place(x=350,y=620)
            l73.bind('<Button-1>', lambda event:pos(event,(9,1)))

            l74=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l74.place(x=398,y=620)
            l74.bind('<Button-1>', lambda event:pos(event,(9,2)))

            l75=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l75.place(x=446,y=620)
            l75.bind('<Button-1>', lambda event:pos(event,(9,3)))

            l76=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l76.place(x=494,y=620)
            l76.bind('<Button-1>', lambda event:pos(event,(9,4)))

            l77=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l77.place(x=542,y=620)
            l77.bind('<Button-1>', lambda event:pos(event,(9,5)))

            l78=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l78.place(x=590,y=620)
            l78.bind('<Button-1>', lambda event:pos(event,(9,6)))

            l79=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l79.place(x=638,y=620)
            l79.bind('<Button-1>', lambda event:pos(event,(9,7)))

            l80=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l80.place(x=686,y=620)
            l80.bind('<Button-1>', lambda event:pos(event,(9,8)))

            l81=Label(ventana,width=4,heigh=3,bg="white",bd=2,relief="solid",font=("Arial",14))
            l81.place(x=734,y=620)
            l81.bind('<Button-1>', lambda event:pos(event,(9,9)))
            
            Button(ventana,text=9,command=lambda:boton(9,"si"),bg="black",fg="white",font=("Helvetica",14)).place(x=300,y=635)

    #Nombre del jugador
    nombre=StringVar()
    Label(ventana,text="     Nombre del jugador     ",bg="yellow",font=("Helvetica",14)).place(x=5,y=5)
    entryName = Entry(ventana,textvariable=nombre,font=("Helvetica",14))
    entryName.place(x=5,y=35)
    name=Button(ventana,text="Guardar",bg="white",command=lambda:guardarJugador(),font=("Helvetica",12))
    name.place(x=5,y=65)

    #Botones principales del juego
    Button(ventana,text="Iniciar\nJuego",command=lambda:crear_juego(creado,"Si"),bg="red",font=("Helvetica",14)).place(x=60,y=120)
    Button(ventana,text="Validar\nJuego",command=lambda:validarCeldas(),bg="green2",font=("Helvetica",14)).place(x=60,y=200)
    Button(ventana,text="Otro\nJuego",command=lambda:otroJuego("No"),bg="lightblue",font=("Helvetica",14)).place(x=160,y=120)
    Button(ventana,text="Reiniciar\nJuego",command=lambda:reiniciar("No"),bg="orange",font=("Helvetica",14)).place(x=160,y=200)
    Button(ventana,text="Terminar\nJuego",command=lambda:terminar(),bg="pink",font=("Helvetica",14)).place(x=60,y=280)
    Button(ventana,text="Deshacer\nJugada",command=lambda:deshacerJugadas(),bg="lightgreen",font=("Helvetica",14)).place(x=60,y=360)
    Button(ventana,text="Rehacer\nJugada",command=lambda:rehacerJugadas(),bg="yellow",font=("Helvetica",14)).place(x=160,y=360)
    Button(ventana,text="Guardar\nJuego",command=lambda:guardarPartida(),bg="gray",font=("Helvetica",14)).place(x=60,y=440)
    Button(ventana,text="Cargar\nJuego",command=lambda:cargarJuego(),bg="white",font=("Helvetica",14)).place(x=160,y=440)
    Button(ventana,text="  Borrar  \n",command=lambda:boton("","si"),bg="black",fg="white",font=("Helvetica",14)).place(x=160,y=280)
        
    def guardarJugadas(num): #Guarda las jugadas que se vayan realizando
        global posc,jugadas
        jugadas+=[[posc,num]]
        
    def deshacerJugadas(): #Permite deshacer una jugada
        global jugadas,rehacer,posc,listo,creado
        if listo=="No":
            return messagebox.showinfo("ERROR","EL JUGADOR NO HA DADO SU NOMBRE")
        elif creado=="No":
            return messagebox.showinfo("ERROR","NO HA INICIADO NINGUN JUEGO")
        elif pausado=="Si":
            return messagebox.showinfo("ERROR","EL JUEGO ESTA PAUSADO")
        elif jugadas == []:
            return messagebox.showinfo("ERROR","NO HAY MÁS JUGADAS POR DESHACER")
        else:
            posc = jugadas[-1][0]
            rehacer+=[jugadas.pop()]
            copia = jugadas.copy()
            copia.reverse()
            for i in copia:
                if i[0] == posc:
                    posiblesJugadas()
                    return boton(i[1],'no')
            posiblesJugadas()
            boton('','no')

    def rehacerJugadas(): #Rehace las jugadas que se hayan deshecho anteriormente
        global rehacer,jugadas,posc,listo,creado,pausado
        if listo=="No":
            return messagebox.showinfo("ERROR","EL JUGADOR NO HA DADO SU NOMBRE")
        elif creado=="No":
            return messagebox.showinfo("ERROR","NO HA INICIADO NINGUN JUEGO")
        elif pausado=="Si":
            return messagebox.showinfo("ERROR","EL JUEGO ESTA PAUSADO")
        elif rehacer == []:
            return messagebox.showinfo("ERROR","NO HAY MÁS JUGADAS POR REHACER")
        else:
            posc = rehacer[-1][0]
            numero = rehacer[-1][1]
            jugadas+=[rehacer.pop()]
            posiblesJugadas()
            return boton(numero,'no')

    def posiblesJugadas(): #Permite mostrar las posibles jugadas de una celda de la cuadricula
        global posc, juego
        operacion = 0
        cantidad = 0
        for llave in juego:
            if posc in juego[llave]:
                operacion = juego[llave][0] #Contiene la operacion, ya sea 20x, 14+...; e incluso puede ser un solo numero
                cantidad = len(juego[llave])-1 #Contiene la cantidad de celdas que se ocupan para realizar una operacion
                if cantidad==1: #En caso de que solo sea un casilla, por ende solo hay un numero
                    colocarOpciones(juego[llave][1:],[[int(operacion)]],[])
                elif cantidad==2: #Para 2 celdas
                    buenas_y_malas(posibilidades(combinaciones2(),operacion),juego[llave][1:])
                elif cantidad==3: #Para 3 celdas
                    buenas_y_malas(posibilidades(combinaciones3(),operacion),juego[llave][1:])
                elif cantidad==4: #Para 4 celdas
                    buenas_y_malas(posibilidades(combinaciones4(),operacion),juego[llave][1:])
                break

    def combinaciones2(): #Retorna todas las combinaciones para 2 casillas
        archivo=open("kenken_configuración.dat").readlines()
        size=int(archivo[3][0])
        lista=[]
        for num1 in range(1,size+1):
            for num2 in range(1,size+1):
                lista+=[[num1,num2]]
        return lista

    def combinaciones3(): #Retorna todas las combinaciones para 3 casillas
        archivo=open("kenken_configuración.dat").readlines()
        size=int(archivo[3][0])
        lista=[]
        for num1 in range(1,size+1):
            for num2 in range(1,size+1):
                for num3 in range(1,size+1):
                    lista+=[[num1,num2,num3]]
        return lista

    def combinaciones4(): #Retorna todas las combinaciones para 4 casillas
        archivo=open("kenken_configuración.dat").readlines()
        size=int(archivo[3][0])
        lista=[]
        for num1 in range(1,size+1):
            for num2 in range(1,size+1):
                for num3 in range(1,size+1):
                    for num4 in range(1,size+1):
                        lista+=[[num1,num2,num3,num4]]
        return lista

    def posibilidades(combinaciones,operacion): #Determina cuales combinaciones dan la respectiva operacion
        resultado = int(operacion[:-1]) #el número
        operador = operacion[-1]
        lista=[]
        if operador=="x":
            operador="*"
        for sublista in combinaciones:
            result=""
            copia=sublista.copy()
            copia.sort()
            copia.reverse()
            for numero in copia:
                result+=str(numero)+operador
            result=eval(result[:-1])
            if resultado==result:
                lista+=[sublista]
        return lista

    def buenas_y_malas(posibles,tuplas): #Determina cuales de las soluciones no se pueden poner en el juego, ya sea porque un numero se repite en una misma fila o colummna
        buenas=[]
        malas=[]
        for sublista in posibles:
            indice=0
            dic={}
            for numero in sublista:
                if numero in dic:
                    dic[numero]+=[tuplas[indice]]
                    indice+=1
                else:
                    dic[numero]=[tuplas[indice]]
                    indice+=1

            buena="Si"   
            for llave in dic:
                fila=dic[llave][0][0]
                columna=dic[llave][0][1]
                for tupla in dic[llave][1:]:
                    if tupla[0]==fila or tupla[1]==columna:
                        buena="No"
            if buena=="Si":
                buenas+=[sublista]
            else:
                malas+=[sublista]
                
        colocarOpciones(tuplas,buenas,malas)

    def colocarOpciones(tuplas,buenas,malas): #Coloca las combinaciones que se pueden realizar y cuales no, ademas muestra la celda seleccionada
        Label(ventana,text="Posibles Jugadas",bg="yellow",font=("Helvetica",16)).place(x=890,y=200)
        Label(ventana,text="SI",bg="lightgreen",font=("Helvetica",14)).place(x=883,y=267)
        Label(ventana,text="NO",bg="red",font=("Helvetica",14)).place(x=1027,y=267)
        LbTuplas=Listbox(ventana,width=20,heigh=1,font=("Helvetica",14))
        LbTuplas.place(x=860,y=235)
        LbTuplas.insert(END,str(list(tuplas)))
        LbBuenas=Listbox(ventana,width=8,heigh=10,font=("Helvetica",14))
        LbBuenas.place(x=850,y=300)
        for buena in buenas:
            LbBuenas.insert(END,str(buena))

        LbMalas=Listbox(ventana,width=8,heigh=10,font=("Helvetica",14))
        LbMalas.place(x=1000,y=300)
        for mala in malas:
            LbMalas.insert(END,str(mala))

    def guardarPartida(): #Guarda la partida actual
        global listo,creado,juego,jugadas,tipo
        if listo=="Si": #Verificamos que el usuario haya puesto su nombre
            if creado=="Si": #Vemos que exista un juego creado
                configuracion=open("kenken_configuración.dat").readlines()
                archivo=open("kenken_juegoactual.dat",'w')
                if hours['text']==0 and minuts['text']==0: #Caso especial
                    archivo.write(nombre.get()+"\n"+str(juego)+"\n"+str(jugadas)+'\n'+str(configuracion)+"\n"+tipo+"\n"+"000"+str(seconds['text']))
                    archivo.close()
                elif hours['text']==0:
                    if minuts['text']>9:
                        archivo.write(nombre.get()+"\n"+str(juego)+"\n"+str(jugadas)+'\n'+str(configuracion)+"\n"+tipo+"\n"+"0"+str(minuts['text']*100+seconds['text']))
                        archivo.close()
                    else:
                        archivo.write(nombre.get()+"\n"+str(juego)+"\n"+str(jugadas)+'\n'+str(configuracion)+"\n"+tipo+"\n"+"00"+str(minuts['text']*100+seconds['text']))
                        archivo.close()
                else:
                    archivo.write(nombre.get()+"\n"+str(juego)+"\n"+str(jugadas)+'\n'+str(configuracion)+"\n"+tipo+"\n"+str(hours['text']*10000+minuts['text']*100+seconds['text']))
                    archivo.close()
            else:
                return messagebox.showinfo("ERROR","NO HA INICIADO NINGUN JUEGO")
        else:
            return messagebox.showinfo("ERROR","EL JUGADOR NO HA DADO SU NOMBRE")

    def cargarJuego(): #Carga un juego guardado anteriormente
        global listo,cargado
        if listo=="Si":
            return messagebox.showinfo("ERROR","EL JUGADOR YA HA DADO SU NOMBRE")
        else:
            try: #Vemos si existe el archivo
                archivo=open("kenken_juegoactual.dat").readlines()
                cargado="Si"
                jugarKenken(ventana)
            except:
                return messagebox.showinfo("ERROR","AUN NO EXISTE UN JUEGO GUARDADO")

    def cargarJuegoAux(): #Funcion que permite cargar todos los datos guardados anteriormente en el archivo kenken_juegoactual.dat
        global listo,creado,juego,posc,tipo,pausado

        archivo=open("kenken_juegoactual.dat").readlines()
        listo="Si"
        creado="Si"
            
        tipo=archivo[4][:-1]
            
        nombre.set(archivo[0][:-1])
        guardarJugador()
        configuracion=eval(archivo[3][:-1])
        file=open('kenken_configuración.dat','w')
        try:
            file.write(configuracion[0]+configuracion[1]+configuracion[2]+configuracion[3]+configuracion[4])
        except:
            file.write(configuracion[0]+configuracion[1]+configuracion[2]+configuracion[3])
        file.close()

        labels()
                
        juego=eval(archivo[1][:-1])
        jugadas=eval(archivo[2][:-1])
                
        crear_juego_aux(juego)
        for jugada in jugadas:
            posc=jugada[0]
            boton(jugada[1],"si")

        hours['text']=int(archivo[5][:1])
        minuts['text']=int(archivo[5][1:3])
        seconds['text']=int(archivo[5][3:5])

        creado="No"

        reloj=configuracion[1]
        if reloj=="relojSi\n" or tipo=="Cronometro":
            pausado="Si"
            cortina.destroy()
            inicio=Button(ventana,text="Iniciar\nJuego",command=lambda:sacarCronometro(inicio),bg="red",font=("Helvetica",14))
            inicio.place(x=60,y=120)
        elif reloj=="timer\n" and tipo=="Timer":
            pausado="Si"
            cortina.destroy()
            inicio=Button(ventana,text="Iniciar\nJuego",command=lambda:sacarTimer(inicio),bg="red",font=("Helvetica",14))
            inicio.place(x=60,y=120)
        else:
            inicio=Button(ventana,text="Iniciar\nJuego",command=lambda:incializar(inicio),bg="red",font=("Helvetica",14))
            inicio.place(x=60,y=120)
            
    def incializar(inicio): #Solo se usa al cargar un juego guardado sin reloj o timer y poder iniciar
        global creado
        creado="Si"
        inicio.destroy()
        
    def sacarCronometro(inicio): #Solo se usa al cargar un juego guardado con reloj y poder iniciar
        global count,creado
        creado="Si"
        inicio.destroy()
        count=seconds['text']
        cronometro()

    def sacarTimer(inicio): #Solo se usa al cargar un juego guardado con timer y poder iniciar
        global count,creado
        creado="Si"
        inicio.destroy()
        count=seconds['text']
        timer()
    
    def boton(num,var): #Aca se coloca los valores cada label
        global posc,listo,creado,pausado, rehacer
        if listo=="Si": #Verificamos que el usuario haya puesto su nombre
            if creado=="Si": #Vemos que exissta un juego creado
                if pausado=="No": #Vemos que el juego no este pausado
                    if posc==():
                        return messagebox.showinfo("ERROR","PRIMERO DEBE SELECCIONAR UNA CASILLA")
                    else:
                        etiquetas={(1,1):l1,(1,2):l2,(1,3):l3,(1,4):l10,(1,5):l17,(1,6):l26,(1,7):l37,(1,8):l50,(1,9):l65,\
                        (2,1):l4,(2,2):l5,(2,3):l6,(2,4):l11,(2,5):l18,(2,6):l27,(2,7):l38,(2,8):l51,(2,9):l66,\
                        (3,1):l7,(3,2):l8,(3,3):l9,(3,4):l12,(3,5):l19,(3,6):l28,(3,7):l39,(3,8):l52,(3,9):l67,\
                        (4,1):l13,(4,2):l14,(4,3):l15,(4,4):l16,(4,5):l20,(4,6):l29,(4,7):l40,(4,8):l53,(4,9):l68,\
                        (5,1):l21,(5,2):l22,(5,3):l23,(5,4):l24,(5,5):l25,(5,6):l30,(5,7):l41,(5,8):l54,(5,9):l69,\
                        (6,1):l31,(6,2):l32,(6,3):l33,(6,4):l34,(6,5):l35,(6,6):l36,(6,7):l42,(6,8):l55,(6,9):l70,\
                        (7,1):l43,(7,2):l44,(7,3):l45,(7,4):l46,(7,5):l47,(7,6):l48,(7,7):l49,(7,8):l56,(7,9):l71,\
                        (8,1):l57,(8,2):l58,(8,3):l59,(8,4):l60,(8,5):l61,(8,6):l62,(8,7):l63,(8,8):l64,(8,9):l72,\
                        (9,1):l73,(9,2):l74,(9,3):l75,(9,4):l76,(9,5):l77,(9,6):l78,(9,7):l79,(9,8):l80,(9,9):l81}
                        if var == "si":
                            guardarJugadas(num)
                            etiquetas[posc]['text']=num #Se pone el valor en el label
                            rehacer = []
                        else:
                            etiquetas[posc]['text']=num #Se pone el valor en el label
                else:
                    return messagebox.showinfo("ERROR","EL JUEGO ESTA PAUSADO")
            else:
                return messagebox.showinfo("ERROR","NO HA INICIADO NINGUN JUEGO")
        else:
            return messagebox.showinfo("ERROR","EL JUGADOR NO HA DADO SU NOMBRE")
    
    if cargado=="No":
        labels() #Funcion que retorna una cuadricula nxn
    else:
        cargado="No"
        cargarJuegoAux()
        
    mainloop()

def configuracion(ventana): #Ventana de la configuracion, recibe la ventana del menu
    ventana.destroy() #Se destruye la ventana del menu
    config = Tk()
    config.title("Configuracion")
    config.geometry('850x600')
    config.resizable(False,False)
    config.config(bg="CadetBlue")

    def guardar(): #Se guarda la informacion
        try:
            file=open('kenken_configuración.dat').readlines()
        except:
            pass
        archivo=open('kenken_configuración.dat','w')
        try:
            archivo.write(opcionDificultad.get()+opcionReloj.get()+opcionSonido.get()+opcionSize.get()+file[4])
        except:
            archivo.write(opcionDificultad.get()+opcionReloj.get()+opcionSonido.get()+opcionSize.get())
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
                archivo.write(opcionDificultad.get()+opcionReloj.get()+opcionSonido.get()+opcionSize.get()+"000"+str(segundos))
                archivo.close()
            elif horas==0: #Caso especial
                if minutos>9:
                    archivo=open('kenken_configuración.dat','w')
                    archivo.write(opcionDificultad.get()+opcionReloj.get()+opcionSonido.get()+opcionSize.get()+"0"+str(minutos*100+segundos))
                    archivo.close()
                else:
                    archivo=open('kenken_configuración.dat','w')
                    archivo.write(opcionDificultad.get()+opcionReloj.get()+opcionSonido.get()+opcionSize.get()+"00"+str(minutos*100+segundos))
                    archivo.close()
            else:
                archivo=open('kenken_configuración.dat','w')
                archivo.write(opcionDificultad.get()+opcionReloj.get()+opcionSonido.get()+opcionSize.get()+str(horas*10000+minutos*100+segundos))
                archivo.close()
        except: #Mensaje de error ya que los elementos no eran numeros
            messagebox.showinfo("ERROR","LOS VALORES DEL TIMER DEBEN SER NUMEROS ENTEROS")

    def verCronometro(): #Se usa para timer
        archivo=open("kenken_configuración.dat").readlines()
        if archivo[1]=="timer\n" and archivo[3][1]!="M":
            try: #Vemos si ya habia un tiempo configurado
                h.set(int(archivo[4][:1]))
                m.set(int(archivo[4][1:3]))
                s.set(int(archivo[4][3:5]))
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
    opcionSize = StringVar() #Medida de la cuadricula
    
    guardado=open("kenken_configuración.dat").readlines() #Se obtiene una lista con los datos guardados de la configuracion
    opcionDificultad.set(guardado[0])
    opcionReloj.set(guardado[1])
    opcionSonido.set(guardado[2])
    opcionSize.set(guardado[3])
    verCronometro()        

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
    #Tamaño de la cuadricula
    Label(config, text = "4. Definir tamaño de la cuadricula",bg="lightgreen",font=("Helvetica",12)).place(x=500,y= 50)
    Radiobutton(config,text="3x3",bg="CadetBlue",variable = opcionSize, value = "3\n",command = guardar,font=("Helvetica",11)).place(x=500,y=100)
    Radiobutton(config,text="4x4",bg="CadetBlue",variable = opcionSize, value = "4\n",command = guardar,font=("Helvetica",11)).place(x=500,y=150)
    Radiobutton(config,text="5x5",bg="CadetBlue",variable = opcionSize, value = "5\n",command = guardar,font=("Helvetica",11)).place(x=500,y=200)
    Radiobutton(config,text="6x6",bg="CadetBlue",variable = opcionSize, value = "6\n",command = guardar,font=("Helvetica",11)).place(x=500,y=250)
    Radiobutton(config,text="7x7",bg="CadetBlue",variable = opcionSize, value = "7\n",command = guardar,font=("Helvetica",11)).place(x=500,y=300)
    Radiobutton(config,text="8x8",bg="CadetBlue",variable = opcionSize, value = "8\n",command = guardar,font=("Helvetica",11)).place(x=500,y=350)
    Radiobutton(config,text="9x9",bg="CadetBlue",variable = opcionSize, value = "9\n",command = guardar,font=("Helvetica",11)).place(x=500,y=400)
    Radiobutton(config,text="Multitamaño",bg="CadetBlue",variable = opcionSize, value = "3M\n",command = guardar,font=("Helvetica",11)).place(x=500,y=450)

    regresar=Button(config,text="Regresar",command=lambda:menu("Si",config),bg="lightgreen",font=("Helvetica",12)).place(x=20,y=550)

    mainloop()


def menu(opcion,window): #Recibe Si para eliminar la ventana de configuracion o de jugarKenken
    if opcion=="Si": #Se usa para destruir la ventana anterior
        window.destroy()
    ventana= Tk()
    ventana.title("Menu")
    ventana.geometry("590x200")
    ventana.resizable(False,False)
    ventana.config(bg="CadetBlue")

    try:
        guardado=open("kenken_configuración.dat").readlines() #Se obtiene una lista con los datos guardados de la configuracion
        if guardado[3][1]=="M":
            archivo=open('kenken_configuración.dat','w')
            try:
                archivo.write(guardado[0]+guardado[1]+guardado[2]+"3M\n"+guardado[4])
                archivo.close()
            except:
                archivo.write(guardado[0]+guardado[1]+guardado[2]+"3M\n")
                archivo.close()
    except:
        archivo=open('kenken_configuración.dat','w')
        archivo.write("F\n"+"relojSi\n"+"sonidoNo\n"+"6\n")
        archivo.close()

    #Boton de jugar
    jugar=Button(ventana,text="Jugar",command=lambda:jugarKenken(ventana),bg="white",font=("Helvetica",14)).place(x=40,y=80)

    #Boton para configurar el juego
    config=Button(ventana,text="Configurar",command=lambda:configuracion(ventana),bg="white",font=("Helvetica",14)).place(x=130,y=80)

    #Despliega una ventana con el manual de usuario 
    helps=Button(ventana,text="Ayuda",command=lambda:os.startfile("manual_de_usuario_kenken.pdf"),bg="white",font=("Helvetica",14)).place(x=262,y=80)

    #Permite conocer un poco sobre la tarea
    acerca=Button(ventana,text="Acerca de",command=lambda:messagebox.showinfo("Acerca de","Nombre del programa: Kenken \nVersión: 2.0 \nCreacion: 29/10/2018 \nAutores: Mariela Murillo Artavia\n                Mauricio Gamboa Godínez"),bg="white",font=("Helvetica",14))
    acerca.place(x=360,y=80)

    #Boton salir
    salir=Button(ventana,text="Salir",command=lambda:ventana.destroy(),bg="white",font=("Helvetica",14)).place(x=495,y=80)

    mainloop()

menu("No",0) #Se llama a la funcion para iniciar la ejecucion
