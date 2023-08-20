function y = gradient(x)

y1 = exp(x(1) + x(2)) + 2 * x(1) - x(2);
y2 = exp(x(1) + x(2)) + 6 * x(2) - x(1);
y = [y1; y2];