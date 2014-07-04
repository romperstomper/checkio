import sys


def pcheck(data):
  if len(data) < 10:
    return False
  num, low, up = False, False, False
  for chr in data:
    if chr.isdigit():
      num = True
    if chr.islower():
      low = True
    if chr.isupper():
      up = True
  if num and low and up:
    return True
  return False

def main():
  print pcheck(sys.argv[1])

if __name__ == '__main__':
  main()

