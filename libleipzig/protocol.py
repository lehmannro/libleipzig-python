# Copyright (C) 2009 Robert Lehmann

services = {
    'Baseform': (
        ['Wort'],
        ['Grundform', 'Wortart']),
    'Cooccurrences': (
        ['Wort', 'Mindestsignifikanz', 'Limit'],
        ['Wort', 'Kookkurrenz', 'Signifikanz']),
    'Sentences': (
        ['Wort', 'Limit'],
        ['Satz']),
    'RightNeighbours': (
        ['Wort', 'Limit'],
        ['Wort', 'Nachbar', 'Signifikanz']),
    'LeftNeighbours': (
        ['Wort', 'Limit'],
        ['Nachbar', 'Wort', 'Signifikanz']),
    'Frequencies': (
        ['Wort'],
        ['Anzahl', 'Frequenzklasse']),
    'Synonyms': (
        ['Wort', 'Limit'],
        ['Synonym']),
    'Thesaurus': (
        ['Wort', 'Limit'],
        ['Synonym']),
    'Wordforms': (
        ['Word', 'Limit'],
        ['Form']),
    'Similarity': (
        ['Wort', 'Limit'],
        ['Wort', 'Verwandter', 'Signifikanz']),
    'LeftCollocationFinder': (
        ['Wort', 'Wortart', 'Limit'],
        ['Kollokation', 'Wortart', 'Wort']),
    'RightCollocationFinder': (
        ['Wort', 'Wortart', 'Limit'],
        ['Wort', 'Kollokation', 'Wortart']),
    'Sachgebiet': (
        ['Wort'],
        ['Sachgebiet']),
    'Kreuzwortraetsel': (
        ['Wort', 'Wortlaenge', 'Limit'],
        ['Wort']),
}
