function g = gradient_ls(x)

global A;
global b;

g = 2 * A' * A * x - 2 * A' * b; 