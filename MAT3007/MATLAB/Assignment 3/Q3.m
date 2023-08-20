c = [2 3 3 1 -2];
A = [1 3 0 4 1;
    1 2 0 -3 1;
    -1 -4 3 0 0];
b = [2;2;1];

cvx_begin quiet
    variable x(5)
    minimize c*x
    subject to
        A*x == b;
        x >= 0;
cvx_end

x
optval = cvx_optval