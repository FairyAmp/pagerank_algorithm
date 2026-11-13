#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler
import itertools

# default plotting style
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['axes.labelsize'] = 18
plt.rcParams['legend.fontsize'] = 14
plt.rcParams['lines.markersize'] = 8
plt.rcParams['lines.linewidth'] = 4
plt.rcParams['axes.prop_cycle'] = (
    cycler('color', ['r', 'g', 'b', 'y']) +
    cycler('linestyle', ['-', '--', '-', '-.']) +
    cycler('marker', ['o', 's', 'D', 'X'])
)

n = 12
alpha = 0.85

# Q1. hyperlink to G
G = np.array([[  0, 1/2,   0,   0, 1/2,   0, 0,   0,   0,   0,   0,     0],
              [1/3,   0, 1/3, 1/3,   0,   0, 0,   0,   0,   0,   0,     0],
              [  0, 1/2,   0, 1/2,   0,   0, 0,   0,   0,   0,   0,     0],
              [1/3,   0,   0,   0, 1/3,   0, 0,   0, 1/3,   0,   0,     0],
              [  0,   0,   0, 1/2,   0,   0, 0, 1/2,   0,   0,   0,     0],
              [  0,   0,   0,   0, 1/2,   0, 0,   0, 1/2,   0,   0,     0],
              [  0,   0, 1/4, 1/4,   0,   0, 0,   0, 1/4,   0,   0,   1/4],
              [  0,   0,   0,   0, 1/5, 1/5, 0,   0, 1/5, 1/5, 1/5,     0],
              [  0,   0,   0,   0,   0,   0, 0,   0,   0,   0,   0,     1],
              [  0,   0,   0,   0,   0,   0, 0,   0,   0,   0,   0,     0],
              [  0,   0,   0,   0,   0,   0, 0,   0, 1/3, 1/3,   0, 1/3],
              [  0,   0,   0,   0,   0,   0, 1,   0,   0,   0,   0,     0]])

# Q2. eigenvector decomposition
eigenvalues, eigenvectors = np.linalg.eig(G.T)

# Q3. Get the eigenvector corresponding to the eigenvalue of 1
index = np.argmin(abs(eigenvalues - 1))
pi = eigenvectors[:, index].real

# Q4. Fix dangling pages
# note: python index starts at 0
G[9, :] = 1/n

# Q5. Check the eigenvector corresponding to the updated G
eigenvalues, eigenvectors = np.linalg.eig(G.T)
index = np.argmin(abs(eigenvalues - 1))
pi = eigenvectors[:, index].real

#descending order eigenvalues
eigenvalues = np.sort(eigenvalues)[::-1]

#print(eigenvalues)

# Q6. Normalize pi
normalized_pi = pi / np.sum(pi)

print(normalized_pi)

# Q7. Sort the relative importance, and get the ranking
pis_sorted = np.sort(normalized_pi)[::-1]
rank = np.argsort(normalized_pi)[::-1]
# Ranking based on pi:
# [ 7 12  4  9  5  1  2  3  8 10 11  6]


# Q8. Power method function
def power_method(G):
    n = G.shape[0]
    pi_current = np.ones(n) / n
    epsilon = 1e-8
    error = np.sum(pi_current)
    iteration = 0
    error_history = []
    while error > epsilon:
        pi_next = np.dot(G.T, pi_current)
        error = np.linalg.norm(pi_next - pi_current)
        error_history.append(error)
        pi_current = pi_next
        iteration += 1
    return pi_current, iteration, error_history

# Q8. Apply power method to G
pi_power, iteration_num, error_history = power_method(G)

# print(iteration_num)
# iterations = 31

plt.plot(range(iteration_num), error_history)
plt.xlabel('Iteration Number (k)')
plt.ylabel('Power Method Error')
plt.title('Error vs Iteration Number (n)')
plt.grid(True)
#plt.show()
plt.savefig('power_method_errors.png')



# Q9. Construct G_tilda
E = np.ones((n, n)) / n
G_tilda = alpha * G + (1 - alpha) * E

# Q10. Eigendecomposition of G_tilda
eigenvalues, eigenvectors = np.linalg.eig(G_tilda.T)
pi2_normed = eigenvectors[:, 0].real

# Q11. Get the ranking for G_tilda
pis2_sorted = np.sort(pi2_normed)[::-1]
rank2 = np.argsort(pi2_normed)[::-1]

## Ranking based on pi2_normed:
## [11  6 10  8  3  2  1  5  9  4  7 12]
# running this in python is slightly different
# in Matlab it ranks 6 higher than 11, everything else is the same

