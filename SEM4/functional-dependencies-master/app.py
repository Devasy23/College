import streamlit as st
import pandas as pd



def decomposition(newList):
    decomposedList = []
    for i in newList:
        splitfd = i.split("->")
        if(len(splitfd[1])>1):
            extra = list(splitfd[1])
            for j in extra:
                decomposedList.append("->".join([splitfd[0],j]))
        else:
            decomposedList.append(i)
    return decomposedList

# 3) finding Closure of FD
def closure(fd,fdList):  # fdList -> containing all FDs ,fd -> particular FD (attribute or set of attributes)
    fd = fd.split("->")
    attrClosure = []
    leftSide = []
    rightSide = []
    attrClosure+=list(fd[0])   # every set of attribute can determine itself
    # attrClosure.append(fd[1]) 
    # print("initial attrClosure : ",attrClosure)
    for i in fdList:
        leftSide.append(i.split("->")[0])
    # print("leftside attr : ",leftSide)
    for i in fdList:
        rightSide.append(i.split("->")[1])
    while(True):   # for queue like
        prevClosure = attrClosure.copy()
        for value in range(len(leftSide)):  # all value of leftside in attrClosure
            if(all(item in attrClosure  for item in list(leftSide[value]))):
                attrClosure.append(rightSide[value])
        # attrClosure = duplicate(attrClosure)
        # print("prevattrClosure : ",prevClosure)
        # print("newattrClosure : ",attrClosure)
        if(prevClosure == attrClosure):
            return attrClosure

# 4) finding extraneous FD and removing it --> (i.e. only considering essential FD in final FDs)
def removeExtraFD(fdList):  # fdlist --> decomposed list
    for _ in fdList:
        for j in fdList:
            tempList=fdList.copy()
            tempList.remove(j)
            if(sorted(closure(j,tempList))==sorted(closure(j,fdList))): # if the closure changes by removing the FD , then it is essential otherwise redundant
                fdList.remove(j)
    return fdList

# 5) removing extra attributes
def removeExtraAttribute(fdList):
    for i in range(len(fdList)):
        fd = fdList[i].split("->")[0]   # leftside of FDs
        fd_value = fdList[i].split("->")[1]   # rightside of FDs
        if(len(fd)>1):
            for j in range(len(fd)):
                tempAttr=fd[:j]+fd[j+1:]
                # print(tempAttr)
                a = "->".join([tempAttr,fd_value])
                # print(closure(tempAttr,fdList))
                if((fd[j] in closure(tempAttr,fdList)) and (fdList[i] in fdList)):
                    fdList.append(a)
                    fdList.remove(fdList[i])
    return fdList


# 6) Composition
def composition(fdList):
    for i in fdList:
        fd=i.split('->')
        tempList=[]
        for j in fdList:
            fdTemp=j.split('->')
            if(fd[0]==fdTemp[0] and (j not in tempList)):
                tempList.append(j)
        
        if(len(tempList)>1):
            for t in tempList:
                fdList.remove(t)
            tempAttr = ""
            for i in tempList:
                temp = i.split("->")
                tempAttr+= temp[1]
            new = temp[0] +"->"+ tempAttr
            fdList.append(new)
    
    return fdList
# st.write('''#Hello''')
print("start here")
st.write("Minimal Cover ----- Finder")
from fds import fds
f = fds.FDs()
slide = st.slider('No. of FDs')
l =[]
for i in range(slide):
    title = st.text_input('Enter FDs', key =i)
    x= title.split('->')
    f.addfd(fds.FDs.mkfd(x[0], x[1]))
    l.append(title)
# '''new test set
# # '''
# f.addfd(fds.FDs.mkfd('B', 'A'))
# f.addfd(fds.FDs.mkfd('AD', 'BC'))
# f.addfd(fds.FDs.mkfd('C', 'ABD'))
st.write('Minimal Cover')
# st.write(f.minimalCover())
min_cover = f.minimalCover()
men1 = decomposition(l)
st.write(men1)
men2 = removeExtraFD(men1)
st.write(men2)
men3 =removeExtraAttribute(men2)
st.write(men3)
men4 = composition(men3)
st.write(men4)

for fd in min_cover:
    key = fd[0];k_opp = fd[1]
    st.write(key,'-->',k_opp)

# '''set ends                 '''

# st.write('Keys')
# st.write(f.keys())
# st.write('Minimal Cover')
# st.write(f.minimalCover())
# min_cover = f.minimalCover()
# for fd in min_cover:
#     key = fd[0];k_opp = fd[1]
#     st.write(key,'-->',k_opp)
# st.write("Is 3nf", f.is3nf())
# st.write("Is BCNF", f.isbcnf())
# st.write("Complete FD closure")
# for fdc in f.fdclosure():
#     st.write(''.join(fdc[0]), '->', ''.join(fdc[1]), fdc[2] or '')