import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# ==========================================
# 1. TINH THE TICH BANG SYMPY (CO NHAN SO PI)
# ==========================================
x_sym = sp.symbols('x')

print("--- Bai toan 1. The tich khoi tron xoay quay quanh truc Ox ---")
print("Luu y: Ban co the nhap can la so (1, 2) hoac hang so pi (pi, pi/2, 2*pi)")
print("-" * 65)

try:
    # Nhap ham so va cac can tu ban phim duoi dang chuoi
    chuoi_f = input("Nhap ham so f(x) : ")
    chuoi_a = input("Nhap can duoi a  : ")
    chuoi_b = input("Nhap can tren b  : ")

    # Chuyen doi tat ca sang bieu thuc toan hoc cua SymPy
    f_sym = sp.sympify(chuoi_f)
    a_sym = sp.sympify(chuoi_a)
    b_sym = sp.sympify(chuoi_b)

    # Ap dung cong thuc: V = pi * tich phan cua [f(x)]^2 tu a den b
    bieu_thuc_tich_phan = f_sym**2
    V_sym = sp.pi * sp.integrate(bieu_thuc_tich_phan, (x_sym, a_sym, b_sym))

    print(f"\n-> Bieu thuc tich phan: V = pi * tich phan tu {a_sym} den {b_sym} cua ({bieu_thuc_tich_phan}) dx")
    print(f"-> The tich cua V = {V_sym}")
    print(f"-> Gia tri xap xi V ~ {float(V_sym):.4f}")
    print("-" * 65)

    # Chuyen doi cac can sang dang so thuc float de phuc vu ve do thi 3D
    can_a = float(a_sym)
    can_b = float(b_sym)

    # ==========================================
    # 2. VE MO HINH VAT THE TRON XOAY 3D
    # ==========================================
    f_num = sp.lambdify(x_sym, f_sym, 'numpy')

    # Tao luoi toa do xoay quanh truc Ox
    x_vals = np.linspace(can_a, can_b, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    X, Theta = np.meshgrid(x_vals, theta)
    
    R = np.abs(f_num(X))
    Y = R * np.cos(Theta)
    Z = R * np.sin(Theta)

    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Ve be mat vat the tron xoay
    surf = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.75, edgecolor='none')
    
    # Ve hai mat day phang
    ax.plot_surface(np.full_like(X, can_a), Y, Z, color='gray', alpha=0.3)
    ax.plot_surface(np.full_like(X, can_b), Y, Z, color='gray', alpha=0.3)

    # Ve truc doi xung Ox
    ax.plot([can_a - 0.5, can_b + 0.5], [0, 0], [0, 0], color='black', linestyle='--', linewidth=2, label='Truc Ox')

    plt.title('Bai toan 1. The tich khoi tron xoay quay quanh truc Ox', fontsize=12, fontweight='bold', pad=20)
    ax.set_xlabel('Truc X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend(loc='upper left')
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='Do lon ban kinh f(x)')
    ax.set_box_aspect((np.ptp(x_vals), np.ptp(Y), np.ptp(Z)))
    
    plt.show()

except Exception as e:
    print(f"\nDa xay ra loi: {e}")
    print("Vui long kiem tra lai bieu thuc ham so hoac gia tri can da nhap!")