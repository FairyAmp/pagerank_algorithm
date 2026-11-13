n = 5;
A = rand(n);
%disp(A);

x = rand(n,1);
%disp(x);

b = A*x;
%disp(b);


function [iter,y_final] = power_method(A,x);
iter = 0;
%n=length(x) or norm(x);
y_final = zeros(n,1);
y_final = x;
%epsilon = preset tolerance
epsilon = 1e-8;
    while(1)
        old_iter = iter;
        y_final = A*y_final;
        iter = max(y_final);
        y_final = y_final/iter;
     if (iter-old_iter)<epsilon
         break;
     end
    end
end






