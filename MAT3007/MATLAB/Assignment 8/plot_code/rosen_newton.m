function [x, iter] = rosen_newton(x, tol, sigma, gamma, gamma1, gamma2)
%% Objective: minimize 100 * (x(2) - x(1)^2)^2 + (1 - x(1))^2 (Using Newton's Method)

%% Initialize iteration number
iter = 0;

%% Setting backtracking search parameter
ft = 1; % Indicator for full step

%% Main Iteration
while norm(grad_r(x)) > tol
    sk = hess_r(x) \ grad_r(x);
    if grad_r(x)' * sk >= gamma1 * min(1, norm(sk)^gamma2) * norm(sk)^2
        dk = sk;
    else
        dk = grad_r(x);
    end
    t = 1;
    xtemp = x - t * dk;
    
    while obj_r(xtemp) >= obj_r(x) - gamma * t * grad_r(x)' * dk
        t = t * sigma;
        xtemp = x - t * dk;
    end
    if t ~= 1
        ft = 0;
    end
        
    %% Output the solution in each step
    iter = iter + 1
    x = xtemp
    
end
end

