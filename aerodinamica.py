# Aerodinâmica

from math import pi, floor

c_r = 5   # [] - Corda na raiz
c_t = 5   # [] - Corda na ponta
b = 5   # [] - Envergadura
M = 5   # [] - Comprimento do meio

S = M*c_r + (c_r + c_t)*(b - M)/2   # [] - Área
AR = (b**2)/S   # [] - Alongamento
afil = c_t/c_r   # [] - Afilamento

# Fator de Arrasto Induzido
def fator_arrasto_induzido(AR: int, x: float):
    if AR == 4:
        return 6.415*x**6 - 21.859*x**5 + 29.124*x**4 - 19.23*x**3 + 6.6564*x**2 - 1.1486*x + 0.0801
    if AR == 6:
        return 5.0804*x**6 - 17.793*x**5 + 24.632*x**4 - 17.234*x**3 + 6.5662*x**2 - 1.2921*x + 0.1065
    if AR == 8:
        return 5.2993*x**6 - 18.309*x**5 + 25.037*x**4 - 17.401*x**3 + 6.7302*x**2 - 1.3847*x + 0.125
    if AR == 10:
        return 2.1557*x**6 - 8.3335*x**5 + 13.186*x**4 - 11.12*x**3 + 5.533*x**2 - 1.4659*x + 0.1624

fai = fator_arrasto_induzido(AR, afil)   # [] - Fator de Arrasto Induzido
e = 1/(1+fai)   # [] - Fator de Eficiência de Envergadura

# Sustentação
a_0 = 5   # [] - Coeficiente de Sustentação
alpha_L = 5   # [°] - Ângulo de Sustentação Nula
a = a_0/(1 + (57.3*a_0/(pi*e*AR)))

