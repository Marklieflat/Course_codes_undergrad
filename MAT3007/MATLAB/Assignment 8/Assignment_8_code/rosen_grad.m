function [x, iter] = rosen_grad(x, tol, sigma, gamma)
%% Objective: minimize 100 * (x(2) - x(1)^2)^2 + (1 - x(1))^2 (Using Gradient Descent Method)

%% Initialize iteration number
iter = 0;

%% Main Iteration
while norm(grad_r(x)) > tol
    %% Doing backtracking search
    d = grad_r(x);
    t = 1;
    
    xtemp = x - t * d;
    while obj_r(xtemp) >= obj_r(x) - gamma * t * grad_r(x)' * d
        t = t * sigma;
        xtemp = x - t * d;
    end
    

    %% Output the solution in each step
    iter = iter + 1
    x = xtemp

end

end

