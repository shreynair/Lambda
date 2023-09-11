def isPalindrome(n):
  strn = str(n)
  i = 0
  j = len(strn) - 1

  while i != j:
    if(strn[i] != strn[j]):
      return False

    i += 1;
    j -= 1;

  return True

def nthmax(n, a):
  mini = min(a)
  maxi = max(a)
  nth = maxi

  if(n >= len(a)):
    return None

  for i in range(0, n):
    nextLargest = mini
    for j in range(0, len(a)):
      if(a[j] > nextLargest and a[j] < nth):
        nextLargest = a[j]
    nth = nextLargest

  return nth

def freq(s):
  freqc = {}
  max = 0
  maxc = ""

  for i in s:
    freqc[i] = freqc.get(i,0) + 1
    if(freqc[i] > max):
      max = freqc[i]
      maxc = i

  return maxc


def zipHash(arr1, arr2):
  new_dict = {}
  if(len(arr1) != len(arr2)):
    return None
  
  for i in range(0,len(arr1)):
    new_dict[arr1[i]] = arr2[i]
  
  return new_dict


def hashToArray(hash):
  new_arr = []
  for i in hash:
    new_arr.append([i,hash[i]])
  
  return new_arr

def maxLambdaChain(init, lambdas):
  chain = [init]

  for i in range(0, len(lambdas)):
    for j in range(0, len(chain)):
      chain.append(lambdas[i](chain[j]))

  return max(chain)