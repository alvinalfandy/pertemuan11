
import math

# Fungsi a(x) mengembalikan kuadrat dari x
def a(x):
    return x ** 2

# Fungsi lambda ac melakukan hal yang sama seperti fungsi a
ac = lambda x: x ** 2

# Mencetak hasil dari pemanggilan fungsi a dengan argumen 8
print(a(8))

# Mencetak hasil dari pemanggilan fungsi ac dengan argumen 11
print(ac(11))

# Fungsi b(x, y) mengembalikan akar kuadrat dari jumlah kuadrat x dan y
def b(x, y):
    return math.sqrt(x**2 + y**2)

# Fungsi lambda bc melakukan hal yang sama seperti fungsi b
bc = lambda x, y: math.sqrt(x**2 + y**2)

# Mencetak hasil dari pemanggilan fungsi b dengan argumen 1 dan 4
print(b(1, 4))

# Mencetak hasil dari pemanggilan fungsi bc dengan argumen 2 dan 5
print(bc(2, 5))

# Fungsi c(*args) mengembalikan rata-rata dari argumen yang diberikan
def c(*args):
    return sum(args) / len(args)

# Fungsi lambda cC melakukan hal yang sama seperti fungsi c
cC = lambda *args: sum(args) / len(args)

# Mencetak hasil dari pemanggilan fungsi c dengan argumen 100 dan 50
print(c(100, 50))

# Mencetak hasil dari pemanggilan fungsi cC dengan argumen 100 dan 25
print(cC(100, 25))

# Fungsi d(s) mengembalikan string unik dari karakter dalam s
def d(s):
    return "".join(set(s))

# Fungsi lambda dc melakukan hal yang sama seperti fungsi d
dc = lambda s: "".join(set(s))

# Mencetak hasil dari pemanggilan fungsi d dengan argumen "IMiissYou"
print(d("IMiissYou"))

# Mencetak hasil dari pemanggilan fungsi dc dengan argumen "IMiisYouToo"
print(dc("IMiisYouToo"))
