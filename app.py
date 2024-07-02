import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Definición de los datos
# Probabilidad de una computadora defectuosa producida por cada máquina
prob_P1 = 0.48
prob_P2 = 0.20
prob_P3 = 0.32

prob_D_given_P1 = 0.035
prob_D_given_P2 = 0.060
prob_D_given_P3 = 0.068

# Calculo de la probabilidad conjunta de (Máquina y Defecto)
prob_P1_and_D = prob_P1 * prob_D_given_P1
prob_P2_and_D = prob_P2 * prob_D_given_P2
prob_P3_and_D = prob_P3 * prob_D_given_P3

# Calculo de la probabilidad de una computadora defectuosa
prob_D = prob_P1_and_D + prob_P2_and_D + prob_P3_and_D

# Probabilidades condicionales
prob_P1_given_D = prob_P1_and_D / prob_D
prob_P2_given_D = prob_P2_and_D / prob_D
prob_P3_given_D = prob_P3_and_D / prob_D

# Crear el primer diagrama de Venn para probabilidades conjuntas
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
venn = venn3(subsets={'100': prob_P1_and_D, '010': prob_P2_and_D, '001': prob_P3_and_D,
                      '110': min(prob_P1_and_D, prob_P2_and_D), 
                      '101': min(prob_P1_and_D, prob_P3_and_D), 
                      '011': min(prob_P2_and_D, prob_P3_and_D), 
                      '111': min(prob_P1_and_D, prob_P2_and_D, prob_P3_and_D)},
             set_labels=('P1', 'P2', 'P3'))
plt.title("Probabilidades Conjuntas de Defectos por Máquina")

# Crear el segundo diagrama de Venn para probabilidades condicionales
plt.subplot(1, 2, 2)
venn = venn3(subsets={'100': prob_P1_given_D, '010': prob_P2_given_D, '001': prob_P3_given_D,
                      '110': min(prob_P1_given_D, prob_P2_given_D), 
                      '101': min(prob_P1_given_D, prob_P3_given_D), 
                      '011': min(prob_P2_given_D, prob_P3_given_D), 
                      '111': min(prob_P1_given_D, prob_P2_given_D, prob_P3_given_D)},
             set_labels=('P1', 'P2', 'P3'))
plt.title("Probabilidades Condicionales de Defectos por Máquina")

# Mostrar los diagramas
plt.tight_layout()
plt.show()
