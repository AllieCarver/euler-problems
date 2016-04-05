#!-*-coding=utf8 -*-

import time
from itertools import permutations

"""
========================
Project Euler Problem 61
========================


Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are
all figurate (polygonal) numbers and are generated by the following formulae:
Triangle 	  	P3,n=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
Square 	  	P4,n=n2 	  	1, 4, 9, 16, 25, ...
Pentagonal 	  	P5,n=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
Hexagonal 	  	P6,n=n(2n−1) 	  	1, 6, 15, 28, 45, ...
Heptagonal 	  	P7,n=n(5n−3)/2 	  	1, 7, 18, 34, 55, ...
Octagonal 	  	P8,n=n(3n−2) 	  	1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three
interesting properties.

  1)  The set is cyclic, in that the last two digits of each number is the first
     two digits of the next number (including the last number with the first).

  2)  Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and
     pentagonal (P5,44=2882), is represented by a different number in the set.

  3) This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which
each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and
octagonal, is represented by a different number in the set.



"""

def tri(n):
    return n * (n + 1)/2

def squ(n):
    return n**2

def pen(n):
    return n * (3*n - 1)/2

def hexa(n):
    return n*(2*n - 1)

def hep(n):
    return n*(5*n-3)/2

def octa(n):
    return n*(3*n-2)
    
