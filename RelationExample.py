# -*-coding:utf-8-*-
import os,sys
from xml.etree.ElementTree import *
from pprint import pprint

from Relation import Relation

class RelationExample(Relation):
    """ relation with something
    """
    relation = 'sector'         # relation
    item = 'stock'              # item
    name = 'name'               # name
    def __init__(self,rel):
        super().__init__(rel)

if __name__ == '__main__':
    i = '2.xml'
    r = RelationExample(i)
    relations = r.relations
    pprint(relations)

    
