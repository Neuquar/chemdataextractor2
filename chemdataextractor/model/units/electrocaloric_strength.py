# created by jyz
# -*- coding: utf-8 -*-
"""
Units and models for electrocaloric strength.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from .quantity_model import QuantityModel, StringType
from .unit import Unit
from .dimension import Dimension
from .temperature import Temperature
from .length import Length
from .electric_potential import ElectricPotential
from ...parse.elements import W, I, R, Optional, Any, OneOrMore, Not, ZeroOrMore
from ...parse.actions import merge, join

log = logging.getLogger(__name__)


class Electrocaloric_strength(Dimension):
    constituent_dimensions = Temperature() * Length() / ElectricPotential()


class Electrocaloric_strengthModel(QuantityModel):

    dimensions = Electrocaloric_strength()


class Electrocaloric_strengthUnit(Unit):

    def __init__(self, magnitude=0.0, powers=None):
        super(Electrocaloric_strengthUnit, self).__init__(Electrocaloric_strength(), magnitude, powers)


class Joule(Electrocaloric_strengthUnit):

    def convert_value_to_standard(self, value):
        return value

    def convert_value_from_standard(self, value):
        return value

    def convert_error_to_standard(self, error):
        return error

    def convert_error_from_standard(self, error):
        return error


class ElectronVolt(Electrocaloric_strengthUnit):

    def convert_value_to_standard(self, value):
        return value * 1.6021766208e-19

    def convert_value_from_standard(self, value):
        return value / 1.6021766208e-19

    def convert_error_to_standard(self, error):
        return error * 1.6021766208e-19

    def convert_error_from_standard(self, error):
        return error / 1.6021766208e-19


class Erg(Electrocaloric_strengthUnit):
    def convert_value_to_standard(self, value):
        return 1e-7 * value

    def convert_value_from_standard(self, value):
        return 1e7 * value

    def convert_error_to_standard(self, error):
        return 1e-7 * error

    def convert_error_from_standard(self, error):
        return 1e7 * error


units_dict = {R('(J|j)(oule(s)?)?', group=0): Joule,
              R('(E|e)(lectron)?( )?(V|v)(olts)?', group=0): ElectronVolt,
              R('(E|e)rg', group=0): Erg}
Electrocaloric_strength.units_dict.update(units_dict)
Electrocaloric_strength.standard_units = Joule()

