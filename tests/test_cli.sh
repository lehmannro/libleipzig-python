#!/bin/bash
. assert.sh || exit

assert "wortschatz | head -1" "Usage: wortschatz [options]"
assert "wortschatz -h | head -1" "Usage: wortschatz [options]"
assert_raises "wortschatz" 1
assert "wortschatz Baseform Schlangen" "Schlange,N\nSchlangen,S"
assert_raises "python -mlibleipzig.main -h" 0
assert_end basic

assert_raises "wortschatz Baseform 2>/dev/null" 1
assert_raises "wortschatz Baseform foo bar 2>/dev/null" 1
assert_raises "wortschatz Synonyms Schlange a 2>/dev/null" 2
assert 'wortschatz Synonyms Schlange a 2>&1 | cut -d" " -f1-5' \
       "remote failure: Server raised fault:"
assert_end failure

assert "wortschatz -s Baseform" "Grundform,Wortart"
assert "wortschatz -d- Baseform Schlangen" "Schlange-N\nSchlangen-S"
assert "wortschatz -v Synonyms Schlange a 2>&1 | head -1" \
       '<?xml version="1.0" encoding="UTF-8"?>'
assert_end options

