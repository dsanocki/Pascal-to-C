# Pascal To C Compiler

## Zespół
1. Dawid Sanocki – dsanocki@student.agh.edu.pl  
2. Bartosz Płoszczyński – bploszcz@student.agh.edu.pl  

## Założenia programu

### Ogólne cele programu
Celem projektu jest stworzenie kompilatora, który tłumaczy kod Pascala na język C.

### Rodzaj translatora
- Kompilator

### Planowany wynik działania programu
- konwerter języka Pascal do kodu w języku C  

### Planowany język implementacji
- Python

### Generator parsera
- ANTLR4

## Opis tokenów

| Nazwa tokenu | Regex / Definicja | Opis |
|--------------|------------------|------|
| KW_PROGRAM   | `"program"`      | początek programu |
| KW_CONST     | `"const"`        | sekcja stałych |
| KW_VAR       | `"var"`          | sekcja zmiennych |
| KW_BEGIN     | `"begin"`        | początek bloku |
| KW_END       | `"end"`          | koniec bloku |
| KW_IF        | `"if"`           | instrukcja warunkowa |
| KW_THEN      | `"then"`         | część warunku |
| KW_ELSE      | `"else"`         | alternatywa |
| KW_WHILE     | `"while"`        | pętla while |
| KW_DO        | `"do"`           | ciało pętli |
| KW_FOR       | `"for"`          | pętla for |
| KW_TO        | `"to"`           | zakres rosnący |
| KW_DOWNTO    | `"downto"`       | zakres malejący |
| KW_PROCEDURE | `"procedure"`    | deklaracja procedury |
| KW_FUNCTION  | `"function"`     | deklaracja funkcji |
| KW_REPEAT    | `"repeat"`       | początek pętli repeat |
| KW_UNTIL     | `"until"`        | warunek zakończenia |
| KW_CASE      | `"case"`         | instrukcja wyboru |
| KW_OF        | `"of"`           | część case/array |
| KW_ARRAY     | `"array"`        | deklaracja tablicy |
| TYPE_INT     | `"integer"`      | typ całkowity |
| TYPE_REAL    | `"real"`         | typ rzeczywisty |
| TYPE_BOOL    | `"boolean"`      | typ logiczny |
| TYPE_CHAR    | `"char"`         | typ znakowy |
| TYPE_LONG    | `"longint"`      | typ długi całkowity |
| TYPE_STRING  | `"string"`       | typ tekstowy |
| OP_EQ        | `"="`            | równość |
| OP_NE        | `"<>"`           | nierówność |
| OP_LE        | `"<="`           | mniejsze lub równe |
| OP_LT        | `"<"`            | mniejsze niż |
| OP_GE        | `">="`           | większe lub równe |
| OP_GT        | `">"`            | większe niż |
| OP_ADD       | `"+"`            | dodawanie |
| OP_SUB       | `"-"`            | odejmowanie |
| OP_MUL       | `"*"`            | mnożenie |
| OP_DIV       | `"/"`            | dzielenie |
| OP_DIV_INT   | `"div"`          | dzielenie całkowite |
| OP_MOD       | `"mod"`          | modulo |
| OP_AND       | `"and"`          | koniunkcja |
| OP_OR        | `"or"`           | alternatywa |
| OP_NOT       | `"not"`          | negacja |
| SYM_ASSIGN   | `":="`           | przypisanie |
| SYM_SEMI     | `";"`            | separator instrukcji |
| SYM_COMMA    | `","`            | separator |
| SYM_DOTDOT   | `".."`           | zakres |
| SYM_DOT      | `"."`            | koniec programu |
| SYM_LPAREN   | `"("`            | nawias otwierający |
| SYM_RPAREN   | `")"`            | nawias zamykający |
| SYM_LBRACKET | `"["`            | nawias kwadratowy otwierający |
| SYM_RBRACKET | `"]"`            | nawias kwadratowy zamykający |
| SYM_COLON    | `":"`            | separator typu |
| CHAR_LIT     | `'\'' ( '\'\'' \| ~['\r\n] ) '\''` | literał znakowy |
| STRING_LIT   | `'\'' ( '\'\'' \| ~['\r\n] )* '\''` | literał tekstowy |
| BOOL_CONST   | `"true" \| "false"` | stała logiczna |
| REAL_NUMBER | `[0-9]+ '.' [0-9]+ ([eE][+-]?[0-9]+)?`<br>`\| [0-9]+ [eE][+-]?[0-9]+` | liczba rzeczywista |
| INT_NUMBER   | `[0-9]+`         | liczba całkowita |
| IDENTIFIER   | `[a-zA-Z_][a-zA-Z0-9_]*` | identyfikator |
| COMMENT      | `{...} \| (*...*) \| //...` | komentarz (pomijany) |
| WS           | `[ \t\r\n]+`     | białe znaki (pomijane) |

## Gramatyka

