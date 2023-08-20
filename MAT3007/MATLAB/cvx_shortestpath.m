%% A code to compute the shortest path given W
%% Make the following line uncommented if you want to make it a function
%% Otherwise keep it commented

%function [x, optval] = cvx_shortestpath(W)

%Input the W matrix
M = 100;
W = [M, 3, 4, M, M, M, M;
    3, M, 2, M, 2, 5, M;
    4, 2, M, 3, M, 6, M;
    M, M, 3, M, 3, 2, M;
    M, 2, M, 3, M, 1, 4;
    M, 5, 6, 2, 1, M, 2;
    M, M, M, M, 4, 2, M];

%% Retrive the size of the problem
[n, ~] = size(W);            

%% Solve the problem
cvx_begin
variables x(n,n)
    minimize sum(sum(W .* x))
    subject to
        sum(x(1,:)) == 1;
        sum(x(:,n)) == 1;
        sum(x(2:n-1,:), 2) - sum(x(:,2:n-1))' == 0;
        0 <= x <= 1
cvx_end
x
optval = cvx_optval