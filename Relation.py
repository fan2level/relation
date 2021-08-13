# -*-coding:utf-8-*-
import os,sys
from xml.etree.ElementTree import *
from pprint import pprint

class Relation(object):
    """ relation with something
    re-define class variable from subclass
    """
    relation = 'r'              # relation
    item = 'i'                  # item
    name = 'n'                  # name
    def __init__(self,rel):
        if os.path.exists(rel) == False:
            raise FileNotFoundError
        self.__relations = dict()
        tree = parse(rel)
        root = tree.getroot()

        self.__relations = self.parse(root)

    def parse(self, xmlrelations):
        relation = xmlrelations.get(self.name)
        
        relations = {self.name: relation}
        for xmlitem in xmlrelations.findall(self.item):
            if 'item' not in relations:
                relations['item'] = list()
            item = xmlitem.get(self.name)
            relations['item'].append(item)
        for xmlrelation in xmlrelations.findall(self.relation):
            if 'relation' not in relations:
                relations['relation'] = list()
            relations['relation'].append(self.parse(xmlrelation))

        return relations

    def plot(self):
        pprint(self.relations)
        
    @property
    def relations(self):
        return self.__relations

if __name__ == '__main__':
    i = '1.xml'
    r = Relation(i)
    r.plot()
    # relations = r.relations
    # pprint(relations)

    
