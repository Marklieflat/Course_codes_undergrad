%% Least squares problem

m = 100;
n = 5;
d = 2;

X = rand(m, n);
y = rand(m, 1);
W = rand(d, n);
xi = rand(d, 1);

% %% Unconstrained problem
% cvx_begin
% variable beta1(n)
% minimize norm(X * beta1 - y)
% cvx_end
% 
% beta_unconstrained = beta1
% beta_KKT = inv(X' * X) * X' * y


%% Constrained problem
cvx_begin
variable beta2(n)
minimize norm(X * beta2 - y)
subject to 
        W * beta2 == xi
cvx_end 

beta_constrained = beta2
temp = inv([W, zeros(d); X' * X, -0.5 * W']) * [xi; X' * y];
beta_KKT2 = temp(1:n)
