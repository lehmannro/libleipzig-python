# Copyright (C) 2009, 2010 Robert Lehmann
#
# SOAP description data
# cf. http://wortschatz.uni-leipzig.de/axis/servlet/ServiceOverviewServlet

from libleipzig.transport import service

@service('Grundform', 'Wortart')
def Baseform(Wort): """
    Return the lemmatized (base) form.
    """
@service('Wort', 'Kookkurrenz', 'Signifikanz')
def Cooccurrences(Wort, Mindestsignifikanz, Limit): """
    Return statistically significant co-occurrences.
    """
@service('Satz')
def Sentences(Wort, Limit): """
    Return sample sentences containing the input word.
    """
@service('Wort', 'Nachbar', 'Signifikanz')
def RightNeighbours(Wort, Limit): """
    Return statistically significant right neighbours (words co-occurring
    immediately next to the input word).
    """
@service('Nachbar', 'Wort', 'Signifikanz')
def LeftNeighbours(Wort, Limit): """
    Returns statistically significant left neighbours (words co-occurring
    immediately next to the input word).
    """
@service('Anzahl', 'Frequenzklasse')
def Frequencies(Wort): """
    Return the frequency and frequency class. Frequency classes are computed
    in relation to the most frequent word in the corpus. The higher the class,
    the rarer the word.
    """
@service('Synonym')
def Synonyms(Wort, Limit): """
    Return synonyms. In other words, this is a thesaurus.
    """
@service('Synonym')
def Thesaurus(Wort, Limit): """
    Return synonyms (like the `Synonyms` service). However, this lemmatizes
    the input word first and thus returns more synonyms.
    """
@service('Form')
def Wordforms(Word, Limit): """
    Return all other word forms of the same lemma.
    """
@service('Wort', 'Verwandter', 'Signifikanz')
def Similarity(Wort, Limit): """
    Return automatically computed contextually similar words of the input
    word. Such similar words may be antonyms, hyperonyms, synonyms, cohyponyms
    or other. Note that due to the huge amount of data any query to this
    service may take a long time.
    """
@service('Kollokation', 'Wortart', 'Wort')
def LeftCollocationFinder(Wort, Wortart, Limit): """
    Attempt to find linguistic collocations that occur left to the word. The
    `Wortart` parameter shall be either A, V, N, or S meaning adjective, verb,
    noun and stopword, respectively. The parameter restricts the type of words
    found.
    """
@service('Wort', 'Kollokation', 'Wortart')
def RightCollocationFinder(Wort, Wortart, Limit): """
    Attempt to find linguistic collocations that occur right to the word. The
    `Wortart` parameter shall be either A, V, N, or S meaning adjective, verb,
    noun and stopword, respectively. The parameter restricts the type of words
    found.
    """
@service('Sachgebiet')
def Sachgebiet(Wort): """
    Return categories.
    """
@service('Wort')
def Kreuzwortraetsel(Wort, Wortlaenge, Limit): """
    Return words that match the pattern `Wort`. The percentage sign (%) acts
    as a wildmask.
    """