```antlr
grammar PascalCompiler;

options { caseInsensitive=true; }

pascalProgram    : KW_PROGRAM IDENTIFIER SYM_SEMI executionBlock SYM_DOT ;
executionBlock   : declSection compoundStmt ;
declSection      : constDeclPart? varDeclPart? subprogramDecls ;

constDeclPart    : KW_CONST constDecl+ ;
constDecl        : IDENTIFIER SYM_EQ sign? constantValue SYM_SEMI ;

varDeclPart      : KW_VAR varDecl+ ;
varDecl          : idList SYM_COLON dataType SYM_SEMI ;
idList           : IDENTIFIER (SYM_COMMA IDENTIFIER)* ;

dataType         : TYPE_INT | TYPE_REAL | TYPE_BOOL | TYPE_CHAR | TYPE_LONG | TYPE_STRING | arrayType ;
arrayType        : KW_ARRAY SYM_LBRACKET idxRange (SYM_COMMA idxRange)* SYM_RBRACKET KW_OF dataType ;
idxRange         : sign? constantValue SYM_DOTDOT sign? constantValue ;
sign             : OP_ADD | OP_SUB ;

subprogramDecls  : subprogramDecl* ;
subprogramDecl   : subprogramHeader SYM_SEMI executionBlock SYM_SEMI ;
subprogramHeader : KW_PROCEDURE IDENTIFIER paramList?
                 | KW_FUNCTION IDENTIFIER paramList? SYM_COLON dataType ;

paramList        : SYM_LPAREN paramGroup (SYM_SEMI paramGroup)* SYM_RPAREN ;
paramGroup       : KW_VAR? idList SYM_COLON dataType ;

designator       : IDENTIFIER (SYM_LBRACKET expr (SYM_COMMA expr)* SYM_RBRACKET)*
                 | IDENTIFIER (SYM_LPAREN argList? SYM_RPAREN)? ;

compoundStmt     : KW_BEGIN stmtList KW_END ;
stmtList         : statement? (SYM_SEMI statement?)* ;

statement
    : designator SYM_ASSIGN expr                                        # AssignStmt
    | compoundStmt                                                      # CompStmt
    | KW_IF expr KW_THEN statement (KW_ELSE statement)?                 # IfStmt
    | KW_WHILE expr KW_DO statement                                     # WhileStmt
    | KW_FOR IDENTIFIER SYM_ASSIGN expr (KW_TO | KW_DOWNTO) expr KW_DO statement # ForStmt
    | KW_REPEAT stmtList KW_UNTIL expr                                  # RepeatStmt
    | KW_CASE expr KW_OF caseItem+ (KW_ELSE statement SYM_SEMI?)? KW_END # CaseStmt
    | designator                                                        # ProcCallStmt
    ;

caseItem         : caseLabels SYM_COLON statement SYM_SEMI ;
caseLabels       : (sign? constantValue) (SYM_COMMA sign? constantValue)* ;
constantValue    : INT_NUMBER | REAL_NUMBER | CHAR_LIT | STRING_LIT | BOOL_CONST ;
argList          : expr (SYM_COMMA expr)* ;

expr
    : SYM_LPAREN expr SYM_RPAREN                                        # ParensExpr
    | (OP_NOT | OP_ADD | OP_SUB) expr                                   # UnaryExpr
    | expr op=(OP_MUL | OP_DIV | OP_DIV_INT | OP_MOD | OP_AND) expr     # MulDivExpr
    | expr op=(OP_ADD | OP_SUB | OP_OR) expr                            # AddSubExpr
    | expr op=(OP_EQ | OP_NE | OP_LT | OP_GT | OP_LE | OP_GE) expr      # RelExpr
    | constantValue                                                     # ConstExpr
    | designator                                                        # DesigExpr
    ;


KW_PROGRAM : 'program';
KW_CONST   : 'const';
KW_VAR     : 'var';
KW_BEGIN   : 'begin';
KW_END     : 'end';
KW_IF      : 'if';
KW_THEN    : 'then';
KW_ELSE    : 'else';
KW_WHILE   : 'while';
KW_DO      : 'do';
KW_FOR     : 'for';
KW_TO      : 'to';
KW_DOWNTO  : 'downto';
KW_PROCEDURE : 'procedure';
KW_FUNCTION  : 'function';
KW_REPEAT  : 'repeat';
KW_UNTIL   : 'until';
KW_CASE    : 'case';
KW_OF      : 'of';
KW_ARRAY   : 'array';

TYPE_INT    : 'integer';
TYPE_REAL   : 'real';
TYPE_BOOL   : 'boolean';
TYPE_CHAR   : 'char';
TYPE_LONG   : 'longint';
TYPE_STRING : 'string';

OP_EQ      : '=';
OP_NE      : '<>';
OP_LE      : '<=';
OP_LT      : '<';
OP_GE      : '>=';
OP_GT      : '>';
OP_ADD     : '+';
OP_SUB     : '-';
OP_MUL     : '*';
OP_DIV     : '/';
OP_DIV_INT : 'div';
OP_MOD     : 'mod';
OP_AND     : 'and';
OP_OR      : 'or';
OP_NOT     : 'not';

SYM_ASSIGN   : ':=';
SYM_SEMI     : ';';
SYM_COMMA    : ',';
SYM_DOTDOT   : '..';
SYM_DOT      : '.';
SYM_LPAREN   : '(';
SYM_RPAREN   : ')';
SYM_LBRACKET : '[';
SYM_RBRACKET : ']';
SYM_COLON    : ':';

CHAR_LIT    : '\'' ( '\'\'' | ~['\r\n] ) '\'' ;
STRING_LIT  : '\'' ( '\'\'' | ~['\r\n] )* '\'' ;
BOOL_CONST  : 'true' | 'false' ;
REAL_NUMBER : [0-9]+ '.' [0-9]+ ([eE][+-]?[0-9]+)? | [0-9]+ [eE][+-]?[0-9]+ ;
INT_NUMBER  : [0-9]+ ;
IDENTIFIER  : [a-zA-Z_] [a-zA-Z0-9_]* ;

COMMENT     : ('{' .*? '}' | '(*' .*? '*)' | '//' ~[\r\n]* ) -> skip ;
WS          : [ \t\r\n]+ -> skip ;
