{
  [*] ������� ������� ������������
  [*] ���-17-1
  [*] �������: 16
  [*] �������: 201a
  [*] ���� ����������� ����� n, �������������� ����� a1,...,an. ��������:
    �) max (a1,...,an);
}
program matrix2;
const max = byte.MaxValue;
type matrix = array [1..max] of real;
var mass : matrix;
    res: real;
    n: integer;
begin
 repeat
    write('������� ������ ������� (�� ����� ', max, '): ');
    readln(n);
  until (n > 0) and (n <= max);
  
  res := 0;
  for var i:=1 to n do
  begin
    write('������� �������� ������� [',i,'] = ');
    readln(mass[i]);  
    if(mass[i] > res) then     
      res := mass[i];    
  end;
  write('��������� = ', res);
end.