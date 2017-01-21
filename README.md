# mem-garden


Guppy module test, heap output


    [@sandbox memtest]$ python guppytest.py
    Partition of a set of 27642 objects. Total size = 3449520 bytes.
     Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
         0  12210  44   981696  28    981696  28 str
         1   6065  22   495200  14   1476896  43 tuple
         2    325   1   297976   9   1774872  51 dict (no owner)
         3     69   0   216696   6   1991568  58 dict of module
         4    200   1   211904   6   2203472  64 dict of type
         5   1635   6   209280   6   2412752  70 types.CodeType
         6   1599   6   191880   6   2604632  76 function
         7    200   1   177912   5   2782544  81 type
         8    124   0   135328   4   2917872  85 dict of class
         9   1045   4    83600   2   3001472  87 __builtin__.wrapper_descriptor
    <91 more rows. Type e.g. '_.more' to view.>
    [@sandbox memtest]$

