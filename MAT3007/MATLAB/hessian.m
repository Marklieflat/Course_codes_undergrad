function y = hessian(x)
y = zeros(2,2);
y(1,1) = exp(x(1) + x(2)) + 2;
y(1,2) = exp(x(1) + x(2)) - 1;
y(2,1) = y(1,2);
y(2,2) = exp(x(1) + x(2)) + 6;
