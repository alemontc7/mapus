# **********************************************************
# * Clase: Agente buscador                                 *
# * Autor: Victor Estevez                                  *
# * Version: v2023.03.29                                   *
# * Descripcion: Implementacion de algoritmos de busqueda  *
# *              sin informacion y con informacion         *
# **********************************************************

from AgenteIA.Agente import Agente
from copy import deepcopy
import time


class AgenteBuscador(Agente):
    def __init__(self):
        Agente.__init__(self)
        self.estado_inicial = None
        self.estado_meta = None
        self.funcion_sucesor = []
        self.tecnica = None

    def add_funcion(self, f):
        self.funcion_sucesor.append(f)

    def test_objetivo(self, e):
        return e == self.estado_meta

    def generar_hijos(self, e):
        hijos = []
        for fun in self.funcion_sucesor:
            h = fun(e)
            hijos.append(h)
        return hijos

    def get_costo(self, camino):
        raise Exception("Error: No existe implementacion")

    def get_heuristica(self, camino):
        raise Exception("Error: No existe implementacion")

    def interpreter(self, camino):
        raise Exception("Error: No existe implementacion")

    def get_funcion_a(self, camino):
        return self.get_costo(camino) + self.get_heuristica(camino)

    def mide_tiempo(funcion):
        def funcion_medida(*args, **kwards):
            inicio = time.time()
            c = funcion(*args, **kwards)
            print("Tiempo de ejecucion: ", time.time()-inicio)
            return c
        return funcion_medida

    @mide_tiempo
    def programa(self):
        print("Aqui el nodo inicial es", self.estado_inicial)
        frontera = [[self.estado_inicial]]
        visitados = []
        while frontera:
            if self.tecnica == "profundidad":
                camino = frontera.pop()  
            else:
                camino = frontera.pop(0)

            nodo = camino[-1]
            visitados.append(nodo)

            print("Frontera actual:", frontera)
            print("Camino actual:", camino)
            print("Nodo actual:", nodo)
            #time.sleep(5)

            if self.test_objetivo(nodo):
                print("¡Solución encontrada!")
                print(camino)
                self.acciones = [self.interpreter(camino)]
                break
            else:
                for hijo in self.generar_hijos(nodo):
                    if hijo not in visitados:
                        aux = deepcopy(camino)
                        aux.append(hijo)
                        frontera.append(aux)
