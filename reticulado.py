# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 08:59:59 2021

@author: juanp
"""

import numpy as np
from scipy.linalg import solve

class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 100

    #constructor
    def __init__(self):
        super(Reticulado, self).__init__()
        
        print("Constructor de Reticulado")
        
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
   
        


    def agregar_nodo(self, x, y, z=0):
        

        print(f"Quiero agregar un nodo en ({x} {y} {z})")
        numero_de_nodo_actual = self.Nnodos

        self.xyz[numero_de_nodo_actual,:] = [x, y, z]

        self.Nnodos += 1
        
        return 0

    def agregar_barra(self, barra):
        
        self.barras.append(barra)        
        
        return 0

    def obtener_coordenada_nodal(self, n):
        
        coordenada_nodal = self.xyz[n]
        
        print(f"{n}: {coordenada_nodal}")
        
        return (coordenada_nodal)

    def calcular_peso_total(self):
        
        peso_total = 0
        for i in self.barras:
            peso_total += i.calcular_peso(self)
            
        return peso_total
      
    def obtener_nodos(self):
        
        return self.xyz

    def obtener_barras(self):
        
        return self.barras



    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        
        """Implementar"""	
        
        if nodo in self.restricciones:
            self.restricciones[nodo].append([gdl,valor])
        else:
            self.restricciones[nodo] = [[gdl,valor]]
            
        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        
        """Implementar"""	
        
         if nodo in self.cargas:
            self.cargas[nodo].append([gdl,valor])
        else:
            self.cargas[nodo] = [[gdl,valor]]	
            
        return 0


    def ensamblar_sistema(self, factorpeso_propio=0.):
        
        """Implementar"""
        
        n = self.Nnodos*3 + 2
        self.K = np.zeros((n,n)) 
        self.f = np.zeros(n) 
        self.u = np.zeros(n)
        
        
        for e in self.barras:
            
            d = [3*e.ni, 3*e.ni + 1, 3*e.ni + 2, 3*e.nj, 3*e.nj +1, 3*e.nj +2]
            ke = e.obtener_rigidez(self)
            fe = e.obtener_vector_de_cargas(self)
            
            if factor_peso_propio != [0.,0.,0.]:
                
                    valor = fe[2]
                    x = sqtr((factor_peso_propio[0])**2)
                    y = sqtr((factor_peso_propio[1])**2)
                    z = sqtr((factor_peso_propio[2])**2)   
                    fe = [x*valor, y*valor, z*valor, x*valor, y*valor, z*valor ]
                    
            else:
                fe = np.zeros(6)
                
            for i in range (6):
                p = d[i]
                for j in range (6):
                    q = d[j]
                    self.K[p,q]+=ke[i,j]
                    
                if factor_peso_propio != 0.:
                    self.f[p] += fe[i]
            
                
                
                
        for node in self.cargas:
            for carga in self.cargas[node]:
                gdl = carga[0]
                valor = carga[1]
                gdl_global = node*3 + gdl
                self.f[gdl_global] = valor
        
        return 0


    def resolver_sistema(self):
        
        gdl_libres = np.arrange(self.Nnodos*3)
        gdl_fijos = []
        
        kff = self.K[np.ix_(gdl_libres,gdl_libres)]
        kcc = self.K[np.ix_(gdl_fijos,gdl_fijos)]
        kcf = self.K[np.ix_(gdl_fijos,gdl_libres)]
        kfc = self.K[np.ix_(gdl_libres,gdl_fijos)]
        
        uc = self.u[gdl_fijos]
        
        Ff = self.F[gdl_libres] - kfc@uc
        self.u[gdl_libres] = linalg.solve(kff,Ff)

        R = kcf@self.u[gdl_libres] + kcc@uc - self.F[gdl_fijos]

        return 0	
        

    def obtener_desplazamiento_nodal(self, n):
        
        """Implementar"""	
        
        return 0


    def obtener_fuerzas(self):
        
        """Implementar"""	
        
        return 0


    def obtener_factores_de_utilizacion(self, f):
        
        """Implementar"""	
        
        return 0

    def rediseñar(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0



    def chequear_diseño(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0


     def __str__(self):
        s = 'nodos:\n'
        for i in range(len(self.xyz)):
            s += f'{i} : ({self.obtener_coordenada_nodal(i)})\n'
        s += 'barras:\n'
        for i in range(len(self.barras)):
            s += f'{i} : {self.barras[i].ni,self.barras[i].nj}\n'
        return(s)
    




    
    

