# -*- coding: utf-8 -*-
"""

Test relex snowball

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import io
import sys
import logging
import os
import unittest

from chemdataextractor.relex import Snowball, Relation, Entity
from chemdataextractor.model import TemperatureModel
from chemdataextractor.model import BaseModel, StringType, ListType, ModelType, Compound
from chemdataextractor.parse.elements import I, R, Any, OneOrMore, Optional, W
from chemdataextractor.parse.common import lrb, rrb, delim
from chemdataextractor.parse.actions import join, merge
from chemdataextractor.parse.cem import chemical_name
from chemdataextractor.doc import Sentence


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

# Define a test model
class CurieTemperature(TemperatureModel):
    specifier_expression = (W('Curie') + I('temperature')).add_action(join)
    specifier = StringType(parse_expression=specifier_expression, required=True, mutable=True)
    compound = ModelType(Compound, required=True)


class TestSnowball(unittest.TestCase):

    maxDiff = None
    training_corpus = 'tests/data/relex/curie_training_set/'

    def test_snowball_candidates(self):
        """Test that Candidate Relation objects are correctly created
        """

        pass
    
    def test_retrieve_entities(self):
        """Test entity retrieval from a parse result
        """
        pass
    
    def test_parse_sentence(self):
        """Test Snowball Sentence Parsing
        """
        pass
    
    def test_parse_interpret(self):
        """Test the relation interpretation
        """
        pass







if __name__ == '__main__':
    unittest.main()
