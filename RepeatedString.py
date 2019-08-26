# Complete the repeatedString function below.
def repeatedString(s, n):
    s_count = s.count("a")
    n_len = n // len(s)
    count_final = s[:n % len(s)].count("a")
    return s_count * n_len + count_final

print(repeatedString("aba", 10))