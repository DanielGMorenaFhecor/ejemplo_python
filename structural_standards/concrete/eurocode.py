import numpy as np
from structural_standards.structural_standard import StructuralStandard

class Eurocode_1992_2(StructuralStandard):
    """Eurocode 2: Design of concrete structures. Release date: 2004"""

    @staticmethod
    def __get_valid_national_codes() -> tuple:
        """
        Returns valid national country codes
        """
        return ('', 'ES', 'UK', 'IT', 'FR')

    def __init__(self, national_code=''):
        """
        Creates an instance of EN 1992

        Parameters
        ----------
        national_code : str, optional
            country code if any national annex required (default is empty)

        Raises
        ------
        ValueError
            if input national code value is not valid or does not exist
        """
        super().__init__(name='EN 1992-2', release_year=2004, materials=('Concrete'))

        valid_national_codes = Eurocode_1992_2.__get_valid_national_codes()
        if national_code not in valid_national_codes:
            raise ValueError(f'{national_code} is not a valid national code')

        self.national_code = national_code
        
# Chapter 1-1: General rules and rules for buildings
# Section 3: Materials

    def beta_cc(self, t: float, s: float) -> float:
        """
        EN 1992-1.1:2004 Eq. 3.2

        Parameters
        ----------
        t : float
            time in days
        s : float
            cement coefficient

        Raises
        ------
        ValueError
            if number of days is lower or equal than 3 days or cement coefficient is not between 0 and 1
        """

        if t <= 3:
            raise ValueError(f'Number of days t cannot be lower than 0. Current: {t}')
        if s < 0 or s > 1:
            raise ValueError(f'Cement coefficient s has to be between 0 and 1. Current: {s}')

        if t < 28:
            return np.exp(s * (1 - (28/t)**0.5))

        return 1

    def fcm_t(self, fcm: float, t: float, s: float) -> float:
        """
        EN 1992-1.1:2004 Eq. 3.1
        Computes compressive strength of concrete at an age 't' and a type of cement.

        Parameters
        ----------
        fcm : float
            the mean compressive strength at 28 days according to Table 3.1 in MPa
        t : float
            time in days
        s : float
            cement coefficient

        Raises
        ------
        ValueError
            if fcm lower than 0
        """
        return fcm * self.beta_cc(t, s)

    def fck_t(self, fck: float, fcm: float, t: float, s: float) -> float:
        """
        EN 1992-1.1:2004 3.1.2 (5)
        Computes the concrete compressive strength at time 't'

        Parameters
        ----------
        fck : float
            concrete compressive strength at 28 days
        fcm : float
            the mean compressive strength at 28 days according to Table 3.1 in MPa
        t : float
            time in days
        s : float
            cement coefficient
        """
        if t < 28:
            return self.fcm_t(fcm, t, s) - 8
        return fck

    def fcm(self, fck: float) -> float:
        """
        EN 1992-1.1:2004 Table 3.1
        Returns the concrete mean compressive strength at 28 days

        Parameters
        ----------
        fck : float
            concrete compressive strength at 28 days

        Raises
        ------
        ValueError
            if 'fck' value is lower than 0
        """
        return fck + 8

    def Ecm(self, fck: float) -> float:
        """
        EN 1992-1.1:2004 Table 3.1
        Returns the module of elasticity in MPa at 28 days of a concrete given its compressive strength

        Parameters
        ----------
        fck : float
            concrete compressive strength at 28 days in MPa
        """
        return 22000 * (self.fcm(fck)/10.0)**0.3

    def Ecm_t(self, fcm_t: float, fcm: float, Ecm: float) -> float:
        """
        EN 1992-1.1:2004 Eq. 3.5
        Returns the modulus of elasticity with respect time

        Parameters
        ----------
        fcm_t : float
            mean concrete compressive strength at a time 't' in MPa
        fcm : float
            mean compressive strength at 28 days in MPa
        Ecm : float
            modulus of elasticity in MPa

        Raises
        ------
        ValueError
            if fcm_t, fcm or Ecm are lower than 0
        """

        if fcm_t < 0:
            raise ValueError(f'fcm_t cannot be lower than 0. Current: {fcm_t}')
        if fcm < 0:
            raise ValueError(f'fcm cannot be lower than 0. Current: {fcm}')
        if Ecm < 0:
            raise ValueError(f'Ecm cannot be lower than 0. Current: {Ecm}')

        return (fcm_t / fcm)**0.3 * Ecm
