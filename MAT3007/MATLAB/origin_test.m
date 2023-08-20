cvx_solver mosek
cvx_begin quiet
    variables x1 x2 x3 x4
    minimize x2 - 1/2 * x3 + x4
    subject to
        x1 + x2 + 3*x3 == 1;
        x3 - x4 == -3;
        x1 + 2*x3 - x4 <= 0;
        [x1 x2 x3 x4] >= 0;
cvx_end
[x1 x2 x3 x4]
optval = cvx_optval
