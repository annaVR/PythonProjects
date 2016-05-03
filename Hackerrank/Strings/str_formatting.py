__author__ = 'anna'

maxim = 17
width = len(format(maxim, "b"))

# padding = 2 + len(format(maxim, 'b'))
# dec = "%d"
# oc = "%o"
# he = "%X"
# rep = "%r"
# for num in range(1, maxim +1):
#     print(dec.rjust(padding - len(str(num))) % num, oc.rjust(padding - len(format(num, "o")))\
#     % num, he.rjust(padding - len(format(num, "X"))) % num, dec.rjust(padding - len(format(num, "b")))\
#     % int(format(num, "b")))

for num in range(1, maxim + 1):
    print('{:>{}}'.format(num, width), '{:>{}o}'.format(num, width), '{:>{}X}'.format(num, width),
          '{:>{}b}'.format(num, width))

print()
for num in range(1, maxim + 1):
    print('{0:*>{width}} {0:*>{width}o} {0:*>{width}X} {0:*>{width}b}'.format(num, width=width))
