# -*-coding:utf-8-*-
import os,sys
from xml.etree.ElementTree import *

from Relation import Relation

class RelationExample(Relation):
    """ relation with something
    """
    relation = 's'              # relation
    item = 'stock'              # item
    name = 'n'                  # name
    def __init__(self,rel):
        super().__init__(rel)

if __name__ == '__main__':
    i = '2.xml'
    i = '3.xml'
    r = RelationExample(i)
    r.plot()

    