def problem61():
    tri_list = []
    squ_list = []
    pen_list = []
    hexa_list = []
    hep_list = []
    octa_list = []

    tri_ = True
    squ_ = True
    pen_ = True
    hexa_ = True
    hep_ = True
    octa_ = True

    n = 0

    while tri_ or squ_ or pen_ or hexa_ or hep_ or octa_:
          if tri_:
                num = tri(n)
                if num < 200:
                    print 'tri',num
                if 999 < num < 10000:
                      tri_list.append(str(num))
                elif num > 10000:
                      tri_ = False

          if squ_:
                num = squ(n)
                if num < 200:
                    print 'squ',num
                if 999 < num < 10000:
                      squ_list.append(str(num))
                elif num > 10000:
                      squ_ = False
          if pen_:
                num = pen(n)
                if num < 200:
                    print 'pen',num
                if 999 < num < 10000:
                    pen_list.append(str(num))
                elif num > 10000:
                      pen_ = False
          if hexa_:
                num = hexa(n)
                if num < 200:
                    print 'hexa',num
                if 999 < num < 10000:
                      hexa_list.append(str(num))
                elif num > 10000:
                      hexa_ = False

          if hep_:
                num = hep(n)
                if num < 200:
                    print 'hep',num
                if 999 < num < 10000:
                      hep_list.append(str(num))
                elif num > 10000:
                      hep_ = False

          if octa_:
                num = octa(n)
                if num < 200:
                    print 'octa',num
                if 999 < num < 10000:
                      octa_list.append(str(num))
                elif num > 10000:
                      octa_ = False 
          n += 1


    polys = {'tri': set(tri_list), 'squ': set(squ_list),
             'pen': set(pen_list), 'hexa': set(hexa_list),
             'hep': set(hep_list), 'octa': set(octa_list)}
    
    octa_matches_left = set([])
    
    octa_matches_right = {'tri': set([]), 'squ': set([]), 'pen': set([]),
                           'hexa': set([]), 'hep': set([])}
    
    octa_nums = {}
    lcon = 0
    rcon = 0

    print 'tri', tri_list
    print
    print
    print 'squ', squ_list
    print
    print
    print 'pen', pen_list
    print
    print 'hexa', hexa_list
    print
    print
    print 'hep', hep_list
    print
    print 'octa', octa_list
    
    all_nums = {}
    num_types = polys.keys()
    for i in range(5):
    
        for num_type in num_types[::-1]:
            all_nums[num_type]= {}
            for poly_num in polys[num_type]:
                all_nums[num_type][poly_num] = {'l': set([]), 'r': set({})}
                onuml = poly_num[:2]
                onumr = poly_num[2:]
                for key in polys.keys():
                    if key != num_type:
                        for num in polys[key]:
                            if num[:2] == onumr:
                                #octa_matches_right[key].add(num)
                                all_nums[num_type][poly_num]['r'].add((num, key))
                                #rcon+=1
                            if num[2:]==onuml:
                                #lcon+=1
                                if num_type == 'octa':
                                     octa_matches_left.add(num)
                                all_nums[num_type][poly_num]['l'].add((num, key))
                if  len(all_nums[num_type][poly_num]['l']) < 1 or len(all_nums[num_type][poly_num]['r']) < 1:
                    all_nums[num_type].pop(poly_num)
                #else:
                    #polys[num_type] = set(all_nums[num_type].keys())
    octals = set([])
    for key in all_nums['octa'].keys():
        for i in all_nums['octa'][key]['l']:
            octals.add(i)

    print 'start'        
    alltup = set([])
    alltup.update(octals)
    for ptype, num_dic in all_nums.items():
        for num in num_dic.keys():
            alltup.update(all_nums[ptype][num]['r'])
    possibilities = set([])
    for perm in permutations(alltup,6):
   
        if len(set([perm[0][1], perm[1][1], perm[2][1], perm[3][1], perm[4][1], perm[5][1]])) == 6:
            if perm[0][0][2:] == perm[1][0][:2] and perm[1][0][2:]== perm[2][0][:2]:
                print '1', perm
                if perm[2][0][2:]== perm[3][0][:2] and perm[3][0][2:] == perm[4][0][:2]:
                    print '2',perm
                    if perm[4][0][2:]== perm[5][0][:2] and perm[5][0][2:]==perm[0][0][:2]:
                        print 'found!!!', perm
            #print perm
 
    #print possiblities

    print
    print
    print
    print 'end'
    all_keys = set(polys.keys())
    for octa_num in polys['octa']:
        print 'passed 1'
        if all_nums['octa'].has_key(octa_num):
            for num2, type2 in all_nums['octa'][octa_num]['r']:
                print 'passed 2'
                if all_nums[type2].has_key(num2):
                    for num3, type3 in all_nums[type2][num2]['r']:
                        print 'passed 3'
                        if all_nums[type3].has_key(num3):
                            for num4, type4 in all_nums[type3][num3]['r']:
                                print 'passed 4'
                                if all_nums[type4].has_key(num4):
                                    for num5, type5 in all_nums[type4][num4]['r']:
                                        print 'passed 5'
                                        if num5 in  octals:
                                        #if all_nums['octa'][num5]:
                                            for num6, type6 in all_nums['octa'][num5]['l']:
                                                print 'passed 6'
                                                if octa_num[2:] == num2[:2]:
                                                    print 'passed 7'
                                                    if num2[2:] == num3[:2]:
                                                        print 'passed 8'
                                                        if num3[2:] == num4[:2]:
                                                            if num4[2:] == num5[:2]:
                                                                if num5[2:] == num6[:2]:
                                                                    if num6[2:] == octa_num[:2]:
                                                                        if set(['octa','type2', 'type3', 'type4', 'type5', 'type6']) == all_keys:
                                                                            print [octa_num, num2, num3, num4, num5, num6]
        """        
        for octa_num in polys[num_type]:
            octa_nums[octa_num] = {'l': set([]), 'r': set({})}
            onuml = octa_num[:2]
            onumr = octa_num[2:]
            for key in polys.keys():
                for num in polys[key]:
                    if num[:2]==onumr:
                        octa_matches_right[key].add(num)
                        octa_nums[octa_num]['r'].add((num, key))
                        rcon+=1
                    if num[2:]==onuml:
                        lcon+=1
                        octa_matches_left[key].add(num)
                        octa_nums[octa_num]['l'].add((num, key))
            if  len(octa_nums[octa_num]['l']) < 1 or len(octa_nums[octa_num]['r']) < 1:
                octa_nums.pop(octa_num)
        """

    print len(tri_list) 
    print len(squ_list)
    print len(pen_list)
    print len(hexa_list)
    print len(hep_list)
    print len(octa_list)
    print
    print 'lcon', lcon
    print 'rcon', rcon
    print 'octa nums'
    #for key,val in polys.items():
    #    print key, len(val)
    #    for i in val:
    #        print i
    
    
    print len(octa_nums.keys())


    print
    print

    """
    for i in ashort:
        for j in bshort:
            for k in cshort:
                for l in dshort:
                    for m in eshort:
                        for n in fshort:
                            if i[2:]==j[:2]:
                                if j[2:]==k[:2]:
                                    if k[2:]==l[:2]:
                                        if l[2:]==m[:2]:
                                            if m[2:]==n[:2]:
                                                if n[2:]==i[:2]:
                                                    return [i,j,k,l,m,n]
    
                
    refor each in  [tri,squ, pen, hexa, hep, octa]:y
        for i in range(1,6):
            print str(each(i))+',',
        print '\n'   """
    
                                                
if __name__ == '__main__':        
    time1=time.time()
    problem61()
    time2=time.time()
    print time2-time1
