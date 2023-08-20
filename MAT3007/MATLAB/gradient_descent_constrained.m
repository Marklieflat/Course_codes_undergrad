%% Objective: minimize exp(x1 + x2) + x1^2 + 3x2^2 - x1x2 subject to x1 + 2x2 = 1 (Using Gradient Descent Method)

clc;
%% Setting initial points (have to be feasible)
x = [1; 0];

%% Setting tolerance factor epsilon
epsilon = 10^(-5);

%% Initialize iteration number
iter = 0;

%% Setting backtracking search parameter 
alpha = 0.5;
beta = 0.5;

PA = [0.8, -0.4; -0.4, 0.2];

%% Main Iteration
while norm(PA * gradient(x)) > epsilon
    
    %% Doing backtracking search
    d = PA * gradient(x);
    t = 1;
    
    xtemp = x - t * d;
    while f(xtemp) >= f(x) - alpha * t * gradient(x)' * d % backtracking stopping crieterion
        t = t * beta; % update the step size
        xtemp = x - t * d;
    end
    
    %% Make some plots
    plot(x(1), x(2), '*r');     hold on;
    plot([x(1), xtemp(1)], [x(2), xtemp(2)], '-g');     hold on;
    
    %% Output the solution in each step
    iter = iter + 1
    x = xtemp;
    
end


cvx_begin 
variables x1 x2
minimize exp(x1 + x2) + (x1 - 0.5 * x2)^2 + 2.75 * x2^2 
subject to 
    x1 + 2 * x2 == 1
cvx_end

gradient_projection_x = x
cvx_x = [x1 x2]
