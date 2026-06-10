# Generated from src/parser/PascalCompiler.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PascalCompilerParser import PascalCompilerParser
else:
    from PascalCompilerParser import PascalCompilerParser

# This class defines a complete generic visitor for a parse tree produced by PascalCompilerParser.

class PascalCompilerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PascalCompilerParser#pascalProgram.
    def visitPascalProgram(self, ctx:PascalCompilerParser.PascalProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#executionBlock.
    def visitExecutionBlock(self, ctx:PascalCompilerParser.ExecutionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#declSection.
    def visitDeclSection(self, ctx:PascalCompilerParser.DeclSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#constDeclPart.
    def visitConstDeclPart(self, ctx:PascalCompilerParser.ConstDeclPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#constDecl.
    def visitConstDecl(self, ctx:PascalCompilerParser.ConstDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#varDeclPart.
    def visitVarDeclPart(self, ctx:PascalCompilerParser.VarDeclPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#varDecl.
    def visitVarDecl(self, ctx:PascalCompilerParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#idList.
    def visitIdList(self, ctx:PascalCompilerParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#dataType.
    def visitDataType(self, ctx:PascalCompilerParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#arrayType.
    def visitArrayType(self, ctx:PascalCompilerParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#idxRange.
    def visitIdxRange(self, ctx:PascalCompilerParser.IdxRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#sign.
    def visitSign(self, ctx:PascalCompilerParser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#subprogramDecls.
    def visitSubprogramDecls(self, ctx:PascalCompilerParser.SubprogramDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#subprogramDecl.
    def visitSubprogramDecl(self, ctx:PascalCompilerParser.SubprogramDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#subprogramHeader.
    def visitSubprogramHeader(self, ctx:PascalCompilerParser.SubprogramHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#paramList.
    def visitParamList(self, ctx:PascalCompilerParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#paramGroup.
    def visitParamGroup(self, ctx:PascalCompilerParser.ParamGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#designator.
    def visitDesignator(self, ctx:PascalCompilerParser.DesignatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#compoundStmt.
    def visitCompoundStmt(self, ctx:PascalCompilerParser.CompoundStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#stmtList.
    def visitStmtList(self, ctx:PascalCompilerParser.StmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#AssignStmt.
    def visitAssignStmt(self, ctx:PascalCompilerParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#CompStmt.
    def visitCompStmt(self, ctx:PascalCompilerParser.CompStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#IfStmt.
    def visitIfStmt(self, ctx:PascalCompilerParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#WhileStmt.
    def visitWhileStmt(self, ctx:PascalCompilerParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#ForStmt.
    def visitForStmt(self, ctx:PascalCompilerParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#RepeatStmt.
    def visitRepeatStmt(self, ctx:PascalCompilerParser.RepeatStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#CaseStmt.
    def visitCaseStmt(self, ctx:PascalCompilerParser.CaseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#WriteStmt.
    def visitWriteStmt(self, ctx:PascalCompilerParser.WriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#WritelnStmt.
    def visitWritelnStmt(self, ctx:PascalCompilerParser.WritelnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#ProcCallStmt.
    def visitProcCallStmt(self, ctx:PascalCompilerParser.ProcCallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#caseItem.
    def visitCaseItem(self, ctx:PascalCompilerParser.CaseItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#caseLabels.
    def visitCaseLabels(self, ctx:PascalCompilerParser.CaseLabelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#constantValue.
    def visitConstantValue(self, ctx:PascalCompilerParser.ConstantValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#argList.
    def visitArgList(self, ctx:PascalCompilerParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#log_expr.
    def visitLog_expr(self, ctx:PascalCompilerParser.Log_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#ConstExpr.
    def visitConstExpr(self, ctx:PascalCompilerParser.ConstExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:PascalCompilerParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#RelExpr.
    def visitRelExpr(self, ctx:PascalCompilerParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#ParensExpr.
    def visitParensExpr(self, ctx:PascalCompilerParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#UnaryExpr.
    def visitUnaryExpr(self, ctx:PascalCompilerParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:PascalCompilerParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PascalCompilerParser#DesigExpr.
    def visitDesigExpr(self, ctx:PascalCompilerParser.DesigExprContext):
        return self.visitChildren(ctx)



del PascalCompilerParser