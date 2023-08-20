cvx_begin
    variables x1 x2
    maximize x1+x2
    subject to
        -x1 + x2 <= 2.5;
        x1 + 2*x2 <= 8;
        0 <= x1 <= 4;
        0 <= x2 <= 3;
cvx_end
[x1 x2]
optval = cvx_optval