{
  [*] ������� ������� ������������
  [*] ���-16-2
  [*] �������: 16
  [*] �������: 186
  [*] ���������
}
program matrix2;
const max = 999;
type matrix = array [1..max] of real;
var mass : matrix;
    res: real;
    n, fact: integer;
begin
 repeat
    write('������� ������ �������: ');
    readln(n);
  until (n > 0) and (n <= max);
  
  for var i:=1 to n do
  begin
    write('������� �������� ������� [',i,'] = ');
    readln(mass[i]);    
  end;
  fact:=1;
  res:=1;
  for var i:=1 to n do
  begin
    writeln('������ ������� [', i, '] = ', mass[i]);
    fact := fact * i;
    if(i+1 < mass[i]) and (mass[i] < fact) then
      res := res * mass[i];
  end;
    write('��������� = ', abs(1/res));
end.