import string
import sys

def count_chars(text):
  charfreq = {}
  for char in text:
    if char in string.ascii_letters:
      if char in charfreq:
        charfreq[char] += 1
      else:
        charfreq[char] = 1

  return max(charfreq, key=charfreq.get)

def main():
  print count_chars(sys.argv[1])


if __name__ == '__main__':
  main()


    
