%% Objective: minimize x1^4 + 2/3*x1^3 + 1/2*x1^2 - 2*x1^2*x2 + 4/3 * x2^2 (Using Gradient Descent Method)

%% Setting initial points 
x = [3;3];

%% Setting tolerance factor epsilon
tol_1 = 10^(-5);

%% Initialize iteration number
iter = 0;

%% Setting backtracking search parameter 
sigma = 0.5;
gamma = 0.1;

%% Main Iteration
while norm(grad(x)) > tol_1
    %% Doing backtracking search
    d = grad(x);
    t = 1;
    
    xtemp = x - t * d;
    while obj(xtemp) >= obj(x) - gamma * t * grad(x)' * d
        t = t * sigma;
        xtemp = x - t * d;
    end
    
    %% Doing exact line search
%     xl = x;
%     xr = x - 10 * grad(x);
%     phi = (3 - sqrt(5)) / 2;
%     maxit = 100;
%     it = 0;
%     tol_2 = 10^(-6);
%     while norm(xr - xl) > tol_2
%         x1 = phi * xr + (1 - phi) * xl;
%         x2 = phi * xl + (1 - phi) * xr;
%         if  obj(x1) >  obj(x2)
%             xl = x1;
%         else
%             xr = x2;
%         end
%         it = it + 1;
%         if it == maxit
%             break;
%         end
%     end
%     
%    xtemp = (xr + xl) / 2;
%    a = 2;
%    if xtemp > a
%        xtemp = a;
%    end
       
   
   %% Output the solution in each step
   iter = iter + 1
   x = xtemp

    %% Make some plots
    plot(x(1), x(2), '*r');
    hold on;
    plot([x(1), xtemp(1)], [x(2), xtemp(2)], '-g');
    hold on;
    
   
end


