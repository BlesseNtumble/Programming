{
  [*] ������� ������� ������������
  [*] ���-17-1
  [*] �������: 16
  [*] �������: 338�
}
program matrix2;
const max = 15;
type matrix = array [1..max] of integer;
var mass, mass2 : matrix;
    n: integer;
    o, debug: boolean;
    sposob: string;
    label test;
begin
  debug := true;
  n:=Random(max) + 1; 
  repeat
    writeln('�������� ������ �����:');
    writeln('1 = ������');
    writeln('2 = ��������������');
    write('������ �����: ');
    readln(sposob);
  until (sposob = '1') or (sposob = '2');

test:
  if(debug) then writeln('������ �������: ', n);
  for var k:=1 to 2 do
    for var i:=1 to n do
      begin
        if(sposob = '1') then          
          if (k = 1) then
          begin
            write('������� �������� ������� ������� [',i,'] = ');
            readln(mass[i]);
          end
          else
          begin
            write('������� �������� ������� ������� [',i,'] = ');
            readln(mass2[i]);
          end        
        else
          begin
            if(k = 1) then 
            begin
              mass[i] := Random(999) - 666;
              if(debug) then writeln('[DEBUG] ��������� = ', mass[i]);
            end
            else 
            begin
              mass2[i] := Random(999) - 666;
              if(debug) then writeln('[DEBUG] ��������� 2 = ', mass2[i]);
            end;
          end;
      end; 

  for var i:=2 to n do
  begin
    if(mass[i-1] = mass[i]) or (mass2[i-1] = mass[i]) then 
    begin
      writeln('�������� ���� ����� ����������� ���� ��� ��������� ���.');
      writeln('���������� ��������� �������.');
      goto test;
    end;
  end;
  
  o:= false;
  for var i:=1 to n do
  begin    
    if(mass[i] = mass2[i]) then
    begin
      o:= true;
      writeln(mass[i], '|', mass2[i]);
    end;
  end;
  if (o = false) then writeln('���')
  else writeln('��');
end.