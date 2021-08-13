# -*-coding:utf-8-*-
import os,sys
from xml.etree.ElementTree import *
from pprint import pprint

class Relation(object):
    """ relation with something
    re-define class variable from subclass

    fixme: duplicate relation name
    """
    relation = 'relation'       # relation
    item = 'item'               # item
    name = 'name'               # name
    colorrelation = 'lightsalmon'
    coloritem = 'white'
    colorname = 'white'
    def __init__(self,rel):
        if os.path.exists(rel) == False:
            raise FileNotFoundError
        self.__relations = dict()
        tree = parse(rel)
        root = tree.getroot()

        self.dot = None
        self.__relations = self.parse(root)

    def parse(self, xmlrelations):
        relation = xmlrelations.get(self.name)
        
        relations = {self.name: relation}
        for xmlitem in xmlrelations.findall(self.item):
            if self.item not in relations:
                relations[self.item] = list()
            item = xmlitem.get(self.name)
            relations[self.item].append(item)
        for xmlrelation in xmlrelations.findall(self.relation):
            if self.relation not in relations:
                relations[self.relation] = list()
            relations[self.relation].append(self.parse(xmlrelation))

        return relations

    def plot(self):
        try:
            from graphviz import Digraph
            dot = Digraph(comment="plot relations",
                          format="svg",
                          encoding="utf-8",
                          engine="neato")
            self.dot = dot
            dot.attr('graph', overlap='false')
            dot.attr('graph', concentrate='true')
            dot.attr('node', width='.3', height='.3')
            
            self.plotRelation(self.relations)
            self.dot.view()
        except ModuleNotFoundError as e:
            print(f"warning!!!")
            print(f"$>pip install graphviz")
            print()
            pprint(self.relations)
    def plotRelation(self, relations):
        rname = relations[self.name]
        if rname == self.relations[self.name]:
            self.dot.attr('node', shape='box3d', style='filled', fillcolor=self.colorrelation)
        else:
            self.dot.attr('node', shape='box', style='filled', fillcolor=self.colorrelation)
        self.dot.node(rname)
        if self.item in relations:
            for item in relations[self.item]:
                self.dot.attr('node', shape='box', style='filled', fillcolor=self.coloritem)
                self.dot.node(item)
                self.dot.edge(rname, item)
        if self.relation in relations:
            for relation in relations[self.relation]:
                rname2 = relation[self.name]
                self.dot.attr('node', shape='box', style='filled', fillcolor=self.colorrelation)
                self.dot.node(rname2)
                self.dot.edge(rname, rname2)
                self.plotRelation(relation)

    @property
    def relations(self):
        return self.__relations

if __name__ == '__main__':
    i = '1.xml'
    r = Relation(i)
    r.plot()
