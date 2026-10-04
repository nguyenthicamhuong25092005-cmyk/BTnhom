import sympy as sp

# 1. Khoi tao bien ky hieu toan hoc x
x = sp.symbols('x')
C = sp.symbols('C')

print("--- CHUONG TRINH TINH NGUYEN HAM & TICH PHAN TU DONG ---")
try:
    # 2. Nhap ham so f(x) tu ban phim
    chuoi_nhap = input("Nhap ham so f(x): ")
    
    # Chuyen doi chuoi ky tu thanh bieu thuc toan hoc cua SymPy
    f = sp.sympify(chuoi_nhap)
    print(f"\nHam so ban da nhap: f(x) = {f}")
    print("-" * 30)

    # 3. Tinh va in Nguyen ham
    F = sp.integrate(f, x) + C
    print(f"-> Nguyen ham F(x) = {F}")
    print("-" * 30)

    # 4. Nhap can va tinh Tich phan xac dinh
    print("Nhap can cho tich phan xac dinh:")
    can_duoi_nhap = input("Can duoi (a): ")
    can_tren_nhap = input("Can tren (b): ")
    
    # Chuyen doi can sang bieu thuc toan hoc (ho tro ca pi, E, 1/2)
    a = sp.sympify(can_duoi_nhap)
    b = sp.sympify(can_tren_nhap)

    # Tinh tich phan xac dinh
    I = sp.integrate(f, (x, a, b))
    
    print(f"\n-> Tich phan xac dinh tu {a} den {b}:")
    print(f"Gia tri chinh xac (phan so/can/pi): I = {I}")
    print(f"Gia tri xap xi (so thap phan): I ~ {float(I):.4f}")

except Exception as e:
    print(f"\nDa xay ra loi: {e}")
    print("Vui long kiem tra lai dinh dang ham so hoac can ban da nhap!")