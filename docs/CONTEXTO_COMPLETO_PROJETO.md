# CONTEXTO COMPLETO DO PROJETO: Briefing Trioma (estilo Tinder)

Exportação feita em 20/10/2026 a partir do projeto do Claude chamado **"TINDER BRIEFING"** (conta de Lucas, lucas.paula.damasceno@gmail.com), para continuar o trabalho em outra conta sem recomeçar.

Este arquivo é a documentação principal. Os demais arquivos do pacote estão listados em `MANIFESTO.md`. O conteúdo completo de cada ambiente (imagens, páginas, perguntas, opções, perguntas desligadas) está em `CATALOGO_AMBIENTES_E_PERGUNTAS.md`.

---

## 0. Fontes usadas, limites e legenda

### 0.1 O que foi analisado

| Fonte | O que contém | Situação |
|---|---|---|
| Documento do projeto `claude/briefing-trioma.md` (atualizado em 14/10/2026) | Estado do projeto, decisões, fluxo, ajustes por ambiente, pendências | Lido na íntegra. Cópia literal em `referencias/doc_do_projeto_briefing-trioma.md` e no Apêndice A |
| Memória do projeto (2 notas) | Contexto da Trioma e preferência de organização de arquivos | Lidas. Cópia literal no Apêndice B |
| Artifact "Briefing Trioma Visual" (versão 32, publicada em 14/10/2026 às 20:58) | Versão final da interface (cliente + painel do escritório), 192 imagens | Baixado na íntegra, byte a byte |
| Artifact "Trioma no iPhone" (versão 17, 14/10/2026 às 20:58) | Simulação do briefing num iPhone 16 Pro com Safari | Baixado na íntegra |
| Artifact "Briefing Trioma" (versão 1, 14/10/2026 às 10:27) | Primeira versão, com perguntas em texto | Baixado na íntegra, 116 imagens |
| Computador do Lucas: `Downloads\Trioma Briefing` | `Imagens\<ambiente>` (fotos finais organizadas) e `Site de teste\trioma-briefing-teste.zip` | Listado. O zip foi aberto e conferido (é uma build, sem código-fonte) |

### 0.2 O que NÃO estava acessível (informado explicitamente)

1. **O histórico das conversas anteriores.** Esta exportação foi pedida numa conversa nova, sem mensagens anteriores. As conversas em que o projeto foi construído não podem ser lidas daqui. Tudo o que está neste documento vem das fontes da tabela acima: o documento do projeto (que já era o registro de decisões mantido durante o trabalho), a memória do projeto e o próprio código das versões publicadas.
2. **O código-fonte original em TypeScript/React e o backend em Python (FastAPI + SQLAlchemy).** Ele foi escrito no espaço de trabalho temporário das sessões anteriores, que é apagado quando a sessão termina. Nenhuma cópia dos arquivos-fonte (`src/...`, `app/...`) foi encontrada nos Artifacts, no projeto ou na pasta do computador. O que sobreviveu, e está preservado integralmente neste pacote, são as **builds compiladas** (HTML de arquivo único com todo o JavaScript e CSS dentro). Elas funcionam por completo e contêm toda a lógica e todos os textos, mas em forma compilada. Para facilitar a leitura, o pacote traz também o script e o CSS reformatados (`codigo_legivel/`) e o catálogo de ambientes extraído em JSON (`dados/`).
3. **As versões intermediárias dos Artifacts** (versões 2 a 31 da versão visual e 1 a 16 da simulação no iPhone). Só a versão atual de cada Artifact pode ser baixada.
4. **Outros Artifacts da conta** que não pertencem a este projeto (Tours 360, Por Pontos, Larevo, Design Systems, Story, etc.) foram vistos na listagem e deixados de fora de propósito.

### 0.3 Legenda de confiabilidade

- **[CONFIRMADO]**: está escrito no documento do projeto, na memória ou aparece no código publicado.
- **[OBSERVADO NO CÓDIGO]**: encontrado na build final ao analisar o código, mas não descrito no documento do projeto.
- **[INFERIDO]**: conclusão minha a partir das fontes, não declarada por Lucas.
- **[SUGESTÃO]**: proposta para os próximos passos, ainda não aprovada.

Sem marcação, vale [CONFIRMADO].

---

## 1. Visão geral

### 1.1 Nome, objetivo e finalidade

- **Nome de trabalho:** Briefing Trioma (estilo Tinder). O projeto do Claude se chama "TINDER BRIEFING". Na interface aparece como "Briefing de interiores" e, no painel, "Briefings".
- **Empresa:** Trioma Arquitetura e Interiores, escritório de arquitetura e ambientação/interiores do Lucas, tocado em sociedade com um sócio. A Trioma já tem um site próprio feito com TypeScript, Vite e Python.
- **Objetivo:** substituir o briefing em PDF de cerca de 40 a 60 páginas (a memória cita "60+ páginas") por uma página interativa no site da Trioma, hospedada na área do cliente.
- **Como funciona:** o escritório monta o briefing de cada cliente só com os ambientes do projeto fechado, escolhendo as imagens e as perguntas de cada ambiente, e envia um link. O cliente arrasta as imagens (direita = Gosto, esquerda = Não gosto, para cima = Neutro) e responde perguntas rápidas. O foco é celular e iPad, mas também funciona no computador. O escritório vê um relatório com perfil de estilo e exporta um PDF para a equipe.

### 1.2 Problema que resolve

- O PDF longo cansa o cliente, é difícil de preencher no celular e gera respostas incompletas.
- Grande parte do PDF não se aplica a cada cliente (ambientes que não fazem parte do projeto contratado).
- Como o trabalho é de **interiores**, a planta já vem pronta: perguntas de arquitetura não fazem sentido.
- O escritório precisa transformar gosto visual em informação objetiva (perfil de estilo, referências marcadas, comentários) e ter tudo organizado para a equipe.

### 1.3 Escopo e funcionalidades

**Lado do cliente (link recebido):**
- Tela inicial que é o menu de ambientes, com nome do cliente, roteiro numerado e progresso de cada ambiente em anel.
- Tela "Como responder" com animação do gesto.
- Para cada ambiente: capa com foto, baralho de imagens para arrastar (quando o ambiente tem baralho), página "O que mais chamou sua atenção nessas referências?" com comentário opcional, páginas de perguntas visuais.
- Menu acessível a qualquer momento (botão de grade no topo), "Continuar de onde parei", revisão final e envio.
- Tela final de agradecimento com "Avisar no WhatsApp" e "Copiar mensagem".
- Progresso salvo a cada toque.

**Lado do escritório (painel):**
- Lista de briefings com status, progresso e ações.
- Editor de briefing: dados do cliente, ambientes (com ordem fixa para os principais), Personalizar por ambiente (imagens e perguntas ligadas ou desligadas), salvar e gerar link com mensagem pronta para WhatsApp.
- Biblioteca de ambientes: adicionar, retirar e restaurar fotos, ajustar estilos de cada foto, criar e apagar perguntas próprias.
- Relatório (Respostas): perfil de estilo, referências por ambiente, comentários, respostas; "Copiar resumo" e "Exportar PDF".
- Aviso por e-mail quando o cliente conclui (no backend).

### 1.4 Tecnologias, ferramentas e integrações

| Item | Detalhe | Status |
|---|---|---|
| Front-end | React + TypeScript + Vite | [CONFIRMADO] no doc. A build usa React 18.3.1 e ícones lucide-react 0.460.0 [OBSERVADO NO CÓDIGO] |
| Backend | FastAPI + SQLAlchemy (Python), com rotas para a Biblioteca | [CONFIRMADO] no doc. Código não acessível |
| PDF | jsPDF no navegador (`src/admin/pdf.ts`), com tabelas (jspdf-autotable) | [CONFIRMADO]; autotable [OBSERVADO NO CÓDIGO] |
| E-mail de conclusão | `app/notify.py`, variáveis `NOTIFY_EMAIL` (provisório `briefings@trioma.example`), `SMTP_HOST`, `SMTP_USER`, `SMTP_PASSWORD`; sem SMTP só registra no log | [CONFIRMADO]; código não acessível |
| WhatsApp | Link `https://wa.me/<numero>?text=<mensagem>`; número fixo opcional `OFFICE_WHATSAPP` em `src/config.ts` (vazio na build) | [CONFIRMADO] |
| Fonte | Hanken Grotesk (Google Fonts), pesos 300 a 700 | [OBSERVADO NO CÓDIGO] |
| Build de teste | `vite build --mode single` gera um arquivo só; no site, o PDF fica num pedaço separado que só o painel carrega | [CONFIRMADO] |
| Hospedagem de teste | Artifacts do Claude (preferido pelo Lucas) e, só quando ele pedir, zip para Netlify Drop | [CONFIRMADO] |
| Persistência no protótipo | `localStorage`, chave `trioma-briefing:v2` | [OBSERVADO NO CÓDIGO] |
| Site da Trioma | TypeScript, Vite e Python; rota prevista `/briefing` | [CONFIRMADO] |
| Imagens | Pinterest (fotos reais de projetos, sem renders de IA) e Pexels, lado maior 1400 px | [CONFIRMADO] |

---

## 2. Histórico e decisões

### 2.1 Cronologia

As datas abaixo vêm dos carimbos das versões publicadas, dos arquivos no computador e do documento do projeto. A ordem fina das conversas anteriores não está acessível.

| Quando | O que aconteceu | Fonte |
|---|---|---|
| Antes de 14/10/2026 | Concepção: briefing estilo Tinder para substituir o PDF; definição do fluxo (escritório monta, cliente arrasta e responde) e da stack | Memória e doc |
| 14/10/2026, 10:27 | Publicada a **versão 1** ("Briefing Trioma"): 12 ambientes, perguntas em texto, imagens leves | Artifact v1 |
| 14/10/2026 (ao longo do dia) | Criação da **versão visual** ("Briefing Trioma Visual"), que chegou à versão 32 no mesmo dia: perguntas com ícones, desenhos e fotos; novos ambientes; menu com progresso; relatório; PDF; Biblioteca | Artifact visual e doc |
| 14/10/2026 | Criação da simulação **"Trioma no iPhone"** (iPhone 16 Pro com Safari), que chegou à versão 17 | Artifact |
| 14/10/2026, por volta de 19:25 a 19:30 | Gerado o **site de teste** `trioma-briefing-teste.zip` (Netlify Drop) e salvo em `Downloads\Trioma Briefing\Site de teste` | Arquivo no computador |
| 14/10/2026, 19:41 a 19:58 | Imagens finais baixadas e organizadas em `Downloads\Trioma Briefing\Imagens\<ambiente>` | Arquivos no computador |
| 14/10/2026, 20:58 | Últimas publicações: **versão visual 32** e **iPhone 17** (as duas carregam o mesmo app) | Artifacts |
| 14/10/2026 | Documento do projeto atualizado com o estado acima | Doc |
| 14 e 15/10/2026 | Notas de memória do projeto atualizadas | Memória |
| 20/10/2026 | Esta exportação | |

**Comparação v1 → v32 [OBSERVADO NO CÓDIGO]:**

| Ambiente | v1 (imagens / perguntas) | v32 (imagens / perguntas) |
|---|---|---|
| Sobre a família | 0 / 19 | 0 / 28 (9 desligadas) |
| Hall de entrada | 0 / 5 | 0 / 6 |
| Sala de estar e jantar | 12 / 10 | 24 / 13 |
| Cozinha | 16 / 13 | 21 / 19 |
| Varanda gourmet | 7 / 7 | 20 / 9 |
| Lavabo interno | não existia | 0 / 5 |
| Lavabo externo | não existia | 0 / 6 |
| Suíte master | 14 / 5 | 21 / 10 |
| Closet (v1) → Closet master | 9 / 7 | 11 / 10 |
| Banheiro master | 9 / 16 | 14 / 20 |
| Área de serviço | 0 / 6 | 0 / 5 |
| Quarto | 14 / 12 | 12 / 15 |
| Closet suíte | não existia | 5 / 6 |
| Suíte de hóspedes (v1) → Suíte de hóspedes térreo | 8 / 11 | 10 / 10 |
| Suíte de hóspedes superior | não existia | 10 / 10 (espelho do térreo) |
| Banheiro (v1) → Banheiros da casa | 11 / 7 | 11 / 10 |
| **Total** | **12 ambientes, 118 perguntas** | **16 ambientes, 182 perguntas (27 desligadas), 159 cartas de baralho** |

