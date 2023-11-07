#Given the set of positive integers S and the natural number k, display one of the subsets of S which sum to k.
# For example, if S = { 2, 3, 5, 7, 8 } and k = 14, subset { 2, 5, 7 } sums to 14.


def find_subset_sum(S, k):
    n = len(S)
    dp = [[False] * (k + 1) for _ in range(n + 1)]

    # Initialize the first column to True
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j < S[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - S[i - 1]]

    for i in range(k + 1):
        print(f"     {i}", end="")
    print()
    for i in range(n + 1):
        print(f"{0 if i == 0 else S[i-1]}  ", end="")
        print(dp[i])

    # Reconstruct the subset
    subset = []
    i, j = n, k
    while i > 0 and j > 0:
        if dp[i][j] and not dp[i - 1][j]:
            subset.append(S[i - 1])
            j -= S[i - 1]
        i -= 1

    if dp[n][k]:
        return subset[::-1]
    else:
        return None


def subset_sum(S, n, k):
    # Base cases
    if k == 0:
        return True
    if n == 0:
        return False

    # If the last element is greater than the target sum, exclude it
    if S[n - 1] > k:
        return subset_sum(S, n - 1, k)

    # Recursive step: include or exclude the current element in the subset
    return subset_sum(S, n - 1, k) or subset_sum(S, n - 1, k - S[n - 1])


# Function to find subset with sum k
def find_subset(S, k):
    n = len(S)
    if subset_sum(S, n, k):
        return [S[i] for i in range(n - 1, -1, -1) if subset_sum(S, i, k)]
    else:
        return None


# Example usage
S = [2, 3, 5, 7, 8]
k = 14
result = find_subset(S, k)

if result:
    print("Subset with sum", k, ":", result)
else:
    print("No subset found with sum", k)

#print(naive_version(lst, 14))