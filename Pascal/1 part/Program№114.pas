{
  [*] ������� ������� ������������
  [*] ���-17-1
  [*] �������: 16
  [*] �������: 114a
  [*] ��������� 
}
program XpeHb;
var i:byte; 
  count:real;
begin
  count :=0;
  for i:=1 to 100 do
     count += 1 / sqr(i);
  write(count);
end.