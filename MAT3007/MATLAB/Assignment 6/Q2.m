A = [0 0.25 1 1 0 -0.5;
    0 0 0 1 1 -0.5];
B = [0 0.5 2 2 0 -1;
     0 0 0 2 2 -1;
     -1 -1 -1 -1 -1 -1];
 cvx_solver mosek
 cvx_begin quiet
    variable y(3)
    s = 0;
    for i = 1:6
        s = s + power(sum(power(norm(A(:,i)),2) - B(:,i)'* y),2);
    end
    minimize s
cvx_end
y
x = y([1 2])
r = (norm(x)^2 - y(3))^(0.5)
optval = cvx_optval


u = -pi: 0.001: pi;
x0 = x(1) + r*cos(u);
y0 = x(2) + r*sin(u);
plot(x0,y0);
xlabel('x');
ylabel('y');
axis equal;
grid on;
hold on;
axis([-2 2, -2, 2])
ax = [0 0.25 1 1 0 -0.5];  
ay = [0 0 0 1 1 -0.5];
scatter(ax,ay);
hold off;


    
    
    
    
    