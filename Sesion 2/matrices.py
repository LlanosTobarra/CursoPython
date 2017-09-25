#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Módulo matrices
Created on Sun Sep 24 20:33:17 2017

@author: alvarory

Módulo de ejemplo para el cálculo de la suma de matrices
"""

def suma(m1,m2):
    """Esta función recibe matrices como listas y devuelve como resultado la matriz suma"""
    matrizSalida=[]
    
    for numFila in xrange(0,len(m1)):
        fila=[]
        for numColumna in xrange(0,len(m1[numFila])):
            valor = m1[numFila][numColumna] + m2[numFila][numColumna]
            fila.append(valor)
        matrizSalida.append(fila)
    return matrizSalida

