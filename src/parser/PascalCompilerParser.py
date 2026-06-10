# Generated from src/parser/PascalCompiler.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,61,347,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,2,3,2,65,8,2,1,2,3,2,68,8,
        2,1,2,1,2,1,3,1,3,4,3,74,8,3,11,3,12,3,75,1,4,1,4,1,4,3,4,81,8,4,
        1,4,1,4,1,4,1,5,1,5,4,5,88,8,5,11,5,12,5,89,1,6,1,6,1,6,1,6,1,6,
        1,7,1,7,1,7,5,7,100,8,7,10,7,12,7,103,9,7,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,3,8,112,8,8,1,9,1,9,1,9,1,9,1,9,5,9,119,8,9,10,9,12,9,122,
        9,9,1,9,1,9,1,9,1,9,1,10,3,10,129,8,10,1,10,1,10,1,10,3,10,134,8,
        10,1,10,1,10,1,11,1,11,1,12,5,12,141,8,12,10,12,12,12,144,9,12,1,
        13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,3,14,154,8,14,1,14,1,14,1,
        14,3,14,159,8,14,1,14,1,14,3,14,163,8,14,1,15,1,15,1,15,1,15,5,15,
        169,8,15,10,15,12,15,172,9,15,1,15,1,15,1,16,3,16,177,8,16,1,16,
        1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,5,17,188,8,17,10,17,12,17,
        191,9,17,1,17,1,17,5,17,195,8,17,10,17,12,17,198,9,17,1,17,1,17,
        1,17,3,17,203,8,17,1,17,3,17,206,8,17,3,17,208,8,17,1,18,1,18,1,
        18,1,18,1,19,3,19,215,8,19,1,19,1,19,3,19,219,8,19,5,19,221,8,19,
        10,19,12,19,224,9,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,3,20,237,8,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,4,20,262,8,20,11,20,12,20,263,1,20,1,20,1,20,3,20,269,
        8,20,3,20,271,8,20,1,20,1,20,1,20,1,20,1,20,3,20,278,8,20,1,20,1,
        20,1,20,1,20,3,20,284,8,20,1,20,1,20,3,20,288,8,20,1,21,1,21,1,21,
        1,21,1,21,1,22,3,22,296,8,22,1,22,1,22,1,22,1,22,3,22,302,8,22,1,
        22,5,22,305,8,22,10,22,12,22,308,9,22,1,23,1,23,1,24,1,24,1,24,5,
        24,315,8,24,10,24,12,24,318,9,24,1,25,1,25,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,3,26,331,8,26,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,5,26,342,8,26,10,26,12,26,345,9,26,1,26,0,1,52,
        27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,0,7,1,0,35,36,1,0,12,13,1,0,54,58,2,0,35,36,43,43,
        1,0,37,41,2,0,35,36,42,42,1,0,29,34,373,0,54,1,0,0,0,2,60,1,0,0,
        0,4,64,1,0,0,0,6,71,1,0,0,0,8,77,1,0,0,0,10,85,1,0,0,0,12,91,1,0,
        0,0,14,96,1,0,0,0,16,111,1,0,0,0,18,113,1,0,0,0,20,128,1,0,0,0,22,
        137,1,0,0,0,24,142,1,0,0,0,26,145,1,0,0,0,28,162,1,0,0,0,30,164,
        1,0,0,0,32,176,1,0,0,0,34,207,1,0,0,0,36,209,1,0,0,0,38,214,1,0,
        0,0,40,287,1,0,0,0,42,289,1,0,0,0,44,295,1,0,0,0,46,309,1,0,0,0,
        48,311,1,0,0,0,50,319,1,0,0,0,52,330,1,0,0,0,54,55,5,1,0,0,55,56,
        5,59,0,0,56,57,5,45,0,0,57,58,3,2,1,0,58,59,5,48,0,0,59,1,1,0,0,
        0,60,61,3,4,2,0,61,62,3,36,18,0,62,3,1,0,0,0,63,65,3,6,3,0,64,63,
        1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,68,3,10,5,0,67,66,1,0,0,0,
        67,68,1,0,0,0,68,69,1,0,0,0,69,70,3,24,12,0,70,5,1,0,0,0,71,73,5,
        2,0,0,72,74,3,8,4,0,73,72,1,0,0,0,74,75,1,0,0,0,75,73,1,0,0,0,75,
        76,1,0,0,0,76,7,1,0,0,0,77,78,5,59,0,0,78,80,5,29,0,0,79,81,3,22,
        11,0,80,79,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,83,3,46,23,0,83,
        84,5,45,0,0,84,9,1,0,0,0,85,87,5,3,0,0,86,88,3,12,6,0,87,86,1,0,
        0,0,88,89,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,11,1,0,0,0,91,92,
        3,14,7,0,92,93,5,53,0,0,93,94,3,16,8,0,94,95,5,45,0,0,95,13,1,0,
        0,0,96,101,5,59,0,0,97,98,5,46,0,0,98,100,5,59,0,0,99,97,1,0,0,0,
        100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,15,1,0,0,0,103,
        101,1,0,0,0,104,112,5,23,0,0,105,112,5,24,0,0,106,112,5,25,0,0,107,
        112,5,26,0,0,108,112,5,27,0,0,109,112,5,28,0,0,110,112,3,18,9,0,
        111,104,1,0,0,0,111,105,1,0,0,0,111,106,1,0,0,0,111,107,1,0,0,0,
        111,108,1,0,0,0,111,109,1,0,0,0,111,110,1,0,0,0,112,17,1,0,0,0,113,
        114,5,20,0,0,114,115,5,51,0,0,115,120,3,20,10,0,116,117,5,46,0,0,
        117,119,3,20,10,0,118,116,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,
        0,120,121,1,0,0,0,121,123,1,0,0,0,122,120,1,0,0,0,123,124,5,52,0,
        0,124,125,5,19,0,0,125,126,3,16,8,0,126,19,1,0,0,0,127,129,3,22,
        11,0,128,127,1,0,0,0,128,129,1,0,0,0,129,130,1,0,0,0,130,131,3,46,
        23,0,131,133,5,47,0,0,132,134,3,22,11,0,133,132,1,0,0,0,133,134,
        1,0,0,0,134,135,1,0,0,0,135,136,3,46,23,0,136,21,1,0,0,0,137,138,
        7,0,0,0,138,23,1,0,0,0,139,141,3,26,13,0,140,139,1,0,0,0,141,144,
        1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,25,1,0,0,0,144,142,1,
        0,0,0,145,146,3,28,14,0,146,147,5,45,0,0,147,148,3,2,1,0,148,149,
        5,45,0,0,149,27,1,0,0,0,150,151,5,14,0,0,151,153,5,59,0,0,152,154,
        3,30,15,0,153,152,1,0,0,0,153,154,1,0,0,0,154,163,1,0,0,0,155,156,
        5,15,0,0,156,158,5,59,0,0,157,159,3,30,15,0,158,157,1,0,0,0,158,
        159,1,0,0,0,159,160,1,0,0,0,160,161,5,53,0,0,161,163,3,16,8,0,162,
        150,1,0,0,0,162,155,1,0,0,0,163,29,1,0,0,0,164,165,5,49,0,0,165,
        170,3,32,16,0,166,167,5,45,0,0,167,169,3,32,16,0,168,166,1,0,0,0,
        169,172,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,171,173,1,0,0,0,
        172,170,1,0,0,0,173,174,5,50,0,0,174,31,1,0,0,0,175,177,5,3,0,0,
        176,175,1,0,0,0,176,177,1,0,0,0,177,178,1,0,0,0,178,179,3,14,7,0,
        179,180,5,53,0,0,180,181,3,16,8,0,181,33,1,0,0,0,182,196,5,59,0,
        0,183,184,5,51,0,0,184,189,3,52,26,0,185,186,5,46,0,0,186,188,3,
        52,26,0,187,185,1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,190,
        1,0,0,0,190,192,1,0,0,0,191,189,1,0,0,0,192,193,5,52,0,0,193,195,
        1,0,0,0,194,183,1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,197,
        1,0,0,0,197,208,1,0,0,0,198,196,1,0,0,0,199,205,5,59,0,0,200,202,
        5,49,0,0,201,203,3,48,24,0,202,201,1,0,0,0,202,203,1,0,0,0,203,204,
        1,0,0,0,204,206,5,50,0,0,205,200,1,0,0,0,205,206,1,0,0,0,206,208,
        1,0,0,0,207,182,1,0,0,0,207,199,1,0,0,0,208,35,1,0,0,0,209,210,5,
        4,0,0,210,211,3,38,19,0,211,212,5,5,0,0,212,37,1,0,0,0,213,215,3,
        40,20,0,214,213,1,0,0,0,214,215,1,0,0,0,215,222,1,0,0,0,216,218,
        5,45,0,0,217,219,3,40,20,0,218,217,1,0,0,0,218,219,1,0,0,0,219,221,
        1,0,0,0,220,216,1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,222,223,
        1,0,0,0,223,39,1,0,0,0,224,222,1,0,0,0,225,226,3,34,17,0,226,227,
        5,44,0,0,227,228,3,52,26,0,228,288,1,0,0,0,229,288,3,36,18,0,230,
        231,5,6,0,0,231,232,3,50,25,0,232,233,5,7,0,0,233,236,3,40,20,0,
        234,235,5,8,0,0,235,237,3,40,20,0,236,234,1,0,0,0,236,237,1,0,0,
        0,237,288,1,0,0,0,238,239,5,9,0,0,239,240,3,50,25,0,240,241,5,10,
        0,0,241,242,3,40,20,0,242,288,1,0,0,0,243,244,5,11,0,0,244,245,5,
        59,0,0,245,246,5,44,0,0,246,247,3,52,26,0,247,248,7,1,0,0,248,249,
        3,52,26,0,249,250,5,10,0,0,250,251,3,40,20,0,251,288,1,0,0,0,252,
        253,5,16,0,0,253,254,3,38,19,0,254,255,5,17,0,0,255,256,3,50,25,
        0,256,288,1,0,0,0,257,258,5,18,0,0,258,259,3,52,26,0,259,261,5,19,
        0,0,260,262,3,42,21,0,261,260,1,0,0,0,262,263,1,0,0,0,263,261,1,
        0,0,0,263,264,1,0,0,0,264,270,1,0,0,0,265,266,5,8,0,0,266,268,3,
        40,20,0,267,269,5,45,0,0,268,267,1,0,0,0,268,269,1,0,0,0,269,271,
        1,0,0,0,270,265,1,0,0,0,270,271,1,0,0,0,271,272,1,0,0,0,272,273,
        5,5,0,0,273,288,1,0,0,0,274,275,5,21,0,0,275,277,5,49,0,0,276,278,
        3,48,24,0,277,276,1,0,0,0,277,278,1,0,0,0,278,279,1,0,0,0,279,288,
        5,50,0,0,280,281,5,22,0,0,281,283,5,49,0,0,282,284,3,48,24,0,283,
        282,1,0,0,0,283,284,1,0,0,0,284,285,1,0,0,0,285,288,5,50,0,0,286,
        288,3,34,17,0,287,225,1,0,0,0,287,229,1,0,0,0,287,230,1,0,0,0,287,
        238,1,0,0,0,287,243,1,0,0,0,287,252,1,0,0,0,287,257,1,0,0,0,287,
        274,1,0,0,0,287,280,1,0,0,0,287,286,1,0,0,0,288,41,1,0,0,0,289,290,
        3,44,22,0,290,291,5,53,0,0,291,292,3,40,20,0,292,293,5,45,0,0,293,
        43,1,0,0,0,294,296,3,22,11,0,295,294,1,0,0,0,295,296,1,0,0,0,296,
        297,1,0,0,0,297,298,3,46,23,0,298,306,1,0,0,0,299,301,5,46,0,0,300,
        302,3,22,11,0,301,300,1,0,0,0,301,302,1,0,0,0,302,303,1,0,0,0,303,
        305,3,46,23,0,304,299,1,0,0,0,305,308,1,0,0,0,306,304,1,0,0,0,306,
        307,1,0,0,0,307,45,1,0,0,0,308,306,1,0,0,0,309,310,7,2,0,0,310,47,
        1,0,0,0,311,316,3,52,26,0,312,313,5,46,0,0,313,315,3,52,26,0,314,
        312,1,0,0,0,315,318,1,0,0,0,316,314,1,0,0,0,316,317,1,0,0,0,317,
        49,1,0,0,0,318,316,1,0,0,0,319,320,3,52,26,0,320,51,1,0,0,0,321,
        322,6,26,-1,0,322,323,5,49,0,0,323,324,3,52,26,0,324,325,5,50,0,
        0,325,331,1,0,0,0,326,327,7,3,0,0,327,331,3,52,26,6,328,331,3,46,
        23,0,329,331,3,34,17,0,330,321,1,0,0,0,330,326,1,0,0,0,330,328,1,
        0,0,0,330,329,1,0,0,0,331,343,1,0,0,0,332,333,10,5,0,0,333,334,7,
        4,0,0,334,342,3,52,26,6,335,336,10,4,0,0,336,337,7,5,0,0,337,342,
        3,52,26,5,338,339,10,3,0,0,339,340,7,6,0,0,340,342,3,52,26,4,341,
        332,1,0,0,0,341,335,1,0,0,0,341,338,1,0,0,0,342,345,1,0,0,0,343,
        341,1,0,0,0,343,344,1,0,0,0,344,53,1,0,0,0,345,343,1,0,0,0,38,64,
        67,75,80,89,101,111,120,128,133,142,153,158,162,170,176,189,196,
        202,205,207,214,218,222,236,263,268,270,277,283,287,295,301,306,
        316,330,341,343
    ]

