#from itertools import combinations, permutations
#from eulertools import ero_sieve

a = set([1,3])
b = set([3,1])
c= set([4,1])
print a == b == c
from itertools import permutations

a = 'abc'
count = 0
perms= set([])

def is_cubic(n):
    if str(n**(float(1)/3)).split('.')[-1]=='0':
        return True
    return False

for perm in permutations('41063625', len('41063625')):
    if is_cubic(int(''.join(perm))):
        perms.add(''.join(perm))

print perms, len(perms)
print count


x =  [41063625, 56623104, 66430125]
for i in x:
    print is_cubic(i)
