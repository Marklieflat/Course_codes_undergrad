%% Objective: minimize 100 * (x(2) - x(1)^2)^2 + (1 - x(1))^2 (Using Newton's Method)

%% Setting initial points 
x = [-1; -0.5];

%% Setting tolerance factor epsilon
tol = 10^(-7);

%% Initialize iteration number
iter = 0;

%% Setting backtracking search parameter 
sigma = 0.5;
gamma = 10^(-4);
gamma1 = 10^(-6);
gamma2 = 0.1;
ft = 1; % Indicator for full step
nd = 1;

%% Main Iteration
while norm(grad_r(x)) > tol
    sk = hess_r(x) \ grad_r(x);
    if grad_r(x)' * sk >= gamma1 * min(1, norm(sk)^gamma2) * norm(sk)^2
        dk = sk;
    else
        dk = grad_r(x);
        nd = 0;
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
        
    %% Make some plots
    plot(x(1), x(2), '*r');
    hold on;
    plot([x(1), xtemp(1)], [x(2), xtemp(2)], '-g');
    hold on;
    
    %% Output the solution in each step
    iter = iter + 1
    x = xtemp
    
end
