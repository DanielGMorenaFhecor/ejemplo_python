#LA CLASE PRINCIPAL de la AASHTO
class Aashto():

    def Ec(self, density: float, fc: float) -> float:
        return (density*100)**1.5 * 0.0045 * fc**0.5
