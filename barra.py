#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 19:56:48 2021

@author: sandramunozavila
"""
import numpy as np
#Hola probando
from constantes import g_, ρ_acero, E_acero


class Barra(object):

    """Constructor para una barra"""
    def __init__(self, ni, nj, seccion, color=np.random.rand(3)):
        super(Barra, self).__init__()
        self.ni = ni
        self.nj = nj
        self.seccion = seccion
        self.color = color


    def obtener_conectividad(self):
        return [self.ni, self.nj]

    def calcular_largo(self, reticulado):
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        
        ni = self.ni
        nj = self.nj

        xi = reticulado.xyz[ni,:]
        xj = reticulado.xyz[nj,:]

        print(f"Barra {ni} a {nj} xi = {xi} xj = {xj}")
        
        Largo=np.linalg.norm(xi-xj)
        
        return Largo

    def calcular_peso(self, reticulado):
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        
        Area=self.seccion.area()
        Largo=self.calcular_largo(reticulado)
        Peso=Area*Largo*ρ_acero*g_
        
        return(Peso)

        
    def obtener_rigidez(self, ret):
        
        L = self.calcular_largo(ret)
        
        ni = self.ni
        nj = self.nj

        xi = ret.xyz[ni,:]
        xj = ret.xyz[nj,:]
        
        Lx=(xj[0]-xi[0])
        Ly=(xj[1]-xi[1])
        Lz=(xj[2]-xi[2])
        
        costhetax=Lx/self.calcular_largo(ret)
        costhetay=Ly/self.calcular_largo(ret)
        costhetaz=Lz/self.calcular_largo(ret)
        
        T=np.array([[-costhetax, -costhetay, -costhetaz, costhetax, costhetay, costhetaz]])
        
        Ke=self.seccion.area()*E_acero/L*(T.T@T)
        
        return Ke

    def obtener_vector_de_cargas(self, ret):
        
        return (self.calcular_peso(ret))/2*np.array([0,1,0,1])


    def obtener_fuerza(self, ret):
        
        ni = self.ni
        nj = self.nj

        xi = ret.xyz[ni,:]
        xj = ret.xyz[nj,:]
        
        Lx=(xj[0]-xi[0])
        Ly=(xj[1]-xi[1])
        Lz=(xj[2]-xi[2])
        
        costhetax=Lx/self.calcular_largo(ret)
        costhetay=Ly/self.calcular_largo(ret)
        costhetaz=Lz/self.calcular_largo(ret)
        
        T=np.array([-costhetax, -costhetay, -costhetaz, costhetax, costhetay, costhetax])
        
        u_e=np.array([ret.u[3*ni], ret.u[3*ni+1], ret.u[3*ni+2], ret.u[3*nj], ret.u[3*nj+1], ret.u[3*nj+2]])
        
        se=self.seccion.area()*E_acero/self.calcular_largo(ret)*T*u_e
        
        return se




    def chequear_diseño(self, Fu, ret, ϕ=0.9):
        
        """Implementar"""	
        
        return 0





    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0


    def rediseñar(self, Fu, ret, ϕ=0.9):
        
        """Implementar"""	
        
        return 0
