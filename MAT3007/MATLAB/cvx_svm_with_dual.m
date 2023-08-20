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


%% Solve the optimization problem
cvx_begin quiet
variables deltas(n) sigmas(m) a(d) b;
    minimize ones(1,n) * deltas + ones(1,m) * sigmas
        subject to
            X' * a + ones(n,1) * b + deltas >= ones(n,1);
            Y' * a + ones(m,1) * b - sigmas <= -ones(m,1);
            sigmas >= 0, deltas >= 0
cvx_end

primal_opt = cvx_optval;

%% Solve the dual problem
cvx_begin quiet
variables w(n) v(m);
    maximize sum(w) - sum(v)
        subject to 
        X * w  + Y * v == 0;
        sum(w) + sum(v) == 0;
        0 <= w <= 1;
        -1 <= v <= 0;
cvx_end
dual_opt = cvx_optval;

primal_opt
dual_opt