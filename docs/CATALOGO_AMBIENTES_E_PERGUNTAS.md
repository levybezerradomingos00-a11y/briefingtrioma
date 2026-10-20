# Catálogo de ambientes e perguntas (versão final, v32)

Extraído automaticamente da build publicada em "Briefing Trioma Visual" (versão 32, 14/10/2026 20:58). É o conteúdo real que o app usa: ambientes, imagens dos baralhos com estilos, páginas, perguntas, opções e quais perguntas vêm desligadas por padrão. Os mesmos dados, em formato estruturado, estão em `dados/catalogo_ambientes_v32.json`.

Legenda: **[DESLIGADA]** = pergunta com `off: true` (entra desmarcada quando o ambiente é adicionado; o escritório liga em Personalizar). **[exclusiva]** = opção que desmarca as outras. `showIf` = só aparece quando outra resposta tem certo valor. `skipIfBriefingHas` = some quando o briefing também tem o ambiente indicado (evita pergunta repetida).

## Estilos usados nas imagens (perfil de estilo do relatório)

| chave | rótulo |
|---|---|
| `amadeirado` | Madeira aparente |
| `claro` | Tons claros |
| `escuro` | Tons escuros |
| `minimalista` | Minimalista |
| `classico` | Clássico |
| `pedra` | Pedras e mármores |
| `natural` | Natural e orgânico |
| `iluminacao` | Iluminação cênica |
| `cor` | Cor marcante |
| `industrial` | Metal e industrial |
| `dourado` | Dourado e luxo |

## Ordem fixa dos ambientes (constante `Am` no código)

`geral` → `hall` → `sala` → `cozinha` → `gourmet` → `lavabo_interno` → `lavabo_externo` → `master` → `closet` → `banho_master` → `servico` → `quarto` → `closet_suite` → `hospedes` → `hospedes_superior` → `banheiro`

## Resumo

| # | id | Ambiente | Imagens no baralho | Páginas | Perguntas | Desligadas | Repetível |
|---|---|---|---|---|---|---|---|
| 01 | `geral` | Sobre a família | 0 | 4 | 28 | 9 | não |
| 02 | `hall` | Hall de entrada | 0 | 1 | 6 | 2 | não |
| 03 | `sala` | Sala de estar e jantar | 24 | 2 | 13 | 3 | não |
| 04 | `cozinha` | Cozinha | 21 | 3 | 19 | 4 | não |
| 05 | `gourmet` | Varanda gourmet | 20 | 2 | 9 | 2 | não |
| 06 | `lavabo_interno` | Lavabo interno | 0 | 1 | 5 | 0 | não |
| 07 | `lavabo_externo` | Lavabo externo | 0 | 1 | 6 | 0 | não |
| 08 | `master` | Suíte master | 21 | 2 | 10 | 0 | não |
| 09 | `closet` | Closet master | 11 | 1 | 10 | 0 | não |
| 10 | `banho_master` | Banheiro master | 14 | 2 | 20 | 1 | não |
| 11 | `servico` | Área de serviço | 0 | 1 | 5 | 0 | não |
| 12 | `quarto` | Quarto | 12 | 2 | 15 | 4 | sim |
| 13 | `closet_suite` | Closet suíte | 5 | 1 | 6 | 0 | sim |
| 14 | `hospedes` | Suíte de hóspedes térreo | 10 | 2 | 10 | 0 | não |
| 15 | `hospedes_superior` | Suíte de hóspedes superior | 10 | 2 | 10 | 0 | não |
| 16 | `banheiro` | Banheiros da casa | 11 | 1 | 10 | 2 | não |

## 01. Sobre a família (`geral`)

- Chamada: Pessoas · Rotina · Convivência
- Introdução: Começamos entendendo quem vai viver na casa, como é a rotina e o que vocês mais valorizam.
- Capa: `img/capas/geral.jpg`
- Repetível no mesmo briefing: não

Sem baralho de imagens (só perguntas).

### Página 1: Quem vai viver nesta casa? (`quem`)
_As pessoas e os pets da casa. Quase tudo aqui é só tocar._

1. **Quem vai morar na casa?** `moradores` · contagem por categoria · ícone `users`
   - Dica: Toque para incluir e ajuste a quantidade.
   - Unidade: pessoa / pessoas
   - Máximo: 10
   - Opções:
     - Bebê (até 2 anos; ícone `baby`) · valor `bebe`
     - Criança (3 a 12 anos; ícone `puzzle`) · valor `crianca`
     - Adolescente (13 a 17 anos; ícone `gamepad`) · valor `adolescente`
     - Adulto (ícone `user`) · valor `adulto`
     - 60+ (ícone `armchair`) · valor `60`
2. **Pretendem aumentar a família?** `aumentar` · uma opção · ícone `user-plus` **[DESLIGADA]**
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
3. **Têm animais de estimação?** `pets` · contagem por categoria · ícone `paw`
   - Dica: Toque para incluir e ajuste a quantidade.
   - Lembrete: Mande fotos dos seus pets no nosso grupo do WhatsApp. Isso ajuda a escolher tecidos, pisos e o cantinho deles.
   - Unidade: pet / pets
   - Opção de nenhum: "Não temos"
   - Texto do outro: "Qual animal?"
   - Máximo: 10
   - Opções:
     - Cachorro (ícone `dog`) · valor `cachorro`
     - Gato (ícone `cat`) · valor `gato`
     - Pássaro (ícone `bird`) · valor `passaro`
     - Outro (ícone `paw`) · valor `outro`

### Página 2: Rotina e convivência (`rotina`)
_Cuidados da família, quem trabalha na casa e como vocês recebem._

1. **Alguma necessidade de acessibilidade, alergia ou condição de saúde a considerar?** `acessibilidade` · texto livre · ícone `accessibility`
   - Texto de exemplo no campo: "Se não houver, pode pular"
2. **Quantos funcionários trabalham na casa?** `funcionarios` · número · ícone `briefcase`
   - Faixa: 0 a 8, passo 1
3. **Onde costumam assistir TV?** `tv` · uma opção · ícone `tv` **[DESLIGADA]**
   - Opções:
     - Na sala (ícone `sofa`) · valor `na-sala`
     - Nos quartos (ícone `bed`) · valor `nos-quartos`
     - Em ambos (sala e quartos; ícone `house`) · valor `em-ambos`
4. **Quem cozinha no dia a dia?** `quem-cozinha` · uma opção · ícone `chef-hat` **[DESLIGADA]**
   - Opções:
     - Nós mesmos (ícone `users`) · valor `nos-mesmos`
     - Funcionário(a) (ícone `briefcase`) · valor `funcionario-a`
     - Os dois (ícone `house`) · valor `os-dois`
     - Quase ninguém (pedimos fora; ícone `coffee`) · valor `quase-ninguem`
5. **Alguém trabalha ou estuda em casa?** `home-office` · uma opção · ícone `laptop`
   - Campo extra de observação: Quem e em que horário? (opcional)
   - Opções:
     - Ninguém (ícone `x`) · valor `ninguem`
     - Às vezes (ícone `calendar`) · valor `as-vezes`
     - Todo dia (ícone `laptop`) · valor `todo-dia`
6. **Gostam de receber amigos e família?** `receber` · uma opção · ícone `party`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
7. **Quantas pessoas querem receber ao mesmo tempo, com conforto?** `receber-qtd` · uma opção · ícone `users`
   - Dica: Somando sala, varanda e cozinha.
   - Só aparece se `receber` = `sim`
   - Opções:
     - Até 8 · valor `ate-8`
     - 9 a 15 · valor `9-a-15`
     - 16 a 25 · valor `16-a-25`
     - 26 a 40 · valor `26-a-40`
     - Mais de 40 · valor `mais-de-40`
8. **Algum hobby em comum?** `hobby` · várias opções · ícone `heart` **[DESLIGADA]**
   - Aceita "Outro" com texto
   - Opções:
     - Cozinhar (ícone `chef-hat`) · valor `cozinhar`
     - Filmes e séries (ícone `popcorn`) · valor `filmes-e-series`
     - Leitura (ícone `book`) · valor `leitura`
     - Música (ícone `music`) · valor `musica`
     - Games (ícone `gamepad`) · valor `games`
     - Esportes (ícone `dumbbell`) · valor `esportes`
     - Plantas (ícone `sprout`) · valor `plantas`
     - Receber (ícone `party`) · valor `receber`
     - Trabalhos manuais (ferramentas, consertos; ícone `hammer`) · valor `trabalhos-manuais`
     - Cuidar do carro (lavar, polir, estética; ícone `car`) · valor `cuidar-do-carro`
9. **Querem um cantinho com bancada e ferramentas?** `oficina` · uma opção · ícone `hammer`
   - Dica: Para trabalhos manuais, consertos ou marcenaria.
   - Campo extra de observação: O que costumam fazer? (opcional)
   - Só aparece se `hobby` = `trabalhos-manuais`
   - Opções:
     - Na varanda ou deck (ícone `sun`) · valor `na-varanda-ou-deck`
     - Na área de serviço (ícone `washer`) · valor `na-area-de-servico`
     - Na garagem (ícone `car`) · valor `na-garagem`
     - Um cômodo só para isso (ícone `door-open`) · valor `um-comodo-so-para-isso`
     - Não precisa (ícone `x`) · valor `nao-precisa`
10. **O que prever na garagem para cuidar do carro?** `garagem` · várias opções · ícone `car`
   - Só aparece se `hobby` = `cuidar-do-carro`
   - Opções:
     - Ponto de água (torneira ou mangueira; ícone `droplets`) · valor `ponto-de-agua`
     - Tomada (aspirador, politriz; ícone `plug`) · valor `tomada`
     - Armário para produtos (ícone `archive`) · valor `armario-para-produtos`
     - Boa iluminação (ícone `bulb`) · valor `boa-iluminacao`
     - Não precisa (ícone `x`) · valor `nao-precisa`

### Página 3: O que importa para vocês (`prefs`)
_Isso orienta as decisões de layout, materiais e orçamento._

1. **E o que mais valorizam?** `valorizam` · várias opções · ícone `heart` **[DESLIGADA]**
   - Aceita "Outro" com texto
   - Opções:
     - Conforto · valor `conforto`
     - Iluminação aconchegante · valor `iluminacao-aconchegante`
     - Praticidade · valor `praticidade`
     - Beleza · valor `beleza`
     - Integração · valor `integracao`
     - Contato com a natureza · valor `contato-com-a-natureza`
     - Tecnologia · valor `tecnologia`
     - Silêncio · valor `silencio`
2. **O que mais incomoda vocês numa casa?** `incomoda` · várias opções · ícone `thumbs-down`
   - Aceita "Outro" com texto
   - Opções:
     - Bagunça à vista · valor `bagunca-a-vista`
     - Pouca luz natural · valor `pouca-luz-natural`
     - Calor · valor `calor`
     - Pouco espaço para guardar · valor `pouco-espaco-para-guardar`
     - Ambientes apertados · valor `ambientes-apertados`
     - Falta de privacidade · valor `falta-de-privacidade`
3. **Se tivessem que escolher prioridades para investir mais, quais seriam?** `prioridades` · várias opções · ícone `gem` **[DESLIGADA]**
   - Máximo: 3
   - Opções:
     - Marcenaria (ícone `boxes`) · valor `marcenaria`
     - Iluminação (ícone `bulb`) · valor `iluminacao`
     - Móveis (ícone `sofa`) · valor `moveis`
     - Revestimentos (ícone `layers`) · valor `revestimentos`
     - Tecnologia (ícone `wifi`) · valor `tecnologia`
     - Decoração (ícone `frame`) · valor `decoracao`
