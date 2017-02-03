program xpeHb;
const n = 8;
type matrix = array [1..n, 1..n] of integer;
var mass : matrix;
    sposob: string;
begin

 repeat
    writeln('Выберите способ ввода:');
    writeln('1 = ручной');
    writeln('2 = автоматический');
    write('Способ ввода: ');
    readln(sposob);
  until (sposob = '1') or (sposob = '2');
  
  for var i:=1 to n do
  begin 
    write('||'); 
    for var j:=1 to n do
    begin
      if(sposob = '1') then
      begin
        write('Введите значение массива [',j,'] = ');
        readln(mass[i, j]);
      end
      else
      begin
        mass[i, j] := Random(999) - 666;              
      end;       
        mass[1, j] := 1;
        if(i > 1) then write(' ', mass[i, j] * i, ' ')
        else write(' ', mass[i, j], ' ');
                 
    end;
    write('||');
    writeln; 
  end;
end.