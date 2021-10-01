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
ret.agregar_nodo(x0+13*L ,0, y0+L)    # 42      ######### +1 todos los nodos
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

ret.agregar_nodo(x0 ,H, y0)         # 58
ret.agregar_nodo(x0 + 1*L,H, y0)    # 59
ret.agregar_nodo(x0+2*L ,H, y0)     # 60
ret.agregar_nodo(x0+3*L ,H, y0)     # 61
ret.agregar_nodo(x0+4*L ,H, y0)    # 62
ret.agregar_nodo(x0+5*L ,H, y0)     # 63 
ret.agregar_nodo(x0+6*L ,H, y0)     # 64
ret.agregar_nodo(x0+7*L ,H, y0)      # 65 
ret.agregar_nodo(x0+8*L ,H, y0)     # 66
ret.agregar_nodo(x0+9*L ,H, y0)    # 67
ret.agregar_nodo(x0+10*L ,H, y0)     #68              ########### +2 todos los nodos
ret.agregar_nodo(x0+11*L ,H, y0)     # 69
ret.agregar_nodo(x0+12*L ,H, y0)     # 70
ret.agregar_nodo(x0+13*L ,H, y0)    # 71 
ret.agregar_nodo(x0+14*L ,H, y0)     # 72 
ret.agregar_nodo(x0+15*L ,H, y0)    # 73
ret.agregar_nodo(x0+16*L ,H, y0)     # 74 
ret.agregar_nodo(x0+17*L ,H, y0)     # 75
ret.agregar_nodo(x0+18*L ,H, y0)     # 76 
ret.agregar_nodo(x0+20*L ,H, y0)  # 77 
ret.agregar_nodo(x0+21*L ,H, y0)  #78
ret.agregar_nodo(x0+22*L ,H, y0)  #79
ret.agregar_nodo(x0+23*L ,H, y0)  #80
ret.agregar_nodo(x0+24*L ,H, y0)  #81
ret.agregar_nodo(x0+25*L ,H, y0)  #82
ret.agregar_nodo(x0+26*L ,H, y0)  #83
ret.agregar_nodo(x0+27*L ,H, y0)  #84
ret.agregar_nodo(x0+28*L ,H, y0)  #85
ret.agregar_nodo(x0+29*L ,H, y0) #88


ret.agregar_nodo(x0 ,H, y0+L)         # 86
ret.agregar_nodo(x0 + 1*L,H, y0+L)    # 87
ret.agregar_nodo(x0+2*L ,H, y0+L)     # 88
ret.agregar_nodo(x0+3*L ,H, y0+L)     # 89
ret.agregar_nodo(x0+4*L ,H, y0+L)    # 90
ret.agregar_nodo(x0+5*L ,H, y0+L)     # 91 
ret.agregar_nodo(x0+6*L ,H, y0+L)     # 92
ret.agregar_nodo(x0+7*L ,H, y0+L)      # 93 
ret.agregar_nodo(x0+8*L ,H, y0+L)     # 94 
ret.agregar_nodo(x0+9*L ,H, y0+L)    # 95       ####### +3
ret.agregar_nodo(x0+10*L ,H, y0+L)     # 96 
ret.agregar_nodo(x0+11*L ,H, y0+L)     # 97
ret.agregar_nodo(x0+12*L ,H, y0+L)     # 98
ret.agregar_nodo(x0+13*L ,H, y0+L)    # 99
ret.agregar_nodo(x0+14*L ,H, y0+L)     # 100 
ret.agregar_nodo(x0+15*L ,H, y0+L)    # 101
ret.agregar_nodo(x0+16*L ,H, y0+L)     # 102 
ret.agregar_nodo(x0+17*L ,H, y0+L)     # 103
ret.agregar_nodo(x0+18*L ,H, y0+L)     # 104
ret.agregar_nodo(x0+20*L ,H, y0+L)  # 105
ret.agregar_nodo(x0+21*L ,H, y0+L)  #106
ret.agregar_nodo(x0+22*L ,H, y0+L)  #107
ret.agregar_nodo(x0+23*L ,H, y0+L)  #108
ret.agregar_nodo(x0+24*L ,H, y0+L)  #109
ret.agregar_nodo(x0+25*L ,H, y0+L)  #110
ret.agregar_nodo(x0+26*L ,H, y0+L)  #111
ret.agregar_nodo(x0+27*L ,H, y0+L)  #112
ret.agregar_nodo(x0+28*L ,H, y0+L)  #113
ret.agregar_nodo(x0+29*L ,H, y0+L)  ##### 117



