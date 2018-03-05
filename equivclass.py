# Anthony Krivonos
# 3/4/2018
# Equivalence Classes
# equivclass.py

import math;

# A is a set, m, n in A
# mRn iff x | (m^2 + n^2)
def sqrtDivisibleRelation(A, x):
    R = [];
    for a in range(len(A)):
        for b in range(a, len(A)):
            m = A[a];
            n = A[b];
            testVal = math.pow(m, 2) + math.pow(n, 2);
            if testVal % x == 0:
                pair = [m, n];
                R.append(pair);
                if (m != n):
                    pair = [n, m];
                    R.append(pair);
    return R;

# Prints a paired set, i.e. A = {(a1, b1), (a2, b2)...}
def printRelation(R):
    strR = 'Relation:\n{';
    for i in range(len(R) - 1):
        strR += '(' + str(R[i][0]) + ', ' + str(R[i][1]) + '), ';
    strR += '(' + str(R[len(R) - 1][0]) + ', ' + str(R[len(R) - 1][1]) + ')}';
    print strR;

# Determine equivalence classes from a paired set
def equivalenceClasses(R):
    classes = {};
    for r in R:
        key = r[0];
        val = r[1];
        if key in classes:
            if val not in classes[key]:
                classes[key].append(val);
        else:
            classes[key] = [val];
    return classes;

# Print equivalence classes from dictionary form
def printEquivalenceClasses(classes):
    strC = 'Equivalence Classes:\n';
    for key in sorted(classes):
        strC += '[' + str(key) + '] = {';
        for i in range(len(classes[key]) - 1):
            strC += str(classes[key][i]) + ', ';
        strC += str(classes[key][len(classes[key]) - 1]) + '}';
        print strC;
        strC = '';
