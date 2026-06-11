from parser.PascalCompilerVisitor import PascalCompilerVisitor
from parser.SemanticErrors import PascalSemanticError


class SemanticAnalyzer(PascalCompilerVisitor):

    def __init__(self):
        # słowniki na symbole
        self.variables = {}   # zmienne globalne/lokalne
        self.constants = {}   # stałe z const
        self.functions = {}   # funkcje
        self.procedures = {}  # procedury

    # pomocnicza normalizacja nazw
    def norm(self, name):
        # wszystko na małe litery
        return name.lower().strip()

    # PROGRAM START
    def visitPascalProgram(self, ctx):
        # start analizy całego programu
        return self.visitChildren(ctx)

    # STAŁE (const)
    def visitConstDecl(self, ctx):
        try:
            text = ctx.getText()
            parts = text.split(";")  # czasem kilka stałych w jednej deklaracji

            for p in parts:
                if "=" in p:
                    name, val = p.split("=")
                    name = self.norm(name)

                    # zapisujemy stałą do tabeli
                    self.constants[name] = val.strip()

        except Exception:
            pass

        return None

    # ZMIENNE (var)
    def visitVarDecl(self, ctx):
        var_type = ctx.dataType().getText().lower()

        for id_node in ctx.idList().IDENTIFIER():
            name = self.norm(id_node.getText())

            # nie pozwalamy na duplikaty
            if name in self.variables:
                raise PascalSemanticError(f"Zmienna '{name}' już istnieje")

            # zapis zmiennej do tabeli symboli
            self.variables[name] = var_type

        return None

    # FUNKCJE / PROCEDURY
    def visitSubprogramDecl(self, ctx):
        header = ctx.subprogramHeader()
        name = self.norm(header.IDENTIFIER().getText())

        # liczymy parametry
        param_count = 0
        if header.paramList():
            for g in header.paramList().paramGroup():
                param_count += len(g.idList().IDENTIFIER())

        # funkcja
        if header.KW_FUNCTION():
            self.functions[name] = {
                "param_count": param_count,
                "return_type": header.dataType().getText().lower()
            }

        # procedura
        else:
            self.procedures[name] = {
                "param_count": param_count
            }

        return None

    # DESIGNATOR (zmienna / wywołanie funkcji)
    def visitDesignator(self, ctx):

        name = self.norm(ctx.getChild(0).getText())
        has_args = ctx.argList() is not None

        if has_args:
            actual = len(ctx.argList().expr()) if ctx.argList() else 0

            # funkcja
            if name in self.functions:
                expected = self.functions[name]["param_count"]

            # procedura
            elif name in self.procedures:
                expected = self.procedures[name]["param_count"]

            else:
                raise PascalSemanticError(f"Nieznana funkcja/procedura '{name}'")

            # sprawdzamy liczbę argumentów
            if expected != actual:
                raise PascalSemanticError(
                    f"[BŁĄD] '{name}' oczekuje {expected}, dostał {actual}"
                )

            return None

        if name in self.variables:
            return None

        if name in self.constants:
            return None

        # jak nic nie pasuje -> błąd
        raise PascalSemanticError(f"Niezadeklarowana zmienna '{name}'")

    # PRZYPISANIE
    def visitAssignStmt(self, ctx):

        name = self.norm(ctx.designator().getChild(0).getText())

        # sprawdzamy czy zmienna istnieje
        if name not in self.variables:
            raise PascalSemanticError(f"Niezadeklarowana zmienna '{name}'")

        # przechodzimy po prawej stronie (walidacja wyrażeń)
        return self.visitChildren(ctx)

    # WYRAŻENIA
    def visitExpr(self, ctx):
        return self.visitChildren(ctx)