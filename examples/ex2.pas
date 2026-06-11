program Example;

const
    MAX_SIZE = 10;
    PI = 3.14159;

var
    globalInt, i : integer;
    globalReal : real;
    globalBool : boolean;
    vector : array [1..10] of integer;

function ComputeValue(x : integer) : real;
var
    temp : real;
begin
    if x > 0 then
        temp := x * PI
    else
        temp := -1.0;
    ComputeValue := temp
end;

procedure ProcessVector(limit : integer);
var
    k : integer;
begin
    for k := 1 to limit do
    begin
        vector[k] := k * 2
    end
end;

begin
    globalInt := 10;
    globalBool := false;
    globalReal := 0.0;

    ProcessVector(MAX_SIZE);

    i := 1;
    while i <= MAX_SIZE do
    begin
        globalReal := globalReal + vector[i];
        i := i + 1
    end;

    repeat
        globalInt := globalInt - 1
    until globalInt = 0;

    case globalInt of
        0: globalBool := true;
        1: globalBool := false;
        else globalBool := false
    end
end.