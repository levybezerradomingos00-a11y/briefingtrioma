# MANIFESTO: pacote de migração "BRIEFING TINDER"

Relação dos arquivos exportados do projeto Briefing Trioma (estilo Tinder), com função e dependências. Exportação de 20/10/2026. Documento principal: `CONTEXTO_COMPLETO_PROJETO.md`.

## Estrutura

```text
BRIEFING TINDER/
├── CONTEXTO_COMPLETO_PROJETO.md        documentação integral (ler primeiro)
├── MANIFESTO.md                        este arquivo
├── CATALOGO_AMBIENTES_E_PERGUNTAS.md   conteúdo dos 16 ambientes, legível
├── interfaces/
│   ├── briefing_visual_v32/            VERSÃO ATUAL
│   │   ├── index.html                  app completo (cliente + painel), v32
│   │   ├── iphone.html                 simulação no iPhone 16 Pro, v17
│   │   └── img/                        192 fotos (capas, opcoes, baralhos)
│   └── briefing_v1_perguntas_em_texto/ histórico
│       ├── index.html                  versão 1
│       └── img/                        116 fotos (resolução menor)
├── codigo_legivel/
│   ├── briefing_visual_v32.script.formatado.js
│   ├── briefing_visual_v32.estilos.formatado.css
│   └── trioma_no_iphone_v17.moldura.html
├── dados/
│   ├── catalogo_ambientes_v32.json
│   ├── clientes_exemplo_v32.json
│   └── catalogo_ambientes_v1.json
├── capturas_de_tela/                   20 imagens PNG
├── referencias/
│   ├── doc_do_projeto_briefing-trioma.md
│   └── notas_de_memoria_do_projeto.md
├── BRIEFING_TINDER_parte1de2.zip       tudo acima, compactado (parte 1)
└── BRIEFING_TINDER_parte2de2.zip       tudo acima, compactado (parte 2)
```

## Função de cada arquivo

