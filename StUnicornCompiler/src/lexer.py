#!/usr/bin/python

import sys
import ply.lex as lex
reserved = {
	'and' : 'RESERVED_AND',
	'start' : 'RESERVED_BEGIN',
	'const' : 'RESERVED_CONST',
	'div' : 'RESERVED_DIV',
	'do' : 'RESERVED_DO',
	'stop' : 'RESERVED_END',
	'for' : 'RESERVED_FOR',
	'func' : 'RESERVED_FUNCTION',
	'if' : 'RESERVED_IF',
	'mod' : 'RESERVED_MOD',
	'not' : 'RESERVED_NOT',
	'or' : 'RESERVED_OR',
	'program' : 'RESERVED_PROGRAM',
	'repeat' : 'RESERVED_REPEAT',
	'string' : 'RESERVED_STRING',
	'then' : 'RESERVED_THEN',
	'to' : 'RESERVED_TO',
	'until' : 'RESERVED_UNTIL',
	'var' : 'RESERVED_VAR',
	'while' : 'RESERVED_WHILE',
	'false' : 'RESERVED_FALSE',
	'true' : 'RESERVED_TRUE',
}
modifiers = {
	'break' : 'MODIFIER_BREAK',
	'continue' : 'MODIFIER_CONTINUE',
	'write' : 'MODIFIER_WRITE'
}

literals = ['.', ',', ';', ':', '=', '(', ')', '+', '-', '*', '/', '<', '>']


tokens = [
	'LESSOREQ', 'MOREOREQ', 'NOTEQ',
	'COLON',
	'ASSIGNMENT',
	'DOT',
	'SEMI_COLON',
	'COMMA',
	'LPAREN',
	'RPAREN',
	'COMMENT',
	'IDENTIFIER',
	'DIGITSEQ',
	'REALNUMBER',
	'STRING'
] + list(reserved.values())



t_LESSOREQ = r'\<\='
t_MOREOREQ = r'\>\='
t_NOTEQ = r'\<\>'
t_COLON = r'\:'
t_ASSIGNMENT = r'\:\='
t_DOT = r'\.'
t_SEMI_COLON = r'\;'
t_COMMA = r'\,'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DIGITSEQ = r'([0-9]+)'

def t_REALNUMBER(t):
	r'([0-9]+)(\.[0-9]+|)([eE]([+-]|)[0-9]+|)'
	if '.' in t.value:
		t.value = float(t.value)
	else:
		t.type = 'DIGITSEQ'
		t.value = int(t.value)
	return t

t_STRING = r'(\'.*?\')'

def t_COMMENT(t):
    r'(//.*)|(/\*)(.|\n)*?\*/|\(\*(.|\n)*?\*\)|{(.|\n)*?}'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(),"IDENTIFIER")
    if t.type == 'RESERVED_FALSE':
    	t.value = 0
    	t.type = 'DIGITSEQ'
    if t.type == 'RESERVED_TRUE':
    	t.value = 1
    	t.type = 'DIGITSEQ'
    return t

output = ""
curr_line = ""

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
	global output
	global curr_line
	output = ""
	curr_line = ""

def t_indent(t):
	r'\ |\t'
	global output
	global curr_line
	curr_line += t.value

def t_error(t):
    print("Illegal character '%s'" % t.value[0] )
    t.lexer.skip(1)

lexer = lex.lex()