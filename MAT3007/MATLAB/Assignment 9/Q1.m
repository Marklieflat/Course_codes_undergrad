c = [2500 3000 1400 1600 3200];
one = ones(5,1);
cvx_solver mosek
cvx_begin quiet
    variable x1(5) binary 
    variable x2(5) binary
    variable x3(5) binary
    minimize 10 * max(0,2800 - c * x1) + 6 * max(0,4200 - c * x2) + 8 * max(0,5000 - c * x3)
    subject to
        2800 - c * x1 <= 500;
        4200 - c * x2 <= 400;
        5000 - c * x3 <= 300;
        x1 + x2 + x3 == one;
cvx_end
x = [x1 x2 x3]
optval = cvx_optval
        