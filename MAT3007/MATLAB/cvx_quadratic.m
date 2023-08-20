%% Quadratic function

cvx_begin
variables x1 x2 
maximize ((x1 - 1)^2 + (x2 - 1)^2)
subject to 
        x1 + x2 == 1
cvx_end

[x1  x2]


% cvx_begin
% variables x1 x2 
% minimize exp(x1 + x2) + (x1 - 0.5 * x2)^2 + 2.75 * x2^2
% subject to 
%         x1 + 2 * x2 == 1
% cvx_end
% 
% [x1  x2]