#Secciones de las barras

seccion_grande = SeccionICHA("[]350x150x37.8", color="#3A8431")#, debug=True)
seccion_chica = SeccionICHA("[]80x40x8", color="#A3500B")


#Crear y agregar las barras
#Crear y agregar las barras
ret.agregar_barra(Barra(0, 1, seccion_chica))   #0
ret.agregar_barra(Barra(1, 2, seccion_chica))   #1
ret.agregar_barra(Barra(2, 3, seccion_chica))   #2
ret.agregar_barra(Barra(3, 4, seccion_chica))   #3
ret.agregar_barra(Barra(4, 5, seccion_chica))   #4
ret.agregar_barra(Barra(5, 6, seccion_chica))   #5
ret.agregar_barra(Barra(6, 7, seccion_chica))   #6
ret.agregar_barra(Barra(7, 8, seccion_chica))   #7
ret.agregar_barra(Barra(8, 9, seccion_chica))   #8
ret.agregar_barra(Barra(9, 10, seccion_chica))  #9
ret.agregar_barra(Barra(10, 11, seccion_chica)) #10
ret.agregar_barra(Barra(11, 12, seccion_chica)) #11
ret.agregar_barra(Barra(12, 13, seccion_chica)) #12
ret.agregar_barra(Barra(13, 14, seccion_chica)) #13
ret.agregar_barra(Barra(14, 15, seccion_chica)) #14
ret.agregar_barra(Barra(15, 16, seccion_chica)) #15
ret.agregar_barra(Barra(16, 17, seccion_chica)) #16
ret.agregar_barra(Barra(17, 18, seccion_chica)) #17
ret.agregar_barra(Barra(18, 19, seccion_chica)) #18
ret.agregar_barra(Barra(19, 20, seccion_chica)) #19


ret.agregar_barra(Barra(21, 22, seccion_chica)) #20
ret.agregar_barra(Barra(22, 23, seccion_chica)) #21
ret.agregar_barra(Barra(23, 24, seccion_chica)) #22
ret.agregar_barra(Barra(24, 25, seccion_chica)) #23
ret.agregar_barra(Barra(25, 26, seccion_chica)) #24
ret.agregar_barra(Barra(26, 27, seccion_chica)) #25
ret.agregar_barra(Barra(27, 28, seccion_chica)) #26
ret.agregar_barra(Barra(28, 29, seccion_chica)) #27
ret.agregar_barra(Barra(29, 30, seccion_chica)) #28
ret.agregar_barra(Barra(30, 31, seccion_chica)) #29
ret.agregar_barra(Barra(31, 32, seccion_chica)) #30
ret.agregar_barra(Barra(32, 33, seccion_chica)) #31
ret.agregar_barra(Barra(33, 34, seccion_chica)) #32
ret.agregar_barra(Barra(34, 35, seccion_chica)) #33
ret.agregar_barra(Barra(35, 36, seccion_chica)) #34
ret.agregar_barra(Barra(36, 37, seccion_chica)) #35
ret.agregar_barra(Barra(37, 38, seccion_chica)) #36
ret.agregar_barra(Barra(38, 39, seccion_chica)) #37
ret.agregar_barra(Barra(39, 40, seccion_chica)) #38
ret.agregar_barra(Barra(40, 41, seccion_chica)) #39


# triangulos


