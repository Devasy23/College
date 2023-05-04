# giu frontend for CFG simplifier
import streamlit as st

def remove_unit(CFG):
    single_terminals = []
    for i in CFG:
        if len(CFG[i])==1 and CFG[i][0].islower():
            single_terminals.append(i)
    st.write("Single Terminals are : ",single_terminals)
    # Now, checking if any of the single terminals are in RHS of any other state
    while True:
        changed = False
        for i in CFG:
            for j in CFG[i]:
                for l in j:
                    if l in single_terminals:
                        k = single_terminals.index(l)
                        CFG[i].append(j.replace(single_terminals[k], CFG[single_terminals[k]][0]))
                        CFG[i].remove(j)
                        if len(CFG[i])==1:
                            single_terminals.append(i)
                        st.write("Single Terminals are : ",single_terminals)
                        changed = True
        if not changed:
            break
    print(CFG)
    return CFG
def remove_useless(CFG):
    reachable_states = []
    given_states = []
    terminals = []
    for i in CFG:
        if i not in given_states:
            given_states.append(i)
        for j in CFG[i]:
            for l in j:
                if l not in reachable_states:
                    if l.isupper():
                        reachable_states.append(l)
                    else:
                        terminals.append(l)
    st.write("Reachable states are : ", reachable_states)
    # st.write(given_states)
    st.write("Terminals states are : ",terminals)
    unreachable = []
    for i in given_states:
        if i=="S":
            continue
        elif i not in reachable_states:
            unreachable.append(i)
    st.write("Unreachable states are ", unreachable)
    for i in unreachable:
        CFG.pop(i)
    st.write(CFG)
    return CFG

def remove_null(CFG):
    # Find nullable non-terminals
    nullable = set()
    for nonterm in CFG:
        if '' in CFG[nonterm]:
            nullable.add(nonterm)
            st.write("Nullable found i.e. : ", nonterm)
    while True:
        new_nullable = set()
        for nonterm, prods in CFG.items():
            for prod in prods:
                if all(s in nullable for s in prod):
                    new_nullable.add(nonterm)
                    break
        if new_nullable == nullable:
            break
        nullable = new_nullable
    
    # Construct new productions
    new_prods = {}
    for nonterm, prods in CFG.items():
        new_prods[nonterm] = set()
        for prod in prods:
            new_prod = ['']
            for s in prod:
                if s in nullable:
                    new_prod += [x + s for x in new_prod]
                else:
                    new_prod = [x + s for x in new_prod]
            new_prods[nonterm] |= set(new_prod)
    
    # Now Remove epsilon productions and return the new CFG
    new_CFG = {}
    for nonterm, prods in new_prods.items():
        new_CFG[nonterm] = set()
        for prod in prods:
            if prod != '':
                new_CFG[nonterm].add(prod)
    return new_CFG

st.title("CFG Simplifier")
st.subheader("Enter the CFG in the following format:")
st.write("S->aS|bS|c")
st.write("A->aA|bA|c")
st.write("B->aB|bB|c")
st.write("C->aC|bC|c")
 
 
data = st.text_area("Enter CFG here")
print(data)
data = data.split('\n')
CFG = {}
for i in data:
    print(i)
    var = i[0]
    j = i.split(' | ')
    t = 1
    CFG[var] = []
    CFG[var].append(j[0].split(" → ")[1])
    if len(j) > 1:
        while (t < len(j)):
            CFG[var].append(j[t])
            t += 1
st.write(CFG)
from graphviz import Digraph

def plot_cfg(cfg):
    dot = Digraph(format='png')

    dot.node('S', shape='circle')
    
    dot.node('D0', shape='doublecircle')

    for lhs in cfg:
        for rhs in cfg[lhs]:
            if len(rhs) == 1:  
                dot.edge(lhs, 'D0', label=rhs)
            else:  
                dot.edge(lhs, rhs[1], label=rhs[0])
    
    dot.render('cfg', view=True)
    dot.save('cfg.png')

if st.button("Simlify CFG"):
    CFG1 = remove_unit(CFG)
    CFG2 = remove_useless(CFG1)
    CFG3 = remove_null(CFG2)
    st.write("Plotting CFG")
    plot_cfg(CFG3)
    st.write(CFG3)
if st.button("Plot CFG"):
    st.write("Plotting CFG")
    plot_cfg(CFG3)