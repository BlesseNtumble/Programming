program matrix2;
const max = 999;
type matrix = array [1..max] of real;
var mass : matrix;
    res: real;
    n: integer;
begin
 repeat
    write('������� ������ �������: ');
    readln(n);
  until (n > 0) and (n <= max);
  
  res := 0;
  for var i:=1 to n do
  begin
    write('������� �������� ������� [',i,'] = ');
    readln(mass[i]);  
    if(mass[i] > res) then 
    begin
      res := mass[i];
    end
  end;
  write('��������� = ', res);
end.