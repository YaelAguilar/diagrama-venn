import matplotlib.pyplot as plt
from matplotlib_venn import venn3

prob_P1 = 0.48
prob_P2 = 0.20
prob_P3 = 0.32

prob_D_given_P1 = 0.035
prob_D_given_P2 = 0.060
prob_D_given_P3 = 0.068

prob_P1_and_D = prob_P1 * prob_D_given_P1
prob_P2_and_D = prob_P2 * prob_D_given_P2
prob_P3_and_D = prob_P3 * prob_D_given_P3

prob_D = prob_P1_and_D + prob_P2_and_D + prob_P3_and_D

prob_P1_given_D = prob_P1_and_D / prob_D
prob_P2_given_D = prob_P2_and_D / prob_D
prob_P3_given_D = prob_P3_and_D / prob_D

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
venn = venn3(subsets={'100': prob_P1_and_D, '010': prob_P2_and_D, '001': prob_P3_and_D,
                      '110': min(prob_P1_and_D, prob_P2_and_D), 
                      '101': min(prob_P1_and_D, prob_P3_and_D), 
                      '011': min(prob_P2_and_D, prob_P3_and_D), 
                      '111': min(prob_P1_and_D, prob_P2_and_D, prob_P3_and_D)},
             set_labels=('P1', 'P2', 'P3'))
plt.title("Probabilidades Conjuntas de Defectos por Máquina")

plt.subplot(1, 2, 2)
venn = venn3(subsets={'100': prob_P1_given_D, '010': prob_P2_given_D, '001': prob_P3_given_D,
                      '110': min(prob_P1_given_D, prob_P2_given_D), 
                      '101': min(prob_P1_given_D, prob_P3_given_D), 
                      '011': min(prob_P2_given_D, prob_P3_given_D), 
                      '111': min(prob_P1_given_D, prob_P2_given_D, prob_P3_given_D)},
             set_labels=('P1', 'P2', 'P3'))
plt.title("Probabilidades Condicionales de Defectos por Máquina")

plt.tight_layout()
plt.show()
