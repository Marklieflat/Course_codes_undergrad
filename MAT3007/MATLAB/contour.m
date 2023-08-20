% Created on Mon Apr 04 2022
% @author: Guokai Li

x = linspace(-5.5, -4, 100);
y = linspace(0.4, 1, 100);
[X, Y] = meshgrid(x, y);
Z = 8*X + 12*Y + 2*X.*Y + X.^2 - 2*Y.^2;
figure;
hold on;
contourf(X, Y, Z, 10);
plot(-14/3, 2/3, 'rx');
colorbar();
xlabel('x');
ylabel('y');
hold off;

figure;
surf(X, Y, Z);
hold on;
plot3(-14/3, 2/3, -44/3, 'rx')
hold off;