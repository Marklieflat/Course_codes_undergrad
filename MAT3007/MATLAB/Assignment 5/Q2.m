%% part 1
cvx_begin quiet
    variables x1 x2
    maximize 4*x1 + x2
    subject to 
        3*x1 + x2 <= 6;
        5*x1 + 3*x2 <= 15;
        [x1 x2] >= 0;
cvx_end
[x1 x2]
optval = cvx_optval

%% part 2
b = [6 15];
A = [3 5;
    1 3];
c = [4;1];

cvx_begin quiet
    variable y(2)
    minimize b*y
    subject to
        A*y >= c;
        y >= 0;
cvx_end
y
optval = cvx_optval


