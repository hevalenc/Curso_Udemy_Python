#aula sobre Expressões Regulares

# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

"""
Regular expressions (called REs, or regexes, or regex patterns) are essentially a tiny, highly specialized programming
language embedded inside Python and made available through the re module. Using this little language, you specify the
rules for the set of possible strings that you want to match; this set might contain English sentences, or e-mail
addresses, or TeX commands, or anything you like. You can then ask questions such as “Does this string match the
pattern?”, or “Is there a match for the pattern anywhere in this string?”. You can also use REs to modify a string or
to split it apart in various ways.
"""
import re

# Funções
# findall search sub
# compile

string = 'Este é um teste de expressões teste regulares.'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'ABCD', string))

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string))