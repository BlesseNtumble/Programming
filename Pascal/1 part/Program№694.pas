{
  [*] Мигунов Виталий Владимирович
  [*] ИВТ-17-1
  [*] Вариант: 16
  [*] Задание: 694к
}
program xpeHb;
const n = 9;
type mass = array [1..n, 1..n] of integer;
var matrix:mass;
k:integer;
mode:char;
begin
  repeat
  Write('Select mode (a or k): '); Readln(mode);
  until (mode = 'a') or (mode = 'k');
  case mode of
  'a': begin
        for var j := 1 to n do 
        begin    
          for var o := 1 to n do 
          begin
          k:=o;
          if(j > 1) then
              begin
                k:=(o-j)+1;
                if((j = 2) and (o = n - 1)) or ((j = n - 1) and (o = 2))then
                  k:=0;
              end;         
            matrix[j, o] := k; 
            write('| ', matrix[j, o], ' |'); 
          end; 
          writeln;    
        end;
       end;
       
  'k': begin
        for var j := 1 to n do 
        begin    
          for var o := 1 to n do 
          begin
            k:=o;
              if(j > 1) and not(j = n)then
              begin
                k:=(o-j)+1;
                if(j = 2) and (o = n) then
                  k:=0;
              end;
              matrix[j, o] := k; 
              write('| ', matrix[j, o], ' |'); 
          end; 
          writeln;     
        end;
       end;
  end;
  
end.