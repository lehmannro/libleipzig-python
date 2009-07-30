# Copyright (C) 2009 Robert Lehmann

from libleipzig.transport import service

@service('Grundform', 'Wortart')
def Baseform(Wort): pass
@service('Wort', 'Kookkurrenz', 'Signifikanz')
def Cooccurrences(Wort, Mindestsignifikanz, Limit): pass
@service('Satz')
def Sentences(Wort, Limit): pass
@service('Wort', 'Nachbar', 'Signifikanz')
def RightNeighbours(Wort, Limit): pass
@service('Nachbar', 'Wort', 'Signifikanz')
def LeftNeighbours(Wort, Limit): pass
@service('Anzahl', 'Frequenzklasse')
def Frequencies(Wort): pass
@service('Synonym')
def Synonyms(Wort, Limit): pass
@service('Synonym')
def Thesaurus(Wort, Limit): pass
@service('Form')
def Wordforms(Word, Limit): pass
@service('Wort', 'Verwandter', 'Signifikanz')
def Similarity(Wort, Limit): pass
@service('Kollokation', 'Wortart', 'Wort')
def LeftCollocationFinder(Wort, Wortart, Limit): pass
@service('Wort', 'Kollokation', 'Wortart')
def RightCollocationFinder(Wort, Wortart, Limit): pass
@service('Sachgebiet')
def Sachgebiet(Wort): pass
@service('Wort')
def Kreuzwortraetsel(Wort, Wortlaenge, Limit): pass
