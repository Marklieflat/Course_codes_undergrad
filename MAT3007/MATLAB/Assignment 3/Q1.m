cvx_solver mosek
cvx_begin quiet
    variables x1 x2 x3 s1 s2 s3
    maximize 500*x1 + 250*x2 + 600*x3
    subject to 
        2*x1 + x2 + x3 + s1 == 240;
        3*x1 + x2 + 2*x3 + s2 == 150;
        x1 + 2*x2 + 4*x3 + s3 == 180;
        [x1, x2, x3, s1, s2, s3] >= 0;
cvx_end

[x1 x2 x3 s1]
format rat
optval = cvx_optval