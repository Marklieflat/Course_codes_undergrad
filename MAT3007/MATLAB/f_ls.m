function v = f_ls(x)

global A;
global b;

v = norm(A * x - b, 2)^2;