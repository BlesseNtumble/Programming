{
  [*] ������� ������� ������������
  [*] ���-16-2
  [*] �������: 16
  [*] �������: 82
  [*] ���� �������������� ����� �. ���������:
}
program xpeHb;
var
  x, p1, p2: real; 
  i, j: integer;

begin
  write('������� X: '); 
  readln(x); 
  i := 1; 
  p1 := 1;
  p2 := 1; 
  j := 2;
  while i <= 6 do 
  begin
    if(i <= 5) then
    begin
      p1 := p1 * (x - i); 
      i := 2 * i + 1; 
    end;
    p2 := p2 * (x - j); 
    j := 2 * i; 
  end; 
  
  writeln('��������� = ', (p2 / p1):0:3); 
end.