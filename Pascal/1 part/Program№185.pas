{
  [*] ������� ������� ������������
  [*] ���-17-1
  [*] �������: 16
  [*] �������: 185
}

program matrix2;
const max = byte.MaxValue;
type matrix = array [1..max] of real;
var res  : real; 
    mass : matrix;
    n    : integer;
begin
 repeat
    write('������� ������ ������� (�� ����� ', max, '): ');    
    readln(n);
  until (n >= 1) and (n <= max);
  
  res:=0; 
  for var i:=1 to n do
  begin
    write('������� �������� ������� [',i,'] = ');
    readln(mass[i]);    
    if (mass[i] < 0) then mass[i] := 0;    
    res += mass[i]
  end;   

  write(res*2);
end.