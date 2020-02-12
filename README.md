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

**- - - > Componentes do algoritmo genético**

**1 - Indivíduo, Cromossomo ou Genótipo:** codificam potenciais soluções para o problema a ser tratado, e é através de sua manipulação (pelo processo de evolução) que respostas são encontradas. 
    Tipos de indivíduo mais comuns: 
        binários (001010);
        números inteiros (123456);
        símbolos (ABCDEFG);

Define-se **fenótipo** como o ponto no domínio da *função objetivo* correspondente ao genótipo (G) utilizado.
Função que *decodifica* os genes do cromossomo?
Grau de adaptação?
Grau de aptidão?

**2 - População:** conjunto de indivíduos. Ao propagar características desejáveis a gerações subsequentes (cruzamento), enquanto novas são testadas (mutação), um Algoritmo Genético manipula a frequência com que determinadas sequências de genes aparecem nas populações sobre as quais atua.

Critérios de parada: invariância da média de adaptação (M_A) entre as últimas gerações.

**- - - > Operadores Genéticos**

**1 - Inicialização:** primeira etapa do processo, onde vão ser definidos os indivíduos da primeira geração. Normalmente, o genoma do indivíduo é produzido aleatoriamente, mas o usuário pode gerar todas as combinações possíveis dos *genes* (espaço de um parâmetro, bit, no caso de binário). Todavia, se torna óbvio que, nesse caso, o cromossomo deve ser pequeno. Tomando o tipo de genoma binário, tem-se que um cromossomo de tamanho 10, geraria 2^10 possibilidades de indivíduo. Quanto menor for o cromossomo, menos variação no campo de busca terá o algoritmo.

- Inicialização randômica:toma valores puramente aleatórios no domínio da função objetivo, podendo permitir áreas não exploradas.
- Inicialização por grid: toma valores igualmente espaçados no espaço de busca, causando uma exploração uniforme no espaço de busca para a primeira população.

**2 - Avaliação:** 

**3 - Seleção:** estágio onde os indivíduos são escolhidos para posterior cruzamento. Neste ponto, fazendo uso do grau de adequação de cada um, é efetuado um sorteio onde os mais aptos possuem maior probabilidade de se reproduzirem. Este grau é calculado a partir da função de avaliação de cada indivíduo, e determina quão apto ele está para a reprodução em relação à população a que pertence.

*Métodos de seleção: *
    - Scaling;
    - Por ranking;
    - Por giro de roleta;
    - Por torneio;
   
**4 - Crossover ou Recombinação:** cruzamento entre indivíduos para gerar a próxima geração.

*Operadores de cruzamento: *
    - cruzamento de um ponto; 
    - cruzamento multiponto;
    - cruzamento Segmentado;
    - cruzamento uniforme;
    - cruzamento por combinação parcial;
    
**5 - Mutação:** 




