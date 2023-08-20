c = [5 2 5];
A = [2 3 1;
    1 2 3];
b = [4;7];

cvx_begin quiet
    variable x(3)
    maximize c*x
    subject to
        A*x <= b;
        x >= 0;
cvx_end
x
optval = cvx_optval