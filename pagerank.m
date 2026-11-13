n = 12;
alpha = 0.85;
% Q1. hyperlink to G
%{
 1 A
 2 B
 3 C
 4 D
 5 E
 6 F
 7 G
 8 H
 9 I
10 J
11 K
12 L
%}

% Web  
%      A    B    C    D    E   F  G    H    I    J    K    L
% Code
%      1    2    3    4    5   6  7    8    9   10   11   12
G = [  0, 1/2,   0,   0, 1/2,  0, 0,   0,   0,   0,   0,   0;
     1/3,   0, 1/3, 1/3,   0,  0, 0,   0,   0,   0,   0,   0;
       0, 1/2,   0, 1/2,   0,  0, 0,   0,   0,   0,   0,   0;
     1/3,   0,   0,   0, 1/3,  0, 0,   0, 1/3,   0,   0,   0;
       0,   0,   0, 1/2,   0,  0, 0, 1/2,   0,   0,   0,   0;
       0,   0,   0,   0, 1/2,  0, 0,   0, 1/2,   0,   0,   0;
       0,   0, 1/4, 1/4,   0,  0, 0,   0, 1/4,   0,   0, 1/4;
       0,   0,   0,   0, 1/5,1/5, 0,   0, 1/5, 1/5, 1/5,   0;
       0,   0,   0,   0,   0,  0, 0,   0,   0,   0,   0,   1;
       0,   0,   0,   0,   0,  0, 0,   0,   0,   0,   0,   0;
       0,   0,   0,   0,   0,  0, 0,   0, 1/3, 1/3,   0, 1/3;
       0,   0,   0,   0,   0,  0, 1,   0,   0,   0,   0,   0];

% check whether the sum of each row is 1 or 0
% sum(G,2)