class PascalCompilerParser ( Parser ):

    grammarFileName = "PascalCompiler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'const'", "'var'", "'begin'", 
                     "'end'", "'if'", "'then'", "'else'", "'while'", "'do'", 
                     "'for'", "'to'", "'downto'", "'procedure'", "'function'", 
                     "'repeat'", "'until'", "'case'", "'of'", "'array'", 
                     "'write'", "'writeln'", "'integer'", "'real'", "'boolean'", 
                     "'char'", "'longint'", "'string'", "'='", "'<>'", "'<='", 
                     "'<'", "'>='", "'>'", "'+'", "'-'", "'*'", "'/'", "'div'", 
                     "'mod'", "'and'", "'or'", "'not'", "':='", "';'", "','", 
                     "'..'", "'.'", "'('", "')'", "'['", "']'", "':'" ]

    symbolicNames = [ "<INVALID>", "KW_PROGRAM", "KW_CONST", "KW_VAR", "KW_BEGIN", 
                      "KW_END", "KW_IF", "KW_THEN", "KW_ELSE", "KW_WHILE", 
                      "KW_DO", "KW_FOR", "KW_TO", "KW_DOWNTO", "KW_PROCEDURE", 
                      "KW_FUNCTION", "KW_REPEAT", "KW_UNTIL", "KW_CASE", 
                      "KW_OF", "KW_ARRAY", "KW_WRITE", "KW_WRITELN", "TYPE_INT", 
                      "TYPE_REAL", "TYPE_BOOL", "TYPE_CHAR", "TYPE_LONG", 
                      "TYPE_STRING", "OP_EQ", "OP_NE", "OP_LE", "OP_LT", 
                      "OP_GE", "OP_GT", "OP_ADD", "OP_SUB", "OP_MUL", "OP_DIV", 
                      "OP_DIV_INT", "OP_MOD", "OP_AND", "OP_OR", "OP_NOT", 
                      "SYM_ASSIGN", "SYM_SEMI", "SYM_COMMA", "SYM_DOTDOT", 
                      "SYM_DOT", "SYM_LPAREN", "SYM_RPAREN", "SYM_LBRACKET", 
                      "SYM_RBRACKET", "SYM_COLON", "CHAR_LIT", "STRING_LIT", 
                      "BOOL_CONST", "REAL_NUMBER", "INT_NUMBER", "IDENTIFIER", 
                      "COMMENT", "WS" ]

    RULE_pascalProgram = 0
    RULE_executionBlock = 1
    RULE_declSection = 2
    RULE_constDeclPart = 3
    RULE_constDecl = 4
    RULE_varDeclPart = 5
    RULE_varDecl = 6
    RULE_idList = 7
    RULE_dataType = 8
    RULE_arrayType = 9
    RULE_idxRange = 10
    RULE_sign = 11
    RULE_subprogramDecls = 12
    RULE_subprogramDecl = 13
    RULE_subprogramHeader = 14
    RULE_paramList = 15
    RULE_paramGroup = 16
    RULE_designator = 17
    RULE_compoundStmt = 18
    RULE_stmtList = 19
    RULE_statement = 20
    RULE_caseItem = 21
    RULE_caseLabels = 22
    RULE_constantValue = 23
    RULE_argList = 24
    RULE_log_expr = 25
    RULE_expr = 26

    ruleNames =  [ "pascalProgram", "executionBlock", "declSection", "constDeclPart", 
                   "constDecl", "varDeclPart", "varDecl", "idList", "dataType", 
                   "arrayType", "idxRange", "sign", "subprogramDecls", "subprogramDecl", 
                   "subprogramHeader", "paramList", "paramGroup", "designator", 
                   "compoundStmt", "stmtList", "statement", "caseItem", 
                   "caseLabels", "constantValue", "argList", "log_expr", 
                   "expr" ]

    EOF = Token.EOF
    KW_PROGRAM=1
    KW_CONST=2
    KW_VAR=3
    KW_BEGIN=4
    KW_END=5
    KW_IF=6
    KW_THEN=7
    KW_ELSE=8
    KW_WHILE=9
    KW_DO=10
    KW_FOR=11
    KW_TO=12
    KW_DOWNTO=13
    KW_PROCEDURE=14
    KW_FUNCTION=15
    KW_REPEAT=16
    KW_UNTIL=17
    KW_CASE=18
    KW_OF=19
    KW_ARRAY=20
    KW_WRITE=21
    KW_WRITELN=22
    TYPE_INT=23
    TYPE_REAL=24
    TYPE_BOOL=25
    TYPE_CHAR=26
    TYPE_LONG=27
    TYPE_STRING=28
    OP_EQ=29
    OP_NE=30
    OP_LE=31
    OP_LT=32
    OP_GE=33
    OP_GT=34
    OP_ADD=35
    OP_SUB=36
    OP_MUL=37
    OP_DIV=38
    OP_DIV_INT=39
    OP_MOD=40
    OP_AND=41
    OP_OR=42
    OP_NOT=43
    SYM_ASSIGN=44
    SYM_SEMI=45
    SYM_COMMA=46
    SYM_DOTDOT=47
    SYM_DOT=48
    SYM_LPAREN=49
    SYM_RPAREN=50
    SYM_LBRACKET=51
    SYM_RBRACKET=52
    SYM_COLON=53
    CHAR_LIT=54
    STRING_LIT=55
    BOOL_CONST=56
    REAL_NUMBER=57
    INT_NUMBER=58
    IDENTIFIER=59
    COMMENT=60
    WS=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PascalProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_PROGRAM(self):
            return self.getToken(PascalCompilerParser.KW_PROGRAM, 0)

        def IDENTIFIER(self):
            return self.getToken(PascalCompilerParser.IDENTIFIER, 0)

        def SYM_SEMI(self):
            return self.getToken(PascalCompilerParser.SYM_SEMI, 0)

        def executionBlock(self):
            return self.getTypedRuleContext(PascalCompilerParser.ExecutionBlockContext,0)


        def SYM_DOT(self):
            return self.getToken(PascalCompilerParser.SYM_DOT, 0)

        def getRuleIndex(self):
            return PascalCompilerParser.RULE_pascalProgram

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPascalProgram" ):
                listener.enterPascalProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPascalProgram" ):
                listener.exitPascalProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPascalProgram" ):
                return visitor.visitPascalProgram(self)
            else:
                return visitor.visitChildren(self)




    def pascalProgram(self):

        localctx = PascalCompilerParser.PascalProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pascalProgram)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(PascalCompilerParser.KW_PROGRAM)
            self.state = 55
            self.match(PascalCompilerParser.IDENTIFIER)
            self.state = 56
            self.match(PascalCompilerParser.SYM_SEMI)
            self.state = 57
            self.executionBlock()
            self.state = 58
            self.match(PascalCompilerParser.SYM_DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExecutionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declSection(self):
            return self.getTypedRuleContext(PascalCompilerParser.DeclSectionContext,0)


        def compoundStmt(self):
            return self.getTypedRuleContext(PascalCompilerParser.CompoundStmtContext,0)


        def getRuleIndex(self):
            return PascalCompilerParser.RULE_executionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecutionBlock" ):
                listener.enterExecutionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecutionBlock" ):
                listener.exitExecutionBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecutionBlock" ):
                return visitor.visitExecutionBlock(self)
            else:
                return visitor.visitChildren(self)




    def executionBlock(self):

        localctx = PascalCompilerParser.ExecutionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_executionBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.declSection()
            self.state = 61
            self.compoundStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subprogramDecls(self):
            return self.getTypedRuleContext(PascalCompilerParser.SubprogramDeclsContext,0)


        def constDeclPart(self):
            return self.getTypedRuleContext(PascalCompilerParser.ConstDeclPartContext,0)


        def varDeclPart(self):
            return self.getTypedRuleContext(PascalCompilerParser.VarDeclPartContext,0)


        def getRuleIndex(self):
            return PascalCompilerParser.RULE_declSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclSection" ):
                listener.enterDeclSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclSection" ):
                listener.exitDeclSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclSection" ):
                return visitor.visitDeclSection(self)
            else:
                return visitor.visitChildren(self)




    def declSection(self):

        localctx = PascalCompilerParser.DeclSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 63
                self.constDeclPart()


            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 66
                self.varDeclPart()


            self.state = 69
            self.subprogramDecls()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_CONST(self):
            return self.getToken(PascalCompilerParser.KW_CONST, 0)

        def constDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.ConstDeclContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.ConstDeclContext,i)


        def getRuleIndex(self):
            return PascalCompilerParser.RULE_constDeclPart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstDeclPart" ):
                listener.enterConstDeclPart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstDeclPart" ):
                listener.exitConstDeclPart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDeclPart" ):
                return visitor.visitConstDeclPart(self)
            else:
                return visitor.visitChildren(self)




    def constDeclPart(self):

        localctx = PascalCompilerParser.ConstDeclPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_constDeclPart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(PascalCompilerParser.KW_CONST)
            self.state = 73 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                self.constDecl()
                self.state = 75 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==59):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PascalCompilerParser.IDENTIFIER, 0)

        def OP_EQ(self):
            return self.getToken(PascalCompilerParser.OP_EQ, 0)

        def constantValue(self):
            return self.getTypedRuleContext(PascalCompilerParser.ConstantValueContext,0)


        def SYM_SEMI(self):
            return self.getToken(PascalCompilerParser.SYM_SEMI, 0)

        def sign(self):
            return self.getTypedRuleContext(PascalCompilerParser.SignContext,0)


        def getRuleIndex(self):
            return PascalCompilerParser.RULE_constDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstDecl" ):
                listener.enterConstDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstDecl" ):
                listener.exitConstDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDecl" ):
                return visitor.visitConstDecl(self)
            else:
                return visitor.visitChildren(self)




    def constDecl(self):

        localctx = PascalCompilerParser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(PascalCompilerParser.IDENTIFIER)
            self.state = 78
            self.match(PascalCompilerParser.OP_EQ)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35 or _la==36:
                self.state = 79
                self.sign()


            self.state = 82
            self.constantValue()
            self.state = 83
            self.match(PascalCompilerParser.SYM_SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_VAR(self):
            return self.getToken(PascalCompilerParser.KW_VAR, 0)

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.VarDeclContext,i)


        def getRuleIndex(self):
            return PascalCompilerParser.RULE_varDeclPart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclPart" ):
                listener.enterVarDeclPart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclPart" ):
                listener.exitVarDeclPart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclPart" ):
                return visitor.visitVarDeclPart(self)
            else:
                return visitor.visitChildren(self)




    def varDeclPart(self):

        localctx = PascalCompilerParser.VarDeclPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varDeclPart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(PascalCompilerParser.KW_VAR)
            self.state = 87 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 86
                self.varDecl()
                self.state = 89 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==59):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idList(self):
            return self.getTypedRuleContext(PascalCompilerParser.IdListContext,0)


        def SYM_COLON(self):
            return self.getToken(PascalCompilerParser.SYM_COLON, 0)

        def dataType(self):
            return self.getTypedRuleContext(PascalCompilerParser.DataTypeContext,0)


        def SYM_SEMI(self):
            return self.getToken(PascalCompilerParser.SYM_SEMI, 0)

        def getRuleIndex(self):
            return PascalCompilerParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = PascalCompilerParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.idList()
            self.state = 92
            self.match(PascalCompilerParser.SYM_COLON)
            self.state = 93
            self.dataType()
            self.state = 94
            self.match(PascalCompilerParser.SYM_SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PascalCompilerParser.IDENTIFIER)
            else:
                return self.getToken(PascalCompilerParser.IDENTIFIER, i)

        def SYM_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PascalCompilerParser.SYM_COMMA)
            else:
                return self.getToken(PascalCompilerParser.SYM_COMMA, i)

        def getRuleIndex(self):
            return PascalCompilerParser.RULE_idList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdList" ):
                listener.enterIdList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdList" ):
                listener.exitIdList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdList" ):
                return visitor.visitIdList(self)
            else:
                return visitor.visitChildren(self)




    def idList(self):

        localctx = PascalCompilerParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(PascalCompilerParser.IDENTIFIER)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 97
                self.match(PascalCompilerParser.SYM_COMMA)
                self.state = 98
                self.match(PascalCompilerParser.IDENTIFIER)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_INT(self):
            return self.getToken(PascalCompilerParser.TYPE_INT, 0)

        def TYPE_REAL(self):
            return self.getToken(PascalCompilerParser.TYPE_REAL, 0)

        def TYPE_BOOL(self):
            return self.getToken(PascalCompilerParser.TYPE_BOOL, 0)

        def TYPE_CHAR(self):
            return self.getToken(PascalCompilerParser.TYPE_CHAR, 0)

        def TYPE_LONG(self):
            return self.getToken(PascalCompilerParser.TYPE_LONG, 0)

        def TYPE_STRING(self):
            return self.getToken(PascalCompilerParser.TYPE_STRING, 0)

        def arrayType(self):
            return self.getTypedRuleContext(PascalCompilerParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return PascalCompilerParser.RULE_dataType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataType" ):
                listener.enterDataType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataType" ):
                listener.exitDataType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataType" ):
                return visitor.visitDataType(self)
            else:
                return visitor.visitChildren(self)




    def dataType(self):

        localctx = PascalCompilerParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dataType)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(PascalCompilerParser.TYPE_INT)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(PascalCompilerParser.TYPE_REAL)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.match(PascalCompilerParser.TYPE_BOOL)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 107
                self.match(PascalCompilerParser.TYPE_CHAR)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 5)
                self.state = 108
                self.match(PascalCompilerParser.TYPE_LONG)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 6)
                self.state = 109
                self.match(PascalCompilerParser.TYPE_STRING)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 7)
                self.state = 110
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ARRAY(self):
            return self.getToken(PascalCompilerParser.KW_ARRAY, 0)

        def SYM_LBRACKET(self):
            return self.getToken(PascalCompilerParser.SYM_LBRACKET, 0)

        def idxRange(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.IdxRangeContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.IdxRangeContext,i)


        def SYM_RBRACKET(self):
            return self.getToken(PascalCompilerParser.SYM_RBRACKET, 0)

        def KW_OF(self):
            return self.getToken(PascalCompilerParser.KW_OF, 0)

        def dataType(self):
            return self.getTypedRuleContext(PascalCompilerParser.DataTypeContext,0)


        def SYM_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PascalCompilerParser.SYM_COMMA)
            else:
                return self.getToken(PascalCompilerParser.SYM_COMMA, i)

        def getRuleIndex(self):
            return PascalCompilerParser.RULE_arrayType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayType" ):
                listener.enterArrayType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayType" ):
                listener.exitArrayType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = PascalCompilerParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arrayType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(PascalCompilerParser.KW_ARRAY)
            self.state = 114
            self.match(PascalCompilerParser.SYM_LBRACKET)
            self.state = 115
            self.idxRange()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 116
                self.match(PascalCompilerParser.SYM_COMMA)
                self.state = 117
                self.idxRange()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self.match(PascalCompilerParser.SYM_RBRACKET)
            self.state = 124
            self.match(PascalCompilerParser.KW_OF)
            self.state = 125
            self.dataType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdxRangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constantValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.ConstantValueContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.ConstantValueContext,i)


        def SYM_DOTDOT(self):
            return self.getToken(PascalCompilerParser.SYM_DOTDOT, 0)

        def sign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.SignContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.SignContext,i)


        def getRuleIndex(self):
            return PascalCompilerParser.RULE_idxRange

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdxRange" ):
                listener.enterIdxRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdxRange" ):
                listener.exitIdxRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdxRange" ):
                return visitor.visitIdxRange(self)
            else:
                return visitor.visitChildren(self)




    def idxRange(self):

        localctx = PascalCompilerParser.IdxRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_idxRange)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35 or _la==36:
                self.state = 127
                self.sign()


            self.state = 130
            self.constantValue()
            self.state = 131
            self.match(PascalCompilerParser.SYM_DOTDOT)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35 or _la==36:
                self.state = 132
                self.sign()


            self.state = 135
            self.constantValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ADD(self):
            return self.getToken(PascalCompilerParser.OP_ADD, 0)

        def OP_SUB(self):
            return self.getToken(PascalCompilerParser.OP_SUB, 0)

        def getRuleIndex(self):
            return PascalCompilerParser.RULE_sign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSign" ):
                listener.enterSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSign" ):
                listener.exitSign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign" ):
                return visitor.visitSign(self)
            else:
                return visitor.visitChildren(self)




    def sign(self):

        localctx = PascalCompilerParser.SignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_sign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            _la = self._input.LA(1)
            if not(_la==35 or _la==36):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubprogramDeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subprogramDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.SubprogramDeclContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.SubprogramDeclContext,i)


        def getRuleIndex(self):
            return PascalCompilerParser.RULE_subprogramDecls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubprogramDecls" ):
                listener.enterSubprogramDecls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubprogramDecls" ):
                listener.exitSubprogramDecls(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubprogramDecls" ):
                return visitor.visitSubprogramDecls(self)
            else:
                return visitor.visitChildren(self)




    def subprogramDecls(self):

        localctx = PascalCompilerParser.SubprogramDeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_subprogramDecls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14 or _la==15:
                self.state = 139
                self.subprogramDecl()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubprogramDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subprogramHeader(self):
            return self.getTypedRuleContext(PascalCompilerParser.SubprogramHeaderContext,0)


        def SYM_SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(PascalCompilerParser.SYM_SEMI)
            else:
                return self.getToken(PascalCompilerParser.SYM_SEMI, i)

        def executionBlock(self):
            return self.getTypedRuleContext(PascalCompilerParser.ExecutionBlockContext,0)


        def getRuleIndex(self):
            return PascalCompilerParser.RULE_subprogramDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubprogramDecl" ):
                listener.enterSubprogramDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubprogramDecl" ):
                listener.exitSubprogramDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubprogramDecl" ):
                return visitor.visitSubprogramDecl(self)
            else:
                return visitor.visitChildren(self)




    def subprogramDecl(self):

        localctx = PascalCompilerParser.SubprogramDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_subprogramDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.subprogramHeader()
            self.state = 146
            self.match(PascalCompilerParser.SYM_SEMI)
            self.state = 147
            self.executionBlock()
            self.state = 148
            self.match(PascalCompilerParser.SYM_SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubprogramHeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_PROCEDURE(self):
            return self.getToken(PascalCompilerParser.KW_PROCEDURE, 0)

        def IDENTIFIER(self):
            return self.getToken(PascalCompilerParser.IDENTIFIER, 0)

        def paramList(self):
            return self.getTypedRuleContext(PascalCompilerParser.ParamListContext,0)


        def KW_FUNCTION(self):
            return self.getToken(PascalCompilerParser.KW_FUNCTION, 0)

        def SYM_COLON(self):
            return self.getToken(PascalCompilerParser.SYM_COLON, 0)

        def dataType(self):
            return self.getTypedRuleContext(PascalCompilerParser.DataTypeContext,0)


        def getRuleIndex(self):
            return PascalCompilerParser.RULE_subprogramHeader

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubprogramHeader" ):
                listener.enterSubprogramHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubprogramHeader" ):
                listener.exitSubprogramHeader(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubprogramHeader" ):
                return visitor.visitSubprogramHeader(self)
            else:
                return visitor.visitChildren(self)




    def subprogramHeader(self):

        localctx = PascalCompilerParser.SubprogramHeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_subprogramHeader)
        self._la = 0 # Token type
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(PascalCompilerParser.KW_PROCEDURE)
                self.state = 151
                self.match(PascalCompilerParser.IDENTIFIER)
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 152
                    self.paramList()


                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(PascalCompilerParser.KW_FUNCTION)
                self.state = 156
                self.match(PascalCompilerParser.IDENTIFIER)
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 157
                    self.paramList()


                self.state = 160
                self.match(PascalCompilerParser.SYM_COLON)
                self.state = 161
                self.dataType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYM_LPAREN(self):
            return self.getToken(PascalCompilerParser.SYM_LPAREN, 0)

        def paramGroup(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.ParamGroupContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.ParamGroupContext,i)


        def SYM_RPAREN(self):
            return self.getToken(PascalCompilerParser.SYM_RPAREN, 0)

        def SYM_SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(PascalCompilerParser.SYM_SEMI)
            else:
                return self.getToken(PascalCompilerParser.SYM_SEMI, i)

        def getRuleIndex(self):
            return PascalCompilerParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = PascalCompilerParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(PascalCompilerParser.SYM_LPAREN)
            self.state = 165
            self.paramGroup()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 166
                self.match(PascalCompilerParser.SYM_SEMI)
                self.state = 167
                self.paramGroup()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 173
            self.match(PascalCompilerParser.SYM_RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamGroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idList(self):
            return self.getTypedRuleContext(PascalCompilerParser.IdListContext,0)


        def SYM_COLON(self):
            return self.getToken(PascalCompilerParser.SYM_COLON, 0)

        def dataType(self):
            return self.getTypedRuleContext(PascalCompilerParser.DataTypeContext,0)


        def KW_VAR(self):
            return self.getToken(PascalCompilerParser.KW_VAR, 0)

        def getRuleIndex(self):
            return PascalCompilerParser.RULE_paramGroup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamGroup" ):
                listener.enterParamGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamGroup" ):
                listener.exitParamGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamGroup" ):
                return visitor.visitParamGroup(self)
            else:
                return visitor.visitChildren(self)




    def paramGroup(self):

        localctx = PascalCompilerParser.ParamGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_paramGroup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 175
                self.match(PascalCompilerParser.KW_VAR)


            self.state = 178
            self.idList()
            self.state = 179
            self.match(PascalCompilerParser.SYM_COLON)
            self.state = 180
            self.dataType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DesignatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PascalCompilerParser.IDENTIFIER, 0)

        def SYM_LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(PascalCompilerParser.SYM_LBRACKET)
            else:
                return self.getToken(PascalCompilerParser.SYM_LBRACKET, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.ExprContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.ExprContext,i)


        def SYM_RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(PascalCompilerParser.SYM_RBRACKET)
            else:
                return self.getToken(PascalCompilerParser.SYM_RBRACKET, i)

        def SYM_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PascalCompilerParser.SYM_COMMA)
            else:
                return self.getToken(PascalCompilerParser.SYM_COMMA, i)

        def SYM_LPAREN(self):
            return self.getToken(PascalCompilerParser.SYM_LPAREN, 0)

        def SYM_RPAREN(self):
            return self.getToken(PascalCompilerParser.SYM_RPAREN, 0)

        def argList(self):
            return self.getTypedRuleContext(PascalCompilerParser.ArgListContext,0)


        def getRuleIndex(self):
            return PascalCompilerParser.RULE_designator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDesignator" ):
                listener.enterDesignator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDesignator" ):
                listener.exitDesignator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDesignator" ):
                return visitor.visitDesignator(self)
            else:
                return visitor.visitChildren(self)




    def designator(self):

        localctx = PascalCompilerParser.DesignatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_designator)
        self._la = 0 # Token type
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(PascalCompilerParser.IDENTIFIER)
                self.state = 196
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 183
                        self.match(PascalCompilerParser.SYM_LBRACKET)
                        self.state = 184
                        self.expr(0)
                        self.state = 189
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==46:
                            self.state = 185
                            self.match(PascalCompilerParser.SYM_COMMA)
                            self.state = 186
                            self.expr(0)
                            self.state = 191
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 192
                        self.match(PascalCompilerParser.SYM_RBRACKET) 
                    self.state = 198
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.match(PascalCompilerParser.IDENTIFIER)
                self.state = 205
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 200
                    self.match(PascalCompilerParser.SYM_LPAREN)
                    self.state = 202
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1135478955223023616) != 0):
                        self.state = 201
                        self.argList()


                    self.state = 204
                    self.match(PascalCompilerParser.SYM_RPAREN)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_BEGIN(self):
            return self.getToken(PascalCompilerParser.KW_BEGIN, 0)

        def stmtList(self):
            return self.getTypedRuleContext(PascalCompilerParser.StmtListContext,0)


        def KW_END(self):
            return self.getToken(PascalCompilerParser.KW_END, 0)

        def getRuleIndex(self):
            return PascalCompilerParser.RULE_compoundStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundStmt" ):
                listener.enterCompoundStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundStmt" ):
                listener.exitCompoundStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundStmt" ):
                return visitor.visitCompoundStmt(self)
            else:
                return visitor.visitChildren(self)




    def compoundStmt(self):

        localctx = PascalCompilerParser.CompoundStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_compoundStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(PascalCompilerParser.KW_BEGIN)
            self.state = 210
            self.stmtList()
            self.state = 211
            self.match(PascalCompilerParser.KW_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.StatementContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.StatementContext,i)


        def SYM_SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(PascalCompilerParser.SYM_SEMI)
            else:
                return self.getToken(PascalCompilerParser.SYM_SEMI, i)

        def getRuleIndex(self):
            return PascalCompilerParser.RULE_stmtList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtList" ):
                listener.enterStmtList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtList" ):
                listener.exitStmtList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtList" ):
                return visitor.visitStmtList(self)
            else:
                return visitor.visitChildren(self)




    def stmtList(self):

        localctx = PascalCompilerParser.StmtListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_stmtList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752310045264) != 0):
                self.state = 213
                self.statement()


            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 216
                self.match(PascalCompilerParser.SYM_SEMI)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752310045264) != 0):
                    self.state = 217
                    self.statement()


                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PascalCompilerParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CompStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PascalCompilerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def compoundStmt(self):
            return self.getTypedRuleContext(PascalCompilerParser.CompoundStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompStmt" ):
                listener.enterCompStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompStmt" ):
                listener.exitCompStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompStmt" ):
                return visitor.visitCompStmt(self)
            else:
                return visitor.visitChildren(self)


    class IfStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PascalCompilerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_IF(self):
            return self.getToken(PascalCompilerParser.KW_IF, 0)
        def log_expr(self):
            return self.getTypedRuleContext(PascalCompilerParser.Log_exprContext,0)

        def KW_THEN(self):
            return self.getToken(PascalCompilerParser.KW_THEN, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.StatementContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.StatementContext,i)

        def KW_ELSE(self):
            return self.getToken(PascalCompilerParser.KW_ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)


    class WritelnStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PascalCompilerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_WRITELN(self):
            return self.getToken(PascalCompilerParser.KW_WRITELN, 0)
        def SYM_LPAREN(self):
            return self.getToken(PascalCompilerParser.SYM_LPAREN, 0)
        def SYM_RPAREN(self):
            return self.getToken(PascalCompilerParser.SYM_RPAREN, 0)
        def argList(self):
            return self.getTypedRuleContext(PascalCompilerParser.ArgListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWritelnStmt" ):
                listener.enterWritelnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWritelnStmt" ):
                listener.exitWritelnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWritelnStmt" ):
                return visitor.visitWritelnStmt(self)
            else:
                return visitor.visitChildren(self)


    class WhileStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PascalCompilerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_WHILE(self):
            return self.getToken(PascalCompilerParser.KW_WHILE, 0)
        def log_expr(self):
            return self.getTypedRuleContext(PascalCompilerParser.Log_exprContext,0)

        def KW_DO(self):
            return self.getToken(PascalCompilerParser.KW_DO, 0)
        def statement(self):
            return self.getTypedRuleContext(PascalCompilerParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)


    class AssignStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PascalCompilerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def designator(self):
            return self.getTypedRuleContext(PascalCompilerParser.DesignatorContext,0)

        def SYM_ASSIGN(self):
            return self.getToken(PascalCompilerParser.SYM_ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(PascalCompilerParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)


    class ProcCallStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PascalCompilerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def designator(self):
            return self.getTypedRuleContext(PascalCompilerParser.DesignatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcCallStmt" ):
                listener.enterProcCallStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcCallStmt" ):
                listener.exitProcCallStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcCallStmt" ):
                return visitor.visitProcCallStmt(self)
            else:
                return visitor.visitChildren(self)


    class CaseStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PascalCompilerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_CASE(self):
            return self.getToken(PascalCompilerParser.KW_CASE, 0)
        def expr(self):
            return self.getTypedRuleContext(PascalCompilerParser.ExprContext,0)

        def KW_OF(self):
            return self.getToken(PascalCompilerParser.KW_OF, 0)
        def KW_END(self):
            return self.getToken(PascalCompilerParser.KW_END, 0)
        def caseItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.CaseItemContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.CaseItemContext,i)

        def KW_ELSE(self):
            return self.getToken(PascalCompilerParser.KW_ELSE, 0)
        def statement(self):
            return self.getTypedRuleContext(PascalCompilerParser.StatementContext,0)

        def SYM_SEMI(self):
            return self.getToken(PascalCompilerParser.SYM_SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseStmt" ):
                listener.enterCaseStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseStmt" ):
                listener.exitCaseStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseStmt" ):
                return visitor.visitCaseStmt(self)
            else:
                return visitor.visitChildren(self)


    class WriteStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PascalCompilerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_WRITE(self):
            return self.getToken(PascalCompilerParser.KW_WRITE, 0)
        def SYM_LPAREN(self):
            return self.getToken(PascalCompilerParser.SYM_LPAREN, 0)
        def SYM_RPAREN(self):
            return self.getToken(PascalCompilerParser.SYM_RPAREN, 0)
        def argList(self):
            return self.getTypedRuleContext(PascalCompilerParser.ArgListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStmt" ):
                listener.enterWriteStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStmt" ):
                listener.exitWriteStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStmt" ):
                return visitor.visitWriteStmt(self)
            else:
                return visitor.visitChildren(self)


    class RepeatStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PascalCompilerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_REPEAT(self):
            return self.getToken(PascalCompilerParser.KW_REPEAT, 0)
        def stmtList(self):
            return self.getTypedRuleContext(PascalCompilerParser.StmtListContext,0)

        def KW_UNTIL(self):
            return self.getToken(PascalCompilerParser.KW_UNTIL, 0)
        def log_expr(self):
            return self.getTypedRuleContext(PascalCompilerParser.Log_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeatStmt" ):
                listener.enterRepeatStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeatStmt" ):
                listener.exitRepeatStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeatStmt" ):
                return visitor.visitRepeatStmt(self)
            else:
                return visitor.visitChildren(self)


    class ForStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PascalCompilerParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_FOR(self):
            return self.getToken(PascalCompilerParser.KW_FOR, 0)
        def IDENTIFIER(self):
            return self.getToken(PascalCompilerParser.IDENTIFIER, 0)
        def SYM_ASSIGN(self):
            return self.getToken(PascalCompilerParser.SYM_ASSIGN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.ExprContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.ExprContext,i)

        def KW_DO(self):
            return self.getToken(PascalCompilerParser.KW_DO, 0)
        def statement(self):
            return self.getTypedRuleContext(PascalCompilerParser.StatementContext,0)

        def KW_TO(self):
            return self.getToken(PascalCompilerParser.KW_TO, 0)
        def KW_DOWNTO(self):
            return self.getToken(PascalCompilerParser.KW_DOWNTO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = PascalCompilerParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                localctx = PascalCompilerParser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.designator()
                self.state = 226
                self.match(PascalCompilerParser.SYM_ASSIGN)
                self.state = 227
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = PascalCompilerParser.CompStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.compoundStmt()
                pass

            elif la_ == 3:
                localctx = PascalCompilerParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.match(PascalCompilerParser.KW_IF)
                self.state = 231
                self.log_expr()
                self.state = 232
                self.match(PascalCompilerParser.KW_THEN)
                self.state = 233
                self.statement()
                self.state = 236
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 234
                    self.match(PascalCompilerParser.KW_ELSE)
                    self.state = 235
                    self.statement()


                pass

            elif la_ == 4:
                localctx = PascalCompilerParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.match(PascalCompilerParser.KW_WHILE)
                self.state = 239
                self.log_expr()
                self.state = 240
                self.match(PascalCompilerParser.KW_DO)
                self.state = 241
                self.statement()
                pass

            elif la_ == 5:
                localctx = PascalCompilerParser.ForStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 243
                self.match(PascalCompilerParser.KW_FOR)
                self.state = 244
                self.match(PascalCompilerParser.IDENTIFIER)
                self.state = 245
                self.match(PascalCompilerParser.SYM_ASSIGN)
                self.state = 246
                self.expr(0)
                self.state = 247
                _la = self._input.LA(1)
                if not(_la==12 or _la==13):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 248
                self.expr(0)
                self.state = 249
                self.match(PascalCompilerParser.KW_DO)
                self.state = 250
                self.statement()
                pass

            elif la_ == 6:
                localctx = PascalCompilerParser.RepeatStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 252
                self.match(PascalCompilerParser.KW_REPEAT)
                self.state = 253
                self.stmtList()
                self.state = 254
                self.match(PascalCompilerParser.KW_UNTIL)
                self.state = 255
                self.log_expr()
                pass

            elif la_ == 7:
                localctx = PascalCompilerParser.CaseStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 257
                self.match(PascalCompilerParser.KW_CASE)
                self.state = 258
                self.expr(0)
                self.state = 259
                self.match(PascalCompilerParser.KW_OF)
                self.state = 261 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 260
                    self.caseItem()
                    self.state = 263 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 558446456873156608) != 0)):
                        break

                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 265
                    self.match(PascalCompilerParser.KW_ELSE)
                    self.state = 266
                    self.statement()
                    self.state = 268
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==45:
                        self.state = 267
                        self.match(PascalCompilerParser.SYM_SEMI)




                self.state = 272
                self.match(PascalCompilerParser.KW_END)
                pass

            elif la_ == 8:
                localctx = PascalCompilerParser.WriteStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 274
                self.match(PascalCompilerParser.KW_WRITE)
                self.state = 275
                self.match(PascalCompilerParser.SYM_LPAREN)
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1135478955223023616) != 0):
                    self.state = 276
                    self.argList()


                self.state = 279
                self.match(PascalCompilerParser.SYM_RPAREN)
                pass

            elif la_ == 9:
                localctx = PascalCompilerParser.WritelnStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 280
                self.match(PascalCompilerParser.KW_WRITELN)
                self.state = 281
                self.match(PascalCompilerParser.SYM_LPAREN)
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1135478955223023616) != 0):
                    self.state = 282
                    self.argList()


                self.state = 285
                self.match(PascalCompilerParser.SYM_RPAREN)
                pass

            elif la_ == 10:
                localctx = PascalCompilerParser.ProcCallStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 286
                self.designator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def caseLabels(self):
            return self.getTypedRuleContext(PascalCompilerParser.CaseLabelsContext,0)


        def SYM_COLON(self):
            return self.getToken(PascalCompilerParser.SYM_COLON, 0)

        def statement(self):
            return self.getTypedRuleContext(PascalCompilerParser.StatementContext,0)


        def SYM_SEMI(self):
            return self.getToken(PascalCompilerParser.SYM_SEMI, 0)

        def getRuleIndex(self):
            return PascalCompilerParser.RULE_caseItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseItem" ):
                listener.enterCaseItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseItem" ):
                listener.exitCaseItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseItem" ):
                return visitor.visitCaseItem(self)
            else:
                return visitor.visitChildren(self)




    def caseItem(self):

        localctx = PascalCompilerParser.CaseItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_caseItem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.caseLabels()
            self.state = 290
            self.match(PascalCompilerParser.SYM_COLON)
            self.state = 291
            self.statement()
            self.state = 292
            self.match(PascalCompilerParser.SYM_SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseLabelsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constantValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.ConstantValueContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.ConstantValueContext,i)


        def SYM_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PascalCompilerParser.SYM_COMMA)
            else:
                return self.getToken(PascalCompilerParser.SYM_COMMA, i)

        def sign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.SignContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.SignContext,i)


        def getRuleIndex(self):
            return PascalCompilerParser.RULE_caseLabels

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseLabels" ):
                listener.enterCaseLabels(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseLabels" ):
                listener.exitCaseLabels(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseLabels" ):
                return visitor.visitCaseLabels(self)
            else:
                return visitor.visitChildren(self)




    def caseLabels(self):

        localctx = PascalCompilerParser.CaseLabelsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_caseLabels)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35 or _la==36:
                self.state = 294
                self.sign()


            self.state = 297
            self.constantValue()
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 299
                self.match(PascalCompilerParser.SYM_COMMA)
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35 or _la==36:
                    self.state = 300
                    self.sign()


                self.state = 303
                self.constantValue()
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_NUMBER(self):
            return self.getToken(PascalCompilerParser.INT_NUMBER, 0)

        def REAL_NUMBER(self):
            return self.getToken(PascalCompilerParser.REAL_NUMBER, 0)

        def CHAR_LIT(self):
            return self.getToken(PascalCompilerParser.CHAR_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(PascalCompilerParser.STRING_LIT, 0)

        def BOOL_CONST(self):
            return self.getToken(PascalCompilerParser.BOOL_CONST, 0)

        def getRuleIndex(self):
            return PascalCompilerParser.RULE_constantValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantValue" ):
                listener.enterConstantValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantValue" ):
                listener.exitConstantValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantValue" ):
                return visitor.visitConstantValue(self)
            else:
                return visitor.visitChildren(self)




    def constantValue(self):

        localctx = PascalCompilerParser.ConstantValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_constantValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 558446353793941504) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.ExprContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.ExprContext,i)


        def SYM_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PascalCompilerParser.SYM_COMMA)
            else:
                return self.getToken(PascalCompilerParser.SYM_COMMA, i)

        def getRuleIndex(self):
            return PascalCompilerParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = PascalCompilerParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.expr(0)
            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 312
                self.match(PascalCompilerParser.SYM_COMMA)
                self.state = 313
                self.expr(0)
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Log_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PascalCompilerParser.ExprContext,0)


        def getRuleIndex(self):
            return PascalCompilerParser.RULE_log_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog_expr" ):
                listener.enterLog_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog_expr" ):
                listener.exitLog_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog_expr" ):
                return visitor.visitLog_expr(self)
            else:
                return visitor.visitChildren(self)




    def log_expr(self):

        localctx = PascalCompilerParser.Log_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_log_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PascalCompilerParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ConstExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PascalCompilerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def constantValue(self):
            return self.getTypedRuleContext(PascalCompilerParser.ConstantValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstExpr" ):
                listener.enterConstExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstExpr" ):
                listener.exitConstExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstExpr" ):
                return visitor.visitConstExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PascalCompilerParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.ExprContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.ExprContext,i)

        def OP_MUL(self):
            return self.getToken(PascalCompilerParser.OP_MUL, 0)
        def OP_DIV(self):
            return self.getToken(PascalCompilerParser.OP_DIV, 0)
        def OP_DIV_INT(self):
            return self.getToken(PascalCompilerParser.OP_DIV_INT, 0)
        def OP_MOD(self):
            return self.getToken(PascalCompilerParser.OP_MOD, 0)
        def OP_AND(self):
            return self.getToken(PascalCompilerParser.OP_AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PascalCompilerParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.ExprContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.ExprContext,i)

        def OP_EQ(self):
            return self.getToken(PascalCompilerParser.OP_EQ, 0)
        def OP_NE(self):
            return self.getToken(PascalCompilerParser.OP_NE, 0)
        def OP_LT(self):
            return self.getToken(PascalCompilerParser.OP_LT, 0)
        def OP_GT(self):
            return self.getToken(PascalCompilerParser.OP_GT, 0)
        def OP_LE(self):
            return self.getToken(PascalCompilerParser.OP_LE, 0)
        def OP_GE(self):
            return self.getToken(PascalCompilerParser.OP_GE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelExpr" ):
                listener.enterRelExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelExpr" ):
                listener.exitRelExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PascalCompilerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SYM_LPAREN(self):
            return self.getToken(PascalCompilerParser.SYM_LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(PascalCompilerParser.ExprContext,0)

        def SYM_RPAREN(self):
            return self.getToken(PascalCompilerParser.SYM_RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PascalCompilerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PascalCompilerParser.ExprContext,0)

        def OP_NOT(self):
            return self.getToken(PascalCompilerParser.OP_NOT, 0)
        def OP_ADD(self):
            return self.getToken(PascalCompilerParser.OP_ADD, 0)
        def OP_SUB(self):
            return self.getToken(PascalCompilerParser.OP_SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PascalCompilerParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PascalCompilerParser.ExprContext)
            else:
                return self.getTypedRuleContext(PascalCompilerParser.ExprContext,i)

        def OP_ADD(self):
            return self.getToken(PascalCompilerParser.OP_ADD, 0)
        def OP_SUB(self):
            return self.getToken(PascalCompilerParser.OP_SUB, 0)
        def OP_OR(self):
            return self.getToken(PascalCompilerParser.OP_OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class DesigExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PascalCompilerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def designator(self):
            return self.getTypedRuleContext(PascalCompilerParser.DesignatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDesigExpr" ):
                listener.enterDesigExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDesigExpr" ):
                listener.exitDesigExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDesigExpr" ):
                return visitor.visitDesigExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PascalCompilerParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                localctx = PascalCompilerParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 322
                self.match(PascalCompilerParser.SYM_LPAREN)
                self.state = 323
                self.expr(0)
                self.state = 324
                self.match(PascalCompilerParser.SYM_RPAREN)
                pass
            elif token in [35, 36, 43]:
                localctx = PascalCompilerParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 326
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8899172237312) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 327
                self.expr(6)
                pass
            elif token in [54, 55, 56, 57, 58]:
                localctx = PascalCompilerParser.ConstExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 328
                self.constantValue()
                pass
            elif token in [59]:
                localctx = PascalCompilerParser.DesigExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 329
                self.designator()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 343
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 341
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = PascalCompilerParser.MulDivExprContext(self, PascalCompilerParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 332
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 333
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4260607557632) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 334
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = PascalCompilerParser.AddSubExprContext(self, PascalCompilerParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 335
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 336
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4501125726208) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 337
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = PascalCompilerParser.RelExprContext(self, PascalCompilerParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 338
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 339
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33822867456) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 340
                        self.expr(4)
                        pass

             
                self.state = 345
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[26] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




