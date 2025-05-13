# Para adicionar cores no python tem que escrever \033[styler:text:back m
# Styler 0(nulo), 1(bold), 4(underline) e 7(negative)
# Text 30(branco) 31(verm) 32(verde) 33(amar) 34(azul) 35(roxo) 36(a. claro) 37(cinza)
# Back 40 41 42 43 44 45 46 47 (repete as cores)

print('\033[4:30:45mOlá Mundo!\033[m')
