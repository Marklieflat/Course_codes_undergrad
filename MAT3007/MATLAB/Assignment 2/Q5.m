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

b = [0;6;10;18;11;7;0;-1];   % represent the intersection of the line

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
% The intersection part with the B matrix
cvx_begin quiet
    variables r y(2)
    maximize r
    subject to
        A * y <= b;
        r * e - B * y - c <= 0;
cvx_end
r
y

        



