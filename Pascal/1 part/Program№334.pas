program XpeHb;
var count:real;  
begin
  count :=0;
  for var i:=1 to 100 do
    for var j:=1 to 60 do
    begin
      count+= sin((sqr(i)*i) + sqr(sqr(j)));
    end;  
  write(count);
end.