import sys
from antlr4 import *
from parser.PascalCompilerLexer import PascalCompilerLexer
from parser.PascalCompilerParser import PascalCompilerParser
from parser.PascalCompilerVisitor import PascalCompilerVisitor

# =====================================================================
# TWÓJ TRANSLATOR (z funkcją IF z poprzedniej wiadomości)
# =====================================================================
class PascalToCTranslator(PascalCompilerVisitor):
    
    # Główny punkt startowy dla całego programu
    def visitPascalProgram(self, ctx):
        # Odwiedza blok wykonawczy (executionBlock)
        return self.visit(ctx.executionBlock())

    def visitExecutionBlock(self, ctx):
        # Interesuje nas tylko kod z bloku begin...end
        return self.visit(ctx.compoundStmt())

    def visitCompoundStmt(self, ctx):
        # Odwiedza listę instrukcji w środku
        return self.visit(ctx.stmtList())

    def visitStmtList(self, ctx):
        # Zbiera przetłumaczone instrukcje oddzielone średnikami
        instructions = []
        for stmt_ctx in ctx.statement():
            if stmt_ctx.getText(): # Pomija puste instrukcje
                translated = self.visit(stmt_ctx)
                if translated:
                    instructions.append(translated)
        return "\n    ".join(instructions)

    # GOTOWA FUNKCJA IF
    def visitIfStmt(self, ctx):
        condition_code = self.visit(ctx.expr())
        then_instruction = self.visit(ctx.statement(0))
        
        c_code = f"if ({condition_code}) {{\n    {then_instruction}\n}}"
        
        if ctx.KW_ELSE():
            else_instruction = self.visit(ctx.statement(1))
            c_code += f" else {{\n    {else_instruction}\n}}"
            
        return c_code

    # ŻEBY IF DZIAŁAŁ, MUSIMY OBSŁUŻYĆ PROSTE WYRAŻENIA I PRZYPISANIE:
    def visitRelExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        op = ctx.op.text
        right = self.visit(ctx.expr(1))
        
        if op == '<>': op = '!='
        elif op == '=': op = '=='
        return f"{left} {op} {right}"

    def visitAssignStmt(self, ctx):
        variable = ctx.designator().getText()
        value = self.visit(ctx.expr())
        return f"{variable} = {value};"

    def visitConstExpr(self, ctx):
        return ctx.constantValue().getText()

    def visitDesigExpr(self, ctx):
        return ctx.designator().getText()


# =====================================================================
# FUNKCJA TESTUJĄCA W KONSOLI
# =====================================================================
