clc;

%% Define the dimension of the problem
d = 2;

%% Number of points in A
n = 1000;

%% Number of points in B
m = 1000;

%% Generate points in A and B
X = randn(d, n) + [-ones(1, n); ones(1, n)];
Y = randn(d, m) + [ones(1, m); -ones(1, m)];

%% Plot the results
for i = 1:n
    plot(X(1,i), X(2,i), 'bd');
    hold on;
end

for j = 1:m
    plot(Y(1,j), Y(2,j), 'r*');
    hold on;
end

pause

%% Solve the optimization problem
cvx_begin 
variables deltas(n) sigmas(m) a(d) b;
    minimize ones(1,n) * deltas + ones(1,m) * sigmas
        subject to
            X' * a + ones(n,1) * b + deltas >= ones(n,1);
            Y' * a + ones(m,1) * b - sigmas <= -ones(m,1);
            sigmas >= 0, deltas >= 0
cvx_end

xmin = min(min(X(1, :)), min(Y(1,:))) - 0.1;
xmax = max(max(X(2, :)), max(Y(2,:))) + 0.1;
ymin = (-b - a(1) * xmin)/a(2);
ymax = (-b - a(1) * xmax)/a(2);

hold on;
plot([xmin, xmax], [ymin, ymax]);