### 2.2 Decisões tomadas (registro de decisões)

**Produto e escopo**
- Projeto de interiores: a planta já vem pronta, então **nada de perguntas de arquitetura**.
- O escritório monta o briefing **por cliente**, só com os ambientes do projeto fechado, escolhendo imagens e perguntas de cada um.
- A página vai ficar hospedada na **área do cliente no site da Trioma**.
- Stack: **React + TypeScript + Vite** no front e **FastAPI + SQLAlchemy** no backend.

**Textos e tom**
- Textos **neutros e sem informalidade**: "Em ambos" ou "Ambos" no lugar de "Nos dois" ou "Os dois"; "Pretendem automatizar algo na casa?".
- Opção **"Arquiteto define"** (ícone de lápis e régua) no lugar de "Ainda não sei" quando a decisão é técnica.
- Para deixar uma decisão em aberto: **"Definir com o arquiteto"**.
- Pedidos de fotos e modelos vão para **"o nosso grupo do WhatsApp"**, com um lembrete na própria pergunta em vez de campo para digitar.

**Estrutura do percurso**
- **Ordem fixa** (os principais primeiro, porque no fim o cliente já está cansado): Sobre a família, Hall, Sala, Cozinha, Varanda gourmet, Lavabo interno, Lavabo externo, Suíte master, com Closet master e Banheiro master logo depois. Só os que estiverem no briefing. O resto segue a ordem que o escritório definir.
- **Banheiros:** um só modelo geral "Banheiros da casa" por briefing (vale para suítes e banheiros comuns). Banheiro master é opção separada e pode ser escolhida sozinha. Lavabo interno e lavabo externo são modelos próprios, uma página cada.
- **Hóspedes:** tudo sobre hóspedes fica nas suítes de hóspedes (saiu de Sobre a família). Dois modelos espelhados: térreo e superior.
- **Ambientes de apoio** (ex.: área de serviço) devem ser rápidos: sem campos de detalhe por item.
- **Closet master:** um por briefing. **Quarto** (modelo de suíte) e **Closet suíte** podem entrar mais de uma vez.

**Perguntas desligadas por padrão**
- Campo `off`: a pergunta entra desmarcada quando o ambiente é adicionado; o escritório liga em Personalizar.
- Quando Lucas diz **"tire essa opção"** sobre uma pergunta, a regra é **desligar por padrão** (não apagar).

**Forma de trabalhar**
- **Antes de reorganizar páginas ou juntar perguntas, propor e perguntar ao Lucas** (exceto quando ele diz "faça como achar melhor").
- **Medir a rolagem no celular, iPad e computador** antes de decidir sobre divisão de páginas.
- Lucas prefere **revisar pelas páginas do Claude** (Artifacts). Só gerar zip de site de teste (Netlify Drop) **se ele pedir**.
- Lucas se preocupa com **consumo de créditos**: preferir soluções simples.
- Ao baixar arquivos no computador dele: **tudo organizado em pastas**, sem arquivos soltos; temporários com nome **"trioma-temp"**.

### 2.3 Requisitos aprovados e descartados

| Item | Decisão | Justificativa registrada |
|---|---|---|
| Perguntas de arquitetura | Descartadas | Planta já vem pronta (projeto de interiores) |
| "Ainda não sei" em decisões técnicas | Trocado por "Arquiteto define" | Decisão técnica cabe ao escritório |
| "Não querem estofada" (altura da cama estofada, suíte master) | Trocado por "Definir com o arquiteto" | Deixar em aberto em vez de negar |
| Hóspedes em Sobre a família | Removido; foi para as suítes de hóspedes | Concentrar o assunto num lugar |
| "Iluminação mal planejada" e "barulho" em "O que incomoda" | Removidos | [INFERIDO] não se aplicam a interiores com planta pronta |
| Tela de "ambiente concluído" | Removida; segue direto para o próximo | Fluxo mais rápido |
| Campos de modelo/detalhe na área de serviço | Removidos; lembrete para mandar o modelo das máquinas no grupo do WhatsApp | Ambientes de apoio devem ser rápidos |
| Campo de texto para pedir fotos | Trocado por lembrete do grupo do WhatsApp | Mais simples para o cliente |
| Adega nos equipamentos da varanda gourmet | Removida; entrou sofá; "Projetor externo" | Ajuste pedido |
| Computador no mobiliário da suíte master | Removido | Ajuste pedido |
| Armário/roupeiro nos equipamentos das suítes de hóspedes | Removido | Já coberto pela pergunta "o que precisa para guardar" |
| Nichos e cesto nos banheiros | Desligados por padrão | Regra "tire essa opção" |
| Vários itens da Sala, Cozinha, Varanda, Hall, Família, Suíte | Desligados por padrão (lista na seção 2.5 e no catálogo) | Regra "tire essa opção" |
| "Como responder" | Mantida a imagem de exemplo antiga | Lucas preferiu |
| Zip para Netlify | Só sob pedido | Lucas revisa pelas páginas do Claude |
| Botão "Editar texto" nas perguntas prontas da Biblioteca | **Oferecido, sem resposta** | Pendente |
| Dividir páginas longas dos banheiros | **Em aberto** | Pendente |
| Cozinha: juntar Organização com Equipamentos | **Em aberto** | Pendente |
| Suíte master: desligar "Para dormir, preferem" | **Em aberto** | Pendente |

### 2.4 Preferências de design, funcionamento e experiência

- **Foco no celular e no iPad**, funcionando também no computador.
- Visual sóbrio de escritório de arquitetura: fundo papel claro (`#f3f0ea`), tinta quase preta, acento bronze (`#8e7660`), telas escuras (`#141413`) nas capas e no menu, tipografia Hanken Grotesk leve nos títulos (300/400). Detalhes na seção 3.1.
- Fotos reais e grandes, em vez de desenhos, quando possível (pedras, cabeceiras, closet, revestimentos, madeira, "o que fica à mostra" na cozinha). Desenhos de lixeira e calha úmida ainda são desenhos e podem virar fotos.
- Quase tudo se responde **com toques**; texto livre só quando necessário e, muitas vezes, recolhido ("Adicionar observação").
- O cliente nunca perde o que fez: salva a cada toque, ao reabrir o link cai no menu e pode continuar exatamente de onde parou.
- Sem telas intermediárias desnecessárias.
- Aviso "Mais perguntas abaixo" enquanto houver pergunta escondida na rolagem.

### 2.5 Instruções específicas que devem continuar sendo respeitadas

1. Não criar perguntas de arquitetura.
2. Usar "Arquiteto define" (decisão técnica) e "Definir com o arquiteto" (deixar em aberto). Não usar "Ainda não sei" em decisão técnica.
3. Tom neutro: "Em ambos"/"Ambos", nunca "Nos dois"/"Os dois".
4. Pedidos de foto ou modelo: lembrete para mandar no "nosso grupo do WhatsApp", sem campo de digitação.
5. "Tire essa opção" sobre uma pergunta significa **desligar por padrão** (`off: true`), não apagar.
6. Respeitar a ordem fixa dos ambientes principais.
7. Um só "Banheiros da casa" por briefing; Banheiro master separado; lavabos com modelo próprio.
8. Hóspedes só nas suítes de hóspedes (térreo e superior espelhados: mudança num vale para o outro).
9. Ambientes de apoio rápidos, sem campos de detalhe por item.
10. Antes de reorganizar páginas ou juntar perguntas: propor e perguntar, medindo rolagem em celular, iPad e computador. Exceção: quando Lucas disser "faça como achar melhor".
11. Revisões pelas páginas do Claude (Artifacts); zip para Netlify só se ele pedir.
12. Soluções simples, por causa do consumo de créditos.
13. Arquivos no computador do Lucas sempre organizados em pastas; temporários em "trioma-temp".
14. Preferências gerais do Lucas para textos: **não usar travessões**; linguagem que soe humana, não gerada por IA; respostas diretas, sem rodeio; levantar só os pontos mais objetivos e visíveis.

**Perguntas desligadas por padrão hoje (27) [OBSERVADO NO CÓDIGO, conferido com o doc]:**
- Sobre a família (9): aumentar a família, quem cozinha, onde assistem TV, hobby, o que valorizam, prioridades para investir, materiais, plantas, quadros.
- Hall (2): tirar os sapatos, o que o hall deve transmitir.
- Sala (3): linguagem, luz, cortinas.
- Cozinha (4): embutidos na bancada, despensa, fruteira, refeições rápidas.
- Varanda gourmet (2): plantas naturais, móvel/elemento.
- Banheiro master (1): nichos.
- Quarto (4): "Sobre o morador", "Para dormir, preferem", vestidos/casacos longos, calçados.
- Banheiros da casa (2): nicho, cesto.
(Os ids exatos estão no catálogo.)

---

## 3. Interfaces e Artifacts

Há três interfaces publicadas, todas preservadas integralmente em `interfaces/`. A versão de trabalho é a **3.1 (Briefing Trioma Visual, v32)**. A 3.2 é uma moldura de apresentação que carrega exatamente o mesmo app. A 3.3 é histórica.

| # | Nome | Link original (privado, conta antiga) | Versão | Arquivos no pacote |
|---|---|---|---|---|
| 3.1 | Briefing Trioma Visual | https://claude.ai/artifact/XtyUiRtrg2Mqv1eNoz8R1H | 32 (14/10/2026 20:58), com permissão de download (para o PDF) | `interfaces/briefing_visual_v32/index.html` + `img/` (192 fotos) |
| 3.2 | Trioma no iPhone | https://claude.ai/artifact/DjesYmV5th18VbjS3Xw23T | 17 (14/10/2026 20:58) | `interfaces/briefing_visual_v32/iphone.html` (usa a mesma pasta `img/`) |
| 3.3 | Briefing Trioma (versão 1, perguntas em texto) | https://claude.ai/artifact/RpcwYBAU4VtBTzKTY7Xkzg | 1 (14/10/2026 10:27) | `interfaces/briefing_v1_perguntas_em_texto/index.html` + `img/` (116 fotos) |
| 3.4 | Site de teste (Netlify Drop) | não é Artifact | build de 14/10/2026 por volta de 19:30 | Fica no computador do Lucas: `Downloads\Trioma Briefing\Site de teste\trioma-briefing-teste.zip` (não copiado: é uma build anterior à v32) |

Os links originais são privados da conta antiga. Na conta nova, publique de novo a partir dos arquivos (ver seção 5.3).

### 3.1 Briefing Trioma Visual (versão 32): interface principal

**Finalidade:** protótipo completo e navegável do produto: o percurso do cliente e o painel do escritório na mesma página. Os dados ficam no navegador (localStorage), o que o painel avisa com o selo "PROTÓTIPO" ("Os dados ficam salvos só neste navegador").

**Como abrir:**
- `index.html` sem nada no endereço abre o **painel do escritório**.
- `index.html#b-<token>` abre o **briefing do cliente**. Tokens de exemplo: `teste-perguntas-p8w2k` (Teste das perguntas), `brendo-x4m9` (Brendo, já respondido), `aldo-e-andressa-7k2p` (Aldo e Andressa, residência completa).
- No site real, o link será `https://<site>/briefing/<token>` (a constante `Ww` está com o valor provisório `https://seusite.com.br`; a rota é `/briefing`). O app também aceita o token por `window.__BRIEFING_TOKEN`.
- Funciona aberto direto do disco (testado em `file://`), mas a fonte Hanken Grotesk vem do Google Fonts e precisa de internet.
- Na tela do cliente aparece um botão flutuante "Painel" que só existe no protótipo.

