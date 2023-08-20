%% Objective: minimize 100 * (x(2) - x(1)^2)^2 + (1 - x(1))^2 (Using Gradient Descent Method)

%% Setting initial points 
x = [-1; -0.5];

%% Setting tolerance factor epsilon
tol_1 = 10^(-7);

%% Initialize iteration number
iter = 0;

%% Setting backtracking search parameter 
sigma = 0.5;
gamma = 0.1;

%% Main Iteration
while norm(grad_r(x)) > tol_1
    %% Doing backtracking search
    d = grad_r(x);
    t = 1;
    
    xtemp = x - t * d;
    while obj_r(xtemp) >= obj_r(x) - gamma * t * grad_r(x)' * d
        t = t * sigma;
        xtemp = x - t * d;
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