| Arquivo ou pasta | Função | Origem | Depende de |
|---|---|---|---|
| `CONTEXTO_COMPLETO_PROJETO.md` | Documentação integral: visão geral, histórico, decisões, interfaces, estado atual, continuidade e instruções de retomada | Escrito nesta exportação a partir do doc do projeto, da memória e do código | Referencia todos os outros |
| `CATALOGO_AMBIENTES_E_PERGUNTAS.md` | Todo o conteúdo dos 16 ambientes: imagens com estilos, páginas, perguntas, opções, perguntas desligadas | Gerado automaticamente a partir da build v32 | `dados/catalogo_ambientes_v32.json` (mesmos dados) |
| `interfaces/briefing_visual_v32/index.html` | **Versão atual.** App completo de arquivo único (HTML + CSS + JavaScript compilados). Sem endereço extra abre o painel; com `#b-<token>` abre o briefing do cliente | Artifact "Briefing Trioma Visual", versão 32, idêntico byte a byte | Pasta `img/` ao lado; internet para a fonte Hanken Grotesk (Google Fonts) |
| `interfaces/briefing_visual_v32/iphone.html` | Simulação num iPhone 16 Pro com Safari. Carrega o mesmo app da v32 (embutido em base64) num iframe | Artifact "Trioma no iPhone", versão 17, idêntico byte a byte | Pasta `img/` ao lado (compartilhada com o index.html) |
| `interfaces/briefing_visual_v32/img/` | 192 fotos: `capas/` (14), `opcoes/` (27), baralhos `sala` 24, `cozinha` 21, `master` 21, `gourmet` 20, `banho_master` 14, `quarto` 14, `banheiro` 11, `closet` 11, `hospedes` 10, `closet_suite` 5 | Arquivos publicados no Artifact v32 (iguais aos do Artifact do iPhone) | Usadas pelos dois HTML acima |
| `interfaces/briefing_v1_perguntas_em_texto/index.html` | Versão 1, perguntas em texto. Só histórico | Artifact "Briefing Trioma", versão 1, idêntico byte a byte | Pasta `img/` ao lado |
| `interfaces/briefing_v1_perguntas_em_texto/img/` | 116 fotos da v1, em resolução menor | Arquivos publicados no Artifact v1 | Usadas pela v1 |
| `codigo_legivel/briefing_visual_v32.script.formatado.js` | O script da v32 reformatado (indentação) para leitura e reconstrução do código-fonte. Não é o TypeScript original | Derivado de `index.html` v32 | Nenhuma (só leitura) |
| `codigo_legivel/briefing_visual_v32.estilos.formatado.css` | Todo o CSS da v32 reformatado | Derivado de `index.html` v32 | Nenhuma (só leitura) |
| `codigo_legivel/trioma_no_iphone_v17.moldura.html` | Código da moldura do iPhone com o base64 removido (para ler) | Derivado de `iphone.html` | Não funciona sozinho; use o `iphone.html` |
| `dados/catalogo_ambientes_v32.json` | Catálogo estruturado: configuração, ordem fixa, estilos e os 16 ambientes com imagens, páginas e perguntas | Extraído da build v32 em execução | Nenhuma |
| `dados/clientes_exemplo_v32.json` | Estado inicial com os 3 clientes de exemplo (Teste das perguntas, Brendo com respostas, Aldo e Andressa) e a biblioteca vazia; formato do localStorage `trioma-briefing:v2` | Extraído da build v32 (função que "Restaurar exemplos" usa) | Ids do catálogo v32 |
| `dados/catalogo_ambientes_v1.json` | Catálogo da v1, para comparação | Extraído da build v1 | Nenhuma |
| `capturas_de_tela/` | 20 capturas: celular (01 a 12), iPad (13), painel no computador (20 a 24), simulação no iPhone (30). Feitas nesta exportação com a v32; a fonte aparece substituída porque o Google Fonts não carregou no ambiente de captura | Geradas nesta exportação | Nenhuma |
| `referencias/doc_do_projeto_briefing-trioma.md` | Cópia literal do documento de estado do projeto (14/10/2026) | Projeto "TINDER BRIEFING" | Nenhuma |
| `referencias/notas_de_memoria_do_projeto.md` | Cópia literal das notas de memória do projeto e preferências gerais do Lucas | Memória do Claude | Nenhuma |
| `BRIEFING_TINDER_parte1de2.zip` e `parte2de2.zip` | Todo o pacote compactado em duas partes, porque um arquivo único passaria do limite de 30 MB de transferência. Extrair as duas na mesma pasta reconstrói a estrutura acima | Gerados nesta exportação | Extrair as duas partes juntas |

## Dependências e como abrir

- **Navegador moderno** (Chrome, Safari, Edge, Firefox). Os HTML funcionam abertos direto do disco ou servidos por qualquer servidor estático.
- **Internet** só para a fonte Hanken Grotesk (sem ela, o navegador usa uma fonte parecida).
- **Pasta `img/` sempre ao lado do HTML.** Os caminhos são relativos (`img/capas/sala.jpg`).
- Endereços úteis: `index.html` (painel), `index.html#b-teste-perguntas-p8w2k` (cliente com 3 imagens por ambiente), `index.html#b-brendo-x4m9` (cliente já respondido), `index.html#b-aldo-e-andressa-7k2p` (residência completa), `iphone.html` (simulação).
- Os dados de teste ficam no navegador (localStorage `trioma-briefing:v2`). "Restaurar exemplos" no painel volta ao estado inicial.
- Bibliotecas já embutidas na build (não precisam ser instaladas): React 18.3.1, lucide-react 0.460.0, jsPDF com jspdf-autotable, html2canvas.

## Fora do pacote (no computador do Lucas)

- `Downloads\Trioma Briefing\Imagens\<ambiente>`: as fotos finais, em pastas com os nomes dos ambientes (Banheiro, Banheiro master, Capas, Closet master, Closet suíte, Cozinha, Opções das perguntas, Quarto, Sala de estar e jantar, Suíte de hóspedes, Suíte master, Varanda gourmet).
- `Downloads\Trioma Briefing\Site de teste\trioma-briefing-teste.zip`: build de teste para Netlify Drop, de 14/10/2026 por volta de 19:30, **anterior à v32**. Contém só a build (index.html, assets e img), sem código-fonte.