**Clientes de exemplo (recriados por "Restaurar exemplos"):**

| Cliente | Projeto | Ambientes | Uso |
|---|---|---|---|
| Teste das perguntas | "Poucas imagens, para ver as perguntas visuais" | 12 ambientes (família, sala, cozinha, lavabos, suíte master, closet master, banheiro master, hóspedes térreo e superior, banheiros da casa, closet suíte), só 3 imagens por ambiente | Testar perguntas |
| Brendo | Sala e cozinha | Sala e Cozinha, com respostas, comentários e swipes prontos; concluído | Testar relatório e PDF |
| Aldo e Andressa | Residência completa | Família, hall, sala, cozinha, varanda gourmet, suíte master, closet master, banheiro master, área de serviço, "Suíte 01" (Quarto), hóspedes térreo, banheiros da casa | Projeto completo |

Clientes salvos antes de uma mudança de perguntas desligadas não mudam sozinhos: usar "Restaurar exemplos" no painel.

#### 3.1.1 Identidade visual (tokens do CSS)

**Cores, tema claro (padrão):**

| Token | Valor | Uso |
|---|---|---|
| `--paper` | `#f3f0ea` | Fundo geral (papel) |
| `--surface` | `#fbfaf7` | Cartões, rodapés |
| `--sunk` | `#ebe6de` | Áreas rebaixadas, miniaturas |
| `--ink` | `#1d1b18` | Texto principal e botão primário |
| `--ink-2` | `#4a453f` | Texto secundário |
| `--muted` | `#776f66` | Legendas |
| `--line` | `#ddd5ca` | Bordas |
| `--accent` | `#8e7660` | Acento bronze (barras de progresso, foco) |
| `--accent-ink` | `#6c5843` | Rótulos em caixa alta, links |
| `--night` | `#141413` | Telas escuras (menu, capas, topo do painel) |
| `--night-2` | `#1f1e1b` | Variação escura |
| `--night-ink` | `#ede8e0` | Texto nas telas escuras |
| `--night-muted` | `#a39c92` | Texto secundário nas telas escuras |
| `--night-accent` | `#bfa88f` | Acento nas telas escuras (anéis de progresso) |
| `--like` | `#00826b` | Gosto (verde) |
| `--nope` | `#c4501f` | Não gosto (laranja queimado) |
| `--neutral` | `#8a847a` | Neutro (cinza quente) |
| `--shadow` | `0 1px 2px rgb(29 27 24 / 6%), 0 8px 24px rgb(29 27 24 / 8%)` | Sombra padrão |

**Tema escuro** (automático por `prefers-color-scheme`, ou forçado com `data-theme="dark"`): paper `#121211`, surface `#1c1b19`, sunk `#262421`, ink `#ede8e0`, ink-2 `#cfc8bd`, muted `#a39c92`, line `#34312c`, accent `#b9a28a`, accent-ink `#c9b49c`, like `#24a08a`, nope `#da6a30`, neutral `#8f897f`.

**Tipografia:** Hanken Grotesk (300, 400, 500, 600, 700), com Helvetica Neue, Helvetica e Arial de reserva. Corpo 16px, altura de linha 1.5.
- Rótulo de seção (`.eyebrow`): 12px, peso 600, espaçamento 0.14em, caixa alta, cor `--accent-ink`.
- Nome do cliente no menu (`.welcome__name`): `clamp(44px, 11vw, 92px)`, peso 300.
- Título da capa do ambiente (`.intro__title`): `clamp(38px, 9vw, 72px)`, peso 300.
- Título de página (`.h1`): `clamp(26px, 5.2vw, 36px)`, peso 400.
- Título do painel (`.admin-title`): `clamp(28px, 4vw, 40px)`, peso 300.
- Texto de apoio (`.lead`): 17px.
- Marca no topo do painel: "TRIOMA" com espaçamento 0.3em e, embaixo, "ARQUITETURA E INTERIORES" em 8.5px com 0.22em.

**Espaçamentos e formas:**
- Margem lateral: `max(16px, área segura do aparelho)`.
- Larguras máximas: páginas de perguntas 640px (larga 980px); menu e capas 820px; painel 1180px.
- Botões em pílula (raio 999px), altura mínima 46px (grande 54px, pequeno 36px).
- Opções de resposta em pílula com altura mínima 44px (alvo de toque confortável).
- Cartões de pergunta: raio 14px, padding 18px. Cartas do baralho: raio 18px. Campos: raio 10px.
- Botões do baralho: discos de 66px (Gosto, Não gosto) e 52px (Neutro); 56px e 46px em telas baixas (altura até 640px).

**Responsividade (pontos de quebra):** 420px (esconde o status do rodapé), 520px, 560px, 600px, 640px (formulários em 1 coluna), 760px (perguntas em 2 colunas a partir daqui), 860px (navegação da Biblioteca vira faixa horizontal), 980px (editor em 1 coluna). Altura até 640px reduz os controles do baralho. Respeita "reduzir movimento" do sistema.

#### 3.1.2 Percurso do cliente (tela a tela)

Capturas em `capturas_de_tela/01` a `13` (celular 393 × 716 e iPad 820 × 1180).

1. **Menu inicial (tela escura)** `01_celular_menu_inicial.png`
   - "BRIEFING DE INTERIORES", nome do cliente em letras grandes, texto de abertura (padrão: "Um roteiro visual para transformar rotina, preferências e prioridades em decisões de projeto."; o escritório pode trocar em "Mensagem de abertura").
   - Lista numerada dos ambientes do briefing. Cada número tem um **anel que enche** conforme o cliente responde, com o **percentual ao lado** (referências avaliadas + perguntas respondidas). Com 100% o número vira um visto. Tocar num ambiente leva direto a ele.
   - O campo opcional "Adicionar observação" só conta no percentual se for preenchido.
   - Botão fixo no rodapé: **"Começar"** antes de começar; depois **"Continuar de onde parei"**; com tudo concluído, **"Revisar e enviar"**. Ao voltar, o texto vira "Que bom ter vocês de volta. X% do briefing já está respondido. Toquem em um ambiente para ir direto a ele ou continuem de onde pararam."
   - Tempo estimado calculado como `máx(5, (imagens × 4 s + perguntas × 18 s) / 60)` minutos [OBSERVADO NO CÓDIGO].
2. **Como responder** `02_celular_como_responder.png`
   - Título "Arraste cada imagem para dizer o que achou" e "Não existem respostas certas. Vá pela primeira impressão: ela costuma ser a mais fiel ao seu gosto."
   - Carta de exemplo animada (direita com selo GOSTO, esquerda NÃO GOSTO, para cima NEUTRO) e três blocos: Esquerda / Não gosto, Cima / Neutro, Direita / Gosto. Usa a imagem de exemplo antiga (`img/opcoes/como_responder.jpg`), que o Lucas preferiu.
   - Botões "Voltar" e "Entendi, vamos lá". Quem entra direto num ambiente com imagens vê esta tela antes do primeiro baralho.
3. **Capa do ambiente (tela escura com foto)** `03_celular_capa_do_ambiente.png`
   - Topo: voltar, "Ambiente N de M", botão de grade (abre o menu). Foto de capa com zoom lento, chamada em caixa alta (ex.: "PESSOAS · ROTINA · CONVIVÊNCIA"), nome do ambiente, introdução, contagem ("19 perguntas" ou "3 referências · 7 perguntas") e botão "Responder" ou "Ver referências".
   - Ao abrir um ambiente pelo menu, o Voltar da capa leva de volta ao menu.
4. **Baralho de imagens** `07_celular_baralho_sala.png`
   - Carta grande com a foto inteira (`object-fit: contain` sobre fundo desfocado da própria foto), número e tema no rodapé da carta (ex.: "01 ESTILO E COMPOSIÇÃO"), botão de ampliar (abre a foto em tela cheia).
   - Gestos: arrastar para a direita = Gosto, esquerda = Não gosto, para cima = Neutro. A carta gira levemente e mostra o selo correspondente enquanto é arrastada.
   - Regra do gesto [OBSERVADO NO CÓDIGO]: Gosto se o arraste passar de 28% da largura (ou for rápido, acima de 0,55 px/ms e 40px); Não gosto no sentido oposto; Neutro se subir mais de 20% da altura (ou rápido para cima, acima de 50px) com movimento mais vertical que horizontal.
   - Botões embaixo: Voltar (desfaz), Não gosto (X), Neutro (traço), Gosto (coração) e contador "1 de 3".
   - **Rever as referências:** volta ao baralho com a escolha atual marcada (o botão da escolha fica preenchido e aparece uma etiqueta na carta); dá para mudar, ir para a anterior ou para a próxima sem alterar.
5. **Depois do baralho** `08_celular_depois_do_baralho_comentario.png`
   - "O que mais chamou sua atenção nessas referências?", com as miniaturas marcadas como Gosto e o campo "Comentário (opcional)" e o link "Rever as referências".
