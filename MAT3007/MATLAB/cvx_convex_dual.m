%% Input of the problem
m = 100;
n = 1000;

A = rand(m, n);
b = - 10 * rand(m, 1);

%% Primal problem
cvx_begin 
variable x(n)
minimize sum_square(x)
subject to 
    A * x <= b
cvx_end

primal_opt = cvx_optval
b = b';

%% Dual problem
cvx_begin quiet
variable lambda(m)
maximize -0.25 * sum_square(A' * lambda) - b * lambda
subject to 
        lambda >= 0
cvx_end 
dual_opt = cvx_optval

