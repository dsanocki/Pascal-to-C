grammar PascalCompiler;

options { caseInsensitive=true; }

pascalProgram    : KW_PROGRAM IDENTIFIER SYM_SEMI executionBlock SYM_DOT ;
executionBlock   : declSection compoundStmt ;
declSection      : constDeclPart? varDeclPart? subprogramDecls ;

constDeclPart    : KW_CONST constDecl+ ;
constDecl        : IDENTIFIER OP_EQ sign? constantValue SYM_SEMI ;

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
    | KW_IF log_expr KW_THEN statement (KW_ELSE statement)?                 # IfStmt
    | KW_WHILE log_expr KW_DO statement                                     # WhileStmt
    | KW_FOR IDENTIFIER SYM_ASSIGN expr (KW_TO | KW_DOWNTO) expr KW_DO statement # ForStmt
    | KW_REPEAT stmtList KW_UNTIL log_expr                                  # RepeatStmt
    | KW_CASE expr KW_OF caseItem+ (KW_ELSE statement SYM_SEMI?)? KW_END # CaseStmt
    | KW_WRITE SYM_LPAREN argList? SYM_RPAREN                           # WriteStmt
    | KW_WRITELN SYM_LPAREN argList? SYM_RPAREN                         # WritelnStmt
    | designator                                                        # ProcCallStmt
    ;

caseItem         : caseLabels SYM_COLON statement SYM_SEMI ;
caseLabels       : (sign? constantValue) (SYM_COMMA sign? constantValue)* ;
constantValue    : INT_NUMBER | REAL_NUMBER | CHAR_LIT | STRING_LIT | BOOL_CONST ;
argList          : expr (SYM_COMMA expr)* ;

log_expr
    : expr
    ;

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
KW_WRITE   : 'write';
KW_WRITELN : 'writeln';

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
REAL_NUMBER : [0-9]+ '.' [0-9]+ ([e][+-]?[0-9]+)? | [0-9]+ [e][+-]?[0-9]+ ;
INT_NUMBER  : [0-9]+ ;
IDENTIFIER  : [a-z_] [a-z0-9_]* ;

COMMENT     : ('{' .*? '}' | '(*' .*? '*)' | '//' ~[\r\n]* ) -> skip ;
WS          : [ \t\r\n]+ -> skip ;