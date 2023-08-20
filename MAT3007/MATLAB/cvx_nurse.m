clc;

%% Nurse scheduling problem

cvx_begin
variables x1 x2 x3 x4 x5 x6 x7;
    minimize x1 + x2 + x3 + x4 + x5 + x6 + x7
    subject to 
        x1           + x4 + x5 + x6 + x7 >= 14
        x1 + x2           + x5 + x6 + x7 >= 15
        x1 + x2 + x3           + x6 + x7 >= 15
        x1 + x2 + x3 + x4           + x7 >= 16
        x1 + x2 + x3 + x4 + x5           >= 12
             x2 + x3 + x4 + x5 + x6      >= 6
                  x3 + x4 + x5 + x6 + x7 >= 7
        [x1,  x2,  x3,  x4,  x5,  x6,  x7] >= 0
cvx_end

[x1, x2, x3, x4, x5, x6, x7]
cvx_optval

% 
% 
% % %% Nurse scheduling problem (matrix formulation)
% % 
% c = ones(1,7);
% A = [1 0 0 1 1 1 1;
%      1 1 0 0 1 1 1;
%      1 1 1 0 0 1 1;
%      1 1 1 1 0 0 1;
%      1 1 1 1 1 0 0;
%      0 1 1 1 1 1 0;
%      0 0 1 1 1 1 1];
% d = [14; 15; 15; 16; 12; 6; 7];
% 
% cvx_begin
%     variable x(7)
%     minimize c * x
%     subject to
%         A * x >= d;
%         x >= 0;
% cvx_end 
% % % 
%  x