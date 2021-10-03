# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 09:05:22 2021

@author: juanp
"""


from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import SeccionICHA



H = 2.*m_
B = 4.*m_

#Inicializar modelo
ret = Reticulado()

#nodo 7

x0 = 5.075777986710320100e+00*m_
y0 = 4.281724747887941618e+01*m_


L_total = 117.48*m_
L = L_total/28



#Nodos
ret.agregar_nodo(x0 ,0, y0)         # 0
ret.agregar_nodo(x0 + 1*L,0, y0)    # 1 
ret.agregar_nodo(x0+2*L ,0, y0)     # 2
ret.agregar_nodo(x0+3*L ,0, y0)     # 3 
ret.agregar_nodo(x0+4*L ,0, y0)    # 4 
ret.agregar_nodo(x0+5*L ,0, y0)     # 5 
ret.agregar_nodo(x0+6*L ,0, y0)     # 6 
ret.agregar_nodo(x0+7*L ,0, y0)      # 7 
ret.agregar_nodo(x0+8*L ,0, y0)     # 8 
ret.agregar_nodo(x0+9*L ,0, y0)    # 9 
ret.agregar_nodo(x0+10*L ,0, y0)     # 10 
ret.agregar_nodo(x0+11*L ,0, y0)     # 11
ret.agregar_nodo(x0+12*L ,0, y0)     # 12
ret.agregar_nodo(x0+13*L ,0, y0)    # 13 
ret.agregar_nodo(x0+14*L ,0, y0)     # 14 
ret.agregar_nodo(x0+15*L ,0, y0)    # 15 
ret.agregar_nodo(x0+16*L ,0, y0)     # 16 
ret.agregar_nodo(x0+17*L ,0, y0)     # 17 
ret.agregar_nodo(x0+18*L ,0, y0)     # 18 
ret.agregar_nodo(x0+19*L ,0, y0)     # 19 
ret.agregar_nodo(x0+20*L ,0, y0)  # 20 
ret.agregar_nodo(x0+21*L ,0, y0)  #21
ret.agregar_nodo(x0+22*L ,0, y0)  #22
ret.agregar_nodo(x0+23*L ,0, y0)  #23
ret.agregar_nodo(x0+24*L ,0, y0)  #24
ret.agregar_nodo(x0+25*L ,0, y0)  #25
ret.agregar_nodo(x0+26*L ,0, y0)  #26
ret.agregar_nodo(x0+27*L ,0, y0)  #27
ret.agregar_nodo(x0+28*L ,0, y0)  #28
ret.agregar_nodo(x0+29*L ,0, y0)  #29


ret.agregar_nodo(x0 ,0, y0+L)         # 29
ret.agregar_nodo(x0 + 1*L,0, y0+L)    # 30
ret.agregar_nodo(x0+2*L ,0, y0+L)     # 31
ret.agregar_nodo(x0+3*L ,0, y0+L)     # 32
ret.agregar_nodo(x0+4*L ,0, y0+L)    # 33
ret.agregar_nodo(x0+5*L ,0, y0+L)     # 34 
ret.agregar_nodo(x0+6*L ,0, y0+L)     # 35
ret.agregar_nodo(x0+7*L ,0, y0+L)      # 36 
ret.agregar_nodo(x0+8*L ,0, y0+L)     # 37
ret.agregar_nodo(x0+9*L ,0, y0+L)    # 38
ret.agregar_nodo(x0+10*L ,0, y0+L)     # 39 
ret.agregar_nodo(x0+11*L ,0, y0+L)     # 40
ret.agregar_nodo(x0+12*L ,0, y0+L)     # 41
ret.agregar_nodo(x0+13*L ,0, y0+L)    # 42      
ret.agregar_nodo(x0+14*L ,0, y0+L)     # 43 
ret.agregar_nodo(x0+15*L ,0, y0+L)    # 44 
ret.agregar_nodo(x0+16*L ,0, y0+L)     # 45 
ret.agregar_nodo(x0+17*L ,0, y0+L)     # 46 
ret.agregar_nodo(x0+18*L ,0, y0+L)     # 47 
ret.agregar_nodo(x0+19*L ,0, y0+L)     # 48 
ret.agregar_nodo(x0+20*L ,0, y0+L)  # 49 
ret.agregar_nodo(x0+21*L ,0, y0+L)  #50
ret.agregar_nodo(x0+22*L ,0, y0+L)  #51
ret.agregar_nodo(x0+23*L ,0, y0+L)  #52
ret.agregar_nodo(x0+24*L ,0, y0+L)  #53
ret.agregar_nodo(x0+25*L ,0, y0+L)  #54
ret.agregar_nodo(x0+26*L ,0, y0+L)  #55
ret.agregar_nodo(x0+27*L ,0, y0+L)  #56
ret.agregar_nodo(x0+28*L ,0, y0+L)  #57
ret.agregar_nodo(x0+29*L ,0, y0+L)  ###59

ret.agregar_nodo(x0 ,H, y0)         # 60
ret.agregar_nodo(x0 + 1*L,H, y0)    # 61
ret.agregar_nodo(x0+2*L ,H, y0)     # 60
ret.agregar_nodo(x0+3*L ,H, y0)     # 62
ret.agregar_nodo(x0+4*L ,H, y0)    # 63
ret.agregar_nodo(x0+5*L ,H, y0)     # 64 
ret.agregar_nodo(x0+6*L ,H, y0)     # 65
ret.agregar_nodo(x0+7*L ,H, y0)      # 66 
ret.agregar_nodo(x0+8*L ,H, y0)     # 67
ret.agregar_nodo(x0+9*L ,H, y0)    # 68
ret.agregar_nodo(x0+10*L ,H, y0)     #69            
ret.agregar_nodo(x0+11*L ,H, y0)     # 70
ret.agregar_nodo(x0+12*L ,H, y0)     # 71
ret.agregar_nodo(x0+13*L ,H, y0)    # 72
ret.agregar_nodo(x0+14*L ,H, y0)     # 73 
ret.agregar_nodo(x0+15*L ,H, y0)    # 74
ret.agregar_nodo(x0+16*L ,H, y0)     # 75 
ret.agregar_nodo(x0+17*L ,H, y0)     # 76
ret.agregar_nodo(x0+18*L ,H, y0)     # 77 
ret.agregar_nodo(x0+19*L ,H, y0)     # 78 
ret.agregar_nodo(x0+20*L ,H, y0)  # 79
ret.agregar_nodo(x0+21*L ,H, y0)  #80
ret.agregar_nodo(x0+22*L ,H, y0)  #81
ret.agregar_nodo(x0+23*L ,H, y0)  #82
ret.agregar_nodo(x0+24*L ,H, y0)  #83
ret.agregar_nodo(x0+25*L ,H, y0)  #84
ret.agregar_nodo(x0+26*L ,H, y0)  #85
ret.agregar_nodo(x0+27*L ,H, y0)  #86
ret.agregar_nodo(x0+28*L ,H, y0)  #87
ret.agregar_nodo(x0+29*L ,H, y0) #88


ret.agregar_nodo(x0 ,H, y0+L)         # 89
ret.agregar_nodo(x0 + 1*L,H, y0+L)    # 90
ret.agregar_nodo(x0+2*L ,H, y0+L)     # 91
ret.agregar_nodo(x0+3*L ,H, y0+L)     # 92
ret.agregar_nodo(x0+4*L ,H, y0+L)    # 93
ret.agregar_nodo(x0+5*L ,H, y0+L)     # 94 
ret.agregar_nodo(x0+6*L ,H, y0+L)     # 95
ret.agregar_nodo(x0+7*L ,H, y0+L)      # 96 
ret.agregar_nodo(x0+8*L ,H, y0+L)     # 97
ret.agregar_nodo(x0+9*L ,H, y0+L)    # 98      ####### +3
ret.agregar_nodo(x0+10*L ,H, y0+L)     # 99 
ret.agregar_nodo(x0+11*L ,H, y0+L)     # 100
ret.agregar_nodo(x0+12*L ,H, y0+L)     # 101
ret.agregar_nodo(x0+13*L ,H, y0+L)    # 102
ret.agregar_nodo(x0+14*L ,H, y0+L)     # 103 
ret.agregar_nodo(x0+15*L ,H, y0+L)    # 104
ret.agregar_nodo(x0+16*L ,H, y0+L)     # 105 
ret.agregar_nodo(x0+17*L ,H, y0+L)     # 106
ret.agregar_nodo(x0+18*L ,H, y0+L)     # 107
ret.agregar_nodo(x0+19*L ,H, y0+L)     # 108
ret.agregar_nodo(x0+20*L ,H, y0+L)  # 109
ret.agregar_nodo(x0+21*L ,H, y0+L)  #110
ret.agregar_nodo(x0+22*L ,H, y0+L)  #111
ret.agregar_nodo(x0+23*L ,H, y0+L)  #112
ret.agregar_nodo(x0+24*L ,H, y0+L)  #113
ret.agregar_nodo(x0+25*L ,H, y0+L)  #114
ret.agregar_nodo(x0+26*L ,H, y0+L)  #115
ret.agregar_nodo(x0+27*L ,H, y0+L)  #116
ret.agregar_nodo(x0+28*L ,H, y0+L)  #117
ret.agregar_nodo(x0+29*L ,H, y0+L)  ##### 118



#Secciones de las barras

seccion_grande = SeccionICHA("H500x250x84.6", color="#3A8431")#, debug=True)
seccion_mediana = SeccionICHA("H450x250x123.2", color="#A3500B")
seccion_chica = SeccionICHA("H450x150x63.2", color="#A3500B")

seccion_ultra_chica = SeccionICHA("[]200x200x24.2", color="#A3500B")
seccion_casimuy_chica = SeccionICHA("[]15x15x0.4", color="#A3500B")
seccion_mega_chica = SeccionICHA("[]12x12x0.3", color="#A3500B")
h=0
hh=30

for nodos in range(30,60): #Arriba eje z y diagonales arriba
    ret.agregar_barra(Barra(nodos,nodos+60,seccion_mega_chica))
    if nodos != 59:
       ret.agregar_barra(Barra(nodos, nodos+61, seccion_mega_chica))





for x in range(30):             #Verticales izq
    ret.agregar_barra(Barra(h, hh, seccion_ultra_chica)) 
    h+=1
    hh+=1              
h=60
hh=90

for x in range(30):           #Dig izq creo
    ret.agregar_barra(Barra(h, hh, seccion_ultra_chica)) 
    h+=1
    hh+=1

h=0
hh=31

for x in range(14):             ##diag derecha
    ret.agregar_barra(Barra(h, hh, seccion_ultra_chica))
    h+=2
    ret.agregar_barra(Barra(h, hh, seccion_ultra_chica))
    hh+=2
ret.agregar_barra(Barra(59, 28, seccion_ultra_chica))
h=60
hh=91

for x in range(14):                         #Diag izq
    ret.agregar_barra(Barra(h, hh, seccion_ultra_chica))
    h+=2
    ret.agregar_barra(Barra(h, hh, seccion_ultra_chica))
    hh+=2
ret.agregar_barra(Barra(119, 88, seccion_ultra_chica))




h=0

for x in range(28):              #   #Longitudinal abajo  der
    ret.agregar_barra(Barra(h, h+1, seccion_chica))
    h+=1
ret.agregar_barra(Barra(28, 29, seccion_grande))
h=30

for x in range(29):                                      #Longitudinal arriba der
    ret.agregar_barra(Barra(h, h+1, seccion_mediana))
    h+=1

h=60

for x in range(28):                                 #Longitudinal abajo izq
    ret.agregar_barra(Barra(h, h+1, seccion_chica))
    h+=1
ret.agregar_barra(Barra(88, 89, seccion_grande))    
h=90

for x in range(29):                                      #Longitudinal arriba izq
    ret.agregar_barra(Barra(h, h+1, seccion_mediana))
    h+=1

h=0
hh=60

for x in range(30):
    ret.agregar_barra(Barra(h, hh, seccion_casimuy_chica))
    h+=1
    
    hh+=1
    
h=0
hh=60

for x in range(30):
    ret.agregar_barra(Barra(h, hh, seccion_casimuy_chica))
    h+=1
    
    hh+=1
h=0
hh=61

for x in range(29):                                    #Cruz abajo
    ret.agregar_barra(Barra(h, hh, seccion_mega_chica))
    h+=1
    
    hh+=1

h=1
hh=60

for x in range(29):#Cruz abajo
    ret.agregar_barra(Barra(h, hh, seccion_mega_chica))
    h+=1
    
    hh+=1
    
    
    


    


#Crear restricciones
for nodo in [0,60]:
	ret.agregar_restriccion(nodo, 0, 0)
	ret.agregar_restriccion(nodo, 1, 0)
	ret.agregar_restriccion(nodo, 2, 0)

for nodo in [89,29]:
    ret.agregar_restriccion(nodo, 0, 0)
    ret.agregar_restriccion(nodo, 1, 0)
    ret.agregar_restriccion(nodo, 2, 0)




#Visualizar y comprobar las secciones
opciones_barras = {
	# "ver_secciones_en_barras": True,
    "ver_numeros_de_barras" : False,
	"color_barras_por_seccion": True,
}
ver_reticulado_3d(ret,opciones_barras=opciones_barras)

# exit(0)



#Resolver el problema peso_propio
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,-1.], factor_cargas=0.0)
ret.resolver_sistema()
f_D = ret.obtener_fuerzas()


#Agregar fuerzas tablero

F1=400*4*(117.48/28)*9.81
F2=F1/4

ret.agregar_fuerza(88, 2, -F2)
ret.agregar_fuerza(60, 2, -F2)
ret.agregar_fuerza(29, 2, -F2)
ret.agregar_fuerza(0, 2, -F2)


for nodo in range(1,29):
	ret.agregar_fuerza(nodo, 2, -2*F2)
	


for nodo in range(61,87):
	ret.agregar_fuerza(nodo, 2, -2*F2)
	
   

#Resolver el problema peso_propio
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,0], factor_cargas=1.0)
ret.resolver_sistema()
f_L = ret.obtener_fuerzas()



#Visualizar f_L en el reticulado
opciones_nodos = {
	"usar_posicion_deformada": False,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":f_L
}

ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="Carga Viva")


#Visualizar f_L en el reticulado
opciones_nodos = {
	"usar_posicion_deformada": False,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":f_D
}

ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="Carga Muerta")


#Calcular carga ultima (con factores de mayoracion)
fu = 1.2*f_D + 1.6*f_L



#Visualizar combinacion en el reticulado
opciones_nodos = {
	"usar_posicion_deformada": False,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":fu
}

ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="1.2D + 1.6L")





cumple = ret.chequear_diseño(fu, ϕ=0.9)

if cumple:
	print(":)  El reticulado cumple todos los requisitos")
else:
	print(":(  El reticulado NO cumple todos los requisitos")

#Calcular factor de utilizacion para las barras
factores_de_utilizacion = ret.obtener_factores_de_utilizacion(fu, ϕ=0.9)


#Visualizar FU en el reticulado
opciones_nodos = {
	"usar_posicion_deformada": False,
	# "factor_amplificacion_deformada": 1.,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":factores_de_utilizacion
}


ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="Factor Utilizacion")


ret.guardar("05_ejemplo_chequear_diseño.h5")