6. **Páginas de perguntas** `04`, `05`, `06`, `09` a `12`
   - Topo: voltar, nome do ambiente com o título da página embaixo, grade (menu), barra fina de progresso.
   - Rótulo do ambiente em caixa alta, título da página, subtítulo explicativo.
   - Cada pergunta num cartão com ícone, texto e, quando houver, dica. Tipos de resposta:
     - **Sim/Não** em dois botões grandes com visto e X.
     - **Uma opção / várias opções** em pílulas, ou em blocos com ícone, desenho (`art`), amostra de cor (`swatch`) ou foto (`image`). Opções marcadas como exclusivas (ex.: "Arquiteto define") desmarcam as outras.
     - **Contagem por categoria** (ex.: moradores: Bebê, Criança, Adolescente, Adulto, 60+, com + e -; pets com "Não temos" e "Outro").
     - **Número** com - e +.
     - **Lista de itens** (o que deve ser previsto): grade de itens com ícone; ao marcar, pode abrir um detalhe (ex.: TV abre os tamanhos 42", 50", 60", 65", 70", 75", 85").
     - **Escala** entre dois polos (ex.: Atual ↔ Atemporal).
     - **Campos nomeados** (ex.: calçados por pessoa, com nome e quantidade).
     - **Texto livre**, às vezes recolhido como "Adicionar observação".
   - Perguntas condicionais (`showIf`): só aparecem conforme outra resposta (ex.: quantas pessoas receber só se "Gostam de receber" = Sim).
   - Aviso flutuante **"Mais perguntas abaixo"** enquanto houver pergunta escondida; tocar rola a página.
   - Rodapé fixo: "Voltar" e "Continuar".
   - **Salva a cada toque.** Sem tela de "ambiente concluído": ao terminar um ambiente segue direto para o próximo.
7. **Revisão e envio:** lista dos ambientes com contagem de Gosto, Neutro e Não gosto; botão **"Enviar briefing"** (marca a conclusão).
8. **Tela final (escura):** visto, "Obrigado, <nome>." e "Recebemos suas escolhas. A equipe Trioma vai usar cada referência e resposta como ponto de partida do projeto." Bloco **"Avisar no WhatsApp"**, que abre o WhatsApp com a mensagem pronta "Olá, equipe Trioma! Aqui é <nome>. Acabei de concluir o briefing de interiores (<projeto>). Fico no aguardo dos próximos passos." O cliente escolhe o grupo e envia. Também **"Copiar mensagem"**. Se o escritório definir um número fixo, a mensagem vai direto para ele.
9. **Menu a qualquer momento:** botão de grade no alto à direita. "Continuar de onde parei" volta exatamente para a tela em que o cliente estava. Ao reabrir o link, o cliente cai no menu. Se o briefing já foi enviado, o link abre direto a tela final de agradecimento [OBSERVADO NO CÓDIGO, testado com o cliente Brendo].

#### 3.1.3 Painel do escritório (tela a tela)

Capturas em `capturas_de_tela/20` a `24` (computador 1280 × 860).

1. **Barra superior escura:** marca TRIOMA, abas "Briefings" e "Biblioteca", selo "PROTÓTIPO" e botão "Restaurar exemplos".
2. **Briefings (lista)** `20_painel_lista_de_briefings.png`: título "Briefings", "Monte o briefing de cada cliente só com os ambientes do projeto fechado." e botão "+ Novo briefing". Cada linha: nome (com etiqueta "Exemplo" quando for exemplo), ambientes, status (Rascunho, Enviado, Em andamento, Concluído) com data, barra de progresso com percentual e ações ("Respostas" quando já começou, "Editar", "Ver como cliente").
3. **Editor do briefing** `22_painel_editor_do_briefing.png` e `23_painel_editor_personalizar.png`:
   - Cabeçalho com nome, total de ambientes, referências e perguntas (ex.: "12 ambientes · 144 referências · 124 perguntas").
   - Bloco "Cliente": "Nome que aparece no briefing *", "Projeto (uso interno)", "Mensagem de abertura (opcional)".
   - "Ambientes deste briefing": explica a ordem fixa dos principais; cada item tem número, miniatura, nome, contagem, etiqueta "Ordem fixa" (ou setas para reordenar os demais), "Personalizar" e lixeira.
   - "Biblioteca de ambientes" ao lado: tocar no + ou **arrastar** para a lista. Quartos e closets de suíte podem entrar mais de uma vez.
   - **Personalizar:** abas Imagens e Perguntas. Nas imagens, grade para tirar e pôr fotos daquele cliente. Nas perguntas, chaves liga/desliga por pergunta (as desligadas por padrão já vêm desligadas).
   - Barra de salvar fixa embaixo: "Tudo salvo", "Salvar" e **"Salvar e gerar link"**, que abre uma janela com o link e a "Mensagem para WhatsApp" pronta: "Olá, <nome>! Preparamos o seu briefing de interiores. São algumas imagens para você arrastar (gosto, não gosto ou neutro) e perguntas rápidas sobre a rotina da casa. Dá para fazer pelo celular ou iPad, com calma, e o progresso fica salvo. <link> Equipe Trioma Arquitetura e Interiores". Botões "Copiar mensagem", "Abrir como cliente" e "Fechar".
4. **Biblioteca** `24_painel_biblioteca.png`: "Biblioteca de ambientes: a base de imagens e perguntas de cada ambiente. O que mudar aqui vale para os próximos briefings." Navegação lateral com os ambientes e contagens. Abas "Imagens (N)" e "Perguntas (N)". Adicionar imagens novas; tocar numa imagem para ajustar os estilos (alimentam o perfil de estilo do relatório); retirar e restaurar fotos da base; criar perguntas novas (sim/não, uma opção, várias, texto, número) e apagar as criadas. As perguntas criadas aparecem no ambiente numa página "Perguntas do escritório". No site, isso tem rotas no backend e não gasta crédito do Claude.
5. **Respostas (relatório)** `21_painel_relatorio_brendo.png`:
   - Status, nome, projeto, data de envio. Botões "Exportar PDF", "Copiar resumo", "Editar", "Ver como cliente".
   - Resumo: percentual concluído, Gosto, Neutro, Não gosto e "Perguntas respondidas x/y".
   - **Perfil de estilo:** frase "Puxa para <estilo> e <estilo>. Evita <estilo>." e barras divergentes por estilo (Não gosto à esquerda em laranja, Gosto à direita em verde, com a razão ao lado). Estilos com menos de 2 imagens avaliadas ficam de fora.
   - Por ambiente: estilos que mais agradaram, miniaturas numeradas em Gosto, Neutro e Não gosto, quantas ficaram sem avaliação, comentário do cliente e lista de respostas.
6. **PDF** (gerado no navegador): capa com números e perfil de estilo, tabela dos ambientes e uma página por ambiente com miniaturas de Gosto e Não gosto (numeradas como no relatório), neutras listadas, comentário do cliente e todas as perguntas por página, inclusive "Sem resposta". Rodapé "Trioma Arquitetura e Interiores · Briefing de <nome>" e número da página. Nome do arquivo: "Briefing <nome>.pdf". Dentro do Artifact, o download usa a permissão de downloads da página; fora dele, um link de download comum.

#### 3.1.4 Modelo de dados do protótipo [OBSERVADO NO CÓDIGO]

Salvo em `localStorage` na chave `trioma-briefing:v2`:

```text
{
  version: 1,
  clients: [{
    id, token, name, project, welcome?, createdAt, sentAt?, example?,
    environments: [{ uid, templateId, label, hiddenImages: [idImagem], hiddenQuestions: [idPergunta] }]
  }],
  responses: {
    <clientId>: {
      clientId,
      swipes:   { <envUid>: { <idImagem>: "like" | "dislike" | "neutral" } },
      swipeLog: { <envUid>: [idImagem, ...] },
      notes:    { <envUid>: "comentário sobre as referências" },
      answers:  { <envUid>: { <idPergunta>: valor } },
      answerNotes: { "<envUid>:<idPergunta>": "observação" },
      step, startedAt, updatedAt, completedAt, doneEnvs: [envUid]
    }
  },
  library: { extraImages: {<envId>: [...]}, removedImages: [id], tagEdits: {<idImagem>: [estilos]}, extraQuestions: {<envId>: [...]} }
}
```

- Ao adicionar um ambiente, `hiddenQuestions` recebe automaticamente todas as perguntas com `off: true`.
- A ordem dos ambientes é normalizada: `geral, hall, sala, cozinha, gourmet, lavabo_interno, lavabo_externo, master` primeiro (com `closet` e `banho_master` logo depois de `master`, quando houver suíte master), depois os demais na ordem do escritório.
- O catálogo completo (ambientes, imagens com estilos, perguntas, opções) está em `dados/catalogo_ambientes_v32.json` e, legível, em `CATALOGO_AMBIENTES_E_PERGUNTAS.md`. O estado inicial com os três clientes de exemplo está em `dados/clientes_exemplo_v32.json`.

#### 3.1.5 Imagens

- 192 arquivos em `img/`: `capas/` (14 capas), `opcoes/` (27 fotos e desenhos usados nas opções das perguntas) e um baralho por ambiente (`sala` 24, `cozinha` 21, `master` 21, `gourmet` 20, `banho_master` 14, `quarto` 14 arquivos (12 em uso), `banheiro` 11, `closet` 11, `hospedes` 10 (usadas também pela suíte de hóspedes superior), `closet_suite` 5). Lavabos sem baralho.
- Fotos do Pinterest (fotos reais de projetos, filtrando renders de IA) e Pexels, lado maior 1400 px.
- Pedras com fotos reais: Super Nano, São Gabriel escovado, Perla Santana (quartzito bege acinzentado com veios), travertino (textura de perto, poros e veios bem visíveis), ônix iluminado.
- "O que fica à mostra" na cozinha: 3 fotos na mesma linha (cozinha branca, minimalista). Revestimentos de banheiro: foto uniforme (pedra bege em tudo) e parede de destaque (azulejo verde no box). Madeira aparente com 3 fotos. Cabeceiras com fotos (estofada, luz, madeira, pedra, simples). Closet: aberto, fechado (portas fechadas com foto), ilha, vidro.
- Ainda são desenhos (podem virar fotos): lixeira e calha úmida, além das torneiras e chuveiros pequenos.
- As fotos do Pinterest têm donos (fotógrafos e escritórios). Para o site público, o ideal é trocar por fotos dos projetos da própria Trioma.
- As mesmas imagens, com nomes de pasta em português, estão no computador do Lucas em `Downloads\Trioma Briefing\Imagens\<ambiente>`.

#### 3.1.6 Modificações ao longo das versões

O que se sabe com segurança (pelo doc e pela comparação v1 × v32):
- Perguntas passaram de texto para respostas visuais (ícones, desenhos, amostras e fotos).
- Entraram Lavabo interno, Lavabo externo, Closet suíte e Suíte de hóspedes superior; "Closet" virou "Closet master", "Suíte de hóspedes" virou "Suíte de hóspedes térreo", "Banheiro" virou "Banheiros da casa".
- Baralhos maiores e em alta resolução (ex.: sala de 12 para 24, varanda de 7 para 20).
- Sobre a família reorganizado em 4 páginas, sem hóspedes, com perguntas desligadas por padrão.
- Cozinha em 3 páginas (Bancada, cuba e metais · Equipamentos · Organização e armazenamento).
- Menu inicial com progresso por ambiente, menu a qualquer momento, "Continuar de onde parei", revisão das referências, aviso "Mais perguntas abaixo", tela final com WhatsApp.
- Painel com Biblioteca, Personalizar, relatório com perfil de estilo, PDF e aviso por e-mail no backend.
- Todos os ajustes por ambiente listados no Apêndice A ("Ajustes por ambiente").

O detalhe de cada uma das 32 versões não está acessível.

#### 3.1.7 Estado exato da última versão aprovada

A última versão publicada e registrada no documento do projeto é a **v32**, e o documento a trata como a versão visual "em evolução", que Lucas vinha revisando ambiente por ambiente. Não há registro de reprovação dela. **Tomar a v32 como base.** O arquivo `interfaces/briefing_visual_v32/index.html` é idêntico byte a byte ao publicado (832.472 bytes).

### 3.2 Trioma no iPhone (versão 17)

- **Finalidade:** mostrar ao Lucas (e a quem ele quiser) como o cliente vê o briefing ao abrir o link no celular em casa.
- **Layout:** fundo neutro com gradiente; coluna de controles à esquerda (no celular, em cima) e um iPhone 16 Pro em escala real (tela 393 × 852 pt) com ilha dinâmica, barra de status (9:41, sinal, Wi-Fi, bateria) que pega a cor do topo da página, e barra do Safari embaixo com "AA", cadeado e "trioma.com.br".
- **Controles:** "Briefing": "Teste rápido" (3 imagens por ambiente, token `teste-perguntas-p8w2k`) e "Aldo e Andressa" (projeto completo); botão "Recomeçar do zero" (apaga as respostas daquele cliente e recarrega); nota "Arraste as fotos com o mouse para os lados ou para cima. As respostas ficam salvas só neste navegador, como o progresso do cliente no link real."
- **Funcionamento:** o app inteiro da v32 está embutido em base64 (`APP_B64`) e é carregado num `iframe` via `srcdoc`, trocando `__TOKEN__` pelo token escolhido. O aparelho é redimensionado para caber na janela. Usa as mesmas chaves de armazenamento (`trioma-briefing:v2` e `trioma-iphone:brief`).
- **Arquivo:** `interfaces/briefing_visual_v32/iphone.html` (idêntico ao publicado, 1.122.393 bytes). Precisa da pasta `img/` ao lado (já está). O código da moldura, sem o base64, está completo no Apêndice C e em `codigo_legivel/trioma_no_iphone_v17.moldura.html`.
- Captura: `capturas_de_tela/30_simulacao_iphone.png`.

### 3.3 Briefing Trioma, versão 1 (perguntas em texto)

- Primeira versão publicada (14/10/2026 10:27). 12 ambientes, 118 perguntas, imagens menores. Chave de armazenamento `trioma-briefing:v1`.
- Serve só como histórico. Não continuar a partir dela.
- Arquivos: `interfaces/briefing_v1_perguntas_em_texto/` e catálogo em `dados/catalogo_ambientes_v1.json`.

---

## 4. Estado atual do projeto

### 4.1 Concluído

- Protótipo navegável completo (v32): percurso do cliente e painel do escritório, salvando no navegador.
- 16 modelos de ambiente com perguntas visuais revisadas, 27 perguntas desligadas por padrão, baralhos com 159 cartas e estilos marcados por foto.
- Ordem fixa do percurso, regras de banheiros, lavabos e hóspedes aplicadas.
- Menu com progresso por ambiente, "Continuar de onde parei", revisão das referências, "Mais perguntas abaixo", tela final com WhatsApp.
- Painel: lista, editor com Personalizar, Biblioteca (fotos, estilos, perguntas próprias), relatório com perfil de estilo, "Copiar resumo" e "Exportar PDF".
- Simulação no iPhone 16 Pro com Safari (v17).
- Imagens finais organizadas no computador do Lucas (`Downloads\Trioma Briefing\Imagens\<ambiente>`).
- Site de teste em zip para Netlify Drop (build de 14/10 por volta de 19:30, anterior à v32).

### 4.2 Parcialmente implementado

- **Backend (FastAPI + SQLAlchemy):** existia, com rotas da Biblioteca e o aviso por e-mail (`app/notify.py`), mas **o front ainda não está ligado na API**: o protótipo usa só o localStorage. O aviso por e-mail só funciona depois dessa ligação. **O código do backend não está acessível** (ver 0.2).
- **Aviso por e-mail:** pronto no backend, mas `NOTIFY_EMAIL` é provisório (`briefings@trioma.example`) e faltam `SMTP_HOST`, `SMTP_USER` e `SMTP_PASSWORD`. Sem SMTP só vai para o log.
- **WhatsApp do escritório:** a mensagem final abre o WhatsApp para o cliente escolher o grupo. O número fixo (`OFFICE_WHATSAPP` em `src/config.ts`, `Vw` na build) está vazio.
- **Endereço do site:** o link gerado usa o provisório `https://seusite.com.br/briefing/<token>`.
- **Revisão ambiente por ambiente** com o Lucas: em andamento.

### 4.3 Falta desenvolver

1. Ligar o front na API e definir a rota `/briefing` no site da Trioma (TypeScript + Vite + Python).
2. Reempacotar o código da versão visual quando Lucas aprovar.
3. Trocar os desenhos de lixeira e calha úmida por fotos.
4. Trocar as fotos do Pinterest por fotos dos projetos da própria Trioma antes de publicar no site público.
5. Seguir a revisão ambiente por ambiente.
6. Se aprovado: botão "Editar texto" na Biblioteca para mudar frase, dica e opções das perguntas prontas.

### 4.4 Pendências para perguntar ao Lucas (registradas no doc)

1. E-mail real para os avisos de briefing concluído (e o servidor de envio).
2. Se quer o botão "Editar texto" nas perguntas prontas da Biblioteca (oferecido, sem resposta).
3. Dividir as páginas longas dos banheiros (Banheiros da casa com cerca de 4 telas no celular, Banheiro master com cerca de 5,7) em "Bancada e metais" e "Banho e revestimentos".
4. Cozinha: manter Organização separada ou juntar com Equipamentos.
5. Suíte master: desligar "Para dormir, preferem" como nas outras suítes.

### 4.5 Problemas conhecidos

| Problema | Detalhe | Origem |
|---|---|---|
| **Código-fonte original indisponível** | Só as builds compiladas sobreviveram. Para continuar no React/TypeScript será preciso reconstruir os arquivos-fonte a partir da build (o catálogo já está extraído em JSON; a lógica e os estilos estão em `codigo_legivel/`) ou localizar os arquivos originais, se Lucas tiver guardado em algum lugar. Alternativa simples: continuar editando o HTML da v32 | [CONFIRMADO] nesta exportação |
| Clientes salvos não acompanham mudanças | Briefings salvos antes de uma mudança em perguntas desligadas não mudam sozinhos; usar "Restaurar exemplos" | [CONFIRMADO] |
| Páginas longas nos banheiros | Banheiros da casa cerca de 4 telas no celular; Banheiro master cerca de 5,7 | [CONFIRMADO] |
| Direitos das fotos | Fotos do Pinterest têm donos | [CONFIRMADO] |
| Dados só no navegador | No protótipo, cada navegador tem seus próprios dados; nada chega ao escritório | [OBSERVADO NO CÓDIGO] |
| Textos que ainda fogem da regra de tom | Opção "Os dois" em "Para dormir, preferem:" da **Suíte master** (pergunta ligada), em "Para dormir, preferem:" do Quarto (desligada) e em "Quem cozinha no dia a dia?" de Sobre a família (desligada). "Ainda não sei" em "Pretendem automatizar algo na casa?" (não é decisão técnica, então pode estar certo). **Confirmar com o Lucas antes de mudar** | [OBSERVADO NO CÓDIGO] |
| Fonte depende de internet | Hanken Grotesk vem do Google Fonts | [OBSERVADO NO CÓDIGO] |

### 4.6 Última solicitação e estado da implementação

- O registro acessível termina na **versão 32** (14/10/2026 20:58) e na atualização do documento do projeto do mesmo dia. **A mensagem exata da última solicitação não está acessível** (as conversas anteriores não podem ser lidas daqui).
- Pelo documento, o trabalho estava na **revisão ambiente por ambiente**, com as pendências da seção 4.4 aguardando resposta do Lucas, entre elas o botão "Editar texto", oferecido e ainda sem resposta.
- Tudo o que estava decidido até ali está implementado na v32 (conferido no código: ordem fixa, perguntas desligadas, ajustes por ambiente, menu com progresso, WhatsApp, relatório, PDF).

---

## 5. Continuidade

### 5.1 Como uma nova instância do Claude deve entender o projeto

1. É um **produto de verdade** para o escritório do Lucas (Trioma Arquitetura e Interiores), não um exercício. O cliente final é leigo, usa celular ou iPad em casa e se cansa rápido.
2. A **v32** é a base. Tudo o que mudar deve partir dela, sem regredir decisões.
3. O registro de decisões (seção 2 e Apêndice A) vale como regra. Na dúvida, perguntar ao Lucas em vez de decidir sozinho, principalmente em reorganização de páginas.
4. O conteúdo (ambientes, perguntas, opções, fotos e estilos) é tão importante quanto o código. O catálogo é a referência.

### 5.2 Padrões e restrições para as próximas modificações

**Conteúdo e textos**
- Seguir as 14 instruções da seção 2.5.
- Perguntas novas: preferir resposta por toque (sim/não, opções com ícone, desenho ou foto). Texto livre só quando não houver alternativa.
- Opções que encerram a escolha ("Arquiteto define", "Definir com o arquiteto", "O máximo que o espaço comportar") devem ser exclusivas.
- Suítes de hóspedes térreo e superior são espelhadas: mudar as duas juntas.
- Ao "tirar" uma pergunta, usar `off: true`.
- Novos ambientes de apoio: rápidos, sem detalhe por item (`noSpecs`).

**Visual e interação**
- Manter os tokens da seção 3.1.1 (paper, ink, bronze, night, like/nope/neutral), a fonte Hanken Grotesk e os pesos leves nos títulos.
- Telas escuras para menu, capas e tela final; telas claras para perguntas.
- Alvos de toque com no mínimo 44px; botões em pílula; rodapé fixo com Voltar e Continuar.
- Manter os três gestos e os botões equivalentes no baralho, com as mesmas cores (verde Gosto, laranja Não gosto, cinza Neutro).
- Manter tema escuro e "reduzir movimento".
- Testar sempre em celular (393 × 852), iPad e computador, medindo a rolagem das páginas.

**Técnica**
- Stack do produto: React + TypeScript + Vite; backend FastAPI + SQLAlchemy; site da Trioma em TypeScript, Vite e Python.
- Build de teste em arquivo único (`vite build --mode single`); no site, o PDF em pedaço separado carregado só pelo painel.
- Chave do protótipo: `trioma-briefing:v2`. Se o formato do estado mudar, mudar a versão e prever "Restaurar exemplos".
- Imagens servidas da pasta `img/` (constante `VITE_ASSET_BASE`, padrão `img`).
- Para publicar como Artifact: publicar `index.html` com a pasta `img/` como arquivos de apoio, e dar permissão de downloads (usada pelo "Exportar PDF").

**Forma de trabalhar com o Lucas**
- Revisões pelas páginas do Claude (Artifacts). Zip para Netlify só se ele pedir.
- Soluções simples e econômicas em créditos.
- Arquivos no computador dele organizados em pastas; temporários em "trioma-temp".
- Textos para ele: sem travessões, linguagem humana, direto ao ponto.

### 5.3 Como reabrir e republicar na conta nova

1. Copiar a pasta `BRIEFING TINDER` inteira (ou extrair os ZIPs numa pasta só).
2. Para ver no computador: abrir `interfaces/briefing_visual_v32/index.html` no navegador (painel) e `index.html#b-teste-perguntas-p8w2k` (cliente). A simulação: `interfaces/briefing_visual_v32/iphone.html`.
3. Para voltar a ter as páginas do Claude: num projeto novo, anexar `CONTEXTO_COMPLETO_PROJETO.md`, `CATALOGO_AMBIENTES_E_PERGUNTAS.md` e `dados/catalogo_ambientes_v32.json` como conhecimento do projeto, e pedir ao Claude para publicar `interfaces/briefing_visual_v32/index.html` como Artifact com a pasta `img/` (e a permissão de downloads). Fazer o mesmo com `iphone.html` se quiser a simulação.
4. Para continuar o desenvolvimento no código React: pedir ao Claude para reconstruir o projeto Vite (`src/`) a partir da build e do catálogo, conferindo tela a tela com as capturas em `capturas_de_tela/` e com a v32.

---

## 6. Arquivos de migração

A relação completa, com funções e dependências, está em `MANIFESTO.md`. Resumo:

| Caminho | O que é |
|---|---|
| `CONTEXTO_COMPLETO_PROJETO.md` | Este documento |
| `MANIFESTO.md` | Lista de arquivos, funções e dependências |
| `CATALOGO_AMBIENTES_E_PERGUNTAS.md` | Todo o conteúdo dos 16 ambientes, legível |
| `interfaces/briefing_visual_v32/` | Versão final (index.html), simulação no iPhone (iphone.html) e 192 imagens |
| `interfaces/briefing_v1_perguntas_em_texto/` | Versão 1 e suas 116 imagens |
| `codigo_legivel/` | Script e CSS da v32 reformatados; moldura do iPhone sem o base64 |
| `dados/` | Catálogo v32 e v1 em JSON; clientes de exemplo |
| `capturas_de_tela/` | 20 capturas do percurso do cliente, do painel e da simulação |
| `referencias/` | Documento do projeto e notas de memória, literais |
| `BRIEFING_TINDER_parte1de2.zip`, `BRIEFING_TINDER_parte2de2.zip` | Tudo acima compactado em duas partes (limite de tamanho por arquivo); extrair as duas na mesma pasta |

Fora do pacote, no computador do Lucas: `Downloads\Trioma Briefing\Imagens\` (mesmas fotos, pastas com nomes dos ambientes) e `Downloads\Trioma Briefing\Site de teste\trioma-briefing-teste.zip` (build de teste anterior à v32).

---

## Apêndices

### Apêndice A: documento do projeto, cópia literal (estado em 14/10/2026)

Texto exatamente como estava em `claude/briefing-trioma.md` no projeto "TINDER BRIEFING". Também em `referencias/doc_do_projeto_briefing-trioma.md`.

````markdown
# Briefing Trioma (estilo Tinder): estado do projeto

Atualizado em 14/10/2026.

## O que é
Página de briefing para o site da Trioma Arquitetura e Interiores. Substitui o PDF de ~40 a 60 páginas. O escritório monta o briefing por cliente (só com os ambientes do projeto fechado, escolhendo imagens e perguntas de cada um) e envia um link. O cliente arrasta as imagens (direita = gosto, esquerda = não gosto, para cima = neutro) e responde perguntas, com foco em celular e iPad (também funciona no computador). O escritório vê um relatório com perfil de estilo e exporta um PDF para a equipe. Vai ficar hospedado na área do cliente no site da Trioma.

## Entregas até aqui
- Versão visual em evolução, "Briefing Trioma Visual": https://claude.ai/artifact/XtyUiRtrg2Mqv1eNoz8R1H (versão 32, com permissão de download para o PDF). Cliente "Teste das perguntas" tem só 3 imagens por ambiente e inclui lavabos, suítes de hóspedes, banheiros e o conjunto da suíte master. Cliente "Brendo" tem respostas de exemplo (bom para testar relatório e PDF).
- Simulação num iPhone 16 Pro com Safari, "Trioma no iPhone": https://claude.ai/artifact/DjesYmV5th18VbjS3Xw23T (versão 17)
- Versão 1 (perguntas em texto): https://claude.ai/artifact/RpcwYBAU4VtBTzKTY7Xkzg
- Lucas prefere revisar pelas páginas do Claude. Só gerar zip de site de teste (Netlify Drop) se ele pedir.
- Imagens finais organizadas no computador do Lucas em Downloads › Trioma Briefing › Imagens › <ambiente>.
- Clientes salvos antes de uma mudança de perguntas desligadas não mudam sozinhos: usar "Restaurar exemplos" no painel.

## Ambientes disponíveis na biblioteca (ordem)
Sobre a família · Hall de entrada · Sala de estar e jantar · Cozinha · Varanda gourmet · Lavabo interno · Lavabo externo · Suíte master · Closet master · Banheiro master · Área de serviço · Quarto (modelo de suíte, repetível) · Closet suíte (repetível) · Suíte de hóspedes térreo · Suíte de hóspedes superior · Banheiros da casa.

## Decisões gerais
- Stack: React + TypeScript + Vite no front, FastAPI + SQLAlchemy no backend.
- Projeto de interiores: a planta já vem pronta, então nada de perguntas de arquitetura.
- Opção "Arquiteto define" (ícone de lápis e régua) no lugar de "Ainda não sei" quando a decisão é técnica. Para deixar em aberto: "Definir com o arquiteto".
- Textos neutros e sem informalidade ("Em ambos" ou "Ambos" no lugar de "Nos dois" / "Os dois"; "Pretendem automatizar algo na casa?").
- Pedidos de fotos e modelos vão para "o nosso grupo do WhatsApp", com um lembrete na própria pergunta em vez de campo para digitar.
- Ambientes de apoio (ex.: área de serviço) devem ser rápidos: sem campos de detalhe por item.
- Perguntas "desligadas por padrão" (campo off): entram desmarcadas quando o ambiente é adicionado; o escritório liga em Personalizar. Quando o Lucas diz "tire essa opção" sobre uma pergunta, usar desligada por padrão.
- Ordem fixa do percurso (os ambientes principais primeiro, porque no fim o cliente já está cansado): Sobre a família, Hall, Sala, Cozinha, Varanda gourmet, Lavabo interno, Lavabo externo, Suíte master (com Closet master e Banheiro master logo depois). Só os que estiverem no briefing. O resto segue a ordem que o escritório definir.
- Banheiros: um só modelo geral "Banheiros da casa" por briefing (vale para suítes e banheiros comuns). Banheiro master é opção separada, que pode ser escolhida sozinha. Lavabo interno e lavabo externo são modelos próprios, uma página cada.
- Hóspedes: tudo sobre hóspedes fica nas suítes de hóspedes (saiu de Sobre a família). Dois modelos espelhados: térreo e superior.
- Antes de reorganizar páginas ou juntar perguntas, propor e perguntar ao Lucas (exceto quando ele diz "faça como achar melhor"). Medir rolagem no celular, iPad e computador antes de decidir.
- Ao baixar arquivos no computador dele, deixar organizado em pastas (temporários com nome "trioma-temp").
- Lucas se preocupa com consumo de créditos: preferir soluções simples.

## Imagens
- Fotos dos baralhos vindas do Pinterest (fotos reais de projetos, filtrando renders de IA) e Pexels. Alta resolução (lado maior 1400 px). Sala 24, cozinha 21, suíte master 21, varanda gourmet 20; demais 5 a 14. Lavabos sem baralho.
- As fotos do Pinterest têm donos (fotógrafos e escritórios). Para o site público, o ideal é trocar por fotos dos projetos da própria Trioma.
- Pedras com fotos reais: Super Nano, São Gabriel escovado, Perla Santana (quartzito bege acinzentado com veios), travertino (textura de perto, poros e veios bem visíveis), ônix iluminado.
- "O que fica à mostra" na cozinha: 3 fotos na mesma linha (cozinha branca, minimalista).
- Revestimentos de banheiro: foto uniforme (pedra bege em tudo) e parede de destaque (azulejo verde no box).
- Madeira aparente com 3 fotos. Tela "Como responder" usa a imagem de exemplo antiga, que o Lucas preferiu.

## Fluxo do cliente
- Tela inicial = menu de ambientes: nome do cliente, o roteiro numerado e, em cada ambiente, um anel em volta do número que enche conforme ele responde, com o percentual ao lado (referências avaliadas + perguntas respondidas). Com 100% o número vira um visto. Tocar num ambiente leva direto a ele.
- O campo opcional "Adicionar observação" só entra no percentual se for preenchido (senão nenhum ambiente chegaria a 100%).
- Botão "Começar" segue na ordem, como antes. Depois de começar, o botão vira "Continuar de onde parei" (ou "Revisar e enviar" quando tudo estiver concluído), e o texto mostra o percentual geral do briefing.
- Dentro do briefing, um botão de grade no alto da tela (à direita) abre o menu a qualquer momento. "Continuar de onde parei" volta exatamente para a tela em que ele estava. Ao abrir um ambiente pelo menu, o Voltar da capa dele leva de volta ao menu.
- Quem entra direto num ambiente com imagens vê o "Como responder" antes do primeiro baralho.
- Salva a cada toque. Sem tela de "ambiente concluído": ao terminar um ambiente, segue direto para o próximo. Ao reabrir o link, cai no menu.
- Rever as referências: volta ao baralho com a escolha atual marcada; dá para mudar, ir para a anterior ou para a próxima sem alterar.
- Aviso "Mais perguntas abaixo" enquanto houver pergunta escondida na rolagem.
- Tela final (obrigado): bloco "Avisar no WhatsApp" que abre o WhatsApp com mensagem pronta ("Olá, equipe Trioma! Aqui é <nome>. Acabei de concluir o briefing..."), o cliente escolhe o grupo e envia; também "Copiar mensagem". Se o escritório definir um número fixo (OFFICE_WHATSAPP em src/config.ts), a mensagem vai direto para ele.

## Painel do escritório
- Biblioteca (Painel › Biblioteca): adicionar fotos novas por ambiente, retirar e restaurar fotos da base, ajustar estilos; criar perguntas novas (sim/não, uma opção, várias, texto, número) e apagar as criadas. Personalizar por cliente. Já tem rotas no backend. Usar isso não gasta crédito do Claude.
- Falta (oferecido, sem resposta ainda): botão "Editar texto" para mudar a frase, dica e opções das perguntas que vieram prontas.
- Respostas (relatório): perfil de estilo, referências por ambiente e respostas; "Copiar resumo" e "Exportar PDF".
- PDF (gerado no navegador com jsPDF, src/admin/pdf.ts): capa com números e perfil de estilo, tabela dos ambientes e uma página por ambiente com miniaturas de Gosto e Não gosto (numeradas como no relatório), neutras listadas, comentário do cliente e todas as perguntas por página, inclusive "Sem resposta". Rodapé com nome do cliente e página.
- Aviso por e-mail quando o cliente conclui (backend, app/notify.py): na primeira conclusão manda e-mail para NOTIFY_EMAIL (provisório briefings@trioma.example; Lucas vai informar o e-mail real) com nome, projeto, ambientes, números e link do painel. Precisa de SMTP_HOST/SMTP_USER/SMTP_PASSWORD; sem isso, só vai para o log. Só funciona depois de ligar o front na API.

## Ajustes por ambiente
- Sobre a família: página 1 "Quem vai viver nesta casa?" só com moradores e pets. Página 2 "Rotina e convivência" começa com acessibilidade/alergia/saúde e funcionários da casa, depois home office e receber. Desligadas: aumentar a família, quem cozinha, onde assistem TV, hobby, o que valorizam, prioridades para investir, materiais, plantas, quadros. Hóspedes saiu daqui. "O que incomoda" sem iluminação mal planejada e sem barulho.
- Hall, desligadas: tirar os sapatos, o que o hall deve transmitir. Espelho com ícone próprio.
- Sala: lugares na mesa com 4, 6, 8, 10, 12 ou "O máximo que o espaço comportar". Ao marcar TV, abre embaixo o tamanho em polegadas (42", 50", 60", 65", 70", 75", 85"). Desligadas: linguagem, luz, cortinas.
- Cozinha: 3 páginas (Bancada, cuba e metais · Equipamentos · Organização). Desligadas: embutidos na bancada, despensa, fruteira, refeições rápidas.
- Varanda gourmet: desligadas plantas naturais e móvel/elemento. Equipamentos sem adega, com sofá; "Projetor externo".
- Lavabos: cuba, torneira, formato do espelho (redondo, orgânico, retangular, arquiteto define), revestimentos. O externo pergunta também da ducha para quem sai da piscina.
- Área de serviço: sem campos de modelo; lembrete de mandar o modelo das máquinas no grupo do WhatsApp. "Ambos".
- Suíte (modelo Quarto): desligadas "Sobre o morador", "Para dormir, preferem", vestidos/casacos longos, calçados. Página "Rotina no quarto".
- Suítes de hóspedes (térreo e superior, espelhadas): frequência, quem se hospeda, quanto tempo, cama, o que precisa para guardar, outro uso, conforto; equipamentos sem armário/roupeiro (já coberto pela pergunta de guardar).
- Suíte master: altura da cama estofada com "Definir com o arquiteto" no lugar de "Não querem estofada"; TV com os mesmos tamanhos em polegadas da sala; sem computador no mobiliário; cabeceiras com fotos.
- Closet master (um por briefing): portas fechadas com foto; ilha "Sim, se o espaço permitir"; calçados com nome e quantidade por pessoa. Closet suíte: modelo enxuto.
- Banheiros da casa: cuba, torneira, acima da bancada (armário com espelho ou só espelho), chuveiro, box, revestimentos (uniformes ou parede de destaque + onde). Desligadas: nicho e cesto.
- Banheiro master: mesma linha + duas cubas, pedra, banheira, som e página de hábitos. Nichos desligados.

## Pendências para perguntar ao Lucas
- E-mail real para os avisos de briefing concluído (e o servidor de envio).
- Se quer o botão "Editar texto" nas perguntas prontas da Biblioteca.
- Dividir as páginas longas dos banheiros (Banheiros da casa ~4 telas no celular, Banheiro master ~5,7) em "Bancada e metais" e "Banho e revestimentos".
- Cozinha: manter Organização separada ou juntar com Equipamentos.
- Suíte master: desligar "Para dormir, preferem" como nas outras suítes.

## Próximos passos possíveis
- Seguir a revisão ambiente por ambiente.
- Trocar desenhos de lixeira e calha úmida por fotos.
- Reempacotar o código da versão visual quando ele aprovar; ligar o front na API e definir a rota /briefing no site.
- Build das páginas de teste: `vite build --mode single` (um arquivo só); no site, o PDF fica num pedaço separado que só o painel carrega.
````

### Apêndice B: notas de memória do projeto, cópia literal

````markdown
# Notas de memória do projeto "TINDER BRIEFING" (cópia literal, 20/10/2026)

Estas são as notas que o Claude guardava na memória deste projeto. A marcação [stated] significa "dito pelo próprio Lucas".

## /areas/trioma-arquitetura.md (atualizado em 15/10/2026)

```
---
name: trioma-arquitetura
description: Trioma Arquitetura e Interiores, the user's architecture and interiors firm, and the swipe-style client briefing page he is building for its website
sources: [cowork]
aliases: [Trioma, Trioma Arquitetura, Tinder briefing]
---
- [stated] Trioma Arquitetura (arquitetura e ambientação/interiores) is his own company; it has an existing website
- [stated] Building a Tinder-style briefing page on the Trioma site: office selects the client's contracted rooms, images and questions, then sends a link; client swipes left (não gosto), right (gosto), up (neutro), mainly on phone or iPad, replacing the 60+ page PDF briefing
- [stated] The existing Trioma website is built with TypeScript, Vite and Python
- [stated] Runs the Trioma office in partnership with a sócio (business partner)
```

## /preferences.md do projeto (atualizado em 14/10/2026)

```
---
name: preferences
description: How Lucas wants Claude to work in this project (file handling on his computer)
sources: [cowork]
---
- [stated] Quando Claude usar o computador dele para baixar arquivos/imagens, quer tudo sempre organizado em pastas, sem arquivos soltos
```

## Preferências gerais do Lucas que valem para este projeto

- Não usar travessões.
- Linguagem que soe humana, não gerada por IA, especialmente em textos que ele vai entregar.
- Levantar apenas os pontos mais objetivos e visíveis, sem detalhes hiperespecíficos.
- Respostas claras que entreguem exatamente o que a pergunta pede, sem rodeio.
````

### Apêndice C: código-fonte completo da moldura "Trioma no iPhone" (v17)

É o arquivo publicado inteiro, com uma única troca: o valor da constante `APP_B64` (o app da v32 codificado em base64, mais de 1 MB) foi substituído por um comentário. O arquivo completo, sem nenhuma troca, é `interfaces/briefing_visual_v32/iphone.html`.

````html
<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#fff;color:#000}img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style></head><body>
<title>Trioma no iPhone</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
/* Layout: o aparelho em escala real no centro de uma bancada neutra; controles numa coluna ao lado (em cima no celular) */
:root {
  --stage: #e7e3dc;
  --stage-2: #dcd6cc;
  --ink: #23211e;
  --muted: #6e695f;
  --line: #cfc8bc;
  --chip: #f7f5f1;
  --accent: #6c5640;
  --on-accent: #fbf8f3;
  --device: #2a2a2c;
  --device-edge: #4a4a4e;
  --bar: rgba(246, 246, 246, 0.92);
  --bar-ink: #1c1c1e;
  --pill: rgba(118, 118, 128, 0.14);
  --font: 'Hanken Grotesk', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --ui: -apple-system, 'SF Pro Text', system-ui, 'Segoe UI', sans-serif;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --stage: #181715; --stage-2: #201f1c; --ink: #ece8e1; --muted: #a39d92; --line: #3a3732; --chip: #24221f;
    --accent: #c9ab86; --on-accent: #1b1a17; --device: #0d0d0e; --device-edge: #3c3c40;
    --bar: rgba(28, 28, 30, 0.92); --bar-ink: #f2f2f7; --pill: rgba(118, 118, 128, 0.28); color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --stage: #181715; --stage-2: #201f1c; --ink: #ece8e1; --muted: #a39d92; --line: #3a3732; --chip: #24221f;
  --accent: #c9ab86; --on-accent: #1b1a17; --device: #0d0d0e; --device-edge: #3c3c40;
  --bar: rgba(28, 28, 30, 0.92); --bar-ink: #f2f2f7; --pill: rgba(118, 118, 128, 0.28); color-scheme: dark;
}
html, body { height: 100%; }
body {
  background: radial-gradient(120% 90% at 50% 40%, var(--stage) 0%, var(--stage-2) 100%);
  color: var(--ink); font-family: var(--font); font-size: 15px;
  padding-left: max(16px, env(safe-area-inset-left, 0px));
  padding-right: max(16px, env(safe-area-inset-right, 0px));
  padding-block: 0; overflow: hidden;
}
.stage { height: 100%; display: flex; align-items: center; justify-content: center; gap: 48px; }
.rail { width: 250px; flex: 0 0 auto; display: flex; flex-direction: column; gap: 18px; }
.eyebrow { font-size: 11px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: var(--muted); }
h1 { margin: 4px 0 0; font-size: 26px; font-weight: 600; line-height: 1.15; letter-spacing: -0.01em; text-wrap: balance; }
.lead { margin: 0; color: var(--muted); line-height: 1.5; font-size: 14px; }
.spec { font-variant-numeric: tabular-nums; color: var(--ink); }
.group { display: flex; flex-direction: column; gap: 8px; }
.label { font-size: 12px; font-weight: 600; color: var(--muted); }
.seg { display: grid; gap: 6px; }
.seg button {
  display: flex; flex-direction: column; align-items: flex-start; gap: 2px; text-align: left;
  padding: 10px 12px; border-radius: 12px; border: 1px solid var(--line); background: var(--chip); color: var(--ink);
  font: inherit; cursor: pointer;
}
.seg button small { color: var(--muted); font-size: 12px; }
.seg button[aria-pressed="true"] { border-color: var(--accent); box-shadow: inset 0 0 0 1px var(--accent); }
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding: 11px 16px; border-radius: 999px;
  border: 0; background: var(--accent); color: var(--on-accent); font: inherit; font-weight: 600; cursor: pointer;
}
.btn:focus-visible, .seg button:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.note { margin: 0; font-size: 12px; color: var(--muted); line-height: 1.45; }
.status-msg { min-height: 1em; font-size: 12px; color: var(--accent); }

/* aparelho: iPhone 16 Pro, tela de 393 x 852 pt */
.holder { flex: 0 0 auto; position: relative; }
.device {
  position: absolute; left: 0; top: 0; width: 417px; height: 876px; transform-origin: top left;
  border-radius: 68px; background: var(--device); padding: 12px;
  box-shadow: 0 0 0 2px var(--device-edge), 0 30px 60px -20px rgb(0 0 0 / 45%), 0 8px 20px rgb(0 0 0 / 18%);
}
.device::before, .device::after { content: ""; position: absolute; width: 4px; border-radius: 2px; background: var(--device-edge); }
.device::before { left: -5px; top: 190px; height: 64px; box-shadow: 0 84px 0 var(--device-edge); }
.device::after { right: -5px; top: 230px; height: 96px; }
.screen { position: relative; width: 393px; height: 852px; border-radius: 56px; overflow: hidden; background: #fff; isolation: isolate; }
.sbar {
  position: absolute; inset: 0 0 auto; height: 54px; z-index: 2; display: flex; align-items: center; justify-content: space-between;
  padding: 6px 30px 0 46px; font-family: var(--ui); font-size: 17px; font-weight: 600; color: #000; background: #f3f0ea;
  transition: background-color 0.2s, color 0.2s;
}
.sbar__icons { display: flex; align-items: center; gap: 6px; }
.sbar svg { display: block; fill: currentColor; }
.island { position: absolute; left: 50%; top: 11px; width: 126px; height: 37px; margin-left: -63px; border-radius: 20px; background: #000; z-index: 3; }
.viewport { position: absolute; left: 0; top: 54px; width: 393px; height: 716px; border: 0; display: block; background: #f3f0ea; }
.safari {
  position: absolute; inset: auto 0 0; height: 82px; z-index: 2; background: var(--bar); color: var(--bar-ink);
  backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-top: 0.5px solid rgb(0 0 0 / 12%);
  padding: 8px 14px 0; font-family: var(--ui);
}
.addr {
  height: 44px; border-radius: 13px; background: var(--pill); display: flex; align-items: center; justify-content: space-between;
  padding: 0 14px; font-size: 16px;
}
.addr__aa { font-size: 15px; font-weight: 500; letter-spacing: -0.02em; }
.addr__url { display: flex; align-items: center; gap: 5px; font-weight: 500; }
.addr svg { display: block; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.home { position: absolute; left: 50%; bottom: 8px; width: 134px; height: 5px; margin-left: -67px; border-radius: 3px; background: var(--bar-ink); opacity: 0.85; }

@media (max-width: 720px) {
  body { overflow: auto; }
  .stage { flex-direction: column; justify-content: flex-start; gap: 18px; padding-block: 18px 28px; height: auto; min-height: 100%; }
  .rail { width: 100%; max-width: 420px; }
  .seg { grid-template-columns: 1fr 1fr; }
}
@media (prefers-reduced-motion: reduce) { .sbar { transition: none; } }
</style>

<div class="stage">
  <section class="rail" aria-label="Controles da simulação">
    <div>
      <span class="eyebrow">Simulação no celular</span>
      <h1>Briefing Trioma no iPhone</h1>
    </div>
    <p class="lead">Tela de um <span class="spec">iPhone 16 Pro (393 × 852 pt)</span> com a barra do Safari, como o cliente vê ao abrir o link em casa.</p>
    <div class="group">
      <span class="label" id="lbl-brief">Briefing</span>
      <div class="seg" role="group" aria-labelledby="lbl-brief">
        <button type="button" id="opt-demo" data-token="teste-perguntas-p8w2k" data-id="c-demo" aria-pressed="true">Teste rápido<small>3 imagens por ambiente</small></button>
        <button type="button" id="opt-aldo" data-token="aldo-e-andressa-7k2p" data-id="c-aldo" aria-pressed="false">Aldo e Andressa<small>projeto completo</small></button>
      </div>
    </div>
    <div class="group">
      <button type="button" class="btn" id="restart">Recomeçar do zero</button>
      <span class="status-msg" id="msg" role="status"></span>
    </div>
    <p class="note">Arraste as fotos com o mouse para os lados ou para cima. As respostas ficam salvas só neste navegador, como o progresso do cliente no link real.</p>
  </section>

  <div class="holder" id="holder">
    <div class="device" id="device">
      <div class="screen">
        <div class="sbar" id="sbar">
          <span>9:41</span>
          <span class="sbar__icons" aria-hidden="true">
            <svg width="18" height="12" viewBox="0 0 18 12"><rect x="0" y="8" width="3" height="4" rx="1"/><rect x="5" y="5.5" width="3" height="6.5" rx="1"/><rect x="10" y="3" width="3" height="9" rx="1"/><rect x="15" y="0" width="3" height="12" rx="1"/></svg>
            <svg width="16" height="12" viewBox="0 0 16 12"><path d="M8 2.6c2.3 0 4.4.9 6 2.4l1.1-1.2A10.4 10.4 0 0 0 8 1 10.4 10.4 0 0 0 .9 3.8L2 5c1.6-1.5 3.7-2.4 6-2.4Zm0 3.3c1.4 0 2.6.5 3.6 1.4l1.1-1.2A6.9 6.9 0 0 0 8 4.3a6.9 6.9 0 0 0-4.7 1.8l1.1 1.2c1-.9 2.2-1.4 3.6-1.4Zm0 3.2c.6 0 1.1.2 1.5.6L8 11.3 6.5 9.7c.4-.4.9-.6 1.5-.6Z"/></svg>
            <svg width="27" height="13" viewBox="0 0 27 13"><rect x="0.5" y="0.5" width="23" height="12" rx="3.5" fill="none" stroke="currentColor" opacity="0.4"/><rect x="2" y="2" width="20" height="9" rx="2.2"/><path d="M25 4.5v4c.8-.3 1.3-1.1 1.3-2s-.5-1.7-1.3-2Z" opacity="0.45"/></svg>
          </span>
        </div>
        <div class="island" aria-hidden="true"></div>
        <iframe class="viewport" id="vp" title="Briefing aberto no iPhone"></iframe>
        <div class="safari" aria-hidden="true">
          <div class="addr">
            <span class="addr__aa">AA</span>
            <span class="addr__url"><svg width="11" height="13" viewBox="0 0 11 13"><rect x="1" y="5.5" width="9" height="6.5" rx="1.5"/><path d="M3 5.5V4a2.5 2.5 0 0 1 5 0v1.5"/></svg>trioma.com.br</span>
            <svg width="16" height="16" viewBox="0 0 16 16"><path d="M13.5 8a5.5 5.5 0 1 1-1.6-3.9"/><path d="M12.5 1.5v3h-3"/></svg>
          </div>
          <div class="home"></div>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
(() => {
  const APP_B64 = "/* conteudo removido aqui: e o index.html da versao visual codificado em base64 (ver iphone.html para o arquivo completo) */";
  const KEY = 'trioma-briefing:v2';
  const vp = document.getElementById('vp');
  const device = document.getElementById('device');
  const holder = document.getElementById('holder');
  const sbar = document.getElementById('sbar');
  const msg = document.getElementById('msg');
  const opts = [...document.querySelectorAll('.seg button')];
  let html = '';
  try {
    html = new TextDecoder().decode(Uint8Array.from(atob(APP_B64), (c) => c.charCodeAt(0)));
  } catch (e) { html = ''; }
  let current = opts[0];
  try { const saved = localStorage.getItem('trioma-iphone:brief'); const o = opts.find((b) => b.id === saved); if (o) current = o; } catch (e) {}

  function load() {
    opts.forEach((b) => b.setAttribute('aria-pressed', String(b === current)));
    vp.srcdoc = html.replace('__TOKEN__', JSON.stringify(current.dataset.token));
  }
  opts.forEach((b) => b.addEventListener('click', () => {
    current = b; try { localStorage.setItem('trioma-iphone:brief', b.id); } catch (e) {}
    msg.textContent = ''; load();
  }));
  document.getElementById('restart').addEventListener('click', () => {
    try {
      const raw = localStorage.getItem(KEY);
      if (raw) { const s = JSON.parse(raw); if (s.responses) delete s.responses[current.dataset.id]; localStorage.setItem(KEY, JSON.stringify(s)); }
      msg.textContent = 'Respostas apagadas. Começando de novo.';
    } catch (e) { msg.textContent = 'Começando de novo.'; }
    load();
  });

  // escala para caber na tela sem cortar o aparelho
  const W = 417, H = 876;
  function fit() {
    const narrow = window.matchMedia('(max-width: 720px)').matches;
    const availH = narrow ? Math.max(480, window.innerHeight * 0.92) : window.innerHeight - 48;
    const availW = narrow ? document.body.clientWidth - 32 : document.body.clientWidth - 250 - 48 - 32;
    const s = Math.min(1, availH / H, Math.max(0.3, availW / W));
    device.style.transform = `scale(${s})`;
    holder.style.width = W * s + 'px';
    holder.style.height = H * s + 'px';
  }
  window.addEventListener('resize', fit); fit();

  // barra de status com a cor do topo da página, como o Safari faz
  function tint() {
    try {
      const d = vp.contentDocument; if (!d || !d.body) return;
      let el = d.elementFromPoint(196, 2);
      let bg = '';
      while (el) { const c = getComputedStyle(el).backgroundColor; if (c && c !== 'transparent' && !/rgba\(.*, 0\)$/.test(c)) { bg = c; break; } el = el.parentElement; }
      if (!bg) bg = getComputedStyle(d.body).backgroundColor;
      const m = bg.match(/\d+(\.\d+)?/g) || [255, 255, 255];
      const lum = (0.299 * m[0] + 0.587 * m[1] + 0.114 * m[2]) / 255;
      sbar.style.backgroundColor = bg; sbar.style.color = lum < 0.5 ? '#fff' : '#000';
      vp.style.background = bg;
    } catch (e) {}
  }
  setInterval(tint, 400);
  load();
})();
</script>

</body></html>
````

### Apêndice D: tokens de design da v32 (trecho literal do CSS)

Blocos `:root` do CSS do app, quebrados em linhas para leitura (o conteúdo é o mesmo). O CSS completo está em `codigo_legivel/briefing_visual_v32.estilos.formatado.css`.

````css
:root{
  --paper: #f3f0ea;
  --surface: #fbfaf7;
  --sunk: #ebe6de;
  --ink: #1d1b18;
  --ink-2: #4a453f;
  --muted: #776f66;
  --line: #ddd5ca;
  --accent: #8e7660;
  --accent-ink: #6c5843;
  --night: #141413;
  --night-2: #1f1e1b;
  --night-ink: #ede8e0;
  --night-muted: #a39c92;
  --night-accent: #bfa88f;
  --like: #00826b;
  --nope: #c4501f;
  --neutral: #8a847a;
  --on-strong: #ffffff;
  --shadow: 0 1px 2px rgb(29 27 24 / 6%), 0 8px 24px rgb(29 27 24 / 8%);
  --font: "Hanken Grotesk", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --gutter-l: max(16px, env(safe-area-inset-left, 0px));
  --gutter-r: max(16px, env(safe-area-inset-right, 0px));
  padding-top:env(safe-area-inset-top,0px);
  padding-bottom:env(safe-area-inset-bottom,0px)
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme=light]){
  --paper: #121211;
  --surface: #1c1b19;
  --sunk: #262421;
  --ink: #ede8e0;
  --ink-2: #cfc8bd;
  --muted: #a39c92;
  --line: #34312c;
  --accent: #b9a28a;
  --accent-ink: #c9b49c;
  --like: #24a08a;
  --nope: #da6a30;
  --neutral: #8f897f;
  --shadow: 0 1px 2px rgb(0 0 0 / 30%), 0 10px 30px rgb(0 0 0 / 35%);
  color-scheme:dark
}
````

### Apêndice E: código-fonte da v32 (onde está)

- Build completa e funcional, idêntica à publicada: `interfaces/briefing_visual_v32/index.html` (832.472 bytes; todo o HTML, CSS e JavaScript num arquivo só, mais a pasta `img/`).
- Mesmo script, só reformatado para leitura (32.475 linhas): `codigo_legivel/briefing_visual_v32.script.formatado.js`. A parte do app começa em `const Ww = "https://seusite.com.br"` (configuração, catálogo `Ou`, estilos `Zr`, ordem `Am`, chave `h2`), segue com os componentes de tela e termina no gerador de PDF (`buildBriefingPdf`). O resto são bibliotecas embutidas (React 18.3.1, lucide-react 0.460.0, jsPDF, jspdf-autotable, html2canvas e dependências).
- O código não foi colado aqui dentro porque tem mais de 1 MB e é compilado (nomes encurtados pelo Vite). Colar no Markdown não ajudaria a ler e deixaria o arquivo pesado demais para anexar numa conversa. Ele está preservado integralmente nos arquivos acima.
- Os arquivos-fonte originais (`src/*.tsx`, `src/config.ts`, `src/admin/pdf.ts`, `app/*.py`, `app/notify.py`) não estavam acessíveis (seção 0.2).

---

## INSTRUÇÕES PARA RETOMADA DO PROJETO

Estas instruções são para a nova instância do Claude que vai continuar o projeto na outra conta. Siga na ordem.

### Passo 1: ler a documentação

1. Leia este arquivo inteiro, com atenção às seções 2 (decisões), 3.1 (interface final), 4 (estado atual) e 5 (padrões).
2. Leia `CATALOGO_AMBIENTES_E_PERGUNTAS.md` para conhecer o conteúdo de cada ambiente. Use `dados/catalogo_ambientes_v32.json` quando precisar dos ids e da estrutura exata.
3. Olhe as capturas em `capturas_de_tela/` para ver como as telas são hoje.
4. Leia `MANIFESTO.md` para saber onde está cada arquivo.

### Passo 2: reconhecer as decisões anteriores

- Trate a seção 2.5 ("Instruções específicas que devem continuar sendo respeitadas") como regra fixa. Não desfaça nenhuma decisão registrada sem o Lucas pedir.
- Lembre principalmente: nada de perguntas de arquitetura; "Arquiteto define" e "Definir com o arquiteto"; tom neutro ("Em ambos"); lembrete do grupo do WhatsApp em vez de campo; "tire essa opção" = desligar por padrão; ordem fixa dos ambientes principais; um só "Banheiros da casa"; hóspedes só nas suítes de hóspedes, térreo e superior espelhados; ambientes de apoio rápidos.
- Antes de reorganizar páginas ou juntar perguntas, proponha e pergunte, com medição de rolagem em celular, iPad e computador. Exceção: quando ele disser "faça como achar melhor".

### Passo 3: identificar a versão atual

- A versão atual é a **v32 do Briefing Trioma Visual**: `interfaces/briefing_visual_v32/index.html` com a pasta `img/`. A simulação no iPhone (`iphone.html`) carrega o mesmo app.
- A versão 1 (`interfaces/briefing_v1_perguntas_em_texto/`) é só histórico.
- O código-fonte original (React/TypeScript e FastAPI) **não veio junto** porque não estava acessível. Não finja que ele existe. Para alterações rápidas de conteúdo ou visual, a forma mais simples e barata é editar o HTML da v32 e republicar. Para seguir com o produto no site da Trioma, combine com o Lucas a reconstrução do projeto Vite a partir da build, do catálogo e das capturas, ou peça a ele os arquivos originais, se tiver.
- Na primeira conversa, publique a v32 como Artifact na conta nova (com a pasta `img/` e permissão de downloads) para o Lucas voltar a revisar pelas páginas do Claude, que é como ele prefere.

### Passo 4: continuar o desenvolvimento

1. Comece pelas pendências da seção 4.4. Pergunte ao Lucas, de forma curta e objetiva:
   - o e-mail real (e o servidor) para os avisos de briefing concluído;
   - se quer o botão "Editar texto" nas perguntas prontas da Biblioteca;
   - se divide as páginas longas dos banheiros em "Bancada e metais" e "Banho e revestimentos";
   - se a Organização da cozinha fica separada ou junta com Equipamentos;
   - se desliga "Para dormir, preferem" na suíte master.
2. Aproveite para confirmar os pontos observados no código que fogem da regra de tom (seção 4.5): "Os dois" na suíte master, no quarto e em "Quem cozinha"; "Ainda não sei" em automação. Não mude sem confirmar.
3. Depois, siga a revisão ambiente por ambiente, na ordem fixa do percurso.
4. Próximos passos técnicos, quando ele aprovar: trocar desenhos de lixeira e calha úmida por fotos; trocar as fotos do Pinterest por fotos da Trioma antes de ir para o site público; ligar o front na API; definir a rota `/briefing` no site; configurar `NOTIFY_EMAIL`, SMTP e, se ele quiser, o número fixo do WhatsApp.

### Passo 5: manter a identidade visual e a lógica

- Mesmas cores (papel `#f3f0ea`, tinta `#1d1b18`, bronze `#8e7660`, noite `#141413`, Gosto `#00826b`, Não gosto `#c4501f`, Neutro `#8a847a`), mesma fonte (Hanken Grotesk, títulos leves), mesmas formas (pílulas, cartões com raio 14 a 18px), telas escuras para menu, capas e final, telas claras para perguntas.
- Mesma lógica: três gestos no baralho com botões equivalentes; salvar a cada toque; menu com progresso; "Continuar de onde parei"; sem tela de ambiente concluído; "Mais perguntas abaixo"; perguntas desligadas por padrão controladas em Personalizar; perfil de estilo calculado pelos estilos das fotos.
- Teste cada mudança em celular (393 × 852), iPad e computador antes de entregar.

### Passo 6: jeito de trabalhar com o Lucas

- Responda em português, de forma direta e humana, **sem travessões**.
- Prefira soluções simples: ele se preocupa com o consumo de créditos.
- Entregue as revisões como páginas do Claude (Artifacts). Zip para Netlify só se ele pedir.
- Se baixar ou salvar algo no computador dele, organize em pastas, com temporários em "trioma-temp".
- Ao fim de cada etapa importante, atualize o documento de estado do projeto (o equivalente ao Apêndice A) para que a próxima sessão não perca nada.