4. **Pretendem automatizar algo na casa?** `automacao` · várias opções · ícone `wifi`
   - Dica: Marque o que gostariam de controlar pelo celular ou por voz.
   - Opções:
     - Iluminação (ícone `bulb`) · valor `iluminacao`
     - Som (ícone `speaker`) · valor `som`
     - TV (ícone `tv`) · valor `tv`
     - Ar-condicionado (ícone `air-vent`) · valor `ar-condicionado`
     - Cortinas (ícone `blinds`) · valor `cortinas`
     - Segurança (ícone `camera`) · valor `seguranca`
     - Ainda não sei (vamos decidir com calma; exclusiva; ícone `help`) · valor `ainda-nao-sei`
5. **Onde querem automação?** `automacao-onde` · uma opção · ícone `house`
   - Só aparece se `automacao` = `['iluminacao', 'som', 'tv', 'ar-condicionado', 'cortinas', 'seguranca']`
   - Opções:
     - Na casa toda (ícone `house`) · valor `na-casa-toda`
     - Só em alguns ambientes (para focar o investimento; ícone `layers`) · valor `so-em-alguns-ambientes`
6. **Em quais ambientes?** `automacao-ambientes` · várias opções · ícone `layers`
   - Campo extra de observação: Algum outro lugar? (opcional)
   - Só aparece se `automacao-onde` = `so-em-alguns-ambientes`
   - Opções montadas a partir de: `briefing` (ambientes do briefing)

### Página 4: Gostos e materiais (`estilo`)
_Cores, texturas e o que já está definido para a casa._

1. **Que tons combinam mais com vocês?** `cores` · várias opções · ícone `palette`
   - Campo extra de observação: Alguma cor que amam ou não suportam? (opcional)
   - Opções:
     - Neutros (amostra de cor) · valor `neutros`
     - Suaves (amostra de cor) · valor `suaves`
     - Intensos (amostra de cor) · valor `intensos`
2. **Gostam de madeira aparente?** `amadeirado` · uma opção · ícone `trees`
   - Opções:
     - Sim, bastante (paredes, teto ou móveis; foto `img/opcoes/madeira_bastante.jpg`) · valor `sim-bastante`
     - Só um detalhe (um painel ou uma peça; foto `img/opcoes/madeira_detalhe.jpg`) · valor `so-um-detalhe`
     - Prefiro não (sem madeira aparente; foto `img/opcoes/madeira_sem.jpg`) · valor `prefiro-nao`
3. **Na escolha dos materiais, o que pesa mais?** `manutencao` · escala entre dois polos · ícone `scale` **[DESLIGADA]**
   - Polos: Praticidade ↔ Sofisticação
4. **Gostam de plantas dentro de casa?** `plantas` · uma opção · ícone `sprout` **[DESLIGADA]**
   - Opções:
     - Muitas naturais (ícone `trees`) · valor `muitas-naturais`
     - Algumas naturais (ícone `sprout`) · valor `algumas-naturais`
     - Só artificiais (sem cuidado diário; ícone `flower`) · valor `so-artificiais`
     - Sem plantas (ícone `x`) · valor `sem-plantas`
5. **Têm quadros ou coleções para expor?** `arte` · uma opção · ícone `frame` **[DESLIGADA]**
   - Opções:
     - Sim, vários (ícone `frame`) · valor `sim-varios`
     - Alguns (ícone `square`) · valor `alguns`
     - Não (ícone `x`) · valor `nao`
6. **Algum móvel já está definido?** `moveis` · várias opções · ícone `sofa`
   - Dica: Móveis já definidos precisam ser enviados no nosso grupo do WhatsApp (fotos e medidas) para entrarem no projeto.
   - Opções:
     - Vamos manter alguns (da casa atual; ícone `house`) · valor `vamos-manter-alguns`
     - Já escolhemos novos (para comprar; ícone `bag`) · valor `ja-escolhemos-novos`
     - Ainda não (ícone `x`) · valor `ainda-nao`
7. **Quais móveis?** `moveis-quais` · texto livre · ícone `armchair`
   - Texto de exemplo no campo: "Ex.: sofá, mesa de jantar, cama, aparador"
   - Lembrete: Importante: envie fotos e medidas desses móveis no nosso grupo do WhatsApp. Precisamos delas para considerar cada peça no projeto.
   - Só aparece se `moveis` = `['vamos-manter-alguns', 'ja-escolhemos-novos']`
   - Campo de várias linhas
8. **Algum desejo especial para a casa nova?** `desejo` · texto livre · ícone `sparkles`
   - Texto de exemplo no campo: "Aquele detalhe que vocês sempre quiseram ter."
   - Campo de várias linhas
9. **Adicionar observação** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Algo que queira contar sobre este ambiente, ou itens que serão mantidos."

## 02. Hall de entrada (`hall`)

- Chamada: Chegada · Acolhimento · Identidade
- Introdução: O primeiro contato com a casa deve combinar acolhimento, funcionalidade e identidade.
- Capa: `img/capas/hall.jpg`
- Repetível no mesmo briefing: não

Sem baralho de imagens (só perguntas).

### Página 1: Hall de entrada (`hall`)
_O primeiro contato com a casa._

1. **O que o hall deve transmitir?** `transmitir` · várias opções · ícone `door-open` **[DESLIGADA]**
   - Opções:
     - Acolhimento (ícone `heart`) · valor `acolhimento`
     - Sofisticação (ícone `gem`) · valor `sofisticacao`
     - Praticidade (ícone `timer`) · valor `praticidade`
     - Impacto visual (ícone `sparkles`) · valor `impacto-visual`
2. **Pedem para tirar os sapatos na entrada?** `sapatos` · uma opção · ícone `footprints` **[DESLIGADA]**
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
3. **Querem um móvel para sapatos, bolsas e chaves?** `movel` · uma opção · ícone `archive`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
4. **Fechadura eletrônica?** `fechadura` · uma opção · ícone `key`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
5. **Espelho no hall, para a última olhada antes de sair?** `espelho` · uma opção · ícone `mirror`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
6. **Adicionar observação** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Algo que queira contar sobre este ambiente, ou itens que serão mantidos."

## 03. Sala de estar e jantar (`sala`)

- Chamada: Convivência · Receber · Relaxar
- Introdução: Um espaço pensado a partir da rotina, das preferências e das prioridades de quem vai viver aqui.
- Capa: `img/capas/sala.jpg`
- Texto do baralho: Composição, materiais e detalhes para a sala.
- Repetível no mesmo briefing: não

### Imagens do baralho (24)

| id | arquivo | tema | estilos |
|---|---|---|---|
| `sala-01` | `img/sala/01.jpg` | Estilo e composição | Minimalista, Tons claros |
| `sala-02` | `img/sala/02.jpg` | Estilo e composição | Iluminação cênica, Tons claros |
| `sala-03` | `img/sala/03.jpg` | Estilo e composição | Metal e industrial, Natural e orgânico, Madeira aparente |
| `sala-04` | `img/sala/04.jpg` | Estilo e composição | Tons escuros, Iluminação cênica |
| `sala-05` | `img/sala/05.jpg` | Estilo e composição | Tons claros, Minimalista |
| `sala-06` | `img/sala/06.jpg` | Estilo e composição | Natural e orgânico, Madeira aparente |
| `sala-07` | `img/sala/07.jpg` | Estilo e composição | Clássico, Tons claros, Dourado e luxo |
| `sala-08` | `img/sala/08.jpg` | Estilo e composição | Metal e industrial, Madeira aparente |
| `sala-09` | `img/sala/09.jpg` | Estilo e composição | Tons claros, Natural e orgânico, Minimalista |
| `sala-10` | `img/sala/10.jpg` | Estilo e composição | Cor marcante, Tons claros |
| `sala-11` | `img/sala/11.jpg` | Estilo e composição | Natural e orgânico, Metal e industrial |
| `sala-12` | `img/sala/12.jpg` | Estilo e composição | Cor marcante, Natural e orgânico, Metal e industrial |
| `sala-13` | `img/sala/13.jpg` | Estilo e composição | Madeira aparente, Natural e orgânico, Cor marcante |
| `sala-14` | `img/sala/14.jpg` | Estilo e composição | Pedras e mármores, Madeira aparente, Natural e orgânico |
| `sala-15` | `img/sala/15.jpg` | Estilo e composição | Cor marcante, Madeira aparente |
| `sala-16` | `img/sala/16.jpg` | Estilo e composição | Madeira aparente, Tons claros |
| `sala-17` | `img/sala/17.jpg` | Estilo e composição | Pedras e mármores, Madeira aparente |
| `sala-18` | `img/sala/18.jpg` | Estilo e composição | Pedras e mármores, Madeira aparente, Iluminação cênica |
| `sala-19` | `img/sala/19.jpg` | Estilo e composição | Madeira aparente, Pedras e mármores |
| `sala-20` | `img/sala/20.jpg` | Estilo e composição | Pedras e mármores, Tons escuros, Iluminação cênica |
| `sala-21` | `img/sala/21.jpg` | Estilo e composição | Tons escuros, Metal e industrial |
| `sala-22` | `img/sala/22.jpg` | Estilo e composição | Iluminação cênica, Tons escuros |
| `sala-23` | `img/sala/23.jpg` | Estilo e composição | Clássico, Tons claros |
| `sala-24` | `img/sala/24.jpg` | Estilo e composição | Clássico, Dourado e luxo, Cor marcante |

### Página 1: Como vocês usam a sala? (`uso`)
_Isso define layout, capacidade e o nível de formalidade._

1. **A família se reúne para ver TV?** `tv-familia` · uma opção · ícone `tv`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
2. **Onde preferem receber visitas?** `visitas` · uma opção · ícone `users`
   - Opções:
     - Na sala (ícone `sofa`) · valor `na-sala`
     - Na varanda (ícone `sun`) · valor `na-varanda`
     - Em ambos (sala e varanda; ícone `house`) · valor `em-ambos`
3. **Quantas pessoas querem receber com conforto?** `receber-qtd` · número · ícone `users`
   - Some se o briefing tiver o ambiente `geral`
   - Faixa: 2 a 40, passo 2
4. **Quantos lugares na mesa de jantar?** `lugares-mesa` · uma opção · ícone `cutlery`
   - Opções em formato de pílulas compactas
   - Opções:
     - 4 · valor `4`
     - 6 · valor `6`
     - 8 · valor `8`
     - 10 · valor `10`
     - 12 · valor `12`
     - O máximo que o espaço comportar (exclusiva; ícone `ruler`) · valor `o-maximo-que-o-espaco-comportar`
5. **Formato da mesa de jantar** `mesa-formato` · uma opção · ícone `cutlery`
   - Opções:
     - Redonda (desenho `mesa-redonda`) · valor `redonda`
     - Retangular (desenho `mesa-retangular`) · valor `retangular`
     - Quadrada (desenho `mesa-quadrada`) · valor `quadrada`
     - Oval (desenho `mesa-oval`) · valor `oval`
     - Orgânica (formas livres, como as de mármore; desenho `mesa-organica`) · valor `organica`
     - Arquiteto define (o que funcionar melhor no espaço; desenho `arquiteto`) · valor `arquiteto-define`
6. **Que linguagem combina mais?** `linguagem` · escala entre dois polos · ícone `clock` **[DESLIGADA]**
   - Polos: Atual ↔ Atemporal
7. **Que clima de luz combina mais?** `luz` · uma opção · ícone `bulb` **[DESLIGADA]**
   - Opções:
     - Clara (luz branca, funcional; amostra de cor) · valor `clara`
     - Aconchegante (luz amarela, indireta; amostra de cor) · valor `aconchegante`
     - Com cenas (muda conforme o momento; amostra de cor) · valor `com-cenas`
8. **Cortina ou persiana?** `cortinas` · várias opções · ícone `blinds` **[DESLIGADA]**
   - Opções:
     - Cortina de tecido (ícone `wind`) · valor `cortina-de-tecido`
     - Persiana (ícone `blinds`) · valor `persiana`
     - Blackout (ícone `moon`) · valor `blackout`
     - Arquiteto define (exclusiva; ícone `architect`) · valor `arquiteto-define`
