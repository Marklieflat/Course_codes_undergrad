%% part 1
c = [200 300 100];
b = [100;120];
A = [3 2 6;
    2 4 8];

cvx_begin quiet
    variable x(3)
    maximize c*x
    subject to
        A*x <= b;
        x >= 0;
cvx_end
x
% format rat
optval = cvx_optval

%% part 2
c = [100 120];
b = [200;300;100];
A = [3 2;
    2 4;
    6 8];

cvx_begin quiet
    variable y(2)
    minimize c*y
    subject to
        A*y >= b;
        y >= 0;
cvx_end
y
% format rat
optval = cvx_optval




