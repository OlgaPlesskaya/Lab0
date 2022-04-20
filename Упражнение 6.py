summa=int(input("Введите сумму заказа в ресторане "))
nalog=summa*0.13
tea=summa*0.18
print("Налог= ", round(nalog,2))
print("Чаевые= ", round(tea,2))
print("Итог= ", round(nalog+tea ,2))