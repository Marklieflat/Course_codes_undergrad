function [x, iter] = newton_p23(x, tol, sigma, gamma, gamma1, gamma2, color_p, color_line)
%% Objective: minimize x1^4 + 2/3*x1^3 + 1/2*x1^2 - 2*x1^2*x2 + 4/3 * x2^2 (Using Newton's Method)

%% Initialize iteration number
iter = 0;

%% Draw the contour plot
a = -6:0.01:6;
[A,B] = meshgrid(a);
Z = A.^4+(2/3)*A.^3+0.5*A.^2 -2*A.^2.*B+ (4/3)*(B).^2;
hold on

contour(A,B,Z,logspace(-3,4,40));
colorbar;

%% Main Iteration
while norm(grad(x)) > tol
    sk = hess_p23(x) \ grad(x);
    if grad(x)' * sk >= gamma1 * min(1, norm(sk)^gamma2) * norm(sk)^2
        dk = sk;
    else
        dk = grad(x);
    end
    t = 1;
    xtemp = x - t * dk;
    
    while obj(xtemp) >= obj(x) - gamma * t * grad(x)' * dk
        t = t * sigma;
        xtemp = x - t * dk;
    end
    
    %% Make some plots
    plot(x(1), x(2), color_p);
    hold on;
    plot([x(1), xtemp(1)], [x(2), xtemp(2)], color_line);
    hold on;
    
    %% Output the solution in each step
    iter = iter + 1
    x = xtemp
    
end

end

