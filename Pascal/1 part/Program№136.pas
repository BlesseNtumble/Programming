{
  [*] ������� ������� ������������
  [*] ���-17-1
  [*] �������: 16
  [*] �������: 136�
  [*] ���� ����������� ����� n, �������������� ����� a1,..., an.	���������:
}
program XpeHb;
const n = word.MaxValue;
var a:real;
    ar: array [1..n] of real;
    count:integer;
begin
  repeat
    write('������� ���-�� ��������: '); readln(count);
  until(count > 0) and (count < n);
  
  a:=0;
  for var i:=1 to count do 
  begin
    write('������� ������ [',i,']: ');
    readln(ar[i]);
  end;
  
  for var i:=1 to n do 
      a += ar[i];   
      
  write('���������: ', a);
end.