9. **Algum móvel ou peça que precisa entrar no projeto?** `movel-especifico` · texto livre · ícone `armchair`
   - Texto de exemplo no campo: "Ex.: piano, aparador da família, quadro grande"
   - Some se o briefing tiver o ambiente `geral`
10. **Algum móvel ou equipamento será mantido?** `mantido` · texto livre · ícone `package`
   - Texto de exemplo no campo: "Se puder, mande fotos e medidas depois"
   - Some se o briefing tiver o ambiente `geral`

### Página 2: Tecnologia e equipamentos (`equip`)
_O que precisa de ponto elétrico, espaço ou infraestrutura._

1. **O que deve ser previsto na sala?** `equip` · lista de itens (tem / não tem + detalhe) · ícone `plug`
   - Itens:
     - TV (detalhe: Tamanho em polegadas) · escolhas: 42", 50", 60", 65", 70", 75", 85" · id `tv`
     - Home theater ou soundbar (detalhe: Marca / configuração) · id `home-theater-ou-soundbar`
     - Som embutido (detalhe: Teto, parede ou piso) · id `som-embutido`
     - Videogame (detalhe: Console / acessórios) · id `videogame`
     - Automação (detalhe: Quais funções?) · id `automacao`
     - Adega (detalhe: Capacidade / embutida ou solta) · id `adega`
     - Bancada de bar (detalhe: Copos, garrafas, coqueteleira) · id `bancada-de-bar`
     - Cantinho do café (detalhe: Cafeteira, xícaras, cápsulas) · id `cantinho-do-cafe`
     - Estante / armário (detalhe: O que precisa guardar?) · id `estante-armario`
     - Ar-condicionado (detalhe: Modelo, se já tiver) · id `ar-condicionado`
     - Outros eletrônicos (detalhe: Quais?) · id `outros-eletronicos`
