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


   def ensamblar_sistema(self, factor_peso_propio = [0.,0.,0.]):
                
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
                    x = ((factor_peso_propio[0])*2)*0.5
                    y = ((factor_peso_propio[1])*2)*0.5
                    z = ((factor_peso_propio[2])*2)*0.5
                    fe = [x*valor, y*valor, z*valor, x*valor, y*valor, z*valor]
                    
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
        
    


    def resolver_sistema(self):
        
       Ngdl = self.Nnodos * self.Ndimensiones
        gdl_libres = np.arange(Ngdl)
        gdl_fijos = []

        #Pre-llenar el vector u

        for nodo in self.restricciones:
            for restriccion in self.restricciones[nodo]:
                gdl = restriccion[0]
                valor = restriccion[1]

                gdl_global = self.Ndimensiones*nodo + gdl
                self.u[gdl_global] += valor

                gdl_fijos.append(gdl_global)

        #gdl_restringidos encuentro  gdl_libres
        gdl_fijos = np.array(gdl_fijos)
        gdl_libres = np.setdiff1d(gdl_libres, gdl_fijos)


        for nodo in self.cargas:
            for carga in self.cargas[nodo]:
                gdl = carga[0]
                valor = carga[1]
                gdl_global = self.Ndimensiones*nodo + gdl
                self.f[gdl_global] = valor


        #Particionar matriz:

        kff = self.K[np.ix_(gdl_libres, gdl_libres)]
        kfc = self.K[np.ix_(gdl_libres, gdl_fijos)]
        kcf = kfc.T
        kcc = self.K[np.ix_(gdl_fijos, gdl_fijos)]
 
        uf = self.u[gdl_libres]
        uc = self.u[gdl_fijos]

        ff = self.f[gdl_libres]
        fc = self.f[gdl_fijos]

        #Solucionar Kff uf = ff
        uf = solve(kff, ff - kfc @ uc)

        self.u[gdl_libres] = uf


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
    




    
    

