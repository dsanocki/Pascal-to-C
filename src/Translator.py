import sys
from antlr4 import *
from parser.PascalCompilerLexer import PascalCompilerLexer
from parser.PascalCompilerParser import PascalCompilerParser
from parser.PascalCompilerVisitor import PascalCompilerVisitor
from parser.PascalErrorListener import ParserErrorListener, PascalSyntaxError

class PascalToCTranslator(PascalCompilerVisitor):
    def __init__(self):
        # Flaga używana do zamiany pascalowego przypisania do nazwy funkcji (NazwaFunkcji := wartosc) 
        # na instrukcję "return wartosc;" w C.
        self.current_function = None 

    def visitPascalProgram(self, ctx):
        # Importy wymagane w języku C
        c_code = "#include <stdio.h>\n#include <stdbool.h>\n#include <string.h>\n\n"
        
        exec_block = ctx.executionBlock()

        # Deklaracje globalne (stałe, zmienne, procedury, funkcje)
        if exec_block.declSection():
            c_code += self.visit(exec_block.declSection()) + "\n"

        # Główna funkcja programu
        c_code += "int main() {\n"
        main_stmts = self.visit(exec_block.compoundStmt())
        
        if main_stmts:
            for line in main_stmts.split('\n'):
                if line.strip():
                    c_code += f"    {line}\n"
                    
        c_code += "    return 0;\n}\n"
        return c_code

    def visitExecutionBlock(self, ctx):
        code = ""
        if ctx.declSection():
            code += self.visit(ctx.declSection()) + "\n"
        code += self.visit(ctx.compoundStmt())
        return code

    def visitDeclSection(self, ctx):
        code = ""
        if ctx.constDeclPart():
            code += self.visit(ctx.constDeclPart()) + "\n"
        if ctx.varDeclPart():
            code += self.visit(ctx.varDeclPart()) + "\n"
        if ctx.subprogramDecls():
            code += self.visit(ctx.subprogramDecls()) + "\n"
        return code

    def visitConstDeclPart(self, ctx):
        return "\n".join([self.visit(decl) for decl in ctx.constDecl()])

    def visitConstDecl(self, ctx):
        name = ctx.IDENTIFIER().getText()
        val = ctx.constantValue().getText()
        sign = ctx.sign().getText() if ctx.sign() else ""
        return f"#define {name} {sign}{val}"

    def visitVarDeclPart(self, ctx):
        return "\n".join([self.visit(decl) for decl in ctx.varDecl()])

    def visitVarDecl(self, ctx):
        ids = self.visit(ctx.idList())
        c_type, is_array, arr_sizes = self.visit(ctx.dataType())

        decls = []
        for var_id in ids:
            if is_array:
                size_str = "".join([f"[{size}]" for size in arr_sizes])
                decls.append(f"{c_type} {var_id}{size_str};")
            else:
                decls.append(f"{c_type} {var_id};")
                
        return "\n".join(decls)

    def visitIdList(self, ctx):
        return [node.getText() for node in ctx.IDENTIFIER()]

    def visitDataType(self, ctx):
        # Zwraca krotkę: (typ_w_C, czy_to_tablica, rozmiary_tablicy)
        if ctx.arrayType():
            c_type, sizes = self.visit(ctx.arrayType())
            return (c_type, True, sizes)

        type_map = {
            'integer': 'int',
            'real': 'float',
            'boolean': 'bool',
            'char': 'char',
            'longint': 'long',
            'string': 'char*'
        }
        pascal_type = ctx.getText().lower()
        return (type_map.get(pascal_type, 'void'), False, [])

    def visitArrayType(self, ctx):
        sizes = [self.visit(rng) for rng in ctx.idxRange()]
        c_type, _, _ = self.visit(ctx.dataType())
        return c_type, sizes

    def visitIdxRange(self, ctx):
        max_val = ctx.constantValue(1).getText()
        return f"{max_val} + 1"

    def visitSubprogramDecls(self, ctx):
        return "\n\n".join([self.visit(decl) for decl in ctx.subprogramDecl()])

    def visitSubprogramDecl(self, ctx):
        header = self.visit(ctx.subprogramHeader())
        
        # Zapisujemy nazwę bieżącej funkcji, by móc podmienić 'Nazwa := ' na 'return'
        self.current_function = header['name']

        body = self.visit(ctx.executionBlock())

        formatted_body = "{\n"
        if body:
            for line in body.split('\n'):
                if line.strip():
                    formatted_body += f"    {line}\n"
        formatted_body += "}"

        self.current_function = None
        return f"{header['signature']} {formatted_body}"


    def visitSubprogramHeader(self, ctx):
        name = ctx.IDENTIFIER().getText()
        is_func = ctx.KW_FUNCTION() is not None

        params = self.visit(ctx.paramList()) if ctx.paramList() else ""

        if is_func:
            ret_type, _, _ = self.visit(ctx.dataType())
        else:
            ret_type = "void"

        return {
            'name': name,
            'signature': f"{ret_type} {name}({params})"
        }

    def visitParamList(self, ctx):
        params = []
        for group in ctx.paramGroup():
            params.extend(self.visit(group))
        return ", ".join(params)

    def visitParamGroup(self, ctx):
        # Jeśli argument jest podany jako VAR, do funkcji w C przesyłamy wskaźnik
        is_var = ctx.KW_VAR() is not None
        ids = self.visit(ctx.idList())
        c_type, is_array, _ = self.visit(ctx.dataType())

        res = []
        for param_id in ids:
            if is_var and not is_array:
                res.append(f"{c_type}* {param_id}")
            elif is_array:
                res.append(f"{c_type} {param_id}[]")
            else:
                res.append(f"{c_type} {param_id}")
        return res

    def visitCompoundStmt(self, ctx):
        stmts = self.visit(ctx.stmtList())
        return stmts if stmts else ""

    def visitStmtList(self, ctx):
        instructions = []
        for stmt_ctx in ctx.statement():
            if stmt_ctx.getText():
                translated = self.visit(stmt_ctx)
                if translated:
                    instructions.append(translated)
        return "\n".join(instructions)

    def visitCompStmt(self, ctx):
        inner = self.visit(ctx.compoundStmt())
        formatted = "{\n"
        if inner:
            for line in inner.split('\n'):
                if line.strip():
                    formatted += f"    {line}\n"
        formatted += "}"
        return formatted

    def visitAssignStmt(self, ctx):
        desig = self.visit(ctx.designator())
        expr = self.visit(ctx.expr())

        # Konwersja Pascalowego zwracania funkcji przez przypisanie (np. MojaFunkcja := 5)
        if self.current_function and desig.lower() == self.current_function.lower():
            return f"return {expr};"

        return f"{desig} = {expr};"


    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.expr())
        then_stmt = self.visit(ctx.statement(0))

        then_block = self.wrap_in_braces(then_stmt)
        code = f"if ({cond}) {then_block}"

        if ctx.KW_ELSE():
            else_stmt = self.visit(ctx.statement(1))
            
            if else_stmt.strip().startswith("if "):
                code += f" else {else_stmt}"
            else:
                else_block = self.wrap_in_braces(else_stmt)
                code += f" else {else_block}"

        return code

    def visitWhileStmt(self, ctx):
        cond = self.visit(ctx.expr())
        stmt = self.visit(ctx.statement())
        
        block = self.wrap_in_braces(stmt)
        return f"while ({cond}) {block}"

    def visitForStmt(self, ctx):
        id_name = ctx.IDENTIFIER().getText()
        start_expr = self.visit(ctx.expr(0))
        end_expr = self.visit(ctx.expr(1))
        stmt = self.visit(ctx.statement())
        
        block = self.wrap_in_braces(stmt)

        if ctx.KW_TO():
            return f"for ({id_name} = {start_expr}; {id_name} <= {end_expr}; {id_name}++) {block}"
        else:
            return f"for ({id_name} = {start_expr}; {id_name} >= {end_expr}; {id_name}--) {block}"
        

    def visitRepeatStmt(self, ctx):
        stmts = self.visit(ctx.stmtList())
        cond = self.visit(ctx.expr())
        
        formatted = "{\n"
        if stmts:
            for line in stmts.split('\n'):
                if line.strip():
                    formatted += f"    {line}\n"
        formatted += "}"
        return f"do {formatted} while (!({cond}));"

    def visitCaseStmt(self, ctx):
        cond = self.visit(ctx.expr())
        code = f"switch ({cond}) {{\n"

        for case_item in ctx.caseItem():
            code += self.visit(case_item)

        if ctx.KW_ELSE():
            else_stmt = self.visit(ctx.statement())
            code += f"    default:\n"
            for line in else_stmt.split('\n'):
                if line.strip():
                    code += f"        {line}\n"
            code += f"        break;\n"

        code += "}"
        return code

    def visitCaseItem(self, ctx):
        labels = self.visit(ctx.caseLabels())
        stmt = self.visit(ctx.statement())
        code = ""
        
        for lbl in labels:
            code += f"    case {lbl}:\n"
            
        for line in stmt.split('\n'):
            if line.strip():
                code += f"        {line}\n"
        
        # W C musimy samodzielnie wymusić przerwanie pętli case
        code += "        break;\n"
        return code

    def visitCaseLabels(self, ctx):
        raw_text = ctx.getText()
        return raw_text.split(',')

    def visitProcCallStmt(self, ctx):
        return f"{self.visit(ctx.designator())};"


    def visitParensExpr(self, ctx):
        return f"({self.visit(ctx.expr())})"

    def visitUnaryExpr(self, ctx):
        op = ctx.getChild(0).getText().lower()
        expr = self.visit(ctx.expr())
        if op == 'not': op = '!'
        return f"{op}{expr}"

    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text.lower()
        
        if op == 'div': op = '/'
        elif op == 'mod': op = '%'
        elif op == 'and': op = '&&'
        return f"{left} {op} {right}"

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text.lower()
        
        if op == 'or': op = '||'
        return f"{left} {op} {right}"

    def visitRelExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        
        if op == '=': op = '=='
        elif op == '<>': op = '!='
        return f"{left} {op} {right}"

    def visitConstExpr(self, ctx):
        return self.visit(ctx.constantValue())

    def visitConstantValue(self, ctx):
        val = ctx.getText()
        if val.lower() == 'true': return 'true'
        if val.lower() == 'false': return 'false'
        
        # Poprawka formatu stringów: w Pascalu są ' ', a w C muszą być " "
        if val.startswith("'") and val.endswith("'"):
            inner = val[1:-1].replace("''", "'")
            return f'"{inner}"'
            
        return val

    def visitDesigExpr(self, ctx):
        return self.visit(ctx.designator())

    def visitDesignator(self, ctx):
        name = ctx.IDENTIFIER().getText()
        code = name

        if ctx.SYM_LBRACKET():
            for expr in ctx.expr():
                idx = self.visit(expr)
                code += f"[{idx}]"
        elif ctx.SYM_LPAREN():
            args = self.visit(ctx.argList()) if ctx.argList() else ""
            code += f"({args})"

        return code


    def visitArgList(self, ctx):
        return ", ".join([self.visit(expr) for expr in ctx.expr()])


    def wrap_in_braces(self, code_str):
        if code_str.strip().startswith("{") and code_str.strip().endswith("}"):
            return code_str
        
        lines = code_str.split('\n')
        indented_lines = []
        for line in lines:
            if line.strip():
                indented_lines.append(f"    {line}")
            else:
                indented_lines.append(line)
                
        return "{\n" + "\n".join(indented_lines) + "\n}"


