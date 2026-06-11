from Translator import *
from SemanticAnalyzer import *
import sys

def main():
    nazwa_pliku = sys.argv[1]

    with open(nazwa_pliku, "r", encoding="utf-8") as f:
        pascal_code = f.read()
    
    print("KOD WEJŚCIOWY (PASCAL)")
    print(pascal_code)
    
    # Uruchomienie parsera ANTLR4
    input_stream = InputStream(pascal_code)
    lexer = PascalCompilerLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PascalCompilerParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ParserErrorListener())
    # Budowanie drzewa od reguły startowej
    try:
        tree = parser.pascalProgram()
        translator = PascalToCTranslator()
        wynik_c = translator.visit(tree)
        semantic = SemanticAnalyzer()
        semantic.visit(tree)
        nazwa_output = nazwa_pliku.replace(".pas", ".c")

        with open(nazwa_output, "w", encoding="utf-8") as f2:
            f2.write(wynik_c)

        print("\nKOD WYJŚCIOWY (C)")
        print(wynik_c)
        print("\nTranslacja zakończona sukcesem.")
        f2.close()

    except PascalSyntaxError as e:
        print(e)
    
    except PascalSemanticError as e:
        print(e)

    except Exception as e:
        print(f"\n[NIEOCZEKIWANY BŁĄD]\n{e}")
    f.close()
    
    
if __name__ == '__main__':
    main()