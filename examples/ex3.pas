program SortowanieTablicy;

var
  MojaTablica : array[1..5] of Integer;
  i, j, temp  : Integer;

begin
  MojaTablica[1] := 42;
  MojaTablica[2] := 12;
  MojaTablica[3] := 89;
  MojaTablica[4] := 23;
  MojaTablica[5] := 11;

  for i := 1 to 4 do
  begin
    for j := 1 to 5 - i do
    begin
      if MojaTablica[j] > MojaTablica[j + 1] then
      begin
        temp := MojaTablica[j];
        MojaTablica[j] := MojaTablica[j + 1];
        MojaTablica[j + 1] := temp;
      end;
    end;
  end;
  writeln('Posortowana tablica:');

  for i := 1 to 5 do
    write(MojaTablica[i], ' ');
  
end.