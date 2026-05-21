from antlr4.error.ErrorListener import ErrorListener


class PascalSyntaxError(Exception):
    pass


class ParserErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):

        token = offendingSymbol.text if offendingSymbol else "UNKNOWN"

        custom_msg = f"\n[BŁĄD SKŁADNI]\n"
        custom_msg += f"Linia: {line}, kolumna: {column}\n"
        custom_msg += f"Niepoprawny token: '{token}'\n"

        lower_msg = msg.lower()

        if "missing 'then'" in lower_msg:
            custom_msg += "Brakuje THEN po instrukcji IF."

        elif "missing 'do'" in lower_msg:
            custom_msg += "Brakuje DO po WHILE albo FOR."

        elif "missing ';'" in lower_msg:
            custom_msg += "Brakuje średnika ';'."

        elif "extraneous input" in lower_msg:
            custom_msg += f"Nieoczekiwany token '{token}'."

        elif "mismatched input" in lower_msg:
            custom_msg += f"Niepoprawna składnia w pobliżu '{token}'."

        elif "missing 'end'" in lower_msg:
            custom_msg += "Brakuje END."

        elif "no viable alternative" in lower_msg:
            custom_msg += "Parser nie potrafi zinterpretować tej instrukcji."

        else:
            custom_msg += f"Szczegóły ANTLR: {msg}"

        raise PascalSyntaxError(custom_msg)