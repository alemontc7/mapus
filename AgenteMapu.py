from AgenteIA.AgenteBuscador import AgenteBuscador


class AgenteMapu(AgenteBuscador):

    def __init__(self):
        AgenteBuscador.__init__(self)
        # aqui tu codigo para la funciona sucesor
        # setear el estado inicial    def programa(self):

    # setear el estado meta, etc
    # funciones sucesor	

    def cantidad_a_texto(self, cantidad, singular, plural):
        if cantidad == 1:
            return f"un {'misionero' if singular == 'misionero' else 'caníbal'}"
        else:
            return f"{cantidad} {plural}"

    def interpreter(self, solucion):
        if(len(solucion) > 1):
            # si o si se tendran mas de de un nodo en la solucion, el actual y el siguiente.
            estado_actual = solucion[0]
            estado_siguiente = solucion[1]
            misioneros_actual, canibales_actual, lado_actual = estado_actual
            misioneros_siguiente, canibales_siguiente, _ = estado_siguiente

            misioneros_movidos = abs(misioneros_actual - misioneros_siguiente)
            canibales_movidos = abs(canibales_actual - canibales_siguiente)

            if lado_actual == 1:
                destino = "derecha"
            else:
                destino = "izquierda"

            misioneros_str = self.cantidad_a_texto(misioneros_movidos, "misionero", "misioneros")
            canibales_str = self.cantidad_a_texto(canibales_movidos, "caníbal", "caníbales")

            if misioneros_movidos == 0:
                movimiento = f"Mover {canibales_str} a la orilla {destino}."
            elif canibales_movidos == 0:
                movimiento = f"Mover {misioneros_str} a la orilla {destino}."
            else:
                movimiento = f"Mover {misioneros_str} y {canibales_str} a la orilla {destino}."
            return movimiento

    def es_valida(self, elem, e):
        misioneros, canibales, lado = e
        if lado == 1:
            m_izq, c_izq = misioneros - elem[0], canibales - elem[1]
            m_der, c_der = 3 - m_izq, 3 - c_izq
        else:
            m_der, c_der = misioneros + elem[0], canibales + elem[1]
            m_izq, c_izq = 3 - m_der, 3 - c_der
        
        if m_izq < 0 or c_izq < 0 or m_der < 0 or c_der < 0:
            return False
        if (m_izq > 0 and m_izq < c_izq) or (m_der > 0 and m_der < c_der):
            return False
        return True

    def construir_hijo(self, elem, e):
        misioneros, canibales, lado = e
        if lado == 1:
            nuevo_estado = [misioneros - elem[0], canibales - elem[1], 0]
        else:
            nuevo_estado = [misioneros + elem[0], canibales + elem[1], 1]
        return nuevo_estado

    def generar_hijos(self, e):
        posibilidades = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        hijos = [self.construir_hijo(elem, e) for elem in posibilidades if self.es_valida(elem, e)]
        return hijos

    

    # una vez configurados bien los atributos de esta clase,
    # deberiamos borrar las siguiente lineas, es decir dejar
    # que el programa implementado en el agente busqueda
    # resuelva el problema y devuelva las acciones....