# Q12. Construct the term-document matrix
'''
 ^reference sorted_set file
 The enumeration of each term:
 {'Apples,': 1, 'Bananas,': 2, 'BlackBeans,': 3,
  'Blackberries,': 4, 'Blueberries,': 5, 'Broccoli,': 6,
  'Cabbage,': 7, 'Carrots,': 8, 'Celery,': 9,
 'Cherries,': 10, 'Coconuts,': 11, 'Corn,': 12,
 'Cucumbers,': 13, 'Kumquats,': 14, 'Lettuce,': 15,
 'Mushrooms,': 16, 'Onions,': 17, 'Oranges,': 18,
 'Peas,': 19, 'Peppers,': 20, 'Pineapples,': 21,
 'Plums,': 22, 'Radishes,': 23, 'Raspberries,': 24,
 'Spinach,': 25, 'Strawberries,': 26}
'''
# Since the indexing starts from 0 in Python, subtract 1 from the indices.

T = np.zeros((12, 26))
T[0, [0, 1, 5, 6, 13, 25]] = 1;
T[1, [17, 21, 10, 13, 4, 9, 25]] = 1;
T[2, [14, 24, 1, 3, 18, 25]] = 1;
T[3, [17, 16, 8, 13, 11, 22]] = 1;
T[4, [20, 21, 11, 9, 5, 18, 25]] = 1;
T[5, [14, 16, 10, 24, 18, 25]] = 1;
T[6, [0, 16, 5, 11, 6, 18]] = 1;
T[7, [21, 4, 23, 3, 25]] = 1;
T[8, [0, 12, 7, 24, 11, 2, 6]] = 1;
T[9, [15, 7, 14, 22, 19, 5, 24]] = 1;
T[10, [7, 14, 8, 16, 6, 18]] = 1;
T[11, [5, 6, 7, 24, 11, 18]] = 1;
T = np.transpose(T)

#print(T)


# Q13. Query

##pi_query = np.dot(query, T.T) * normalized_pi
##pis_query_sorted = np.sort(pi_query)[::-1]
##rank_query = np.argsort(pi_query)[::-1]

# q1 query for kuquats
q1 = np.zeros(26)
q1[13] = 1  # MATLAB uses 1-based indexing, so 14 in MATLAB is 13 in Python

# q2 query for peas and onions
q2 = np.zeros(26)
q2[[16, 18]] = 1  # MATLAB uses 1-based indexing, so 17 and 19 in MATLAB are 16 and 18 in Python

# check for peas only
q_peas = np.zeros(26)
q_peas[18] = 1  # MATLAB uses 1-based indexing, so 19 in MATLAB is 18 in Python

# check for onions only
q_onions = np.zeros(26)
q_onions[16] = 1  # MATLAB uses 1-based indexing, so 17 in MATLAB is 16 in Python

# q3 query for broccoli or spinach
q3 = np.zeros(26)
q3[[5, 24]] = 1  # MATLAB uses 1-based indexing, so 6 and 25 in MATLAB are 5 and 24 in Python

# check for broccoli only
q_broc = np.zeros(26)
q_broc[5] = 1  # MATLAB uses 1-based indexing, so 6 in MATLAB is 5 in Python

# check for spinach only
q_spinach = np.zeros(26)
q_spinach[24] = 1  # MATLAB uses 1-based indexing, so 25 in MATLAB is 24 in Python

# q4 query for radishes not celery
q4 = np.zeros(26)
q4[8] = -1  # MATLAB uses 1-based indexing, so 9 in MATLAB is 8 in Python
q4[22] = 1  # MATLAB uses 1-based indexing, so 23 in MATLAB is 22 in Python

# Q14.

# compute d^T = q^T * T
d1T = np.dot(q1, T)
d1 = d1T.T

# websites 1, 2, 4 have kumquats

d2T = np.dot(q2, T)
d2 = d2T.T

# websites 6, 7, 11 have both peas and onions

d3T = np.dot(q3, T)
d3 = d3T.T

# websites 10 and 12 have both broccoli or spinach

d4T = np.dot(q4, T)
d4 = d4T.T

# website 10 has radishes not celery
# website 11 has both

#Q15.
#check matlab code

# Print results
print("Ranking based on pi:")
print(rank + 1)  # Adding 1 to the rank to match MATLAB indexing
print("Ranking based on pi2_normed:")
print(rank2 + 1)  # Adding 1 to the rank to match MATLAB indexing
print("Ranking based on query:")
#print(rank_query + 1)  # Adding 1 to the rank to match MATLAB indexing

#print(T)
