%% Problem 4

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

%% Problem 5

% x = [0 0 4 8 11 11 7 1 0];  % Plot the points and draw lines between them
% y = [1 6 10 10 7 4 0 0 1];
% plot(x,y,'-or')

A = [-1 0;        % represent the coefficient of the line expression
    -1 1;
    0 1;
    1 1;
    1 0;
    1 -1;
    0 -1
    -1 -1];

b = [0;6;10;18;11;7;0;-1];   % represent the intercept of the line

B = [1 0;                   % represent the point-to-line distance without
    1/sqrt(2) -1/sqrt(2);   % absolute values in order to make the 
    0 -1;                   % problem convex
    -1/sqrt(2) -1/sqrt(2);
    -1 0;
    -1/sqrt(2) 1/sqrt(2);
    0 1
    1/sqrt(2) 1/sqrt(2)];

e = ones(8,1); 

c = [0;6/sqrt(2);10;18/sqrt(2);11;7/sqrt(2);0;-1/sqrt(2)];
% The intercept part with the B matrix

cvx_begin quiet
    variables r y(2)
    maximize r
    subject to
        A * y <= b;
        r * e - B * y - c <= 0;
cvx_end
r
y
