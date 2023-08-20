c = [7.8, 7.1];
A = [1/4, 1/3;
    1/8, 1/3];
b = [90; 80];

cvx_begin
    variable x(2)
    maximize c*x
    subject to
        A*x <= b;
        x >= 0;
cvx_end
x
optval = cvx_optval


