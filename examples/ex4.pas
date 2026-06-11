program test15;

var
    i : integer;
    sum : integer;

function Add(a, b : integer) : integer;
begin
    Add := a + b;
end;

begin
    sum := 0;

    for i := 1 to 5 do
    begin
        sum := Add(sum, i);
    end;

    while sum < 100 do
    begin
        sum := sum + 10;
        writeln(sum);
    end;
end.
