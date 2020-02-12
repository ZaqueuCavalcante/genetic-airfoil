# Genetic_Airfoil

Código para otimização de perfis aerodinâmicos de alta sustentação, baseado no XFoil e num algoritmo genético.

Os aerofólios otimizados serão utilizados pela equipe Hórus Aerodesign, no Torneio de Acesso 2021 para a competição SAE Aerodesign.

Passo a passo genético de um algoritmo genético:
    1 - Inicialização: definição do genoma, do indivíduo e da população;
    2 - Avaliação: determinaa aptidão, o quão boa é a solução. É feita uma 
    análise para saber quão bem as aptidões respondem ao problema proposto;
    3 - Seleção: indivíduos são selecionados para a reprodução. A probabilidade 
    de uma dada soluçãoa ser selecionada é proporcional a sua aptidão;
    4 - Cruzamento: características das soluções escolhidas são recombinadas, 
    gerando novos indivíduos;
    5 - Mutação: características dos indivíduos resultantes do processo de
    reprodução são alteradas, acrescentando assim variedade à população;
    6 - Atualização: os indivíduos criados nesta geração são inseridos na
    população;
    7 - Finalização: verifica se as condições de encerramento da evolução
    foram atingidas, retornando para a etapa de avaliação em caso
    negativo e encerrando a execução em caso positivo.
  