2. **Que tipo de ar-condicionado preferem?** `ar-tipo` · uma opção · ícone `air-vent`
   - Só aparece se `equip` = `ar-condicionado`
   - Opções:
     - Split (aparelho na parede; desenho `ar-split`) · valor `split`
     - Cassete (embutido no teto; desenho `ar-cassete`) · valor `cassete`
     - Arquiteto define (o que funcionar melhor no espaço; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
3. **Adicionar observação** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Algo que queira contar sobre este ambiente, ou itens que serão mantidos."

## 04. Cozinha (`cozinha`)

- Chamada: Rotina · Preparo · Organização
- Introdução: Um espaço pensado a partir da rotina, das preferências e das prioridades de quem vai viver aqui.
- Capa: `img/capas/cozinha.jpg`
- Texto do baralho: Estilo e composição para a cozinha.
- Repetível no mesmo briefing: não

### Imagens do baralho (21)

| id | arquivo | tema | estilos |
|---|---|---|---|
| `cozinha-01` | `img/cozinha/01.jpg` | Estilo e composição | Cor marcante, Madeira aparente |
| `cozinha-02` | `img/cozinha/02.jpg` | Estilo e composição | Metal e industrial, Natural e orgânico |
| `cozinha-03` | `img/cozinha/03.jpg` | Estilo e composição | Pedras e mármores, Tons claros |
| `cozinha-04` | `img/cozinha/04.jpg` | Estilo e composição | Pedras e mármores, Tons claros, Minimalista |
| `cozinha-05` | `img/cozinha/05.jpg` | Estilo e composição | Tons escuros, Madeira aparente |
| `cozinha-06` | `img/cozinha/06.jpg` | Estilo e composição | Madeira aparente, Tons claros |
| `cozinha-07` | `img/cozinha/07.jpg` | Estilo e composição | Cor marcante, Metal e industrial |
| `cozinha-08` | `img/cozinha/08.jpg` | Estilo e composição | Madeira aparente, Natural e orgânico |
| `cozinha-09` | `img/cozinha/09.jpg` | Estilo e composição | Madeira aparente, Cor marcante, Tons escuros |
| `cozinha-10` | `img/cozinha/10.jpg` | Estilo e composição | Cor marcante, Metal e industrial |
| `cozinha-11` | `img/cozinha/11.jpg` | Estilo e composição | Pedras e mármores, Cor marcante |
| `cozinha-12` | `img/cozinha/12.jpg` | Estilo e composição | Cor marcante, Tons claros |
| `cozinha-13` | `img/cozinha/13.jpg` | Estilo e composição | Clássico, Dourado e luxo, Cor marcante |
| `cozinha-14` | `img/cozinha/14.jpg` | Estilo e composição | Madeira aparente, Natural e orgânico, Cor marcante |
| `cozinha-15` | `img/cozinha/15.jpg` | Estilo e composição | Madeira aparente, Tons claros |
| `cozinha-16` | `img/cozinha/16.jpg` | Estilo e composição | Madeira aparente, Cor marcante, Dourado e luxo |
| `cozinha-17` | `img/cozinha/17.jpg` | Estilo e composição | Minimalista, Madeira aparente |
| `cozinha-18` | `img/cozinha/18.jpg` | Estilo e composição | Tons escuros, Madeira aparente, Pedras e mármores |
| `cozinha-19` | `img/cozinha/19.jpg` | Estilo e composição | Metal e industrial, Tons escuros |
| `cozinha-20` | `img/cozinha/20.jpg` | Estilo e composição | Iluminação cênica, Tons escuros |
| `cozinha-21` | `img/cozinha/21.jpg` | Estilo e composição | Pedras e mármores, Madeira aparente, Iluminação cênica |

### Página 1: Bancada, cuba e metais (`bancada`)
_Pedra, cuba e acabamentos. A especificação técnica a gente compatibiliza no projeto._

1. **Pedra da bancada** `material` · várias opções · ícone `layers`
   - Opções:
     - Super Nano (branco liso; foto `img/opcoes/pedra_super_nano.jpg`) · valor `super-nano`
     - São Gabriel escovado (granito preto, textura fosca; foto `img/opcoes/pedra_sao_gabriel.jpg`) · valor `sao-gabriel-escovado`
     - Perla Santana (quartzito bege acinzentado com veios; foto `img/opcoes/pedra_perla_santana.jpg`) · valor `perla-santana`
     - Travertino (bege, com poros e veios aparentes; foto `img/opcoes/travertino.jpg`) · valor `travertino`
     - Detalhes em ônix iluminado (pedra translúcida com luz por trás; foto `img/opcoes/onix.jpg`) · valor `detalhes-em-onix-iluminado`
     - Outra (ícone `help`) · valor `outra`
2. **Tipo de cuba** `cuba` · várias opções · ícone `droplets`
   - Opções:
     - Única (desenho `cuba-unica`) · valor `unica`
     - Dupla (desenho `cuba-dupla`) · valor `dupla`
     - Esculpida (na própria pedra; desenho `cuba-esculpida`) · valor `esculpida`
     - Arquiteto define (o que funcionar melhor; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
3. **Calha úmida na bancada?** `calha` · uma opção · ícone `droplets`
   - Dica: Um rebaixo na pedra, ao lado da cuba, para escorrer a louça e deixar temperos à mão.
   - Figura explicativa `calha-umida`: Vista de cima: a calha fica atrás da cuba, rebaixada na pedra.
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
4. **Sem a calha, como preferem escorrer a louça?** `escorredor` · uma opção · ícone `layers`
   - Só aparece se `calha` = `nao`
   - Opções:
     - Escorredor aparente (sobre a bancada; ícone `layers`) · valor `escorredor-aparente`
     - Escorredor no armário (em cima da cuba; ícone `archive`) · valor `escorredor-no-armario`
     - Não precisa (usamos a lava-louças; ícone `x`) · valor `nao-precisa`
5. **Acabamento dos metais** `metais` · várias opções · ícone `sparkle`
   - Opções:
     - Dourado (amostra de cor) · valor `dourado`
     - Preto (amostra de cor) · valor `preto`
     - Inox (amostra de cor) · valor `inox`
     - Arquiteto define (exclusiva; ícone `architect`) · valor `arquiteto-define`
6. **Algo embutido na bancada?** `embutidos` · várias opções · ícone `plug` **[DESLIGADA]**
   - Opções:
     - Dispenser de detergente (ao lado da cuba, refil por baixo; desenho `dispenser`) · valor `dispenser-de-detergente`
     - Torre de tomadas (sobe quando precisa, some na pedra; desenho `torre-tomadas`) · valor `torre-de-tomadas`
     - Não precisa (ícone `x`) · valor `nao-precisa`
7. **Adicionar modelos ou observações** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Modelos já escolhidos, medidas ou outros detalhes."

### Página 2: Equipamentos (`equip`)
_O que entra na cozinha define pontos de gás, elétrica, água e exaustão._

1. **Com que frequência cozinham em casa?** `frequencia` · uma opção · ícone `pot`
   - Opções:
     - Todo dia (ícone `flame`) · valor `todo-dia`
     - Algumas vezes por semana (ícone `calendar`) · valor `algumas-vezes-por-semana`
     - Raramente (ícone `coffee`) · valor `raramente`
2. **O que deve ser previsto?** `coccao` · lista de itens (tem / não tem + detalhe) · ícone `flame`
   - Itens:
     - Cooktop a gás (detalhe: Número de bocas) · id `cooktop-a-gas`
     - Cooktop de indução (detalhe: Verificar carga elétrica) · id `cooktop-de-inducao`
     - Fogão de piso (detalhe: Modelo / largura) · id `fogao-de-piso`
     - Fogão de embutir (detalhe: Modelo / largura) · id `fogao-de-embutir`
     - Forno elétrico (detalhe: Modelo e dimensões) · id `forno-eletrico`
     - Forno a gás (detalhe: Modelo e dimensões) · id `forno-a-gas`
     - Micro-ondas (detalhe: Solto ou embutido) · id `micro-ondas`
     - Coifa de parede (detalhe: Largura) · id `coifa-de-parede`
     - Coifa de ilha (detalhe: Largura) · id `coifa-de-ilha`
     - Depurador (detalhe: Sem duto externo) · id `depurador`
3. **Quantas bocas?** `bocas` · número · ícone `flame`
   - Só aparece se `coccao` = `['cooktop-a-gas', 'cooktop-de-inducao', 'fogao-de-piso', 'fogao-de-embutir']`
   - Faixa: 2 a 6, passo 1
4. **O que vai ter na cozinha?** `equip` · lista de itens (tem / não tem + detalhe) · ícone `plug`
   - Itens:
     - Geladeira (detalhe: Tipo, modelo e dimensões) · id `geladeira`
     - Freezer (detalhe: Vertical ou horizontal) · id `freezer`
     - Lava-louças (detalhe: Capacidade / modelo) · id `lava-loucas`
     - Triturador de resíduos (detalhe: Sob a cuba) · id `triturador-de-residuos`
     - TV (detalhe: Tamanho / modelo) · id `tv`
     - Ar-condicionado (detalhe: Modelo, se já tiver) · id `ar-condicionado`
5. **Que tipo de ar-condicionado preferem?** `ar-tipo` · uma opção · ícone `air-vent`
   - Só aparece se `equip` = `ar-condicionado`
   - Opções:
     - Split (aparelho na parede; desenho `ar-split`) · valor `split`
     - Cassete (embutido no teto; desenho `ar-cassete`) · valor `cassete`
     - Arquiteto define (o que funcionar melhor no espaço; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
6. **Água filtrada** `agua` · várias opções · ícone `glass`
   - Opções:
     - Gelágua de torre · valor `gelagua-de-torre`
     - Gelágua de bancada · valor `gelagua-de-bancada`
     - Filtro na torneira · valor `filtro-na-torneira`
     - Filtro da geladeira · valor `filtro-da-geladeira`
7. **Adicionar modelos ou observações** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Modelos, dimensões ou outros detalhes."

### Página 3: Organização e armazenamento (`organizacao`)
_O que fica à vista e onde cada coisa é guardada._

1. **O que fica à mostra na cozinha?** `mostra` · uma opção · ícone `eye`
   - Dica: Ajuda a definir quanto vidro e iluminação usar nos armários.
   - Opções:
     - Tudo guardado (portas fechadas, visual limpo; foto `img/opcoes/cozinha_guardado.jpg`) · valor `tudo-guardado`
     - Um pouco de cada (algumas portas de vidro; foto `img/opcoes/cozinha_um_pouco.jpg`) · valor `um-pouco-de-cada`
     - Bastante à mostra (vidro com luz, taças e louças expostas; foto `img/opcoes/cozinha_mostra.jpg`) · valor `bastante-a-mostra`
2. **Lixeira** `lixeira` · várias opções · ícone `trash`
   - Opções:
     - De piso (solta, com pedal; desenho `lixeira-piso`) · valor `de-piso`
     - Embutida na bancada (abertura na pedra, cesto embaixo; desenho `lixeira-bancada`) · valor `embutida-na-bancada`
     - Embutida na marcenaria (gaveta com cestos, inclusive reciclável; desenho `lixeira-marcenaria`) · valor `embutida-na-marcenaria`
3. **Espaço para estoque de mantimentos?** `despensa` · uma opção · ícone `package` **[DESLIGADA]**
   - Opções:
     - Despensa separada (ícone `door-open`) · valor `despensa-separada`
     - Armário alto (ícone `archive`) · valor `armario-alto`
     - Não precisa (ícone `x`) · valor `nao-precisa`
4. **Fruteira** `fruteira` · uma opção · ícone `apple` **[DESLIGADA]**
   - Opções:
     - Aparente (sobre a bancada; desenho `fruteira-aparente`) · valor `aparente`
     - Embutida (nicho ou gaveta na marcenaria; desenho `fruteira-embutida`) · valor `embutida`
     - Não precisa (ícone `x`) · valor `nao-precisa`
5. **Querem um cantinho na cozinha para refeições rápidas?** `refeicoes` · várias opções · ícone `coffee` **[DESLIGADA]**
   - Dica: Café da manhã, lanche, uma refeição a dois. Se o espaço permitir.
   - Opções:
     - Sim, numa ilha ou bancada (ou península; ícone `square`) · valor `sim-numa-ilha-ou-bancada`
     - Não, usamos a mesa de jantar (ícone `cutlery`) · valor `nao-usamos-a-mesa-de-jantar`
     - Não, usamos o deck ou a varanda (ícone `sun`) · valor `nao-usamos-o-deck-ou-a-varanda`

## 05. Varanda gourmet (`gourmet`)

- Chamada: Receber · Cozinhar · Celebrar
- Introdução: Um espaço pensado a partir da rotina, das preferências e das prioridades de quem vai viver aqui.
- Capa: `img/capas/gourmet.jpg`
- Texto do baralho: Churrasqueira, uso e atmosfera da área gourmet.
- Repetível no mesmo briefing: não

### Imagens do baralho (20)

| id | arquivo | tema | estilos |
|---|---|---|---|
| `gourmet-01` | `img/gourmet/01.jpg` | Estilo e composição | Tons escuros, Madeira aparente |
| `gourmet-02` | `img/gourmet/02.jpg` | Estilo e composição | Tons claros, Natural e orgânico |
| `gourmet-03` | `img/gourmet/03.jpg` | Estilo e composição | Tons claros, Minimalista |
| `gourmet-04` | `img/gourmet/04.jpg` | Estilo e composição | Madeira aparente, Pedras e mármores, Iluminação cênica |
| `gourmet-05` | `img/gourmet/05.jpg` | Estilo e composição | Natural e orgânico, Pedras e mármores, Tons claros |
| `gourmet-06` | `img/gourmet/06.jpg` | Estilo e composição | Madeira aparente, Tons claros |
| `gourmet-07` | `img/gourmet/07.jpg` | Estilo e composição | Pedras e mármores, Natural e orgânico, Madeira aparente |
| `gourmet-08` | `img/gourmet/08.jpg` | Estilo e composição | Natural e orgânico, Madeira aparente |
| `gourmet-09` | `img/gourmet/09.jpg` | Estilo e composição | Madeira aparente, Tons claros |
| `gourmet-10` | `img/gourmet/10.jpg` | Estilo e composição | Pedras e mármores, Natural e orgânico, Madeira aparente |
| `gourmet-11` | `img/gourmet/11.jpg` | Estilo e composição | Cor marcante, Natural e orgânico |
| `gourmet-12` | `img/gourmet/12.jpg` | Estilo e composição | Tons claros, Natural e orgânico |
| `gourmet-13` | `img/gourmet/13.jpg` | Estilo e composição | Madeira aparente, Natural e orgânico |
| `gourmet-14` | `img/gourmet/14.jpg` | Estilo e composição | Pedras e mármores, Metal e industrial, Natural e orgânico |
| `gourmet-15` | `img/gourmet/15.jpg` | Estilo e composição | Minimalista, Natural e orgânico |
| `gourmet-16` | `img/gourmet/16.jpg` | Estilo e composição | Madeira aparente, Natural e orgânico |
| `gourmet-17` | `img/gourmet/17.jpg` | Estilo e composição | Metal e industrial, Madeira aparente |
| `gourmet-18` | `img/gourmet/18.jpg` | Estilo e composição | Natural e orgânico, Madeira aparente |
| `gourmet-19` | `img/gourmet/19.jpg` | Estilo e composição | Tons claros, Natural e orgânico, Minimalista |
| `gourmet-20` | `img/gourmet/20.jpg` | Estilo e composição | Cor marcante, Metal e industrial |

### Página 1: Como vocês usam a área gourmet? (`uso`)
_Capacidade, fechamento e paisagismo._

1. **Para que vão usar mais?** `uso` · várias opções · ícone `party`
   - Opções:
     - Churrasco com amigos (ícone `beer`) · valor `churrasco-com-amigos`
     - Almoço em família (ícone `cutlery`) · valor `almoco-em-familia`
     - Festas (ícone `party`) · valor `festas`
     - Descanso (ícone `sun`) · valor `descanso`
2. **Tipo de churrasqueira** `churrasqueira` · várias opções · ícone `flame`
   - Opções:
     - Carvão (tradicional ou parrilla; ícone `flame`) · valor `carvao`
     - Gás (embutida ou de bancada; ícone `pot`) · valor `gas`
     - Elétrica (compacta, pouca fumaça; ícone `zap`) · valor `eletrica`
     - Arquiteto define (exclusiva; ícone `architect`) · valor `arquiteto-define`
3. **Quantas pessoas querem receber com conforto?** `receber` · número · ícone `users`
   - Some se o briefing tiver o ambiente `geral`
   - Faixa: 2 a 60, passo 2
4. **Fechamento em vidro?** `vidro` · uma opção · ícone `wind`
   - Dica: Protege do vento e da chuva sem perder a vista.
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
5. **Plantas naturais integradas?** `vegetacao` · uma opção · ícone `sprout` **[DESLIGADA]**
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
6. **Algum móvel ou elemento que precisa entrar?** `movel` · texto livre · ícone `armchair` **[DESLIGADA]**

### Página 2: Equipamentos e apoio (`equip`)
_Marque o que deve ser previsto no projeto._

1. **O que vai ter na varanda?** `equip` · lista de itens (tem / não tem + detalhe) · ícone `plug`
   - Itens:
     - TV (detalhe: Tamanho / modelo) · id `tv`
     - Som ambiente (detalhe: Teto, parede ou piso) · id `som-ambiente`
     - Automação (detalhe: Iluminação, áudio, cortinas) · id `automacao`
     - Projetor externo (detalhe: Com tela ou projeção na parede) · id `projetor-externo`
     - Sofá (detalhe: Fixo ou solto? Quantos lugares?) · id `sofa`
     - Cervejeira (detalhe: Modelo / dimensões) · id `cervejeira`
     - Freezer (detalhe: Modelo / dimensões) · id `freezer`
     - Cooktop ou fogão (detalhe: Gás ou indução) · id `cooktop-ou-fogao`
     - Ar-condicionado (detalhe: Modelo, se já tiver) · id `ar-condicionado`
     - Outros (detalhe: Quais?) · id `outros`
2. **Que tipo de ar-condicionado preferem?** `ar-tipo` · uma opção · ícone `air-vent`
   - Só aparece se `equip` = `ar-condicionado`
   - Opções:
     - Split (aparelho na parede; desenho `ar-split`) · valor `split`
     - Cassete (embutido no teto; desenho `ar-cassete`) · valor `cassete`
     - Arquiteto define (o que funcionar melhor no espaço; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
3. **Adicionar observação** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Algo que queira contar sobre este ambiente, ou itens que serão mantidos."

## 06. Lavabo interno (`lavabo_interno`)

- Chamada: Receber · Detalhe · Impacto
- Introdução: O banheiro das visitas: pequeno, mas um ótimo lugar para ousar nos acabamentos.
- Capa: `img/capas/lavabo_interno.jpg`
- Repetível no mesmo briefing: não

Sem baralho de imagens (só perguntas).

### Página 1: Lavabo interno (`lavabo`)
_Peças e acabamentos do banheiro das visitas._

1. **Cuba** `cuba` · várias opções · ícone `droplets`
   - Opções:
     - Apoio (sobre a bancada; desenho `lav-apoio`) · valor `apoio`
     - Semiencaixe (metade para fora; desenho `lav-semiencaixe`) · valor `semiencaixe`
     - Esculpida (na própria pedra; desenho `lav-esculpida`) · valor `esculpida`
     - De piso (peça escultural; desenho `lav-piso`) · valor `de-piso`
     - Arquiteto define (o que funcionar melhor; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
2. **Torneira** `torneira` · várias opções · ícone `droplets`
   - Opções:
     - De mesa (foto `img/opcoes/torneira_mesa.jpg`) · valor `de-mesa`
     - De parede (foto `img/opcoes/torneira_parede.jpg`) · valor `de-parede`
3. **Formato do espelho** `espelho` · uma opção · ícone `mirror`
   - Opções:
     - Redondo (desenho `espelho-redondo`) · valor `redondo`
     - Orgânico (formas livres; desenho `espelho-organico`) · valor `organico`
     - Retangular (desenho `espelho-retangular`) · valor `retangular`
     - Arquiteto define (exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
4. **Como preferem os revestimentos?** `revestimento` · uma opção · ícone `layers`
   - Opções:
     - Uniformes (o mesmo material em todas as paredes; foto `img/opcoes/revest_uniforme.jpg`) · valor `uniformes`
     - Uma parede de destaque (geralmente atrás da bancada; foto `img/opcoes/revest_destaque.jpg`) · valor `uma-parede-de-destaque`
     - Arquiteto define (o que valorizar mais o espaço; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
5. **Adicionar observação** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Algo que queira contar sobre este ambiente, ou itens que serão mantidos."

## 07. Lavabo externo (`lavabo_externo`)

- Chamada: Área externa · Praticidade · Resistência
- Introdução: Atende a área gourmet, a piscina ou o jardim. Materiais resistentes e fáceis de limpar.
- Capa: `img/capas/lavabo_externo.jpg`
- Repetível no mesmo briefing: não

Sem baralho de imagens (só perguntas).

### Página 1: Lavabo externo (`lavabo`)
_Para quem está na área gourmet, na piscina ou no jardim._

1. **Cuba** `cuba` · várias opções · ícone `droplets`
   - Opções:
     - Apoio (sobre a bancada; desenho `lav-apoio`) · valor `apoio`
     - Semiencaixe (metade para fora; desenho `lav-semiencaixe`) · valor `semiencaixe`
     - Esculpida (na própria pedra; desenho `lav-esculpida`) · valor `esculpida`
     - Arquiteto define (o que funcionar melhor; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
2. **Torneira** `torneira` · várias opções · ícone `droplets`
   - Opções:
     - De mesa (foto `img/opcoes/torneira_mesa.jpg`) · valor `de-mesa`
     - De parede (foto `img/opcoes/torneira_parede.jpg`) · valor `de-parede`
3. **Ducha para quem sai da piscina?** `ducha` · uma opção · ícone `shower`
   - Dica: Pode ficar do lado de fora, perto da porta.
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
4. **Formato do espelho** `espelho` · uma opção · ícone `mirror`
   - Opções:
     - Redondo (desenho `espelho-redondo`) · valor `redondo`
     - Orgânico (formas livres; desenho `espelho-organico`) · valor `organico`
     - Retangular (desenho `espelho-retangular`) · valor `retangular`
     - Arquiteto define (exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
5. **Como preferem os revestimentos?** `revestimento` · uma opção · ícone `layers`
   - Opções:
     - Uniformes (o mesmo material em todas as paredes; foto `img/opcoes/revest_uniforme.jpg`) · valor `uniformes`
     - Uma parede de destaque (geralmente atrás da bancada; foto `img/opcoes/revest_destaque.jpg`) · valor `uma-parede-de-destaque`
     - Arquiteto define (o que valorizar mais o espaço; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
6. **Adicionar observação** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Algo que queira contar sobre este ambiente, ou itens que serão mantidos."

## 08. Suíte master (`master`)

- Chamada: Descanso · Conforto · Privacidade
- Introdução: Um espaço pensado a partir da rotina, das preferências e das prioridades do casal.
- Capa: `img/capas/master.jpg`
- Texto do baralho: Atmosfera, cabeceiras e materiais para a suíte do casal.
- Repetível no mesmo briefing: não

### Imagens do baralho (21)

| id | arquivo | tema | estilos |
|---|---|---|---|
| `master-01` | `img/master/01.jpg` | Estilo e composição | Madeira aparente, Tons claros |
| `master-02` | `img/master/02.jpg` | Estilo e composição | Tons claros, Minimalista |
| `master-03` | `img/master/03.jpg` | Estilo e composição | Tons escuros, Cor marcante |
| `master-04` | `img/master/04.jpg` | Estilo e composição | Madeira aparente, Minimalista |
| `master-05` | `img/master/05.jpg` | Estilo e composição | Natural e orgânico, Minimalista |
| `master-06` | `img/master/06.jpg` | Estilo e composição | Cor marcante, Clássico |
| `master-07` | `img/master/07.jpg` | Estilo e composição | Tons escuros, Madeira aparente, Iluminação cênica |
| `master-08` | `img/master/08.jpg` | Estilo e composição | Madeira aparente, Tons claros |
| `master-09` | `img/master/09.jpg` | Estilo e composição | Cor marcante, Tons escuros |
| `master-10` | `img/master/10.jpg` | Estilo e composição | Tons claros, Clássico |
| `master-11` | `img/master/11.jpg` | Estilo e composição | Cor marcante, Natural e orgânico |
| `master-12` | `img/master/12.jpg` | Estilo e composição | Natural e orgânico, Tons claros |
| `master-13` | `img/master/13.jpg` | Estilo e composição | Cor marcante, Minimalista |
| `master-14` | `img/master/14.jpg` | Estilo e composição | Cor marcante, Madeira aparente |
| `master-15` | `img/master/15.jpg` | Estilo e composição | Tons escuros, Madeira aparente, Clássico |
| `master-16` | `img/master/16.jpg` | Estilo e composição | Madeira aparente, Pedras e mármores |
| `master-17` | `img/master/17.jpg` | Estilo e composição | Minimalista, Tons claros |
| `master-18` | `img/master/18.jpg` | Estilo e composição | Tons escuros, Madeira aparente |
| `master-19` | `img/master/19.jpg` | Estilo e composição | Madeira aparente, Iluminação cênica, Natural e orgânico |
| `master-20` | `img/master/20.jpg` | Estilo e composição | Natural e orgânico, Madeira aparente, Iluminação cênica |
| `master-21` | `img/master/21.jpg` | Estilo e composição | Pedras e mármores, Tons escuros, Madeira aparente |

### Página 1: O quarto do casal (`rotina`)
_Cama, cabeceira e o jeito de descansar._

1. **Tamanho da cama** `cama` · uma opção · ícone `bed`
   - Opções:
     - Casal (138 × 188 cm; desenho `cama-casal`) · valor `casal`
     - Queen (158 × 198 cm; desenho `cama-queen`) · valor `queen`
     - King (193 × 203 cm; desenho `cama-king`) · valor `king`
2. **Que altura de cama estofada preferem?** `cama-altura` · uma opção · ícone `bed`
   - Dica: Altura do colchão até o chão. Tem gente que não se adapta a camas muito baixas.
   - Opções:
     - Mais baixa (em torno de 35 cm; desenho `cama-baixa`) · valor `mais-baixa`
     - Altura padrão (em torno de 50 cm; desenho `cama-padrao`) · valor `altura-padrao`
     - Mais alta (em torno de 60 cm; desenho `cama-alta`) · valor `mais-alta`
     - Definir com o arquiteto (deixamos em aberto e conversamos depois; exclusiva; desenho `arquiteto`) · valor `definir-com-o-arquiteto`
3. **Que tipo de cabeceira chama mais atenção?** `cabeceira` · várias opções · ícone `frame`
   - Opções:
     - Painel de pedra (foto `img/opcoes/cabeceira_pedra.jpg`) · valor `painel-de-pedra`
     - Madeira (foto `img/opcoes/cabeceira_madeira.jpg`) · valor `madeira`
     - Estofada (foto `img/opcoes/cabeceira_estofada.jpg`) · valor `estofada`
     - Com luz embutida (foto `img/opcoes/cabeceira_luz.jpg`) · valor `com-luz-embutida`
     - Simples e baixa (foto `img/opcoes/cabeceira_simples.jpg`) · valor `simples-e-baixa`
4. **Para dormir, preferem:** `cortina` · uma opção · ícone `moon`
   - Opções:
     - Escuro total (blackout; ícone `moon`) · valor `escuro-total`
     - Luz suave (cortina leve; ícone `sun`) · valor `luz-suave`
     - Os dois (blackout + voil; ícone `layers`) · valor `os-dois`
5. **Luz de leitura na cabeceira?** `leitura` · uma opção · ícone `lamp`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
6. **Estudam ou trabalham no quarto?** `estudar` · uma opção · ícone `laptop`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
7. **Algum móvel ou detalhe que precisa entrar?** `movel` · texto livre · ícone `armchair`

### Página 2: Mobiliário e equipamentos (`equip`)
_Dimensione a partir do uso real e do que vai permanecer._

1. **O que vai ter no quarto?** `equip` · lista de itens (tem / não tem + detalhe) · ícone `plug`
   - Itens:
     - TV (detalhe: Tamanho em polegadas) · escolhas: [, c, i, r, c, u, l, a, r, ] · id `tv`
     - Penteadeira / maquiagem (detalhe: Dimensões / iluminação) · id `penteadeira-maquiagem`
     - Poltrona ou chaise (detalhe: Cantinho de leitura?) · id `poltrona-ou-chaise`
     - Bancada de trabalho (detalhe: Para computador ou notebook. Quantas pessoas usam?) · id `bancada-de-trabalho`
     - Eletrônicos (detalhe: Quais?) · id `eletronicos`
     - Ar-condicionado (detalhe: Modelo, se já tiver) · id `ar-condicionado`
2. **Que tipo de ar-condicionado preferem?** `ar-tipo` · uma opção · ícone `air-vent`
   - Só aparece se `equip` = `ar-condicionado`
   - Opções:
     - Split (aparelho na parede; desenho `ar-split`) · valor `split`
     - Cassete (embutido no teto; desenho `ar-cassete`) · valor `cassete`
     - Arquiteto define (o que funcionar melhor no espaço; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
3. **Adicionar observação** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Algo que queira contar sobre este ambiente, ou itens que serão mantidos."

## 09. Closet master (`closet`)

- Chamada: Organização · Rotina · Cuidado
- Introdução: Objetos, hábitos e volume de peças definem um closet que funciona no dia a dia.
- Capa: `img/capas/closet.jpg`
- Texto do baralho: Referências de closet: portas, iluminação e organização.
- Repetível no mesmo briefing: não

### Imagens do baralho (11)

| id | arquivo | tema | estilos |
|---|---|---|---|
| `closet-01` | `img/closet/01.jpg` | Estilo e composição | Madeira aparente, Tons claros |
| `closet-02` | `img/closet/02.jpg` | Estilo e composição | Madeira aparente |
| `closet-03` | `img/closet/03.jpg` | Estilo e composição | Cor marcante, Minimalista |
| `closet-04` | `img/closet/04.jpg` | Estilo e composição | Madeira aparente, Tons claros |
| `closet-05` | `img/closet/05.jpg` | Estilo e composição | Madeira aparente, Minimalista |
| `closet-06` | `img/closet/06.jpg` | Estilo e composição | Madeira aparente, Pedras e mármores |
| `closet-07` | `img/closet/07.jpg` | Estilo e composição | Madeira aparente, Natural e orgânico, Iluminação cênica |
| `closet-08` | `img/closet/08.jpg` | Estilo e composição | Tons escuros, Madeira aparente |
| `closet-09` | `img/closet/09.jpg` | Estilo e composição | Tons claros, Madeira aparente |
| `closet-10` | `img/closet/10.jpg` | Estilo e composição | Minimalista, Tons claros |
| `closet-11` | `img/closet/11.jpg` | Estilo e composição | Pedras e mármores, Tons claros, Dourado e luxo |

### Página 1: Organização do closet (`organizacao`)
_Quantidade de peças e hábitos definem a divisão interna._

1. **Como imaginam o closet?** `tipo` · várias opções · ícone `shirt`
   - Opções:
     - Aberto (tudo à vista; foto `img/opcoes/closet_aberto.jpg`) · valor `aberto`
     - Portas de vidro (protege e mostra; foto `img/opcoes/closet_vidro.jpg`) · valor `portas-de-vidro`
     - Portas fechadas (tudo guardado; foto `img/opcoes/closet_fechado.jpg`) · valor `portas-fechadas`
2. **Uma ilha com gavetas no meio?** `ilha` · uma opção · ícone `boxes`
   - Figura explicativa `None`: Exemplo de ilha com gavetas
   - Opções:
     - Sim (ícone `check`) · valor `sim`
     - Sim, se o espaço permitir (ícone `ruler`) · valor `sim-se-o-espaco-permitir`
     - Não (ícone `x`) · valor `nao`
3. **Espelho de corpo inteiro?** `espelho` · uma opção · ícone `mirror`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
4. **Roupas mais em cabides ou em gavetas?** `roupas` · uma opção · ícone `shirt`
   - Opções:
     - Mais cabides (ícone `shirt`) · valor `mais-cabides`
     - Mais gavetas (ícone `archive`) · valor `mais-gavetas`
     - Meio a meio (ícone `columns`) · valor `meio-a-meio`
5. **Muitas peças longas?** `pecas-longas` · uma opção · ícone `shirt`
   - Dica: Vestidos e casacos pedem cabideiro alto.
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
6. **Quantos pares de calçados cada um tem, mais ou menos?** `calcados` · campos nomeados · ícone `footprints`
   - Dica: Escreva o nome e a quantidade de cada pessoa.
   - Campos com nome editável (ex.: nome da pessoa)
   - Campos: Pessoa 1 (número), Pessoa 2 (número)
7. **Quantas bolsas, no total?** `bolsas` · número · ícone `bag`
   - Faixa: 0 a 120, passo 5
8. **Guardam joias ou objetos de valor?** `joias` · uma opção · ícone `gem`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
9. **Querem um cofre?** `cofre` · uma opção · ícone `vault`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
10. **Adicionar observação** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Algo que queira contar sobre este ambiente, ou itens que serão mantidos."

## 10. Banheiro master (`banho_master`)

- Chamada: Bem-estar · Rotina · Detalhe
- Introdução: Um espaço pensado a partir da rotina, das preferências e das prioridades do casal.
- Capa: `img/capas/banho_master.jpg`
- Texto do baralho: Atmosfera e materiais para o banheiro do casal.
- Repetível no mesmo briefing: não

### Imagens do baralho (14)

| id | arquivo | tema | estilos |
|---|---|---|---|
| `banho_master-01` | `img/banho_master/01.jpg` | Estilo e composição | Clássico, Cor marcante |
| `banho_master-02` | `img/banho_master/02.jpg` | Estilo e composição | Tons escuros, Pedras e mármores |
| `banho_master-03` | `img/banho_master/03.jpg` | Estilo e composição | Cor marcante, Clássico |
| `banho_master-04` | `img/banho_master/04.jpg` | Estilo e composição | Natural e orgânico, Madeira aparente, Cor marcante |
| `banho_master-05` | `img/banho_master/05.jpg` | Estilo e composição | Pedras e mármores, Madeira aparente |
| `banho_master-06` | `img/banho_master/06.jpg` | Estilo e composição | Tons escuros, Madeira aparente, Cor marcante |
| `banho_master-07` | `img/banho_master/07.jpg` | Estilo e composição | Minimalista, Pedras e mármores |
| `banho_master-08` | `img/banho_master/08.jpg` | Estilo e composição | Pedras e mármores, Tons claros, Minimalista |
| `banho_master-09` | `img/banho_master/09.jpg` | Estilo e composição | Pedras e mármores, Tons claros |
| `banho_master-10` | `img/banho_master/10.jpg` | Estilo e composição | Cor marcante, Pedras e mármores, Clássico |
| `banho_master-11` | `img/banho_master/11.jpg` | Estilo e composição | Pedras e mármores, Dourado e luxo |
| `banho_master-12` | `img/banho_master/12.jpg` | Estilo e composição | Tons escuros, Pedras e mármores |
| `banho_master-13` | `img/banho_master/13.jpg` | Estilo e composição | Tons escuros, Iluminação cênica, Madeira aparente |
| `banho_master-14` | `img/banho_master/14.jpg` | Estilo e composição | Pedras e mármores, Madeira aparente, Cor marcante |

### Página 1: Louças, metais e revestimentos (`loucas`)
_Escolhas de uso primeiro. Acabamento e especificação técnica depois._

1. **Cuba** `cuba` · várias opções · ícone `droplets`
   - Opções:
     - Apoio (desenho `lav-apoio`) · valor `apoio`
     - Embutir (desenho `lav-embutir`) · valor `embutir`
     - Esculpida (desenho `lav-esculpida`) · valor `esculpida`
     - De piso (peça escultural; desenho `lav-piso`) · valor `de-piso`
     - Arquiteto define (o que funcionar melhor; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
2. **Duas cubas, uma para cada?** `duas-cubas` · uma opção · ícone `users`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
3. **Pedra da bancada** `pedra` · várias opções · ícone `layers`
   - Opções:
     - Super Nano (branco liso; foto `img/opcoes/pedra_super_nano.jpg`) · valor `super-nano`
     - São Gabriel escovado (granito preto, textura fosca; foto `img/opcoes/pedra_sao_gabriel.jpg`) · valor `sao-gabriel-escovado`
     - Perla Santana (quartzito bege acinzentado com veios; foto `img/opcoes/pedra_perla_santana.jpg`) · valor `perla-santana`
     - Travertino (bege, com poros e veios aparentes; foto `img/opcoes/travertino.jpg`) · valor `travertino`
     - Detalhes em ônix iluminado (pedra translúcida com luz por trás; foto `img/opcoes/onix.jpg`) · valor `detalhes-em-onix-iluminado`
     - Outra (ícone `help`) · valor `outra`
4. **Torneira** `torneira` · várias opções · ícone `droplets`
   - Opções:
     - De mesa (foto `img/opcoes/torneira_mesa.jpg`) · valor `de-mesa`
     - De parede (foto `img/opcoes/torneira_parede.jpg`) · valor `de-parede`
5. **Acima da bancada** `armario` · uma opção · ícone `archive`
   - Opções:
     - Armário com espelho (espelho na frente das portas; desenho `armario-espelho`) · valor `armario-com-espelho`
     - Só espelho (sem armário em cima; desenho `espelho`) · valor `so-espelho`
6. **Chuveiro** `chuveiro` · várias opções · ícone `shower`
   - Opções:
     - De parede (foto `img/opcoes/chuveiro_parede.jpg`) · valor `de-parede`
     - De teto (foto `img/opcoes/chuveiro_teto.jpg`) · valor `de-teto`
     - Duplo (um para cada; ícone `shower`) · valor `duplo`
7. **Box do chuveiro** `box` · uma opção · ícone `shower`
   - Opções:
     - Até o teto (vidro do piso ao teto; desenho `box-teto`) · valor `ate-o-teto`
     - Padrão (altura comum, aberto em cima; desenho `box-padrao`) · valor `padrao`
     - Arquiteto define (conforme o uso do banheiro; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
8. **Como preferem os revestimentos?** `revestimento` · uma opção · ícone `layers`
   - Opções:
     - Uniformes (o mesmo material em todas as paredes; foto `img/opcoes/revest_uniforme.jpg`) · valor `uniformes`
     - Uma parede de destaque (cor ou textura diferente em uma parede; foto `img/opcoes/revest_destaque.jpg`) · valor `uma-parede-de-destaque`
     - Arquiteto define (o que valorizar mais o espaço; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
9. **Onde seria o destaque?** `revestimento-onde` · uma opção · ícone `layers`
   - Só aparece se `revestimento` = `uma-parede-de-destaque`
   - Opções:
     - Parede do box (ícone `shower`) · valor `parede-do-box`
     - Parede da bancada (ícone `droplets`) · valor `parede-da-bancada`
     - Arquiteto define (exclusiva; ícone `architect`) · valor `arquiteto-define`
10. **Quantos nichos no box?** `nichos` · número · ícone `layers` **[DESLIGADA]**
   - Dica: Para shampoo e produtos de higiene.
   - Faixa: 0 a 4, passo 1
11. **Banheira?** `banheira` · uma opção · ícone `bath`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
12. **Som ambiente?** `som` · uma opção · ícone `speaker`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
13. **Adicionar modelos ou observações** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Modelos já escolhidos, medidas ou outros detalhes."

### Página 2: Hábitos e preferências (`habitos`)
_A rotina define ergonomia, luz e onde guardar cada coisa._

1. **Que luz preferem no banheiro?** `iluminacao` · uma opção · ícone `bulb`
   - Opções:
     - Clara (luz branca, funcional; amostra de cor) · valor `clara`
     - Aconchegante (luz amarela, indireta; amostra de cor) · valor `aconchegante`
     - Com cenas (muda conforme o momento; amostra de cor) · valor `com-cenas`
2. **Onde ficam os perfumes?** `perfumes` · uma opção · ícone `gem`
   - Opções:
     - Banheiro (ícone `droplets`) · valor `banheiro`
     - Closet (ícone `shirt`) · valor `closet`
     - Em ambos (banheiro e closet; ícone `layers`) · valor `em-ambos`
3. **Muitos cremes e itens de cuidado?** `cremes` · uma opção · ícone `sparkles`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
4. **Alguém se maquia no banheiro?** `maquiagem` · uma opção · ícone `sparkle`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
5. **Costumam deixar roupa suja no banheiro?** `roupa-suja` · uma opção · ícone `shirt`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
6. **Gostam de metais aparentes?** `metalicos` · uma opção · ícone `sparkle`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
7. **Adicionar observação** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Algo que queira contar sobre este ambiente, ou itens que serão mantidos."

## 11. Área de serviço (`servico`)

- Chamada: Funcionalidade · Fluxo · Armazenamento
- Introdução: Uma boa área de serviço reduz ruído visual, organiza tarefas recorrentes e facilita a rotina da casa.
- Capa: `img/capas/servico.jpg`
- Repetível no mesmo briefing: não

Sem baralho de imagens (só perguntas).

### Página 1: Rotina e equipamentos (`rotina`)
_Lavagem, secagem, apoio e armazenamento._

1. **Quem mais usa a área de serviço?** `quem` · uma opção · ícone `user`
   - Opções:
     - Os moradores (ícone `users`) · valor `os-moradores`
     - Funcionário(a) (ícone `briefcase`) · valor `funcionario-a`
     - Ambos (ícone `house`) · valor `ambos`
2. **Com que frequência?** `frequencia` · uma opção · ícone `calendar`
   - Opções:
     - Todo dia · valor `todo-dia`
     - Algumas vezes por semana · valor `algumas-vezes-por-semana`
     - Uma vez por semana · valor `uma-vez-por-semana`
3. **O que precisa caber aqui?** `equip` · lista de itens (tem / não tem + detalhe) · ícone `washer`
   - Lembrete: Se as máquinas já estiverem definidas, mandem o modelo (ou uma foto da etiqueta) no nosso grupo do WhatsApp. Assim já consideramos as medidas certas.
   - Sem campo de detalhe por item (ambiente de apoio, rápido)
   - Lembrete aparece ao marcar: maquina-de-lavar, lava-e-seca, secadora
   - Itens:
     - Máquina de lavar (detalhe: Modelo / capacidade) · id `maquina-de-lavar`
     - Lava e seca (detalhe: Modelo / capacidade) · id `lava-e-seca`
     - Secadora (detalhe: Modelo / capacidade) · id `secadora`
     - Tanque (detalhe: Tanque ou cuba funda) · id `tanque`
     - Varal (detalhe: Teto, parede ou articulado) · id `varal`
     - Armário para vassoura e aspirador (detalhe: Altura do aspirador) · id `armario-para-vassoura-e-aspirador`
4. **Lugar específico para a tábua de passar?** `tabua` · uma opção · ícone `shirt`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
5. **Adicionar observação** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Algo que queira contar sobre este ambiente, ou itens que serão mantidos."

## 12. Quarto (`quarto`)

- Chamada: Rotina pessoal · Descanso · Estudo
- Introdução: Um espaço pensado a partir da rotina, das preferências e das prioridades de quem vai dormir aqui.
- Capa: `img/capas/quarto.jpg`
- Texto do baralho: Referências de quartos com estudo, lazer e descanso.
- Repetível no mesmo briefing: sim

### Imagens do baralho (12)

| id | arquivo | tema | estilos |
|---|---|---|---|
| `quarto-01` | `img/quarto/01.jpg` | Estilo e composição | Cor marcante, Tons claros |
| `quarto-02` | `img/quarto/02.jpg` | Estilo e composição | Cor marcante |
| `quarto-03` | `img/quarto/03.jpg` | Estilo e composição | Cor marcante, Clássico |
| `quarto-04` | `img/quarto/04.jpg` | Estilo e composição | Cor marcante, Madeira aparente |
| `quarto-05` | `img/quarto/05.jpg` | Estilo e composição | Madeira aparente, Natural e orgânico |
| `quarto-06` | `img/quarto/06.jpg` | Estilo e composição | Tons claros, Cor marcante |
| `quarto-07` | `img/quarto/07.jpg` | Estilo e composição | Cor marcante, Tons claros |
| `quarto-08` | `img/quarto/08.jpg` | Estilo e composição | Cor marcante, Madeira aparente |
| `quarto-09` | `img/quarto/09.jpg` | Estilo e composição | Tons claros, Minimalista |
| `quarto-10` | `img/quarto/10.jpg` | Estilo e composição | Tons escuros, Minimalista |
| `quarto-11` | `img/quarto/11.jpg` | Estilo e composição | Madeira aparente, Cor marcante |
| `quarto-12` | `img/quarto/12.jpg` | Estilo e composição | Minimalista, Cor marcante |

### Página 1: Rotina no quarto (`perfil`)
_Descanso, estudo e o que precisa ser guardado._

1. **Sobre o morador** `perfil` · campos nomeados · ícone `user` **[DESLIGADA]**
   - Campos: Nome, Idade (número), Profissão / ocupação, Hobbies
2. **Tamanho da cama** `cama` · uma opção · ícone `bed`
   - Opções:
     - Solteiro (88 × 188 cm; desenho `cama-solteiro`) · valor `solteiro`
     - Solteirão (96 × 203 cm; desenho `cama-solteirao`) · valor `solteirao`
     - Casal (138 × 188 cm; desenho `cama-casal`) · valor `casal`
     - Queen (158 × 198 cm; desenho `cama-queen`) · valor `queen`
     - King (193 × 203 cm; desenho `cama-king`) · valor `king`
3. **Para dormir, preferem:** `cortina` · uma opção · ícone `moon` **[DESLIGADA]**
   - Opções:
     - Escuro total (blackout; ícone `moon`) · valor `escuro-total`
     - Luz suave (cortina leve; ícone `sun`) · valor `luz-suave`
     - Os dois (blackout + voil; ícone `layers`) · valor `os-dois`
4. **Luz de leitura na cabeceira?** `leitura` · uma opção · ícone `lamp`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
5. **Recebe amigos para dormir?** `amigos` · uma opção · ícone `users`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
6. **Estuda ou trabalha no quarto?** `estudar` · uma opção · ícone `laptop`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
7. **Tem muitos livros?** `livros` · uma opção · ícone `book`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
8. **Guarda brinquedos, coleções ou objetos?** `colecoes` · uma opção · ícone `puzzle`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
9. **Roupas mais em cabides ou em gavetas?** `roupas` · uma opção · ícone `shirt`
   - Opções:
     - Mais cabides (ícone `shirt`) · valor `mais-cabides`
     - Mais gavetas (ícone `archive`) · valor `mais-gavetas`
     - Meio a meio (ícone `columns`) · valor `meio-a-meio`
10. **Tem vestidos ou casacos longos?** `pecas-longas` · uma opção · ícone `shirt` **[DESLIGADA]**
   - Dica: Pedem um cabideiro mais alto.
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
11. **Que calçados predominam?** `calcados` · várias opções · ícone `footprints` **[DESLIGADA]**
   - Opções:
     - Tênis · valor `tenis`
     - Saltos · valor `saltos`
     - Rasteiras · valor `rasteiras`
     - Botas · valor `botas`
     - Chinelos · valor `chinelos`
12. **Algum móvel ou detalhe que precisa entrar?** `movel` · texto livre · ícone `armchair`

### Página 2: Mobiliário e equipamentos (`equip`)
_Marque o que deve ser previsto no quarto._

1. **O que vai ter no quarto?** `equip` · lista de itens (tem / não tem + detalhe) · ícone `plug`
   - Itens:
     - TV (detalhe: Tamanho / modelo) · id `tv`
     - Bancada de estudo (detalhe: Quantas pessoas usam?) · id `bancada-de-estudo`
     - Computador (detalhe: Desktop, notebook, monitores) · id `computador`
     - Videogame (detalhe: Console / acessórios) · id `videogame`
     - Estante (detalhe: Livros, objetos, coleções) · id `estante`
     - Poltrona (detalhe: Uso / preferência) · id `poltrona`
     - Penteadeira (detalhe: Dimensões / iluminação) · id `penteadeira`
     - Closet (detalhe: Aberto, fechado ou integrado) · id `closet`
     - Itens esportivos (detalhe: Equipamentos / armazenamento) · id `itens-esportivos`
     - Instrumentos ou eletrônicos (detalhe: Quais?) · id `instrumentos-ou-eletronicos`
     - Ar-condicionado (detalhe: Modelo, se já tiver) · id `ar-condicionado`
2. **Que tipo de ar-condicionado preferem?** `ar-tipo` · uma opção · ícone `air-vent`
   - Só aparece se `equip` = `ar-condicionado`
   - Opções:
     - Split (aparelho na parede; desenho `ar-split`) · valor `split`
     - Cassete (embutido no teto; desenho `ar-cassete`) · valor `cassete`
     - Arquiteto define (o que funcionar melhor no espaço; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
3. **Adicionar observação** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Algo que queira contar sobre este ambiente, ou itens que serão mantidos."

## 13. Closet suíte (`closet_suite`)

- Chamada: Organização · Praticidade
- Introdução: Um closet mais enxuto, pensado para as suítes da casa.
- Capa: `img/capas/closet.jpg`
- Texto do baralho: Referências de closet: portas, iluminação e organização.
- Repetível no mesmo briefing: sim

### Imagens do baralho (5)

| id | arquivo | tema | estilos |
|---|---|---|---|
| `closet_suite-01` | `img/closet_suite/01.jpg` | Estilo e composição | Cor marcante, Tons claros |
| `closet_suite-02` | `img/closet_suite/02.jpg` | Estilo e composição | Tons claros |
| `closet_suite-03` | `img/closet_suite/03.jpg` | Estilo e composição | Tons claros, Minimalista |
| `closet_suite-04` | `img/closet_suite/04.jpg` | Estilo e composição | Minimalista, Tons claros |
| `closet_suite-05` | `img/closet_suite/05.jpg` | Estilo e composição | Tons claros, Minimalista |

### Página 1: Organização do closet (`organizacao`)
_O essencial para dividir bem o espaço._

1. **Como imaginam o closet?** `tipo` · várias opções · ícone `shirt`
   - Opções:
     - Aberto (tudo à vista; foto `img/opcoes/closet_aberto.jpg`) · valor `aberto`
     - Portas de vidro (protege e mostra; foto `img/opcoes/closet_vidro.jpg`) · valor `portas-de-vidro`
     - Portas fechadas (tudo guardado; foto `img/opcoes/closet_fechado.jpg`) · valor `portas-fechadas`
2. **Espelho de corpo inteiro?** `espelho` · uma opção · ícone `mirror`
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
3. **Roupas mais em cabides ou em gavetas?** `roupas` · uma opção · ícone `shirt`
   - Opções:
     - Mais cabides (ícone `shirt`) · valor `mais-cabides`
     - Mais gavetas (ícone `archive`) · valor `mais-gavetas`
     - Meio a meio (ícone `columns`) · valor `meio-a-meio`
4. **Muitas peças longas?** `pecas-longas` · uma opção · ícone `shirt`
   - Dica: Vestidos e casacos pedem cabideiro alto.
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
5. **Quantos pares de calçados, mais ou menos?** `calcados` · número · ícone `footprints`
   - Faixa: 0 a 300, passo 5
6. **Adicionar observação** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Algo que queira contar sobre este ambiente, ou itens que serão mantidos."

## 14. Suíte de hóspedes térreo (`hospedes`)

- Chamada: Hospitalidade · Conforto · Acolhimento
- Introdução: Um ambiente neutro, confortável e versátil para receber hóspedes com privacidade. Fica no térreo.
- Capa: `img/capas/hospedes.jpg`
- Texto do baralho: Quartos neutros, pensados para receber bem.
- Repetível no mesmo briefing: não

### Imagens do baralho (10)

| id | arquivo | tema | estilos |
|---|---|---|---|
| `hospedes-01` | `img/hospedes/01.jpg` | Estilo e composição | Tons claros, Madeira aparente |
| `hospedes-02` | `img/hospedes/02.jpg` | Estilo e composição | Cor marcante, Tons claros |
| `hospedes-03` | `img/hospedes/03.jpg` | Estilo e composição | Cor marcante, Natural e orgânico |
| `hospedes-04` | `img/hospedes/04.jpg` | Estilo e composição | Cor marcante, Madeira aparente |
| `hospedes-05` | `img/hospedes/05.jpg` | Estilo e composição | Natural e orgânico, Tons claros |
| `hospedes-06` | `img/hospedes/06.jpg` | Estilo e composição | Madeira aparente, Minimalista |
| `hospedes-07` | `img/hospedes/07.jpg` | Estilo e composição | Cor marcante, Natural e orgânico |
| `hospedes-08` | `img/hospedes/08.jpg` | Estilo e composição | Natural e orgânico, Tons claros |
| `hospedes-09` | `img/hospedes/09.jpg` | Estilo e composição | Cor marcante, Clássico |
| `hospedes-10` | `img/hospedes/10.jpg` | Estilo e composição | Natural e orgânico, Madeira aparente, Cor marcante |

### Página 1: Quem se hospeda e por quanto tempo (`uso`)
_Define flexibilidade, armazenamento e o nível de conforto ideal._

1. **Com que frequência recebem hóspedes?** `frequencia` · uma opção · ícone `calendar`
   - Opções:
     - Raramente · valor `raramente`
     - Todo mês · valor `todo-mes`
     - Com frequência · valor `com-frequencia`
2. **Quem costuma se hospedar?** `quem` · várias opções · ícone `users`
   - Opções:
     - Pais ou sogros (ícone `heart`) · valor `pais-ou-sogros`
     - Outros familiares (ícone `users`) · valor `outros-familiares`
     - Amigos (ícone `party`) · valor `amigos`
     - Família com criança (ícone `baby`) · valor `familia-com-crianca`
3. **Quanto tempo costumam ficar?** `duracao` · uma opção · ícone `clock`
   - Opções:
     - Uma noite ou fim de semana (ícone `moon`) · valor `uma-noite-ou-fim-de-semana`
     - Alguns dias (até uma semana; ícone `calendar`) · valor `alguns-dias`
     - Semanas ou temporadas (ícone `luggage`) · valor `semanas-ou-temporadas`
4. **Configuração de cama** `cama` · várias opções · ícone `bed`
   - Opções:
     - Casal (desenho `cama-casal`) · valor `casal`
     - Queen (desenho `cama-queen`) · valor `queen`
     - 2 de solteiro (juntam e separam; desenho `cama-2solteiro`) · valor `2-de-solteiro`
5. **Do que o hóspede precisa para guardar as coisas?** `guardar` · várias opções · ícone `archive`
   - Dica: Quem está de passagem precisa de pouco. Quem fica mais, como pais que passam o fim de semana, costuma precisar de armário.
   - Opções:
     - Só o básico (mala e um cabideiro; exclusiva; ícone `luggage`) · valor `so-o-basico`
     - Armário para roupas (ícone `archive`) · valor `armario-para-roupas`
     - Closet (ícone `shirt`) · valor `closet`
     - Armário no banheiro (ícone `bath`) · valor `armario-no-banheiro`
6. **O quarto também terá outro uso?** `outro-uso` · várias opções · ícone `house`
   - Opções:
     - Escritório (ícone `laptop`) · valor `escritorio`
     - Academia (ícone `dumbbell`) · valor `academia`
     - Brinquedoteca (ícone `puzzle`) · valor `brinquedoteca`
     - Closet extra (ícone `shirt`) · valor `closet-extra`
     - Só hóspedes (ícone `bed`) · valor `so-hospedes`
7. **Algum item de conforto que não pode faltar?** `conforto` · texto livre · ícone `heart`

### Página 2: Mobiliário e equipamentos (`equip`)
_Praticidade e conforto sem sobrecarregar o ambiente._

1. **O que vai ter na suíte?** `equip` · lista de itens (tem / não tem + detalhe) · ícone `plug`
   - Itens:
     - TV (detalhe: Tamanho / modelo) · id `tv`
     - Maleiro (detalhe: Banco, nicho ou suporte) · id `maleiro`
     - Mesas laterais (detalhe: 1 ou 2) · id `mesas-laterais`
     - Poltrona ou banco (detalhe: Uso / preferência) · id `poltrona-ou-banco`
     - Espelho de corpo inteiro (detalhe: Parede, porta ou solto) · id `espelho-de-corpo-inteiro`
     - Blackout (detalhe: Cortina ou persiana) · id `blackout`
     - Apoio para notebook (detalhe: Mesa ou bancada compacta) · id `apoio-para-notebook`
     - Tomadas e USB na cabeceira (detalhe: Quantidade / posição) · id `tomadas-e-usb-na-cabeceira`
     - Ar-condicionado (detalhe: Modelo, se já tiver) · id `ar-condicionado`
2. **Que tipo de ar-condicionado preferem?** `ar-tipo` · uma opção · ícone `air-vent`
   - Só aparece se `equip` = `ar-condicionado`
   - Opções:
     - Split (aparelho na parede; desenho `ar-split`) · valor `split`
     - Cassete (embutido no teto; desenho `ar-cassete`) · valor `cassete`
     - Arquiteto define (o que funcionar melhor no espaço; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
3. **Adicionar observação** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Algo que queira contar sobre este ambiente, ou itens que serão mantidos."

## 15. Suíte de hóspedes superior (`hospedes_superior`)

- Chamada: Hospitalidade · Conforto · Acolhimento
- Introdução: Um ambiente neutro, confortável e versátil para receber hóspedes com privacidade. Fica no pavimento superior.
- Capa: `img/capas/hospedes.jpg`
- Texto do baralho: Quartos neutros, pensados para receber bem.
- Repetível no mesmo briefing: não

### Imagens do baralho (10)

| id | arquivo | tema | estilos |
|---|---|---|---|
| `hospedes-01` | `img/hospedes/01.jpg` | Estilo e composição | Tons claros, Madeira aparente |
| `hospedes-02` | `img/hospedes/02.jpg` | Estilo e composição | Cor marcante, Tons claros |
| `hospedes-03` | `img/hospedes/03.jpg` | Estilo e composição | Cor marcante, Natural e orgânico |
| `hospedes-04` | `img/hospedes/04.jpg` | Estilo e composição | Cor marcante, Madeira aparente |
| `hospedes-05` | `img/hospedes/05.jpg` | Estilo e composição | Natural e orgânico, Tons claros |
| `hospedes-06` | `img/hospedes/06.jpg` | Estilo e composição | Madeira aparente, Minimalista |
| `hospedes-07` | `img/hospedes/07.jpg` | Estilo e composição | Cor marcante, Natural e orgânico |
| `hospedes-08` | `img/hospedes/08.jpg` | Estilo e composição | Natural e orgânico, Tons claros |
| `hospedes-09` | `img/hospedes/09.jpg` | Estilo e composição | Cor marcante, Clássico |
| `hospedes-10` | `img/hospedes/10.jpg` | Estilo e composição | Natural e orgânico, Madeira aparente, Cor marcante |

### Página 1: Quem se hospeda e por quanto tempo (`uso`)
_Define flexibilidade, armazenamento e o nível de conforto ideal._

1. **Com que frequência recebem hóspedes?** `frequencia` · uma opção · ícone `calendar`
   - Opções:
     - Raramente · valor `raramente`
     - Todo mês · valor `todo-mes`
     - Com frequência · valor `com-frequencia`
2. **Quem costuma se hospedar?** `quem` · várias opções · ícone `users`
   - Opções:
     - Pais ou sogros (ícone `heart`) · valor `pais-ou-sogros`
     - Outros familiares (ícone `users`) · valor `outros-familiares`
     - Amigos (ícone `party`) · valor `amigos`
     - Família com criança (ícone `baby`) · valor `familia-com-crianca`
3. **Quanto tempo costumam ficar?** `duracao` · uma opção · ícone `clock`
   - Opções:
     - Uma noite ou fim de semana (ícone `moon`) · valor `uma-noite-ou-fim-de-semana`
     - Alguns dias (até uma semana; ícone `calendar`) · valor `alguns-dias`
     - Semanas ou temporadas (ícone `luggage`) · valor `semanas-ou-temporadas`
4. **Configuração de cama** `cama` · várias opções · ícone `bed`
   - Opções:
     - Casal (desenho `cama-casal`) · valor `casal`
     - Queen (desenho `cama-queen`) · valor `queen`
     - 2 de solteiro (juntam e separam; desenho `cama-2solteiro`) · valor `2-de-solteiro`
5. **Do que o hóspede precisa para guardar as coisas?** `guardar` · várias opções · ícone `archive`
   - Dica: Quem está de passagem precisa de pouco. Quem fica mais, como pais que passam o fim de semana, costuma precisar de armário.
   - Opções:
     - Só o básico (mala e um cabideiro; exclusiva; ícone `luggage`) · valor `so-o-basico`
     - Armário para roupas (ícone `archive`) · valor `armario-para-roupas`
     - Closet (ícone `shirt`) · valor `closet`
     - Armário no banheiro (ícone `bath`) · valor `armario-no-banheiro`
6. **O quarto também terá outro uso?** `outro-uso` · várias opções · ícone `house`
   - Opções:
     - Escritório (ícone `laptop`) · valor `escritorio`
     - Academia (ícone `dumbbell`) · valor `academia`
     - Brinquedoteca (ícone `puzzle`) · valor `brinquedoteca`
     - Closet extra (ícone `shirt`) · valor `closet-extra`
     - Só hóspedes (ícone `bed`) · valor `so-hospedes`
7. **Algum item de conforto que não pode faltar?** `conforto` · texto livre · ícone `heart`

### Página 2: Mobiliário e equipamentos (`equip`)
_Praticidade e conforto sem sobrecarregar o ambiente._

1. **O que vai ter na suíte?** `equip` · lista de itens (tem / não tem + detalhe) · ícone `plug`
   - Itens:
     - TV (detalhe: Tamanho / modelo) · id `tv`
     - Maleiro (detalhe: Banco, nicho ou suporte) · id `maleiro`
     - Mesas laterais (detalhe: 1 ou 2) · id `mesas-laterais`
     - Poltrona ou banco (detalhe: Uso / preferência) · id `poltrona-ou-banco`
     - Espelho de corpo inteiro (detalhe: Parede, porta ou solto) · id `espelho-de-corpo-inteiro`
     - Blackout (detalhe: Cortina ou persiana) · id `blackout`
     - Apoio para notebook (detalhe: Mesa ou bancada compacta) · id `apoio-para-notebook`
     - Tomadas e USB na cabeceira (detalhe: Quantidade / posição) · id `tomadas-e-usb-na-cabeceira`
     - Ar-condicionado (detalhe: Modelo, se já tiver) · id `ar-condicionado`
2. **Que tipo de ar-condicionado preferem?** `ar-tipo` · uma opção · ícone `air-vent`
   - Só aparece se `equip` = `ar-condicionado`
   - Opções:
     - Split (aparelho na parede; desenho `ar-split`) · valor `split`
     - Cassete (embutido no teto; desenho `ar-cassete`) · valor `cassete`
     - Arquiteto define (o que funcionar melhor no espaço; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
3. **Adicionar observação** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Algo que queira contar sobre este ambiente, ou itens que serão mantidos."

## 16. Banheiros da casa (`banheiro`)

- Chamada: Cuidado · Rotina · Praticidade
- Introdução: Vale para os banheiros das suítes e de uso comum. O banheiro da suíte master e os lavabos têm perguntas próprias.
- Capa: `img/capas/banheiro.jpg`
- Texto do baralho: Referências de banheiro: revestimentos, bancadas e metais.
- Repetível no mesmo briefing: não

### Imagens do baralho (11)

| id | arquivo | tema | estilos |
|---|---|---|---|
| `banheiro-01` | `img/banheiro/01.jpg` | Estilo e composição | Minimalista, Cor marcante |
| `banheiro-02` | `img/banheiro/02.jpg` | Estilo e composição | Madeira aparente, Tons claros |
| `banheiro-03` | `img/banheiro/03.jpg` | Estilo e composição | Cor marcante |
| `banheiro-04` | `img/banheiro/04.jpg` | Estilo e composição | Cor marcante, Tons claros, Madeira aparente |
| `banheiro-05` | `img/banheiro/05.jpg` | Estilo e composição | Tons claros, Natural e orgânico |
| `banheiro-06` | `img/banheiro/06.jpg` | Estilo e composição | Cor marcante, Natural e orgânico |
| `banheiro-07` | `img/banheiro/07.jpg` | Estilo e composição | Madeira aparente, Tons claros |
| `banheiro-08` | `img/banheiro/08.jpg` | Estilo e composição | Madeira aparente, Tons claros |
| `banheiro-09` | `img/banheiro/09.jpg` | Estilo e composição | Minimalista, Tons claros, Dourado e luxo |
| `banheiro-10` | `img/banheiro/10.jpg` | Estilo e composição | Madeira aparente, Minimalista |
| `banheiro-11` | `img/banheiro/11.jpg` | Estilo e composição | Tons claros, Natural e orgânico |

### Página 1: Louças, metais e revestimentos (`loucas`)
_Vale para todos os banheiros da casa. A especificação final a gente compatibiliza no projeto._

1. **Cuba** `cuba` · várias opções · ícone `droplets`
   - Opções:
     - Apoio (sobre a bancada; desenho `lav-apoio`) · valor `apoio`
     - Semiencaixe (metade para fora; desenho `lav-semiencaixe`) · valor `semiencaixe`
     - Embutir (abaixo da pedra; desenho `lav-embutir`) · valor `embutir`
     - Esculpida (na própria pedra; desenho `lav-esculpida`) · valor `esculpida`
     - Arquiteto define (o que funcionar melhor; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
2. **Torneira** `torneira` · várias opções · ícone `droplets`
   - Opções:
     - De mesa (foto `img/opcoes/torneira_mesa.jpg`) · valor `de-mesa`
     - De parede (foto `img/opcoes/torneira_parede.jpg`) · valor `de-parede`
3. **Acima da bancada** `armario` · uma opção · ícone `archive`
   - Opções:
     - Armário com espelho (espelho na frente das portas; desenho `armario-espelho`) · valor `armario-com-espelho`
     - Só espelho (sem armário em cima; desenho `espelho`) · valor `so-espelho`
4. **Chuveiro** `chuveiro` · várias opções · ícone `shower`
   - Opções:
     - De parede (foto `img/opcoes/chuveiro_parede.jpg`) · valor `de-parede`
     - De teto (foto `img/opcoes/chuveiro_teto.jpg`) · valor `de-teto`
5. **Box do chuveiro** `box` · uma opção · ícone `shower`
   - Opções:
     - Até o teto (vidro do piso ao teto; desenho `box-teto`) · valor `ate-o-teto`
     - Padrão (altura comum, aberto em cima; desenho `box-padrao`) · valor `padrao`
     - Arquiteto define (conforme o uso do banheiro; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
6. **Como preferem os revestimentos?** `revestimento` · uma opção · ícone `layers`
   - Opções:
     - Uniformes (o mesmo material em todas as paredes; foto `img/opcoes/revest_uniforme.jpg`) · valor `uniformes`
     - Uma parede de destaque (cor ou textura diferente em uma parede; foto `img/opcoes/revest_destaque.jpg`) · valor `uma-parede-de-destaque`
     - Arquiteto define (o que valorizar mais o espaço; exclusiva; desenho `arquiteto`) · valor `arquiteto-define`
7. **Onde seria o destaque?** `revestimento-onde` · uma opção · ícone `layers`
   - Só aparece se `revestimento` = `uma-parede-de-destaque`
   - Opções:
     - Parede do box (ícone `shower`) · valor `parede-do-box`
     - Parede da bancada (ícone `droplets`) · valor `parede-da-bancada`
     - Arquiteto define (exclusiva; ícone `architect`) · valor `arquiteto-define`
8. **Nicho no box para shampoo e produtos de higiene?** `nicho` · uma opção · ícone `layers` **[DESLIGADA]**
   - Opções:
     - Sim · valor `sim`
     - Não · valor `nao`
9. **Cesto de roupa** `cesto` · uma opção · ícone `shirt` **[DESLIGADA]**
   - Opções:
     - Embutido no móvel (ícone `archive`) · valor `embutido-no-movel`
     - Solto (ícone `package`) · valor `solto`
10. **Adicionar observação** `obs` · texto livre (campo recolhido)
   - Texto de exemplo no campo: "Algo que queira contar sobre este ambiente, ou itens que serão mantidos."

