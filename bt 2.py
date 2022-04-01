from dslk import *

def main():
    ds= DSLienket()
    ds.in_ds()
    
    # a - them
    print('a: them ------------------')
    so = 12
    print(f'Them {so}')
    ds.them(so)
    ds.in_ds()
    
    so = 10
    print(f'Them {so}')
    ds.them(so)
    ds.in_ds()
    # b - chen
    print('b: chen ------------------')
    so = 8
    vt = 0
    print(f'Chen {so} vao vi tri {vt}')
    ds.chen(vt, so)
    ds.in_ds()
    
    so = 15
    vt = 1
    print(f'Chen {so} vao vi tri {vt}')
    ds.chen(vt, so)
    ds.in_ds()
    
    so = 17
    vt = 3
    print(f'Chen {so} vao vi tri {vt}')
    ds.chen(vt, so)
    ds.in_ds()
    # c - tim
    print('c: tim ------------------')
    ds.in_ds()
    so = 99
    print(f'Tim {so}')
    vt =ds.tim(so)
    print(f'So {so} tai vi tri {vt}')
    
    ds.in_ds()
    so = 15
    print(f'Tim {so}')
    vt =ds.tim(so)
    print(f'So {so} tai vi tri {vt}')
    # d - xoa
    print('d: xoa ------------------')
    so = 19
    print(f'Xoa {so}')
    ds.xoa(so)
    ds.in_ds()
    
    so = 15
    print(f'Xoa {so}')
    ds.xoa(so)
    ds.in_ds()
    # e - cap nhat
    print('e: cap nhat ------------------')
    vt = 6
    gia_tri = 23
    print(f'Cap nhat vi tri {vt} voi gia tri {gia_tri}')
    ds.cap_nhat(vt,gia_tri)
    ds.in_ds()
    
    vt = 2
    gia_tri = 9
    print(f'Cap nhat vi tri {vt} voi gia tri {gia_tri}')
    ds.cap_nhat(vt,gia_tri)
    ds.in_ds()
    # f - xoa het
    print('f: xoa het ------------------')
    print('Xoa het')
    ds.xoa_het()
    ds.in_ds()
#def

if __name__ == '__main__':
    main()
#if