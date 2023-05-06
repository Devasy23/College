#!/usr/bin/python
#
# fds.py
#
# a set of methods to manipulate functional dependencies.
#

from asyncio.windows_events import NULL
import itertools
from nbformat import write
from sqlalchemy import false, true
import streamlit as st
def list22set(losi):
    x=""
    st.write(losi)
    for i in losi:
        # ctrl_var =1
        st.write(list3set(i))
        # x+= list3set(i)
        # x+="/n"
        
    # return x
def list3set(losi):
    los = list(losi)
    los.pop()
    s=''
    set = True
    if(True):
        for y in los[0]:
            
            s+=y
            # temp.remove(y)
        if(set):
            s+='-->'
            set=False
        for y in los[1]:
            s+=y
    # print(s)
    return s

def list2set(losi):
    los = losi
    s=''
    set = True
    for x in los:
        temp = list(x)
        for y in temp:
            
            s+=y
            temp.remove(y)
        if(set):
            s+='-->'
            set=False
        # temp = list(x)
        # for y1 in temp:
        #     s+=y1
    # st.write(s)
    return s
            
class FDs:
    FDIsKey = 'k'
    FDIsSuperkey = 's'

    def __init__(self, attributes=None, fds=None):
        self.attributes = set()
        self.fds = []

        if attributes:
            # do some basic type checking. We expect a string (only)
            if type(attributes) is not str:
                raise TypeError("Invalid datatype for attributes")

            self.attributes = {x for x in attributes}

        if fds:
            if type(fds) is not list:
                raise TypeError("Invalid datatype for fds")

            for f in fds:
                self.addfd(f)

        return

    # add a functional dependency. Internally, all FDs are stored in
    # non-trivial, and with a single element on the right hand side.
    def addfd(self, f):
        if type(f) is not tuple:
            raise TypeError("Invalid datatype for an fd")

        if type(f[0]) is not set:
            raise TypeError("Invalid datatype for an fd")

        if type(f[1]) is not set:
            raise TypeError("Invalid datatype for an fd")

        # verify that the attributes in the fd are in the
        # attribute list, and if they are not, add them.
        self.attributes = self.attributes.union(f[0])
        self.attributes = self.attributes.union(f[1])

        nx = f[1].difference(f[0])

        if len([x for x in self.fds if x[0] == f[0]]) > 0:
            for x in self.fds:
                if x[0] == f[0]:
                    # eliminate the FDs that alread exist.
                    nx = nx.difference(x[1])

        # and store what remains
        for x in nx:
            self.fds.append([f[0], set(x)])

        return

    # return a consolidation of the FDs. This operation makes NO
    # change to the FDs as they are stored internally.
    def consolidate(self):
        retval = []
        for f in self.fds:
            if len([x for x in retval if x[0] == f[0]]) > 0:
                for x in retval:
                    if x[0] == f[0]:
                        x[1] = x[1].union(f[1])
                        break
            else:
                retval.append(f.copy())

        return retval

    def attrclosure(self, ta):
        a = {x for x in ta} if type(ta) is not set else ta
        r = a.copy()
        oldr = None
        while oldr != r:
            oldr = r
            for f in self.fds:
                # if r has all the attributes that the present
                # fd's lhs has, then assert all the rhs values in
                # the value of r.
                if f[0].issubset(r):
                    r = r.union(f[1])
        # st.write("difference is : ", r.difference(a))
        return(r.difference(a))

    # returns the fd closure for the currently known attributes and
    # fds.  the return set is a list of tuples where each element in
    # the list is a functional dependency. All FDs are returned in
    # non-trivial form; i.e. nothing on the LHS appears on the
    # RHS. The tuple consists of three parts, the first is the LHS,
    # the second is the RHS, and the third is either a single
    # character or the empty string. The first two are python sets,
    # and the third indicates whether the LHS is a key (k) or superkey
    # (s), or neither (-)
    def fdclosure(self):
        retval = []
        allkeys = self.keys()

        for l in range(0, len(self.attributes)):
            for k in itertools.combinations(self.attributes, l+1):
                r = self.attrclosure(k)
                if len(r) > 0:
                    if k in allkeys:
                        iskey = self.FDIsKey
                    elif self.attrclosure(k).union(k) == self.attributes:
                        iskey = self.FDIsSuperkey
                    else:
                        iskey = None

                    retval.append((set(k), r, iskey))

        return(retval)

    # returns the keys of the currently known fds (and
    # attributes). Return set is a list of python sets.
    def keys(self):
        keys = []

        for l in range(0, len(self.attributes)):
            for c in itertools.combinations(self.attributes, l+1):
                candidate = {x for x in c}

                # if there is a key that is a subset of the candidate, we
                # can skip it, i.e. candidate is a superkey.
                if len([k for k in keys if set(k).intersection(c) ==
                        set(k)]) > 0:
                    continue

                if self.attrclosure(c).union(c) == self.attributes:
                    keys.append(c)

        return(keys)

    def minimalCover(self):
        # the minimal cover is defined as the smallest set of FDs that
        # have the same closure as a given set of FDs.
        fdc = self.fdclosure()
        for ix in range(len(self.fds)-1, -1, -1):
            f = self.fds[ix].copy()
            st.write("--------------------------------------------\n")
            # st.write("Checking for : ",list2set(self.fds[ix]))
            del self.fds[ix]

            fdc1 = self.fdclosure()
            # print(set(fdc).symmetric_difference(set(fdc1)))
            # print(list(set(fdc) - set(fdc1)))
            if fdc1 == fdc:
                # st.write(list22set(fdc1), list22set(fdc),"as they are equal ",list2set(f)," can be eliminated")
                continue

            self.fds.append(f)
            # st.write(list22set(fdc1), list22set(fdc), " as it wasn't the same before and after so it is necessary")

        return self.consolidate()

    def isbcnf(self):
        allkeys = self.keys()
        for c in self.fdclosure():
            # we never generate trivial FDs, therefore we can ignore
            # that check.
            if c[2] is not None:
                # this key is a superkey or key relationship, skip it.
                continue

            return False

        return True

    # determines whether a relation, and its associated FDs is in 3nf
    def is3nf(self):
        if self.isbcnf():
            return True

        allkeys = self.keys()

        for c in self.fdclosure():
            # we never generate trivial FDs, therefore we can ignore
            # that check.
            if c[2] is not None:
                # this key is a superkey or key relationship, skip it.
                continue

            if len([k for k in allkeys if c[1].issubset(k)]) > 0:
                # this FD is to an RHS which is a subset of a key
                continue

            return False

        return True

    @staticmethod
    def mkfd(l, r):
        a = {x for x in l}
        b = {x for x in r}

        return((a, b))

