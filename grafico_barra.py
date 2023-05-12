import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
musicas = ('Lost Without You', 'You Shook Me All Night Long', 'Epitáfio', 'Double Fantasy', 'Stay')
indice = np.arange(len(musicas))
acessos = [15,10,7,5,3]
plt.bar(indice, acessos)
plt.xticks(indice, musicas)
plt.ylabel('Acessos')
plt.title('Músicas mais ouvidas por mim Spotify abril.2023')
plt.bar(indice, acessos,
color=["red","green","cyan","yellow",(0.3,0.6,0.9,0.5)], edgecolor='red' )

plt.show()
