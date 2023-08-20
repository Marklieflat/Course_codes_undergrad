%% Production Planning Problem

cvx_begin 
variables x1  x2;
    maximize x1 + 2 * x2
    subject to 
        x1          <= 100;
             2 * x2 <= 200;
        x1 +     x2 <= 150;
        [x1, x2] >= 0;
cvx_end

[x1  x2]
cvx_optval



%% Production Planning Problem (Alternative syntax)

% c = [1, 2];
% A = [1  0;
%      0  2;
%      1  1];
% b = [100; 200; 150];
% 
% cvx_begin quiet
%     variable x(2)
%     maximize c * x
%     subject to
%         A * x <= b;
%         x >= 0
% cvx_end 
% % 
% x