ret.agregar_barra(Barra(0, 22, seccion_chica)) #39
ret.agregar_barra(Barra(2, 24, seccion_chica)) #39
ret.agregar_barra(Barra(4, 26, seccion_chica)) #39
ret.agregar_barra(Barra(6, 28, seccion_chica)) #39
ret.agregar_barra(Barra(8, 30, seccion_chica)) #39
ret.agregar_barra(Barra(10, 32, seccion_chica)) #39
ret.agregar_barra(Barra(12, 34, seccion_chica)) #39
ret.agregar_barra(Barra(14, 36, seccion_chica)) #39
ret.agregar_barra(Barra(16, 38, seccion_chica)) #39
ret.agregar_barra(Barra(18, 40, seccion_chica)) #39
ret.agregar_barra(Barra(22, 2, seccion_chica)) #39
ret.agregar_barra(Barra(24, 4, seccion_chica)) #39
ret.agregar_barra(Barra(26, 6, seccion_chica)) #39
ret.agregar_barra(Barra(28, 8, seccion_chica)) #39
ret.agregar_barra(Barra(30, 10, seccion_chica)) #39
ret.agregar_barra(Barra(32, 12, seccion_chica)) #39
ret.agregar_barra(Barra(34, 14, seccion_chica)) #39
ret.agregar_barra(Barra(36, 16, seccion_chica)) #39
ret.agregar_barra(Barra(38, 18, seccion_chica)) #39
ret.agregar_barra(Barra(40, 20, seccion_chica)) #39

# verticales

ret.agregar_barra(Barra(0, 21, seccion_chica))   #0
ret.agregar_barra(Barra(1, 22, seccion_chica))   #1
ret.agregar_barra(Barra(2, 23, seccion_chica))   #2
ret.agregar_barra(Barra(3, 24, seccion_chica))   #3
ret.agregar_barra(Barra(4, 25, seccion_chica))   #4
ret.agregar_barra(Barra(5, 26, seccion_chica))   #5
ret.agregar_barra(Barra(6, 27, seccion_chica))   #6
ret.agregar_barra(Barra(7, 28, seccion_chica))   #7
ret.agregar_barra(Barra(8, 29, seccion_chica))   #8
ret.agregar_barra(Barra(9, 30, seccion_chica))  #9
ret.agregar_barra(Barra(10, 31, seccion_chica)) #10
ret.agregar_barra(Barra(11, 32, seccion_chica)) #11
ret.agregar_barra(Barra(12, 33, seccion_chica)) #12
ret.agregar_barra(Barra(13, 34, seccion_chica)) #13
ret.agregar_barra(Barra(14, 35, seccion_chica)) #14
ret.agregar_barra(Barra(15, 36, seccion_chica)) #15
ret.agregar_barra(Barra(16, 37, seccion_chica)) #16
ret.agregar_barra(Barra(17, 38, seccion_chica)) #17
ret.agregar_barra(Barra(18, 39, seccion_chica)) #18
ret.agregar_barra(Barra(19, 40, seccion_chica)) #19
ret.agregar_barra(Barra(20, 41, seccion_chica)) #19


## otro marco ##

ret.agregar_barra(Barra(42, 43, seccion_chica)) #20
ret.agregar_barra(Barra(43, 44, seccion_chica)) #21
ret.agregar_barra(Barra(44, 45, seccion_chica)) #22
ret.agregar_barra(Barra(45, 46, seccion_chica)) #23
ret.agregar_barra(Barra(46, 47, seccion_chica)) #24
ret.agregar_barra(Barra(47, 48, seccion_chica)) #25
ret.agregar_barra(Barra(48, 49, seccion_chica)) #26
ret.agregar_barra(Barra(49, 50, seccion_chica)) #27
ret.agregar_barra(Barra(50, 51, seccion_chica)) #28
ret.agregar_barra(Barra(51, 52, seccion_chica)) #29
ret.agregar_barra(Barra(52, 53, seccion_chica)) #30
ret.agregar_barra(Barra(53, 54, seccion_chica)) #31
ret.agregar_barra(Barra(54, 55, seccion_chica)) #32
ret.agregar_barra(Barra(55, 56, seccion_chica)) #33
ret.agregar_barra(Barra(56, 57, seccion_chica)) #34
ret.agregar_barra(Barra(57, 58, seccion_chica)) #35
ret.agregar_barra(Barra(58, 59, seccion_chica)) #36
ret.agregar_barra(Barra(59, 60, seccion_chica)) #37
ret.agregar_barra(Barra(60, 61, seccion_chica)) #38
ret.agregar_barra(Barra(61, 62, seccion_chica)) #39


