x = -2:0.01:2;
[X,Y] = meshgrid(x);
Z = X.^4+(2/3)*X.^3+0.5*X.^2 -2*X.^2.*Y+ (4/3)*(Y).^2;
t = -2:0.01:3;
figure;
hold on

contour(X,Y,Z,logspace(-2,3,40))

