{
  [*] Мигунов Виталий Владимирович
  [*] ИВТ-17-1
  [*] Вариант: 16
  [*] Задание: 684

}
program xpeHb;
const n = 4;
type mass = array [1..n, 1..n] of real;
var matrix:mass;
    max, u:real;
    x,y:integer;
begin
  max:=0;
  
  for var j := 1 to n do 
  begin    
    for var o := 1 to n do 
    begin
      u:= Random * 100 - 50;
      matrix[j, o] := u; 
      write('| ', matrix[j, o]:0:2, ' |'); 
      if(Abs(matrix[j, o]) > max) then 
        begin
          max := Abs(matrix[j, o]);
          x:= j;
          y:= o;
        end;
    end; 
    writeln;     
  end; 
  
  Writeln('Max: ',max:0:2);
  Writeln('Получаем матрицу без строки и столбца значения max');
  
  for var i := 1 to n do 
  begin
   for var j := 1 to n do 
    if(i <> x) and (j <> y) then
    begin
       write('| ', matrix[i, j]:0:2, ' |'); 
     end;      
     writeln;
   end;
end.