ret.agregar_barra(Barra(63, 64, seccion_chica)) #20
ret.agregar_barra(Barra(64, 65, seccion_chica)) #21
ret.agregar_barra(Barra(65, 66, seccion_chica)) #22
ret.agregar_barra(Barra(66, 67, seccion_chica)) #23
ret.agregar_barra(Barra(67, 68, seccion_chica)) #24
ret.agregar_barra(Barra(68, 69, seccion_chica)) #25
ret.agregar_barra(Barra(69, 70, seccion_chica)) #26
ret.agregar_barra(Barra(70, 71, seccion_chica)) #27
ret.agregar_barra(Barra(71, 72, seccion_chica)) #28
ret.agregar_barra(Barra(72, 73, seccion_chica)) #29
ret.agregar_barra(Barra(73, 74, seccion_chica)) #30
ret.agregar_barra(Barra(74, 75, seccion_chica)) #31
ret.agregar_barra(Barra(75, 76, seccion_chica)) #32
ret.agregar_barra(Barra(76, 77, seccion_chica)) #33
ret.agregar_barra(Barra(77, 78, seccion_chica)) #34
ret.agregar_barra(Barra(78, 79, seccion_chica)) #35
ret.agregar_barra(Barra(79, 80, seccion_chica)) #36
ret.agregar_barra(Barra(80, 81, seccion_chica)) #37
ret.agregar_barra(Barra(81, 82, seccion_chica)) #38
ret.agregar_barra(Barra(82, 83, seccion_chica)) #39


# triangulos


ret.agregar_barra(Barra(42, 64, seccion_chica)) #39
ret.agregar_barra(Barra(44, 66, seccion_chica)) #39
ret.agregar_barra(Barra(46, 68, seccion_chica)) #39
ret.agregar_barra(Barra(48, 70, seccion_chica)) #39
ret.agregar_barra(Barra(50, 72, seccion_chica)) #39
ret.agregar_barra(Barra(52, 74, seccion_chica)) #39
ret.agregar_barra(Barra(54, 76, seccion_chica)) #39
ret.agregar_barra(Barra(56, 78, seccion_chica)) #39
ret.agregar_barra(Barra(58, 80, seccion_chica)) #39
ret.agregar_barra(Barra(60, 82, seccion_chica)) #39
ret.agregar_barra(Barra(64, 44, seccion_chica)) #39
ret.agregar_barra(Barra(66, 46, seccion_chica)) #39
ret.agregar_barra(Barra(68, 48, seccion_chica)) #39
ret.agregar_barra(Barra(70, 50, seccion_chica)) #39
ret.agregar_barra(Barra(72, 52, seccion_chica)) #39
ret.agregar_barra(Barra(74, 54, seccion_chica)) #39
ret.agregar_barra(Barra(76, 56, seccion_chica)) #39
ret.agregar_barra(Barra(78, 58, seccion_chica)) #39
ret.agregar_barra(Barra(80, 60, seccion_chica)) #39
ret.agregar_barra(Barra(82, 62, seccion_chica)) #39



# verticales

ret.agregar_barra(Barra(42, 63, seccion_chica)) #20
ret.agregar_barra(Barra(43, 64, seccion_chica)) #21
ret.agregar_barra(Barra(44, 65, seccion_chica)) #22
ret.agregar_barra(Barra(45, 66, seccion_chica)) #23
ret.agregar_barra(Barra(46, 67, seccion_chica)) #24
ret.agregar_barra(Barra(47, 68, seccion_chica)) #25
ret.agregar_barra(Barra(48, 69, seccion_chica)) #26
ret.agregar_barra(Barra(49, 70, seccion_chica)) #27
ret.agregar_barra(Barra(50, 71, seccion_chica)) #28
ret.agregar_barra(Barra(51, 72, seccion_chica)) #29
ret.agregar_barra(Barra(52, 73, seccion_chica)) #30
ret.agregar_barra(Barra(53, 74, seccion_chica)) #31
ret.agregar_barra(Barra(54, 75, seccion_chica)) #32
ret.agregar_barra(Barra(55, 76, seccion_chica)) #33
ret.agregar_barra(Barra(56, 77, seccion_chica)) #34
ret.agregar_barra(Barra(57, 78, seccion_chica)) #35
ret.agregar_barra(Barra(58, 79, seccion_chica)) #36
ret.agregar_barra(Barra(59, 80, seccion_chica)) #37
ret.agregar_barra(Barra(60, 81, seccion_chica)) #38
ret.agregar_barra(Barra(61, 82, seccion_chica)) #39
ret.agregar_barra(Barra(62, 83, seccion_chica)) #39



