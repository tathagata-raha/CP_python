// C++ program to find the nCr%p
// based on optimal Dynamic
// Programming implementation and
// Pascal Triangle concepts
#include <bits/stdc++.h>
using namespace std;

// Returns (a * b) % mod
long long moduloMultiplication(long long a, long long b,
							long long mod)
{

	// Initialize result
	long long res = 0;

	// Update a if it is more than
	// or equal to mod
	a %= mod;

	while (b) {

		// If b is odd, add a with result
		if (b & 1)
			res = (res + a) % mod;

		// Here we assume that doing 2*a
		// doesn't cause overflow
		a = (2 * a) % mod;
		b >>= 1; // b = b / 2
	}
	return res;
}

// C++ function for extended Euclidean Algorithm
long long int gcdExtended(long long int a, long long int b,
						long long int* x,
						long long int* y);

// Function to find modulo inverse of b. It returns
// -1 when inverse doesn't exists
long long int modInverse(long long int b, long long int m)
{

	long long int x, y; // used in extended GCD algorithm
	long long int g = gcdExtended(b, m, &x, &y);

	// Return -1 if b and m are not co-prime
	if (g != 1)
		return -1;

	// m is added to handle negative x
	return (x % m + m) % m;
}

// C function for extended Euclidean Algorithm (used to
// find modular inverse.
long long int gcdExtended(long long int a, long long int b,
						long long int* x,
						long long int* y)
{

	// Base Case
	if (a == 0) {
		*x = 0, *y = 1;
		return b;
	}

	// To store results of recursive call
	long long int x1, y1;

	long long int gcd = gcdExtended(b % a, a, &x1, &y1);

	// Update x and y using results of recursive
	// call
	*x = y1 - (b / a) * x1;
	*y = x1;
	return gcd;
}

// Function to compute a/b under modlo m
long long int modDivide(long long int a, long long int b,
						long long int m)
{

	a = a % m;
	long long int inv = modInverse(b, m);
	if (inv == -1)
		// cout << "Division not defined";
		return 0;
	else
		return (inv * a) % m;
}

// Function to calculate nCr % p
int nCr(int n, int r, int p)
{

	// Edge Case which is not possible
	if (r > n)
		return 0;

	// Optimization for the cases when r is large
	if (r > n - r)
		r = n - r;

	// x stores the current result at
	long long int x = 1;

	// each iteration
	// Initialized to 1 as nC0 is always 1.
	for (int i = 1; i <= r; i++) {

		// Formula derived for calculating result is
		// C(n,r-1)*(n-r+1)/r
		// Function calculates x*(n-i+1) % p.
		x = moduloMultiplication(x, (n + 1 - i), p);
	
		// Function calculates x/i % p.
		x = modDivide(x, i, p);
	}
	return x;
}

// Driver Code
int main()
{

	long long int n = 5, r = 3, p = 1000000007;
	cout << "Value of nCr % p is " << nCr(n, r, p);
	return 0;
}
