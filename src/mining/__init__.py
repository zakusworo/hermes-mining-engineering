"""Hermes Mining Engineering — pure mining engineering calculations.

NO IAPWS dependency. All modules use empirical, industry-standard methods:
- Hoek-Brown, RMR, GSI for rock mechanics
- ASHRAE psychrometrics for ventilation
- Bingham plastic for slurry rheology
- Tetens / simplified tables for dewatering water properties
"""

from . import rock_mechanics
from . import ventilation
from . import slurry
from . import dewatering

__version__ = "0.1.0"
