{
  [*] ������� ������� ������������
  [*] ���-17-1
  [*] �������: 16
  [*] �������: 223� 
}
program matrix2;
const max = word.MaxValue;
type matrix = array [1..max] of integer;
var mass : matrix;
    n,res: integer;
    sposob: char;
begin  
 
  repeat
    writeln('�������� ������ �����:');
    writeln('1 = ������');
    writeln('2 = ��������������');
    write('������ �����: ');
    readln(sposob);
  until (sposob >= '1') and (sposob <= '2');
    
  res := 0;
  Randomize;
  n:=Random(20) + 1; 
  for var i:=1 to n do
  begin    
    if(sposob = '1') then
    begin
      if(i > 1) and (mass[i-1] < 0) then break;
      repeat      
        write('������� �������� ������� [',i,'] = ');
        readln(mass[i]);      
      until (mass[1] > 0)
    end
    else  
    begin      
      mass[i] := Random(max);
      if(i >= 2) then mass[i] := Random(max) - Random(max)
    end;
    write('������ ������� [',i,'] = ', mass[i]);
    if (mass[i] mod 2 = 0) and (mass[i] mod 4<>0) then
    begin
      res += 1;
      write(' | This');
    end;
    writeln();
  end;  
  writeln('��������� = ', res);
end.