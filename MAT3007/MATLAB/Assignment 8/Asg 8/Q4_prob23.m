%% Objective: minimize  (Using Newton's Method)

%% Setting initial points 
x = [3; 3];

%% Setting tolerance factor epsilon
tol = 10^(-5);

%% Initialize iteration number
iter = 0;

%% Setting backtracking search parameter 
sigma = 0.5;
gamma = 0.1;
gamma1 = 10^(-6);
gamma2 = 0.1;

%% Draw the contour plot
a = -3:0.01:5;
[A,B] = meshgrid(a);
Z = A.^4+(2/3)*A.^3+0.5*A.^2 -2*A.^2.*B+ (4/3)*(B).^2;
figure;
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
    plot(x(1), x(2), '*r');
    hold on;
    plot([x(1), xtemp(1)], [x(2), xtemp(2)], '-g');
    hold on;
    
    %% Output the solution in each step
    iter = iter + 1
    x = xtemp
    
end