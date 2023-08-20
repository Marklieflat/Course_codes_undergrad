cvx_begin
variables y1 y2 y3 y4 x1 x2 x3;
minimize 2*x2 + y1
subject to 
    y1 >= x1 - x3;
    y1 >= x3 - x1;
    y2 >= x1 + 2;
    y2 >= -x1 - 2;
    y3 >= x2;
    y3 >= -x2;
    y2 + y3 <= 5;
    y4 >= x3;
    y4 >= -x3;
    y4 <= 1;
cvx_end

[y1 y2 y3 y4 x1 x2 x3]
cvx_optval