{
  [*] ������� ������� ������������
  [*] ���-16-2
  [*] �������: 16
  [*] �������: 139�
}
program matrix2;
const max = 20;
type matrix = array [1..max] of real;
var res  : real; 
    mass : matrix;
    fact : word;
    n    : integer;
begin
  repeat
    write('������� ���������� ��������� ������������������ (�� ������ ', max,'): ');
    readln(n);
  until (n <= max);
  fact := 1;
  res := 0;
  for var i:=1 to n do
  begin
    fact := fact * i;
    res += 1/fact;
    mass[i] :=  i*res;
    writeln('b','[',i,'] = ', mass[i])
  end;
end.