% Q2. eigenvector decomposition
[V,D] = eig(G.');
lambda0 = diag(D);
lambda0 = sort(lambda0, 'descend');

% Q3. no, there is no eigenvalue of 1. The largest eigenvalue is 0.9852,
% The 2nd element in matrix D is 0.9852, thus pi is the 2nd column
% All values in pi are negative.
pi = V(:,2);

% Q4. fix dangling pages
G(10,:) = 1/n;
% check whether the sum of each row is actually 1
% sum(G,2)

% Q5. D has eigenvalue of 1
[V,D] = eig(G.');
% The first element in D is 1, thus pi is the 1st column of V
pi1 = V(:,1);
% all values in pi are non-negative

lambda1 = diag(D);
lambda1 = sort(lambda1, 'descend');
max_lambda = max(lambda1);

% r1 = G.'*pi - pi is zero
% r2 = pi.' - pi.' * G is zero

% Q6. Normalize pi
normalized_pi = pi1 / sum(pi1);

% Q7. sort the relative importance, The rank is 7(G) 12(L) 4(D) 9(I) ...
[pis, rank] = sort(normalized_pi,'descend');


% Q8. power method
% The power method function is at the bottom of the code

[pi_power, iterations] = power_method(G);
% iter = 31 iterations
% normalized_pi - pi_power == 0, it gives the same answer as before

% Q9. Construct G_tilda
E = ones(n,n)/n;
G_tilda = alpha*G + (1-alpha)*E;

% Q10. eigendecomposition of G_tilda
[V,D] = eig(G_tilda.');
pi2_normed = V(:,1);

% Q11. get the ranking for G_tilda, the rankings are different
[pis2, rank2] = sort(pi2_normed,'descend');

% Q12. Construct the term-document matrix
% ^check the python code for the sorted sets of each term

% The enumeration of each term:
%{'Apples,': 1, 'Bananas,': 2, 'BlackBeans,': 3,
% 'Blackberries,': 4, 'Blueberries,': 5, 'Broccoli,': 6,
% 'Cabbage,': 7, 'Carrots,': 8, 'Celery,': 9,
% 'Cherries,': 10, 'Coconuts,': 11, 'Corn,': 12,
% 'Cucumbers,': 13, 'Kumquats,': 14, 'Lettuce,': 15,
% 'Mushrooms,': 16, 'Onions,': 17, 'Oranges,': 18,
% 'Peas,': 19, 'Peppers,': 20, 'Pineapples,': 21,
% 'Plums,': 22, 'Radishes,': 23, 'Raspberries,': 24,
% 'Spinach,': 25, 'Strawberries,': 26}

% websites 1-12 with the corresponding indices of terms from the list
% 1  [1, 2, 6, 7, 14, 26],
% 2  [18, 22, 11, 14, 5, 10, 26],
% 3  [15, 25, 2, 4, 19, 26],
% 4  [18, 17, 9, 14, 12, 23],
% 5  [21, 22, 12, 10, 6, 19, 26],
% 6  [15, 17, 11, 25, 19, 26],
% 7  [1, 17, 6, 12, 7, 19],
% 8  [22, 5, 24, 4, 26],
% 9  [1, 13, 8, 25, 12, 3, 7],
% 10 [16, 8, 15, 23, 20, 6, 25],
% 11 [8, 15, 9, 17, 7, 19],
% 12 [6, 7, 8, 25, 12, 19]]


T = zeros(12, 26);
T(1, [1, 2, 6, 7, 14, 26]) = 1;
T(2, [18, 22, 11, 14, 5, 10, 26]) = 1;
T(3, [15, 25, 2, 4, 19, 26]) = 1;
T(4, [18, 17, 9, 14, 12, 23]) = 1;
T(5, [21, 22, 12, 10, 6, 19, 26]) = 1;
T(6, [15, 17, 11, 25, 19, 26]) = 1;
T(7, [1, 17, 6, 12, 7, 19]) = 1;
T(8, [22, 5, 24, 4, 26]) = 1;
T(9, [1, 13, 8, 25, 12, 3, 7]) = 1;
T(10, [16, 8, 15, 23, 20, 6, 25]) = 1;
T(11, [8, 15, 9, 17, 7, 19]) = 1;
T(12, [6, 7, 8, 25, 12, 19]) = 1;

T = T.';

% Q13.
% query is (1,26) * T.' * pi.T  -> sort
% let qi = query vector for all i in {1,2,3,4}
% q1 query for kuquats
q1 = zeros(1, 26);
q1(1,14) = 1;
% q2 query for peas and onions
q2 = zeros(1,26);
q2(1, [17,19]) = 1;
%check for peas only
q_peas = zeros(1,26);
q_peas(1, 19) = 1;
%check for onions only
q_onions = zeros(1,26);
q_onions(1,17) = 1;

% q3 query for broccoli or spinach
q3 = zeros(1,26);
q3(1, [6, 25]) = 1;
%check for broccoli only
q_broc = zeros(1,26);
q_broc(1, 6) = 1;
%check for spinach only
q_spinach = zeros(1,26);
q_spinach(1, 25) = 1;

%q4 query for radishes not celery
q4 = zeros(1,26);
q4(1, 9) = -1;
q4(1, 23) = 1;

% Q14.
% compute d^T = q^T * T
d1T = q1*T;
d1 = d1T.';
% websites 1, 2, 4 have kumquats

d2T = q2*T;
d2 = d2T.';
% websites 6, 7, 11 have both peas and onions


d3T = q3*T;
d3 = d3T.';
% websites 10 and 12 have both broccoli or spinach

d4T = q4*T;
d4 = d4T.';
% website 10 has radishes not celery
% website 11 has both

% Q15.
% the corresponding number associated with the letter is as follows:
%{
 1 A
 2 B
 3 C
 4 D
 5 E
 6 F
 7 G
 8 H
 9 I
10 J
11 K
12 L

 for kumquats the order of importance is as follows: A, B, and D all of
 equal importance since they all feature kumquats
 everything else does not have the terms so they would be least important

 for peas and onions: F, G, K
 everything is else will follow since they do not have both

 for broccoli or spinach the order of importance is J and L or equal
 importance since both feature broccoli and spinach
 followed by A, C, E, F, G, and I since these websites only feature only
 one of the two terms (broccoli or spiniach)

 for radishes not celery, website J would rank highest in importance

%}
%ranking of websites for kumquats
website_vector = 1:12;
website_vector = website_vector.';
kumquat_index = [1,2,4,3,5,6,7,8,9,10,11,12];
kumquat_ranks = website_vector(kumquat_index);

% ranking of websites for peas and onions
peas_onions_index = [6,7,11,1,2,3,4,5,8,9,10,12];
peas_onions_ranks = website_vector(peas_onions_index);

%ranking of websites for broccoli or spinach
brocspin_index = [10,12,1,3,5,6,7,9,2,4,8,11];
brocspin_ranks = website_vector(brocspin_index);

%ranking of websites for radishes not celery
radnotcel_index = [10,11,1:9,12];
radnotcel_ranks = website_vector(radnotcel_index);

% this is the power method for question 8
% Matlab has a problem if the function is not at the end

function [pi_next,iteration] = power_method(G)
    n = size(G,1);
    pi_current = ones(n,1)/n;
    epsilon = 1e-8;
    error = sum(pi_current);
    iteration = 0;
    error_history = [];
    while error > epsilon
        pi_next = (pi_current.' * G).';
        error = norm(pi_next - pi_current);
        pi_current = pi_next;
        iteration = iteration + 1;
        error_history(iteration) = error;
    end

    %plot errors
    plot(1:iteration, error_history);
    xlabel('Iteration Number (k)');
    ylabel('Power Method Error');
    title('Error vs Iteration Number (n)')

    grid on;
end

