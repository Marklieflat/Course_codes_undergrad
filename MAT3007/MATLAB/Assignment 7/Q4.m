% cvx_solver mosek
cvx_begin quiet
    variables y1 y2 y3 z
    minimize z
    subject to
        log(exp(2*y1-0.5*y2)+2*exp(0.5*y2-y3)) <= 0;
        log(exp(2*y3-y1+y2)) <= 0;
        log(exp(y1-y2)) - log(z) <= 0;
        log(exp(0.5*y3-y2)) - log(z) <= 0;
cvx_end
[y1 y2 y3]
z
optval = cvx_optval




