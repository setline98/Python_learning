import time

# Исходная функция
def f(x):
    return x**6 + 2.05268*x**5 - 2.86118*x**4 - 5.74764*x**3 + 1.50966*x**2 + 1.95058*x - 0.236566

# Производная функции
def df(x):
    return 6*x**5 + 10.2634*x**4 - 11.4447*x**3 - 17.2429*x**2 + 3.01932*x + 1.95058

# Метод Ньютона
def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x, i + 1
        if dfx == 0:
            raise ValueError("Производная равна нулю. Выберите другую начальную точку.")
        x -= fx / dfx
    return x, max_iter

# Метод бисекции
def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала.")
    for i in range(max_iter):
        c = (a + b) / 2.0
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c, i + 1
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, max_iter

# Поиск всех интервалов, на которых функция меняет знак
def find_all_sign_change_intervals(f, start=-5, end=5, step=0.1):
    intervals = []
    x = start
    while x < end:
        if f(x) * f(x + step) < 0:
            intervals.append((x, x + step))
        x += step
    return intervals

# Начальные условия и параметры точности
tolerance = 1e-6
intervals = find_all_sign_change_intervals(f, -5, 5, 0.01)

# Поиск корней каждым методом
print("Сравнение методов на каждом интервале смены знака:\n")
for idx, (a, b) in enumerate(intervals):
    # Метод Ньютона с начальным приближением в середине интервала
    x0 = (a + b) / 2
    try:
        start_time = time.time()
        root_newton, iter_newton = newton_method(f, df, x0, tol=tolerance)
        time_newton = time.time() - start_time
    except Exception as e:
        root_newton, iter_newton, time_newton = None, None, None
        print(f"[{idx+1}] Метод Ньютона не сошелся: {e}")

    # Метод бисекции
    try:
        start_time = time.time()
        root_bisect, iter_bisect = bisection_method(f, a, b, tol=tolerance)
        time_bisect = time.time() - start_time
    except Exception as e:
        root_bisect, iter_bisect, time_bisect = None, None, None
        print(f"[{idx+1}] Метод бисекции не сошелся: {e}")

    # Вывод результатов
    print(f"[{idx+1}] Интервал: ({a:.2f}, {b:.2f})")
    print(f"    Ньютона : корень = {root_newton:.6f}, итераций = {iter_newton}, время = {time_newton:.6f} сек")\
        if root_newton is not None else None
    print(f"    Бисекция: корень = {root_bisect:.6f}, итераций = {iter_bisect}, время = {time_bisect:.6f} сек\n") \
        if root_bisect is not None else None
