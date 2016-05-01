# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def precompute_hashes(text, pattern_length, multiplier, prime):
  hashes = [None for x in range(len(text) - pattern_length + 1)]
  s = text[len(text) - pattern_length:len(text)]
  hashes[len(text) - pattern_length] = poly_hash(s, multiplier, prime)

  y = 1
  for i in range(0, pattern_length):
    y = (y * multiplier) % prime
  for i in reversed(range(0, len(text) - pattern_length)):
    hashes[i] = (multiplier * hashes[i + 1] + ord(text[i]) - y * ord(text[i + pattern_length])) % prime

  return hashes

def poly_hash(string, multiplier, prime):
  ans = 0
  for c in reversed(string):
      ans = (ans * multiplier + ord(c)) % prime
  return ans

def get_occurrences(pattern, text):
  result = []

  multiplier = 263
  prime = 1000000007
  hashes = precompute_hashes(text, len(pattern), multiplier, prime)

  pattern_hash = poly_hash(pattern, multiplier, prime)
  for i in range(0, len(text) - len(pattern) + 1):
    if hashes[i] != pattern_hash:
      continue
    if text[i:i + len(pattern)] == pattern:
      result.append(i)

  return result

def get_occurrences(pattern, text):
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
