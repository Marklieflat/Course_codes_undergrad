%% Objective: minimize x1^4 + 2/3*x1^3 + 1/2*x1^2 - 2*x1^2*x2 + 4/3 * x2^2 (Using Gradient Descent Method)

%% Setting initial points 
x = [3; 3];

%% Setting tolerance factor epsilon
tol_1 = 10^(-5);

%% Initialize iteration number
iter = 0;

%% Setting backtracking search parameter 
sigma = 0.5;
gamma = 0.1;
epsilon = 10^(-6);
m = 75;
vec1 = zeros(m,1);
vec2 = zeros(m,1);

%% Draw the contour plot
a = -3:0.01:4;
[A,B] = meshgrid(a);
Z = A.^4+(2/3)*A.^3+0.5*A.^2 -2*A.^2.*B+ (4/3)*(B).^2;
figure;
hold on

contour(A,B,Z,logspace(-3,4,40));
colorbar;

%% Main Iteration
while norm(grad(x)) > tol_1
    %% Doing backtracking search
    g = grad(x);
    module = mod(iter, m) + 1;
    vec1(module) = g(1)^2;
    vec2(module) = g(2)^2;
    sum1 = sum(sum(vec1));
    sum2 = sum(sum(vec2));
    v = zeros(2,1);
    v(1) = sqrt(epsilon+sum1);
    v(2) = sqrt(epsilon+sum2);
    Dk = diag(v);
    d = Dk \ grad(x);
    t = 1;
    
    xtemp = x - t * d;
    while obj(xtemp) >= obj(x) - gamma * t * grad(x)' * d
        t = t * sigma;
        xtemp = x - t * d;
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