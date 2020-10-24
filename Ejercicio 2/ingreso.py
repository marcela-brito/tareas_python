"""
2. dar opcion para registrar un ingreso
3. si es un ingreso sumarlo a la cuenta
6. poder generar un reporte de todos los ingresos

"""
class Ingreso:
#se definen los métodos: registrar ingreso y sumar ingreso a la cuenta
    def __init__(self, montoIngreso, ingresoTotal):
        self.montoIngreso = montoIngreso
        self.ingresoTotal = ingresoTotal
        
    def registrarIngreso(self):
        #montoIngreso = float(input("Monto a ingresar ($0.00): "))
        return self.montoIngreso

    def sumarIngreso(self):
        ingresoTotal +=self.montoIngreso
        return ingresoTotal

    montoIngreso = float(input("Monto a ingresar ($0.00): "))
    montoIngreso = 0.0




