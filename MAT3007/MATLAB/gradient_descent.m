%% Objective: minimize exp(x1 + x2) + x1^2 + 3x2^2 - x1x2 (Using Gradient Descent Method)

%% Setting initial points 
x = [0; 0];

%% Setting tolerance factor epsilon
epsilon = 10^(-5);

%% Initialize iteration number
iter = 0;

%% Setting backtracking search parameter 
alpha = 0.5;
beta = 0.5;


%% Main Iteration
while norm(gradient(x)) > epsilon
    
    %% Doing backtracking search
    d = gradient(x);
    t = 1;
    
    xtemp = x - t * d;
    while f(xtemp) >= f(x) - alpha * t * gradient(x)' * d % backtracking stopping crieterion
        t = t * beta; % update the step size
        xtemp = x - t * d;
    end
       
 % Doing exact line search
%     xl = x;
%     xr = x - 10 * gradient(x);
%     phi = (3 - sqrt(5)) / 2;
%     while norm(xr - xl) > 10^(-6)
%         x1 = phi * xr + (1 - phi) * xl;
%         x2 = phi * xl + (1 - phi) * xr;
%         if  f(x1) >  f(x2)
%             xl = x1;
%         else
%             xr = x2;
%         end
%     end
%     
%    xtemp = (xr + xl) / 2;

    
    %% Make some plots
    plot(x(1), x(2), '*r');
    hold on;
    plot([x(1), xtemp(1)], [x(2), xtemp(2)], '-g');
    hold on;
    
    %% Output the solution in each step
    
    iter = iter + 1
    x = xtemp
    
end

% Resize the window
     axis([-0.9, 0.1, -0.5, 0.1])
     hold on;