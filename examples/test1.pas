PROGRAM MathTest;
VAR
    n, resultFact, resultFibo: integer;

FUNCTION Factorial(n: integer): integer;
BEGIN
    if n <= 1 then
        Factorial := 1
    else
        Factorial := n * Factorial(n - 1);
END;

FUNCTION Fibonacci(n: integer): integer;
VAR
    a, b, temp, i: integer;
BEGIN
    if n <= 0 then
        Fibonacci := 0
    else if n = 1 then
        Fibonacci := 1
    else
    begin
        a := 0;
        b := 1;
        for i := 2 to n do
        begin
            temp := a + b;
            a := b;
            b := temp;
        end;
        Fibonacci := b;
    end;
END;

BEGIN
    n := 6;
    resultFact := Factorial(n);
    resultFibo := Fibonacci(n);
END.