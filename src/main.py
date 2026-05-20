from Translator import *
import sys

def main():
    nazwa_pliku = sys.argv[1]

    with open(nazwa_pliku, "r", encoding="utf-8") as f:
        pascal_code = f.read()
    
    print("--- KOD WEJŚCIOWY (PASCAL) ---")
    print(pascal_code)
    
    # Uruchomienie parsera ANTLR4
    input_stream = InputStream(pascal_code)
    lexer = PascalCompilerLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PascalCompilerParser(token_stream)
    
    # Budowanie drzewa od reguły startowej
    tree = parser.pascalProgram()
    
    # Uruchomienie translatora
    translator = PascalToCTranslator()
    wynik_c = translator.visit(tree)
    
    nazwa_output = nazwa_pliku.replace(".pas", ".c")
    with open(nazwa_output, "w", encoding="utf-8") as f2:
        f2.write(wynik_c)
    f.close()
    f2.close()
    
if __name__ == '__main__':
    main()