% To find the optimal solution to exp(-x) * x / (1 + exp(-x))
% The gradient = exp(-x) * (1 + exp(-x) - x) / (1 + exp(-x))^2
 
%% Bisection method
xl = 0;
xr = 5;
while xr - xl > 10^(-5) 
    xm = 0.5 * (xl + xr);
    % We only care about the sign of the gradient
    if (1 + exp(-xm) - xm) > 0 
        xl = xm;
    else
        xr = xm;
    end
end
solution = xm 

%% Golden section method

xl = 0;
xr = 5;
phi = (3 - sqrt(5)) / 2;
while xr - xl > 10^(-5)
    x1 = phi * xr + (1 - phi) * xl;
    x2 = phi * xl + (1 - phi) * xr;
    if  exp(-x1) * x1 / (1 + exp(-x1)) <  exp(-x2) * x2 / (1 + exp(-x2))
        xl = x1;
    else
        xr = x2;
    end
end
solution = (xl + xr) / 2

%% Plot the result

plotx = 0:0.01:5;
ploty = exp(-plotx) .* plotx ./ (1 + exp(-plotx));
plot(plotx, ploty);
hold on;
plot(solution, exp(-solution) * solution / (1 + exp(-solution)),'rd');
