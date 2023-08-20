%% Problem 1

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

%% Problem 4

W = [0, 10, 12, 17, 34;
    10, 0, 18, 8, 46;
    12, 18, 0, 9, 27;
    17, 8, 9, 0, 20;
    34, 46, 27, 20, 0];
a = [115;385;410;480;610];
b = [200;500;800;200;300];

cvx_begin
    variable x(5,5)
    minimize sum(sum(W .* x))
    subject to
        sum(x,2) == a;
        sum(x)' == b;
        sum(sum(x)) == 2000;
        x >= 0;
cvx_end
x
optval = cvx_optval

%% Problem 5

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

cvx_begin
    variable x(10)
    minimize c * x
    subject to
        A * x >= d;
        0 <= x <= 1;
cvx_end
x
optval = cvx_optval


