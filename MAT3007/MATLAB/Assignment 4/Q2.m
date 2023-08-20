%% Problem 2 part 1
b = zeros(4, 1);
A = [1 0 -1 -1 0;
    0 1 1 0 -1;
    -1 -1 0 0 0;
    0 0 0 1 1];
w = [8; 7; 2; 4; 12];
y = [0; 0; 1; -1];

cvx_begin quiet
    variables x(5) delta
    maximize delta
    subject to
        A*x + delta*y == b;
        0 <= x <= w;
cvx_end
x
optval = cvx_optval
%% Problem 2 part 2
cvx_begin quiet
    variables y1 y2 y3 y4 z12 z13 z23 z24 z34
    minimize 8*z12 + 7*z13 + 2*z23 + 4*z24 + 12*z34
    subject to
        y1 - y4 == 1;
        z12 >= y1 - y2;
        z13 >= y1 - y3;
        z23 >= y2 - y3;
        z24 >= y2 - y4;
        z34 >= y3 - y4;
        [z12 z13 z23 z24 z34] >= 0;
cvx_end
[z12 z13 z23 z24 z34]
optval = cvx_optval





