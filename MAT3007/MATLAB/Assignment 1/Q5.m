c = ones(1,10);
A = [1 1 0 0 0 0 0 0 0 0;
    1 0 0 0 1 0 0 0 0 0;
    1 0 0 0 0 1 0 0 0 0;
    0 1 1 0 0 0 0 0 0 0;
    0 1 0 0 0 0 1 0 0 0;
    0 0 1 1 0 0 0 0 0 0;
    0 0 0 1 1 0 0 0 0 0;
    0 0 0 1 0 0 0 0 1 0;
    0 0 0 0 1 0 0 0 0 1;
    0 0 0 0 0 1 0 1 0 0;
    0 0 0 0 0 1 0 0 1 0;
    0 0 0 0 0 0 1 0 1 0;    
    0 0 0 0 0 0 1 0 0 1;
    0 0 0 0 0 0 0 1 0 1];
d = ones(14,1);

cvx_solver mosek
cvx_begin quiet
    variable x(10) integer
    minimize c * x
    subject to
        A * x >= d;
        0 <= x <= 1;
cvx_end
x
optval = cvx_optval





