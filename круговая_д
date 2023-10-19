import random
import matplotlib.pyplot as plt

def lemma(n):
    lab = [str(i) for i in range(1, n + 1)]
    vs = random.choices(range(150), k=n)

    plt.figure(figsize=(8, 6))
    plt.pie(vs, labels=lab, autopct='%.0f%%')
    plt.title("Круговая диаграмма")
    plt.show()

lemma(16)
