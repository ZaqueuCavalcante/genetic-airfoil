# Genetic_Airfoil

Código para otimização de perfis aerodinâmicos de alta sustentação, baseado no XFoil e num algoritmo genético.

Os aerofólios otimizados serão utilizados pela equipe Hórus Aerodesign, no Torneio de Acesso 2021 para a competição SAE Aerodesign.

Passo a passo genérico de um algoritmo genético:

    1 - Inicialização: definição do genoma, do indivíduo e da população;
    
    2 - Avaliação: determinaa aptidão, o quão boa é a solução. É feita uma 
    análise para saber quão bem as aptidões respondem ao problema proposto;
    
    3 - Seleção: indivíduos são selecionados para a reprodução. A probabilidade 
    de uma dada solução a ser selecionada é proporcional a sua aptidão;
    
    4 - Cruzamento: características das soluções escolhidas são recombinadas, 
    gerando novos indivíduos;
    
    5 - Mutação: características dos indivíduos resultantes do processo de
    reprodução são alteradas, acrescentando assim variedade à população;
    
    6 - Atualização: os indivíduos criados nesta geração são inseridos na
    população;
    
    7 - Finalização: verifica se as condições de encerramento da evolução
    foram atingidas, retornando para a etapa de avaliação em caso
    negativo e encerrando a execução em caso positivo.

A ideia geral de um algoritmo genético está fundamentada na **representação de um problema**, por meio de um conjunto de indivíduos que são possíveis soluções para o tal problema. Através de processos de seleção, reprodução e mutação, obtém-se uma nova geração de indivíduos e o processo continua. Após um certo número de gerações, espera-se que convirja para uma geração de elite que corresponde à melhor solução, ou solução aceitável para o problema.

**Componentes do algoritmo genético**

*1 - Indivíduo, cromossomo ou genótipo:* codificam potenciais soluções para o problema a ser tratado, e é através de sua manipulação (pelo processo de evolução) que respostas são encontradas. 
    Tipos de indivíduo mais comuns: 
        binários (001010);
        números inteiros (123456);
        símbolos (ABCDEFG);

