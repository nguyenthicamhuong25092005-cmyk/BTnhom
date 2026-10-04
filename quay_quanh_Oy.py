import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# ==========================================
# 1. TINH THE TICH BANG SYMPY (QUAY QUANH OY)
# ==========================================
y_sym = sp.symbols('y')  # Su dung bien ky hieu la y

print("--- Bai toan 2. The tich khoi tron xoay quay quanh truc Oy ---")
print("Nhap ham so x = g(y) theo bien y (Vi du: y**2, sqrt(y), sin(y),...)")
print("-" * 65)

try:
    # Nhap ham so g(y) va cac can theo truc Oy tu ban phim
    chuoi_g = input("Nhap ham so g(y) : ")
    chuoi_c = input("Nhap can duoi c  : ")
    chuoi_d = input("Nhap can tren d  : ")

    # Chuyen doi tat ca sang bieu thuc toan hoc cua SymPy
    g_sym = sp.sympify(chuoi_g)
    c_sym = sp.sympify(chuoi_c)
    d_sym = sp.sympify(chuoi_d)

    # Ap dung cong thuc quay quanh Oy: V = pi * tich phan cua [g(y)]^2 tu c den d
    bieu_thuc_tich_phan = g_sym**2
    V_sym = sp.pi * sp.integrate(bieu_thuc_tich_phan, (y_sym, c_sym, d_sym))

    print(f"\n-> Bieu thuc tich phan: V = pi * tich phan tu {c_sym} den {d_sym} cua ({bieu_thuc_tich_phan}) dy")
    print(f"-> The tich chinh xac V = {V_sym}")
    print(f"-> Gia tri xap xi V ~ {float(V_sym):.4f}")
    print("-" * 65)

    # Chuyen doi cac can sang dang so thuc float de phuc vu ve do thi 3D
    can_c = float(c_sym)
    can_d = float(d_sym)

    # ==========================================
    # 2. VE MO HINH VAT THE TRON XOAY 3D (QUAY QUANH OY)
    # ==========================================
    g_num = sp.lambdify(y_sym, g_sym, 'numpy')

    # Tao luoi toa do xoay quanh truc Oy
    y_vals = np.linspace(can_c, can_d, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    Y, Theta = np.meshgrid(y_vals, theta) # Truc Y dong vai tro truc doc chinh
    
    # Ban kinh tai moi vi tri y chinh la tri tuyet doi cua g(y)
    R = np.abs(g_num(Y))
    
    # Chuyen sang toa do Descartes 3D (Truc Oy la truc doi xung xoay)
    X = R * np.cos(Theta)
    Z = R * np.sin(Theta)

    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Ve be mat vat the tron xoay quanh Oy
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.75, edgecolor='none')
    
    # Ve hai mat day phang chan tai y = c va y = d
    ax.plot_surface(X, np.full_like(Y, can_c), Z, color='gray', alpha=0.3)
    ax.plot_surface(X, np.full_like(Y, can_d), Z, color='gray', alpha=0.3)

    # Ve truc doi xung Oy (Chay doc tu c den d, X=0 va Z=0)
    ax.plot([0, 0], [can_c - 0.5, can_d + 0.5], [0, 0], color='black', linestyle='--', linewidth=2, label='Truc Oy')

    # Cau hinh giao dien do thi theo dung yeu cau
    plt.title('Bai toan 2. The tich khoi tron xoay quay quanh truc Oy', fontsize=12, fontweight='bold', pad=20)
    ax.set_xlabel('X')
    ax.set_ylabel('Truc Y (Can tu c den d)')
    ax.set_zlabel('Z')
    ax.legend(loc='upper left')
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='Do lon ban kinh g(y)')
    
    # Giu ti le khong gian thuc te khong bi meo lech
    ax.set_box_aspect((np.ptp(X), np.ptp(y_vals), np.ptp(Z))) 
    
    plt.show()

except Exception as e:
    print(f"\nDa xay ra loi: {e}")
    print("Vui long kiem tra lai bieu thuc ham so theo bien y hoac gia tri can da nhap!")
