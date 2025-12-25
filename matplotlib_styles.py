import matplotlib.pyplot as plt
print(plt.style.available) # вызовем разные наборы цветов

# Если все графики должны быть оформлены в едином стиле, в начале проекта вызовите метод plt.style.use():
# plt.style.use('ggplot') # здесь выбран стиль ggplot

with plt.style.context('seaborn-v0_8-pastel'):
    plt.bar([10, 20, 30, 40],[3, 9, 18, 7])
    plt.show()
