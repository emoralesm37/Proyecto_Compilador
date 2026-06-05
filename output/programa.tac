# === Programa: DemoCompleto ===


begin_func fibonacci
    param n
    t1 = n <= 1
    if t1 goto L1
    goto L2
L1:
    return n
L2:
    t2 = n - 1
    push t2
    t3 = call fibonacci, 1
    t4 = n - 2
    push t4
    t5 = call fibonacci, 1
    t6 = t3 + t5
    return t6
end_func fibonacci

# --- Código principal ---
    nums = [3, 1, 4, 1, 5]
    total = 0
    i = 0
L3:
    t7 = i < 5
    if t7 goto L4
    goto L5
L4:
    t8 = nums[i]
    t9 = t8 % 2
    r = t9
    t10 = r == 0
    if t10 goto L6
    goto L7
L6:
    t11 = nums[i]
    t12 = total + t11
    total = t12
L7:
    t13 = i + 1
    i = t13
    t14 = total > 10
    if t14 goto L8
    goto L9
L8:
    goto L5      # break (ciclo)
L9:
    goto L3
L5:
    suma = 0
    j = 1
L10:
    t15 = j <= 12
    if t15 goto L11
    goto L13
L11:
    t16 = suma + j
    suma = t16
L12:
    t17 = j + 1
    j = t17
    goto L10
L13:
    msg = "Fibonacci(10) = "
    print msg
    push 10
    t18 = call fibonacci, 1
    print t18
    print "Suma 1..10:"
    print suma
    print "Total pares del arreglo:"
    print total