## O que não existe neste pacote (e por quê)

- Código-fonte original em TypeScript/React (`src/...`) e backend Python (FastAPI + SQLAlchemy, `app/...`, incluindo `app/notify.py`): não estavam acessíveis. Ficavam no espaço de trabalho temporário das sessões anteriores. Ver seção 0.2 do `CONTEXTO_COMPLETO_PROJETO.md`.
- Versões intermediárias dos Artifacts (v2 a v31 da versão visual, v1 a v16 do iPhone): só a versão atual pode ser baixada.
- Histórico das conversas anteriores: não pode ser lido a partir da conversa em que esta exportação foi feita.

## Inventário completo

341 arquivos, 44.8 MB (sem contar este manifesto e os ZIPs). Para HTML, JSON, Markdown, JS e CSS, os primeiros 16 caracteres do SHA-256 permitem conferir se o arquivo chegou íntegro.

| Arquivo | Tamanho | SHA-256 (início) |
|---|---|---|
| `CATALOGO_AMBIENTES_E_PERGUNTAS.md` | 85 KB | `56ccd8970d4ad700` |
| `CONTEXTO_COMPLETO_PROJETO.md` | 84 KB | `24b3c3f1adf89a6a` |
| `capturas_de_tela/01_celular_menu_inicial.png` | 102 KB |  |
| `capturas_de_tela/01b_celular_menu_inicial_pagina_inteira.png` | 102 KB |  |
| `capturas_de_tela/02_celular_como_responder.png` | 403 KB |  |
| `capturas_de_tela/03_celular_capa_do_ambiente.png` | 1.1 MB |  |
| `capturas_de_tela/04_celular_familia_quem_vai_viver.png` | 134 KB |  |
| `capturas_de_tela/05_celular_familia_rotina.png` | 135 KB |  |
| `capturas_de_tela/06_celular_familia_gostos_materiais.png` | 159 KB |  |
| `capturas_de_tela/07_celular_baralho_sala.png` | 711 KB |  |
| `capturas_de_tela/08_celular_depois_do_baralho_comentario.png` | 361 KB |  |
| `capturas_de_tela/09_celular_sala_como_usam.png` | 131 KB |  |
| `capturas_de_tela/10_celular_sala_equipamentos.png` | 143 KB |  |
| `capturas_de_tela/11_celular_cozinha_bancada_pedras.png` | 440 KB |  |
| `capturas_de_tela/12_celular_cozinha_organizacao.png` | 275 KB |  |
| `capturas_de_tela/13_ipad_menu_inicial.png` | 92 KB |  |
| `capturas_de_tela/20_painel_lista_de_briefings.png` | 111 KB |  |
| `capturas_de_tela/21_painel_relatorio_brendo.png` | 654 KB |  |
| `capturas_de_tela/22_painel_editor_do_briefing.png` | 127 KB |  |
| `capturas_de_tela/23_painel_editor_personalizar.png` | 126 KB |  |
| `capturas_de_tela/24_painel_biblioteca.png` | 645 KB |  |
| `capturas_de_tela/30_simulacao_iphone.png` | 435 KB |  |
| `codigo_legivel/briefing_visual_v32.estilos.formatado.css` | 69 KB | `9bd5b3ff61fd5d45` |
| `codigo_legivel/briefing_visual_v32.script.formatado.js` | 1.1 MB | `ad0dab6544a7b388` |
| `codigo_legivel/trioma_no_iphone_v17.moldura.html` | 13 KB | `44638446678c4751` |
| `dados/catalogo_ambientes_v1.json` | 85 KB | `e89db7029e311ff6` |
| `dados/catalogo_ambientes_v32.json` | 182 KB | `68de9b3066df6008` |
| `dados/clientes_exemplo_v32.json` | 14 KB | `38d257801f00b517` |
| `interfaces/briefing_v1_perguntas_em_texto/index.html` | 261 KB | `a306b78eb5b5ad7b` |
| `interfaces/briefing_v1_perguntas_em_texto/img/banheiro/01.jpg` | 34 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banheiro/02.jpg` | 39 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banheiro/03.jpg` | 35 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banheiro/04.jpg` | 25 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banheiro/05.jpg` | 39 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banheiro/06.jpg` | 49 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banheiro/07.jpg` | 45 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banheiro/08.jpg` | 19 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banheiro/09.jpg` | 42 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banheiro/10.jpg` | 27 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banheiro/11.jpg` | 35 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banho_master/01.jpg` | 48 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banho_master/02.jpg` | 42 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banho_master/03.jpg` | 50 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banho_master/04.jpg` | 47 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banho_master/05.jpg` | 42 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banho_master/06.jpg` | 79 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banho_master/07.jpg` | 37 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banho_master/08.jpg` | 56 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/banho_master/09.jpg` | 37 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/capas/banheiro.jpg` | 26 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/capas/banho_master.jpg` | 56 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/capas/closet.jpg` | 32 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/capas/cozinha.jpg` | 53 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/capas/geral.jpg` | 54 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/capas/gourmet.jpg` | 238 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/capas/hall.jpg` | 54 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/capas/hospedes.jpg` | 201 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/capas/master.jpg` | 61 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/capas/quarto.jpg` | 34 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/capas/sala.jpg` | 38 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/capas/servico.jpg` | 52 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/closet/01.jpg` | 63 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/closet/02.jpg` | 58 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/closet/03.jpg` | 32 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/closet/04.jpg` | 34 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/closet/05.jpg` | 77 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/closet/06.jpg` | 59 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/closet/07.jpg` | 52 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/closet/08.jpg` | 53 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/closet/09.jpg` | 56 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/cozinha/01.jpg` | 23 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/cozinha/02.jpg` | 22 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/cozinha/03.jpg` | 21 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/cozinha/04.jpg` | 25 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/cozinha/05.jpg` | 28 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/cozinha/06.jpg` | 22 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/cozinha/07.jpg` | 24 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/cozinha/08.jpg` | 25 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/cozinha/09.jpg` | 22 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/cozinha/10.jpg` | 28 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/cozinha/11.jpg` | 24 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/cozinha/12.jpg` | 18 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/cozinha/13.jpg` | 24 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/cozinha/14.jpg` | 20 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/cozinha/15.jpg` | 22 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/cozinha/16.jpg` | 20 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/gourmet/01.jpg` | 22 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/gourmet/02.jpg` | 19 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/gourmet/03.jpg` | 22 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/gourmet/04.jpg` | 17 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/gourmet/05.jpg` | 22 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/gourmet/06.jpg` | 22 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/gourmet/07.jpg` | 20 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/hospedes/01.jpg` | 31 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/hospedes/02.jpg` | 30 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/hospedes/03.jpg` | 33 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/hospedes/04.jpg` | 34 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/hospedes/05.jpg` | 35 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/hospedes/06.jpg` | 31 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/hospedes/07.jpg` | 33 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/hospedes/08.jpg` | 34 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/master/01.jpg` | 24 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/master/02.jpg` | 21 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/master/03.jpg` | 43 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/master/04.jpg` | 26 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/master/05.jpg` | 20 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/master/06.jpg` | 24 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/master/07.jpg` | 21 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/master/08.jpg` | 23 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/master/09.jpg` | 32 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/master/10.jpg` | 31 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/master/11.jpg` | 20 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/master/12.jpg` | 26 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/master/13.jpg` | 23 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/master/14.jpg` | 20 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/opcoes/chuveiro_parede.jpg` | 12 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/opcoes/chuveiro_teto.jpg` | 11 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/opcoes/torneira_mesa.jpg` | 9 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/opcoes/torneira_parede.jpg` | 10 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/quarto/01.jpg` | 25 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/quarto/02.jpg` | 26 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/quarto/03.jpg` | 20 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/quarto/04.jpg` | 23 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/quarto/05.jpg` | 20 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/quarto/06.jpg` | 23 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/quarto/07.jpg` | 19 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/quarto/08.jpg` | 21 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/quarto/09.jpg` | 25 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/quarto/10.jpg` | 22 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/quarto/11.jpg` | 25 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/quarto/12.jpg` | 24 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/quarto/13.jpg` | 25 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/quarto/14.jpg` | 23 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/sala/01.jpg` | 46 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/sala/02.jpg` | 32 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/sala/03.jpg` | 71 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/sala/04.jpg` | 61 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/sala/05.jpg` | 85 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/sala/06.jpg` | 57 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/sala/07.jpg` | 59 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/sala/08.jpg` | 46 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/sala/09.jpg` | 47 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/sala/10.jpg` | 58 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/sala/11.jpg` | 61 KB |  |
| `interfaces/briefing_v1_perguntas_em_texto/img/sala/12.jpg` | 50 KB |  |
| `interfaces/briefing_visual_v32/index.html` | 813 KB | `98564eb69a9a3236` |
| `interfaces/briefing_visual_v32/iphone.html` | 1.1 MB | `127aeb7e338817b0` |
| `interfaces/briefing_visual_v32/img/banheiro/01.jpg` | 139 KB |  |
| `interfaces/briefing_visual_v32/img/banheiro/02.jpg` | 120 KB |  |
| `interfaces/briefing_visual_v32/img/banheiro/03.jpg` | 188 KB |  |
| `interfaces/briefing_visual_v32/img/banheiro/04.jpg` | 144 KB |  |
| `interfaces/briefing_visual_v32/img/banheiro/05.jpg` | 126 KB |  |
| `interfaces/briefing_visual_v32/img/banheiro/06.jpg` | 150 KB |  |
| `interfaces/briefing_visual_v32/img/banheiro/07.jpg` | 121 KB |  |
| `interfaces/briefing_visual_v32/img/banheiro/08.jpg` | 142 KB |  |
| `interfaces/briefing_visual_v32/img/banheiro/09.jpg` | 99 KB |  |
| `interfaces/briefing_visual_v32/img/banheiro/10.jpg` | 105 KB |  |
| `interfaces/briefing_visual_v32/img/banheiro/11.jpg` | 122 KB |  |
| `interfaces/briefing_visual_v32/img/banho_master/01.jpg` | 186 KB |  |
| `interfaces/briefing_visual_v32/img/banho_master/02.jpg` | 165 KB |  |
| `interfaces/briefing_visual_v32/img/banho_master/03.jpg` | 170 KB |  |
| `interfaces/briefing_visual_v32/img/banho_master/04.jpg` | 174 KB |  |
| `interfaces/briefing_visual_v32/img/banho_master/05.jpg` | 142 KB |  |
| `interfaces/briefing_visual_v32/img/banho_master/06.jpg` | 144 KB |  |
| `interfaces/briefing_visual_v32/img/banho_master/07.jpg` | 119 KB |  |
| `interfaces/briefing_visual_v32/img/banho_master/08.jpg` | 114 KB |  |
| `interfaces/briefing_visual_v32/img/banho_master/09.jpg` | 97 KB |  |
| `interfaces/briefing_visual_v32/img/banho_master/10.jpg` | 171 KB |  |
| `interfaces/briefing_visual_v32/img/banho_master/11.jpg` | 121 KB |  |
| `interfaces/briefing_visual_v32/img/banho_master/12.jpg` | 161 KB |  |
| `interfaces/briefing_visual_v32/img/banho_master/13.jpg` | 98 KB |  |
| `interfaces/briefing_visual_v32/img/banho_master/14.jpg` | 139 KB |  |
| `interfaces/briefing_visual_v32/img/capas/banheiro.jpg` | 120 KB |  |
| `interfaces/briefing_visual_v32/img/capas/banho_master.jpg` | 103 KB |  |
| `interfaces/briefing_visual_v32/img/capas/closet.jpg` | 198 KB |  |
| `interfaces/briefing_visual_v32/img/capas/cozinha.jpg` | 174 KB |  |
| `interfaces/briefing_visual_v32/img/capas/geral.jpg` | 182 KB |  |
| `interfaces/briefing_visual_v32/img/capas/gourmet.jpg` | 288 KB |  |
| `interfaces/briefing_visual_v32/img/capas/hall.jpg` | 54 KB |  |
| `interfaces/briefing_visual_v32/img/capas/hospedes.jpg` | 185 KB |  |
| `interfaces/briefing_visual_v32/img/capas/lavabo_externo.jpg` | 124 KB |  |
| `interfaces/briefing_visual_v32/img/capas/lavabo_interno.jpg` | 100 KB |  |
| `interfaces/briefing_visual_v32/img/capas/master.jpg` | 167 KB |  |
| `interfaces/briefing_visual_v32/img/capas/quarto.jpg` | 195 KB |  |
| `interfaces/briefing_visual_v32/img/capas/sala.jpg` | 252 KB |  |
| `interfaces/briefing_visual_v32/img/capas/servico.jpg` | 52 KB |  |
| `interfaces/briefing_visual_v32/img/closet/01.jpg` | 199 KB |  |
| `interfaces/briefing_visual_v32/img/closet/02.jpg` | 136 KB |  |
| `interfaces/briefing_visual_v32/img/closet/03.jpg` | 88 KB |  |
| `interfaces/briefing_visual_v32/img/closet/04.jpg` | 140 KB |  |
| `interfaces/briefing_visual_v32/img/closet/05.jpg` | 126 KB |  |
| `interfaces/briefing_visual_v32/img/closet/06.jpg` | 135 KB |  |
| `interfaces/briefing_visual_v32/img/closet/07.jpg` | 232 KB |  |
| `interfaces/briefing_visual_v32/img/closet/08.jpg` | 133 KB |  |
| `interfaces/briefing_visual_v32/img/closet/09.jpg` | 138 KB |  |
| `interfaces/briefing_visual_v32/img/closet/10.jpg` | 91 KB |  |
| `interfaces/briefing_visual_v32/img/closet/11.jpg` | 173 KB |  |
| `interfaces/briefing_visual_v32/img/closet_suite/01.jpg` | 134 KB |  |
| `interfaces/briefing_visual_v32/img/closet_suite/02.jpg` | 131 KB |  |
| `interfaces/briefing_visual_v32/img/closet_suite/03.jpg` | 94 KB |  |
| `interfaces/briefing_visual_v32/img/closet_suite/04.jpg` | 80 KB |  |
| `interfaces/briefing_visual_v32/img/closet_suite/05.jpg` | 72 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/01.jpg` | 216 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/02.jpg` | 229 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/03.jpg` | 157 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/04.jpg` | 97 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/05.jpg` | 163 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/06.jpg` | 163 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/07.jpg` | 176 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/08.jpg` | 204 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/09.jpg` | 123 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/10.jpg` | 105 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/11.jpg` | 139 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/12.jpg` | 151 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/13.jpg` | 198 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/14.jpg` | 204 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/15.jpg` | 116 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/16.jpg` | 201 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/17.jpg` | 102 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/18.jpg` | 110 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/19.jpg` | 211 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/20.jpg` | 128 KB |  |
| `interfaces/briefing_visual_v32/img/cozinha/21.jpg` | 221 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/01.jpg` | 246 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/02.jpg` | 131 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/03.jpg` | 120 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/04.jpg` | 202 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/05.jpg` | 285 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/06.jpg` | 175 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/07.jpg` | 240 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/08.jpg` | 266 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/09.jpg` | 153 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/10.jpg` | 341 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/11.jpg` | 197 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/12.jpg` | 259 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/13.jpg` | 268 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/14.jpg` | 314 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/15.jpg` | 229 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/16.jpg` | 324 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/17.jpg` | 237 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/18.jpg` | 197 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/19.jpg` | 148 KB |  |
| `interfaces/briefing_visual_v32/img/gourmet/20.jpg` | 209 KB |  |
| `interfaces/briefing_visual_v32/img/hospedes/01.jpg` | 105 KB |  |
| `interfaces/briefing_visual_v32/img/hospedes/02.jpg` | 140 KB |  |
| `interfaces/briefing_visual_v32/img/hospedes/03.jpg` | 200 KB |  |
| `interfaces/briefing_visual_v32/img/hospedes/04.jpg` | 158 KB |  |
| `interfaces/briefing_visual_v32/img/hospedes/05.jpg` | 201 KB |  |
| `interfaces/briefing_visual_v32/img/hospedes/06.jpg` | 140 KB |  |
| `interfaces/briefing_visual_v32/img/hospedes/07.jpg` | 221 KB |  |
| `interfaces/briefing_visual_v32/img/hospedes/08.jpg` | 128 KB |  |
| `interfaces/briefing_visual_v32/img/hospedes/09.jpg` | 179 KB |  |
| `interfaces/briefing_visual_v32/img/hospedes/10.jpg` | 217 KB |  |
| `interfaces/briefing_visual_v32/img/master/01.jpg` | 149 KB |  |
| `interfaces/briefing_visual_v32/img/master/02.jpg` | 117 KB |  |
| `interfaces/briefing_visual_v32/img/master/03.jpg` | 160 KB |  |
| `interfaces/briefing_visual_v32/img/master/04.jpg` | 115 KB |  |
| `interfaces/briefing_visual_v32/img/master/05.jpg` | 225 KB |  |
| `interfaces/briefing_visual_v32/img/master/06.jpg` | 140 KB |  |
| `interfaces/briefing_visual_v32/img/master/07.jpg` | 170 KB |  |
| `interfaces/briefing_visual_v32/img/master/08.jpg` | 192 KB |  |
| `interfaces/briefing_visual_v32/img/master/09.jpg` | 198 KB |  |
| `interfaces/briefing_visual_v32/img/master/10.jpg` | 188 KB |  |
| `interfaces/briefing_visual_v32/img/master/11.jpg` | 126 KB |  |
| `interfaces/briefing_visual_v32/img/master/12.jpg` | 232 KB |  |
| `interfaces/briefing_visual_v32/img/master/13.jpg` | 187 KB |  |
| `interfaces/briefing_visual_v32/img/master/14.jpg` | 166 KB |  |
| `interfaces/briefing_visual_v32/img/master/15.jpg` | 164 KB |  |
| `interfaces/briefing_visual_v32/img/master/16.jpg` | 178 KB |  |
| `interfaces/briefing_visual_v32/img/master/17.jpg` | 133 KB |  |
| `interfaces/briefing_visual_v32/img/master/18.jpg` | 117 KB |  |
| `interfaces/briefing_visual_v32/img/master/19.jpg` | 294 KB |  |
| `interfaces/briefing_visual_v32/img/master/20.jpg` | 161 KB |  |
| `interfaces/briefing_visual_v32/img/master/21.jpg` | 199 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/cabeceira_estofada.jpg` | 137 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/cabeceira_luz.jpg` | 159 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/cabeceira_madeira.jpg` | 138 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/cabeceira_pedra.jpg` | 139 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/cabeceira_simples.jpg` | 145 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/chuveiro_parede.jpg` | 11 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/chuveiro_teto.jpg` | 11 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/closet_aberto.jpg` | 68 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/closet_fechado.jpg` | 52 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/closet_ilha.jpg` | 119 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/closet_vidro.jpg` | 160 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/como_responder.jpg` | 43 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/cozinha_guardado.jpg` | 50 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/cozinha_mostra.jpg` | 135 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/cozinha_um_pouco.jpg` | 109 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/madeira_bastante.jpg` | 150 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/madeira_detalhe.jpg` | 128 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/madeira_sem.jpg` | 106 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/onix.jpg` | 116 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/pedra_perla_santana.jpg` | 105 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/pedra_sao_gabriel.jpg` | 195 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/pedra_super_nano.jpg` | 110 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/revest_destaque.jpg` | 177 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/revest_uniforme.jpg` | 100 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/torneira_mesa.jpg` | 9 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/torneira_parede.jpg` | 10 KB |  |
| `interfaces/briefing_visual_v32/img/opcoes/travertino.jpg` | 277 KB |  |
| `interfaces/briefing_visual_v32/img/quarto/01.jpg` | 173 KB |  |
| `interfaces/briefing_visual_v32/img/quarto/02.jpg` | 185 KB |  |
| `interfaces/briefing_visual_v32/img/quarto/03.jpg` | 219 KB |  |
| `interfaces/briefing_visual_v32/img/quarto/04.jpg` | 135 KB |  |
| `interfaces/briefing_visual_v32/img/quarto/05.jpg` | 252 KB |  |
| `interfaces/briefing_visual_v32/img/quarto/06.jpg` | 177 KB |  |
| `interfaces/briefing_visual_v32/img/quarto/07.jpg` | 224 KB |  |
| `interfaces/briefing_visual_v32/img/quarto/08.jpg` | 230 KB |  |
| `interfaces/briefing_visual_v32/img/quarto/09.jpg` | 122 KB |  |
| `interfaces/briefing_visual_v32/img/quarto/10.jpg` | 208 KB |  |
| `interfaces/briefing_visual_v32/img/quarto/11.jpg` | 155 KB |  |
| `interfaces/briefing_visual_v32/img/quarto/12.jpg` | 158 KB |  |
| `interfaces/briefing_visual_v32/img/quarto/13.jpg` | 25 KB |  |
| `interfaces/briefing_visual_v32/img/quarto/14.jpg` | 23 KB |  |
| `interfaces/briefing_visual_v32/img/sala/01.jpg` | 146 KB |  |
| `interfaces/briefing_visual_v32/img/sala/02.jpg` | 210 KB |  |
| `interfaces/briefing_visual_v32/img/sala/03.jpg` | 299 KB |  |
| `interfaces/briefing_visual_v32/img/sala/04.jpg` | 162 KB |  |
| `interfaces/briefing_visual_v32/img/sala/05.jpg` | 152 KB |  |
| `interfaces/briefing_visual_v32/img/sala/06.jpg` | 217 KB |  |
| `interfaces/briefing_visual_v32/img/sala/07.jpg` | 126 KB |  |
| `interfaces/briefing_visual_v32/img/sala/08.jpg` | 173 KB |  |
| `interfaces/briefing_visual_v32/img/sala/09.jpg` | 232 KB |  |
| `interfaces/briefing_visual_v32/img/sala/10.jpg` | 162 KB |  |
| `interfaces/briefing_visual_v32/img/sala/11.jpg` | 296 KB |  |
| `interfaces/briefing_visual_v32/img/sala/12.jpg` | 275 KB |  |
| `interfaces/briefing_visual_v32/img/sala/13.jpg` | 190 KB |  |
| `interfaces/briefing_visual_v32/img/sala/14.jpg` | 282 KB |  |
| `interfaces/briefing_visual_v32/img/sala/15.jpg` | 160 KB |  |
| `interfaces/briefing_visual_v32/img/sala/16.jpg` | 275 KB |  |
| `interfaces/briefing_visual_v32/img/sala/17.jpg` | 263 KB |  |
| `interfaces/briefing_visual_v32/img/sala/18.jpg` | 222 KB |  |
| `interfaces/briefing_visual_v32/img/sala/19.jpg` | 185 KB |  |
| `interfaces/briefing_visual_v32/img/sala/20.jpg` | 177 KB |  |
| `interfaces/briefing_visual_v32/img/sala/21.jpg` | 206 KB |  |
| `interfaces/briefing_visual_v32/img/sala/22.jpg` | 159 KB |  |
| `interfaces/briefing_visual_v32/img/sala/23.jpg` | 201 KB |  |
| `interfaces/briefing_visual_v32/img/sala/24.jpg` | 222 KB |  |
| `referencias/doc_do_projeto_briefing-trioma.md` | 11 KB | `7b0b2f8fa3984592` |
| `referencias/notas_de_memoria_do_projeto.md` | 2 KB | `75f61686161a7e63` |
