"""Exact independent checks of the revised algebraic proof and paper examples.

Standard library only. These checks supplement the written proof; the upper
bound is verified exhaustively by audit_tree.c, not by random examples.
"""
from itertools import product
import json

def mul(x, y, q):
    return tuple(sum(x[3*i+k]*y[3*k+j] for k in range(3)) % q
                 for i in range(3) for j in range(3))

def invariants(x, q):
    a,b,c,d,e,f,g,h,i=x
    return ((a+e+i)%q, (a*e+a*i+e*i-b*d-c*g-f*h)%q,
            (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%q)

def is_nil(x,q):
    return not any(mul(mul(x,x,q),x,q))

def count_F2_graphs():
    count=0
    ys=[y for y in range(1,64) if ((y&7).bit_count()&1)==0]
    for code in range(1<<18):
        rows=[(code>>(6*r))&63 for r in range(3)]
        for y in ys:
            a,e,i,d,g,h=[(y>>k)&1 for k in range(6)]
            b,c,f=[(r&y).bit_count()&1 for r in rows]
            if ((a*e+a*i+e*i+b*d+c*g+f*h)&1)==0 and \
               ((a*(e*i+f*h)+b*(d*i+f*g)+c*(d*h+e*g))&1)==0:
                break
        else:
            count+=1
    assert count==128,count
    return count

def verify():
    checked=0
    for x in product(range(3),repeat=9):
        assert is_nil(x,3)==(invariants(x,3)==(0,0,0))
        checked+=1
    for a,b,c,d,e in product(range(3),repeat=5):
        x=(a,0,b,0,(c-d-e)%3,c,b,d,e)
        tr,c2,det=invariants(x,3)
        if tr==0:
            p=(c-d)%3; z=(c+d)%3
            assert a==(-p)%3
            assert c2==(-z*z+p*e-e*e-b*b)%3
            if c2==0:
                assert det==(-p+(p+e)*b*b)%3
        if is_nil(x,3):
            assert (a,b,c,d,e)==(0,0,0,0,0)
    examples={
        2:[[0,1,0,1,1,0],[1,0,0,0,1,1],[0,1,0,0,0,1]],
        5:[[2,1,0,4,3,3],[2,2,0,0,2,2],[4,1,4,2,0,2]],
    }
    for q,coef in examples.items():
        for y in product(range(q),repeat=6):
            u=[-sum(coef[r][j]*y[j] for j in range(6))%q for r in range(3)]
            x=(y[0],u[0],u[1],y[3],y[1],u[2],y[4],y[5],y[2])
            assert not any(y) or not is_nil(x,q)
    return dict(matrix_invariant_equivalence_cases=checked, lower_bound_cases=243,
                F2_example_cases=64,F5_example_cases=15625,
                F2_coefficient_matrices=1<<18,F2_nilpotent_free_graphs=count_F2_graphs(),
                status='PASS')

if __name__=='__main__':
    print(json.dumps(verify(),indent=2))
