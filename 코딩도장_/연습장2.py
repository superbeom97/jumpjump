def is_palindrome(n):
  s = str(n)
  return s == s[::-1]

def main():
  m = 0
  for i in range(999, 99, -1):
    for j in range(999, 99, -1):
      n = i * j
      if is_palindrome(n) and m < n:
        m = n
  print(m)