import re
import numpy as np
from structural_standards.structural_standard import StructuralStandard

class Aci_318_19(StructuralStandard):
    """
    ACI Standard: Building Code Requirements for Structural Concrete
    """

    def __init__(self):
        """Creates an instance of ACI 318-19"""
        super().__init__(name='ACI 318-19', release_year=2019, materials=('Concrete'))

# Chapter 19: Concrete: Design and durability requirements

    def Ec(self, fc: float, wc=2286.05) -> float:
        """
        ACI 319-19 19.2.2.1
        Computes modulus of elasticity in MPa

        Parameters
        ----------
        fc : float
            compressive strength of concrete fc' in MPa
        wc : float
            concrete density in kg/m3 (default is 2286.05kg/m3)

        Raises
        ------
        ValueError
            if fc or wc are less than 0
        """
        if fc < 0:
            raise ValueError(f"Compressive strength of concrete fc' cannot be less than 0. Current: {fc}")
        if wc < 0:
            raise ValueError(f'Concrete density cannot be less than 0. Current {wc}')

        return wc ** 1.5 * 0.043 * fc ** 0.5

    def fr(self, fc: float, l_fr: float) -> float:
        """
        ACI 319-19 19.2.3.1
        Computes the modulus of rupture in MPa

        Parameters
        ----------
        fc : float
            compressive strength of concrete fc' in MPa
        l : float
            lambda coefficient in accordance with 19.2.4
        
        Raises
        ------
        ValueError
            if fc is less than zero or lambda is not between 0 and 1 (both included)
        """
        if fc < 0:
            raise ValueError(f'Compressive strnegth of concrete cannot be less than zero. Current: {fc}')
        if l_fr < 0 or l_fr > 1:
            raise ValueError(f'l_fr (lambda) cannot be less than zero or greater than one. Current: {l_fr}')

        return 0.62 * l_fr * fc ** 0.5

    def l_fr_a(self, wc: float) -> float:
        """
        ACI 319-19 19.2.4.1(a)
        Returns the value of lambda for the calculation of the concrete modulus of rupture
        as a function of the concrete equilibrium density

        Parameters
        ----------
        wc : float
            concrete density in kg/m3

        Raises
        ------
        ValueError
            if concrete density wc is less than zero
        """
        if wc < 0:
            raise ValueError(f'Concrete density wc cannot be less than zero. Current: {wc}')
        if wc <= 1600:
            return 0.75
        if wc <= 2160:
            return np.min(0.0075*wc,1)
        
        return 1

    def l_fr_b(self, concrete: str, composition_aggregates: str) -> float:
        """
        ACI 319-19 19.2.4.1(b)
        Returns the value of lambda for the calculation of the concrete modulus of rupture
        based on composition aggregates

        Parameters
        ----------
        concrete : str
            possible values: 'all-lightweight', 'lightweight', 'fine blend', 'sand-lightweight', 'coarse blend'
        composition_aggregates: str
            specify 'fine' or 'coarse'

        Raise
        -----
        ValueError
            if no concrete value inside the possible range
        ValueError
            if composition is neither 'fine' nor 'coarse'
        """
        concrete=concrete.lower()
        composition_aggregates=composition_aggregates.lower()

        if composition_aggregates not in ('fine', 'coarse'):
            raise ValueError(f'No possible value for composition aggregates {composition_aggregates}')
        if concrete == 'all-lightweight':
            return 0.75
        if concrete not in ('lightweight', 'fine blend'):
            return 0.75 if composition_aggregates == 'fine' else 0.85
        if concrete == 'sand-lightweight':
            return 0.85
        if concrete not in ('sand-lightweight', 'coarse blend'):
            return 0.85 if composition_aggregates == 'fine' else 1
        
        raise ValueError(f'No value found for concrete value {concrete}')
