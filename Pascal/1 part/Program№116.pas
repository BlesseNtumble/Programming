{
  [*] ������� ������� ������������
  [*] ���-17-1
  [*] �������: 16
  [*] �������: 116�
  [*] ���� ���������� ����� n, �������������� ����� x. ���������:
}
program XpeHb;
const one = 1;
var
  n, fac: integer;
  x, all: real;
 
begin
  repeat
  write('������� ����������� �����: ');  readln(n);
  until (n > 0);
  
  write('������� �������������� �����: ');  readln(x);
  fac := one;
  all := 0;
  for var i := one to n do
  begin    
    all += (one / fac) + sqrt(abs(x));  
    fac := fac * i;
  end;  
  write(all);
end.