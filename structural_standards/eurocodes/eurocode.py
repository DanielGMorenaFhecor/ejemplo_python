#LA CLASE PRINCIPAL del EUROCÓDIGO
class Eurocode():

    # Como idea: en el constructor, por ejemplo, se puede introuducir el código del país para hacer referencia a anejos nationales (ES, FR, IT...)
    def __init__(self, national_code=''):
        self.national_code = national_code

    # Ya estableceremos una convención para nombrar a las fórmulas del Eurocódigo
    def fcm(self, fck):
        return fck + 8

    def Ecm(self, fck: float):
        return 22000.0 * ((fck + 8.0)/10.0)**0.3

    # Mi consejo es que intentemos dividir esta clase en varios archivos (por ejemplo: por capítulos del Eurocódigo) para evitar 
    # generar una clase monstruosa con un montón de métodos y que, por lo tanto, sea más fácil de colaborar a nivel de repositorio 
    # ya que no se modificaría el mismo archivo