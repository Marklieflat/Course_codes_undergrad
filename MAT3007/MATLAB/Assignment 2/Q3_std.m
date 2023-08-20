cvx_begin quiet
    variables x1 x2 x3
    maximize x1+4*x2+x3
    subject to
        2*x1 + 2*x2 + x3 <= 4;
        x1 - x3 >= 1;
        [x1 x2 x3] >= 0;
cvx_end
[x1 x2 x3]
optval = cvx_optval