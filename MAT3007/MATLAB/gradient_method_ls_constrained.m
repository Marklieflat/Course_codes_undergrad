%% Objective: minimize ||Ax - b||^2 subject to Wd == z (Using Gradient Descent Method)

m = 100;
n = 10;
d = 3;

global A;
global b;

A = rand(m, n);
b = rand(m, 1);
W = rand(d, n);
z = W * ones(n, 1); % make sure that ones(n, 1) is a feasible solution

%% Setting initial points
x = ones(n, 1);

%% Setting tolerance factor epsilon
epsilon = 10^(-5);

%% Initialize iteration number
iter = 0;

%% Setting backtracking search parameter 
alpha = 0.5;
beta = 0.5;

PA = eye(n) - W' * inv(W * W') * W;

%% Main Iteration
while norm(PA * gradient_ls(x)) > epsilon
    
    %% Doing backtracking search
    t = 1;
    d = PA * gradient_ls(x);
    xtemp = x - t * d;
    while f_ls(xtemp) >= f_ls(x) - alpha * t * gradient_ls(x)' * d % backtracking stopping crieterion
        t = t * beta; % update the step size
        xtemp = x - t * d;
    end
  
    %% Output the solution in each step
    iter = iter + 1
    x = xtemp;
end

cvx_begin
    variables x_cvx(n)
    minimize norm(A * x_cvx - b, 2)
    subject to 
        W * x_cvx == z
cvx_end 

x 
x_cvx
