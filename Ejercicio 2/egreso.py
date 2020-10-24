"""
1. registrar egreso
2. restar el egreso de la cuenta
3. verficar que si es un egreso y la cuenta esta a 0.0 debe aparecer
    el monto en negativo.
4. poder generar un reporte de todos lo egresos

"""
class Egreso:
       def __init__(self, montoEgreso, montoTotal):
        self.montoEgreso = montoEgreso
        self.montoTotal = montoTotal
        
        def registrarEgreso(self):
            return self.montoEgreso

        def restarEgreso(self):
            montoTotal -=self.montoEgreso
            return montoTotal

montoEgreso = float(input("Monto a egresar ($0.00): "))
montoEgreso = 0.0
    
