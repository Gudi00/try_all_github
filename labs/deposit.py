
ans = 0
mes_sum = 500
stavka = 0.12
mes_stavka = stavka / 12
stavka_2 = 0.14
mes_stavka_2 = stavka_2 / 12
ans_2 = 0
col_mes = 18

for i in range(1, col_mes):
     ans += mes_sum
     ans_2 += mes_sum
     ans *= 1 + mes_stavka
     ans_2 *= 1 + mes_stavka_2

     print(f"first {i}. {round(ans) - mes_sum * i}  second {i}. {round(ans_2) - mes_sum * i}\t\t res {(round(ans) - mes_sum * i) - (round(ans_2) - mes_sum * i)}")