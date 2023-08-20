% Objective: minimize exp(x1 + x2) + x1^2 + 3x2^2 - x1x2

function y = f(x)
y = exp(x(1) + x(2)) + x(1)^2 + 3 * x(2)^2 - x(1) * x(2);