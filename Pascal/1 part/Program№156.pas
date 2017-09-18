{
  [*] ������� ������� ������������
  [*] ���-16-2
  [*] �������: 16
  [*] �������: 156�
}
program matrix2;
const max = 40;
type matrix = array [1..max] of real;
var res  : real; 
    mass : matrix;
    n    : integer;
begin
  repeat
    write('������� ���������� ��������� ������������������ (�� ������ ', max,'): ');
    readln(n);
  until (n >= 3) and (n <= max);

  res := 0;
  for var x:=1 to n do
  begin
    mass[x]:= x;
    if x >= 3 then 
    begin
      res += (mass[x-2] + mass[x-1] + mass[x])*mass[x-1];      
    end;
  end;
  writeln('x = ', res)
end.