#!-*-coding=utf8 -*-

import time

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

    tri_1 = set([])
    squ_1 = []
    pen_1 = []
    hexa_1 = []
    hep_1 = []
    octa_1 = []

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
                if 999 < num < 10000:
                      tri_list.append(str(num))
                elif num > 10000:
                      tri_ = False

          if squ_:
                num = squ(n)
                if 999 < num < 10000:
                      squ_list.append(str(num))
                elif num > 10000:
                      squ_ = False
          if pen_:
                num = pen(n)
                if 999 < num < 10000:
                    pen_list.append(str(num))
                elif num > 10000:
                      pen_ = False
          if hexa_:
                num = hexa(n)
                if 999 < num < 10000:
                      hexa_list.append(str(num))
                elif num > 10000:
                      hexa_ = False

          if hep_:
                num = hep(n)
                if 999 < num < 10000:
                      hep_list.append(str(num))
                elif num > 10000:
                      hep_ = False

          if octa_:
                num = octa(n)
                if 999 < num < 10000:
                      octa_list.append(str(num))
                elif num > 10000:
                      octa_ = False 
          n += 1

          
    poly1 = [squ_list,pen_list, hexa_list,
                 hep_list, octa_list]
    poly2 = [tri_list,pen_list, hexa_list,
                 hep_list, octa_list]
    poly3 = [tri_list, squ_list, hexa_list,
                 hep_list, octa_list]
    poly4 = [tri_list,squ_list,pen_list, 
                 hep_list, octa_list]
    poly5 = [tri_list,squ_list,pen_list, hexa_list,
                 octa_list]
    poly6 = [tri_list,squ_list,pen_list, hexa_list,
                 hep_list]

    polyall = [tri_list,squ_list,pen_list, hexa_list,
                 hep_list, octa_list]
    """    
    while len(octa_list) > 40:
        new_tri_list = set([])
        for num in tri_list:
            first = num[:2]
            second = num[2:]
            f = False
            s = False
            for i in octa_list:
                if i[2:] == first:
                    f=True

            for i in squ_list:
                if i[:2] == second:
                    s=True
            if f and s:
                new_tri_list.add(num)
        tri_list = new_tri_list

        new_squ_list = set([])
        for num in squ_list:
            first = num[:2]
            second = num[2:]
            f = False
            s = False
            #new_squ_list = set([])
            for i in tri_list:
                if i[2:]== first:
                    f=True
            for i in pen_list:
                if i[:2]== second:
                    s=True
            if f and s:
                new_squ_list.add(num)
        squ_list = new_squ_list

        new_pen_list = set([])
        for num in pen_list:
            first = num[:2]
            second = num[2:]
            f = False
            s = False
            #new_pen_list = set([])
            for i in squ_list :
                if i[2:]== first:
                    f = True

            for i in hexa_list:
                if i[:2]== second:
                    s= True
            if f and s:
                new_pen_list.add(num)
        pen_list = new_pen_list

        new_hexa_list = set([])
        for num in hexa_list:
            first = num[:2]
            second = num[2:]
            f=False
            s=False
            #new_hexa_list = set([])
            for i in pen_list:
                if i[2:]== first:
                    f=True
            for i in hep_list:
                if i[:2]== second:
                    s = True
            if f and s:
                new_hexa_list.add(num)
        hexa_list = new_hexa_list

        new_hep_list = set([])
        for num in hep_list:
            first = num[:2]
            second = num[2:]
            f=False
            s=False
            #new_hep_list = set([])
            for i in hexa_list:
                if i[2:]== first:
                    f=True
            for i in octa_list:
                if i[:2]== second:
                    f=True
            if f and s:
                new_hep_list.add(num)
        hep_list = new_hep_list

        new_octa_list = set([])
        for num in octa_list:
            first = num[:2]
            second = num[2:]
            f=False
            s=False
            #new_octa_list = set([])
            for i in hep_list:
                if i[2:]== first:
                        f=True

            for i in tri_list:
                if i[2:]== second:
                    f=True
            if f and s:
                new_octa_list.add(num)
        octa_list = new_octa_list
        
        print (len(tri_list) , len(squ_list), len(pen_list), len(hexa_list),
           len(hep_list), len(octa_list))
    #for i in polyall:
     #   print i
      #  print
    """
    a = tri_list
    b = squ_list
 
    c = pen_list

    d =  hexa_list

    e = hep_list

    f = octa_list
    ashort = set([])
    bshort = set([])
    cshort = set([])
    dshort = set([])
    eshort = set([])
    fshort = set([])
    for i in a:
        for j in b:
            for k in c:
                if i[2:]==j[:2]:
                    if j[2:]==k[:2]:
                        ashort.add(i)
                        bshort.add(j)
                        cshort.add(k)

    for i in a:
        for j in b:
            for k in d:
                if i[2:]==j[:2]:
                    if j[2:]==k[:2]:
                        ashort.add(i)
                        bshort.add(j)
                        dshort.add(k)
    for i in a:
        for j in b:
            for k in e:
                if i[2:]==j[:2]:
                    if j[2:]==k[:2]:
                        ashort.add(i)
                        bshort.add(j)
                        eshort.add(k)

    for i in a:
        for j in b:
            for k in f:
                if i[2:]==j[:2]:
                    if j[2:]==k[:2]:
                        ashort.add(i)
                        bshort.add(j)
                        fshort.add(k)
    for i in a:
        for j in d:
            for k in c:
                if i[2:]==j[:2]:
                    if j[2:]==k[:2]:
                        ashort.add(i)
                        dshort.add(j)
                        cshort.add(k)

    for i in a:
        for j in e:
            for k in c:
                if i[2:]==j[:2]:
                    if j[2:]==k[:2]:
                        ashort.add(i)
                        eshort.add(j)
                        cshort.add(k)


    for i in a:
        for j in f:
            for k in c:
                if i[2:]==j[:2]:
                    if j[2:]==k[:2]:
                        ashort.add(i)
                        fshort.add(j)
                        cshort.add(k)
    for l in d:
        for m in e:
            for n in f:
                if l[2:]==m[:2]:
                    if m[2:]==n[:2]:
                        dshort.add(l)
                        eshort.add(m)
                        fshort.add(n)

    print ashort
    print
    print bshort
    print
    print cshort
    print
    print dshort
    print
    print eshort
    print
    print fshort

    
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
    """            
    refor each in  [tri,squ, pen, hexa, hep, octa]:y
        for i in range(1,6):
            print str(each(i))+',',
        print '\n'   """

                                                
if __name__ == '__main__':        
    time1=time.time()
    problem61()
    time2=time.time()
    print time2-time1
