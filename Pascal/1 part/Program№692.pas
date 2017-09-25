{
  [*] Мигунов Виталий Владимирович
  [*] ИВТ-17-1
  [*] Вариант: 16
  [*] Задание: 692e

}
program xpeHb;
const n = 5;
type mass = array [1..n, 1..n] of real;
var matrix:mass;
    max:real;
begin
max:=0;
for var i := 1 to n do 
  begin    
    for var j := 1 to n do 
    begin
      matrix[i, j] := Random * 100; 
      write('| ', matrix[i, j]:0:2, ' |');
      
      if ((j<=i) and (n-i+1>=j)) or ((j>=i) and (n-i+1<=j)) then
      begin
        if(matrix[i, j] > max) then max:=matrix[i,j];
        Write('X');
      end;
    end; 
    writeln;     
  end; 
  writeln(max:0:2); 
end.