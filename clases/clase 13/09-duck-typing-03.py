def llama_hablar(x):
    x.hablar()

#-----------------------------

class Perro:
    def hablar(self):
        print("¡Guau, Guau!")

class Gato:
    def hablar(self):
        print("¡Miau, Miau!")

class Vaca:
    def hablar(self):
        print("¡Muuu, Muuu!")

#-------------------------------

llama_hablar(Perro())
llama_hablar(Gato())
llama_hablar(Vaca())

# ¡Guau, Guau!
# ¡Miau, Miau!
# ¡Muuu, Muuu!