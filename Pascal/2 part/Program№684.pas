program xpeHb;
const n = 3;
type mass = array [1..n, 1..n] of real;
var matrix:mass;
    max:real;
begin
  for var j := 1 to 3 do 
  begin
    write('||'); 
    for var o := 1 to 3 do 
    begin      
      matrix[j, o] := Random * 100; 
      write(' ', matrix[j, o], ' ');       
    end; 
    write('||'); 
    writeln; 
  end; 
  writeln; 
end.