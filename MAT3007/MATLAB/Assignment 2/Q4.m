e = ones(5,1);
pi = [0.75 0.35 0.40 0.75 0.65];
q = [10;5;10;10;5];
A = [1 1 1 0 0;
    0 0 0 1 1;
    1 0 1 0 1;
    1 1 1 1 0;
    0 1 0 1 1];

cvx_begin quiet
    variables x(5) s 
    maximize s - pi * x
    subject to
        s * e - A'* x <= 0;
        0 <= x <= q;
cvx_end
x
s
optval = cvx_optval