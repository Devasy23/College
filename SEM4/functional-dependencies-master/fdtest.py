#
# a simple program to demonstrate the fds class
#
import streamlit as st

from fds import fds

f = fds.FDs()
# f.addfd(fds.FDs.mkfd('S', 'N'))
# f.addfd(fds.FDs.mkfd('P', 'F'))
# f.addfd(fds.FDs.mkfd('C', 'L'))
# f.addfd(fds.FDs.mkfd('SC', 'G'))
title = st.text_input('Enter FDs', 'B-->A')
f.addfd(fds.FDs.mkfd('B', 'A'))
f.addfd(fds.FDs.mkfd('AD', 'BC'))
f.addfd(fds.FDs.mkfd('C', 'ABD'))




print('Keys')
print(f.keys())
print('Minimal Cover')
print(f.minimalCover())
print("Is 3nf", f.is3nf())
print("Is BCNF", f.isbcnf())

x = f.minimalCover()
s= ''
for y in x:
    set = True
    for a in y:
        if(set):
            for m in a:
                s += m
                # print(m, end='')
            s += ' --> '
            # print(end=' --> ')
            set = False
        else:
            # print(a)
            for m in a:
                s+= m
                # print(m, end='')
    s+= '\n'
    print()
# print("Complete FD closure")
# for fdc in f.fdclosure():
#     print(''.join(fdc[0]), '->', ''.join(fdc[1]), fdc[2] or '')
st.write(s)