## union entre marcos


ret.agregar_barra(Barra(0, 42, seccion_chica))   #0
ret.agregar_barra(Barra(1, 43, seccion_chica))   #1
ret.agregar_barra(Barra(2, 44, seccion_chica))   #2
ret.agregar_barra(Barra(3, 45, seccion_chica))   #3
ret.agregar_barra(Barra(4, 46, seccion_chica))   #4
ret.agregar_barra(Barra(5, 47, seccion_chica))   #5
ret.agregar_barra(Barra(6, 48, seccion_chica))   #6
ret.agregar_barra(Barra(7, 49, seccion_chica))   #7
ret.agregar_barra(Barra(8, 50, seccion_chica))   #8
ret.agregar_barra(Barra(9, 51, seccion_chica))  #9
ret.agregar_barra(Barra(10, 52, seccion_chica)) #10
ret.agregar_barra(Barra(11, 53, seccion_chica)) #11
ret.agregar_barra(Barra(12, 54, seccion_chica)) #12
ret.agregar_barra(Barra(13, 55, seccion_chica)) #13
ret.agregar_barra(Barra(14, 56, seccion_chica)) #14
ret.agregar_barra(Barra(15, 57, seccion_chica)) #15
ret.agregar_barra(Barra(16, 58, seccion_chica)) #16
ret.agregar_barra(Barra(17, 59, seccion_chica)) #17
ret.agregar_barra(Barra(18, 60, seccion_chica)) #18
ret.agregar_barra(Barra(19, 61, seccion_chica)) #19
ret.agregar_barra(Barra(20, 62, seccion_chica)) #19



ret.agregar_barra(Barra(21, 63, seccion_chica)) #20
ret.agregar_barra(Barra(22, 64, seccion_chica)) #20
ret.agregar_barra(Barra(23, 65, seccion_chica)) #21
ret.agregar_barra(Barra(24, 66, seccion_chica)) #22
ret.agregar_barra(Barra(25, 67, seccion_chica)) #23
ret.agregar_barra(Barra(26, 68, seccion_chica)) #24
ret.agregar_barra(Barra(27, 69, seccion_chica)) #25
ret.agregar_barra(Barra(28, 70, seccion_chica)) #26
ret.agregar_barra(Barra(29, 71, seccion_chica)) #27
ret.agregar_barra(Barra(30, 72, seccion_chica)) #28
ret.agregar_barra(Barra(31, 73, seccion_chica)) #29
ret.agregar_barra(Barra(32, 74, seccion_chica)) #30
ret.agregar_barra(Barra(33, 75, seccion_chica)) #31
ret.agregar_barra(Barra(34, 76, seccion_chica)) #32
ret.agregar_barra(Barra(35, 77, seccion_chica)) #33
ret.agregar_barra(Barra(36, 78, seccion_chica)) #34
ret.agregar_barra(Barra(37, 79, seccion_chica)) #35
ret.agregar_barra(Barra(38, 80, seccion_chica)) #36
ret.agregar_barra(Barra(39, 81, seccion_chica)) #37
ret.agregar_barra(Barra(40, 82, seccion_chica)) #38
ret.agregar_barra(Barra(41, 83, seccion_chica)) #39


## diagonales inferiores

