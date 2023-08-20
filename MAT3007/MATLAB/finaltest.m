%% 
c = [8 11 6 4];
A = [5 7 4 3];
b = 14;
zero = zeros(4,1);
one = ones(4,1);
cvx_begin quiet
    variable x(4)
    maximize c * x
    subject to
        A*x <= b;
        zero <= x <= one;
        x(3) == 0;
cvx_end
x
optval = cvx_optval

%% 
c = [4 -2 7 -1];
A = [1 0 5 0;
    1 1 -1 0;
    6 -5 0 0;
    -1 0 2 -2];
b = [10;1;0;3];
cvx_solver mosek
cvx_begin quiet
    variable x1 integer
    variable x2 integer
    variable x3 integer
    variable x4
    maximize 4*x1-2*x2+7*x3-x4
    subject to 
        x1 + 5*x3 <= 10;
        x1 + x2 - x3 <= 1;
        6*x1-5*x2 <= 0;
        -x1 + 2*x3 - 2*x4 <= 3;
        [x1 x2 x3 x4] >= 0;
cvx_end
[x1 x2 x3 x4]
optval = cvx_optval
    
