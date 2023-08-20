%% Objective: minimize exp(x1 + x2) + x1^2 + 3x2^2 - x1x2 (Using Newton's Method)
clc;

%% Setting initial points
x = [0; 0];

%% Setting tolerance factor epsilon
epsilon = 10^(-5);

%% Initialize iteration number
iter = 0;
alpha = 0.5;
beta = 0.5;

%% Main Iteration
while norm(gradient(x)) > epsilon
    
    dk = inv(hessian(x)) * gradient(x); % If changed to gradient(x) only, then it is the gradient descent method
	t = 1;
    xtemp = x - t * dk;
    
    while f(xtemp) >= f(x) - alpha * t * gradient(x)' * dk % backtracking stopping crieterion
        t = t * beta; % update the step size
        xtemp = x - t * dk;
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

% resize the window
    axis([-0.5, 0.1, -0.3, 0.1])
    hold on;