ret.agregar_barra(Barra(0, 43, seccion_chica))   #0
ret.agregar_barra(Barra(1, 44, seccion_chica))   #1
ret.agregar_barra(Barra(2, 45, seccion_chica))   #2
ret.agregar_barra(Barra(3, 46, seccion_chica))   #3
ret.agregar_barra(Barra(4, 47, seccion_chica))   #4
ret.agregar_barra(Barra(5, 48, seccion_chica))   #5
ret.agregar_barra(Barra(6, 49, seccion_chica))   #6
ret.agregar_barra(Barra(7, 50, seccion_chica))   #7
ret.agregar_barra(Barra(8, 51, seccion_chica))   #8
ret.agregar_barra(Barra(9, 52, seccion_chica))  #9
ret.agregar_barra(Barra(10, 53, seccion_chica)) #10
ret.agregar_barra(Barra(11, 54, seccion_chica)) #11
ret.agregar_barra(Barra(12, 55, seccion_chica)) #12
ret.agregar_barra(Barra(13, 56, seccion_chica)) #13
ret.agregar_barra(Barra(14, 57, seccion_chica)) #14
ret.agregar_barra(Barra(15, 58, seccion_chica)) #15
ret.agregar_barra(Barra(16, 59, seccion_chica)) #16
ret.agregar_barra(Barra(17, 60, seccion_chica)) #17
ret.agregar_barra(Barra(18, 61, seccion_chica)) #18
ret.agregar_barra(Barra(19, 62, seccion_chica)) #19

## diagonales superiores


ret.agregar_barra(Barra(21, 64, seccion_chica)) #20
ret.agregar_barra(Barra(22, 65, seccion_chica)) #20
ret.agregar_barra(Barra(23, 66, seccion_chica)) #21
ret.agregar_barra(Barra(24, 67, seccion_chica)) #22
ret.agregar_barra(Barra(25, 68, seccion_chica)) #23
ret.agregar_barra(Barra(26, 69, seccion_chica)) #24
ret.agregar_barra(Barra(27, 70, seccion_chica)) #25
ret.agregar_barra(Barra(28, 71, seccion_chica)) #26
ret.agregar_barra(Barra(29, 72, seccion_chica)) #27
ret.agregar_barra(Barra(30, 73, seccion_chica)) #28
ret.agregar_barra(Barra(31, 74, seccion_chica)) #29
ret.agregar_barra(Barra(32, 75, seccion_chica)) #30
ret.agregar_barra(Barra(33, 76, seccion_chica)) #31
ret.agregar_barra(Barra(34, 77, seccion_chica)) #32
ret.agregar_barra(Barra(35, 78, seccion_chica)) #33
ret.agregar_barra(Barra(36, 79, seccion_chica)) #34
ret.agregar_barra(Barra(37, 80, seccion_chica)) #35
ret.agregar_barra(Barra(38, 81, seccion_chica)) #36
ret.agregar_barra(Barra(39, 82, seccion_chica)) #37
ret.agregar_barra(Barra(40, 83, seccion_chica)) #38

#Crear restricciones
for nodo in [0,5]:
	ret.agregar_restriccion(nodo, 0, 0)
	ret.agregar_restriccion(nodo, 1, 0)
	ret.agregar_restriccion(nodo, 2, 0)

for nodo in [2,7]:
	ret.agregar_restriccion(nodo, 1, 0)
	ret.agregar_restriccion(nodo, 2, 0)




#Visualizar y comprobar las secciones
opciones_barras = {
	# "ver_secciones_en_barras": True,
	"color_barras_por_seccion": True,
}
ver_reticulado_3d(ret,opciones_barras=opciones_barras)

# exit(0)



#Resolver el problema peso_propio
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,-1.], factor_cargas=0.0)
ret.resolver_sistema()
f_D = ret.obtener_fuerzas()


#Agregar fuerzas tablero
ret.agregar_fuerza(0, 2, -F/4)
ret.agregar_fuerza(5, 2, -F/4)
ret.agregar_fuerza(2, 2, -F/4)
ret.agregar_fuerza(7, 2, -F/4)
ret.agregar_fuerza(1, 2, -F/2)
ret.agregar_fuerza(6, 2, -F/2)

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