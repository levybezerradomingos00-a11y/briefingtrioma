# Atualizações do Briefing Trioma

## 20/10/2026 (conta nova, Artifact "Briefing Trioma Visual", versão 2 = antiga v32 + ajustes)

- Sobre a família: acessibilidade, alergia ou saúde virou Sim/Não; com Sim abre o campo "O que devemos considerar?".
- Sala, cozinha e varanda gourmet entram com 15 imagens por padrão (as 15 primeiras do baralho; o resto pode ser ligado em Personalizar).
- Lavabo externo: "Ducha para quem sai da piscina?" desligada por padrão.
- Closet master: bolsas e calçados sobem de 1 em 1 (closet suíte também).
- Banheiros da casa e banheiro master: "Onde seria o destaque?" desligada por padrão.
- Área de serviço: máquina de lavar com ícone de abertura superior, diferente da lava e seca.
- Perguntas abertas (texto) não contam como pendência; o envio nunca fica bloqueado. Menu tem o link "Revisar e enviar" a qualquer momento.
- Menu: ambiente começado e incompleto mostra "Faltam X perguntas/referências"; ao tocar, abre direto na página pendente com as perguntas marcadas "Falta responder".
- Tela final: botão "Baixar resumo em PDF" para o cliente (mesmo PDF do escritório).
- Aviso por e-mail com o PDF ao concluir: rota em servidor/notify.py (levybezerradomingos00@gmail.com e pbstudioarq@gmail.com). Funciona só no site, com a API ligada (zzNotifyApi no front) e SMTP configurado.
- Novo ambiente "Quarto filha adolescente" (quarto_teen, repetível): 12 referências (Pexels), 3 páginas: Quem é ela, Rotina no quarto, Mobiliário e equipamentos.

### Onde estão os arquivos desta versão
- `interfaces/briefing_visual_v32/index_v33.html`: versão atual (abre direto no navegador, usa a mesma pasta `img/`).
- Fotos novas: `img/quarto_teen/01.jpg` a `12.jpg` e `img/capas/quarto_teen.jpg`.
- Regra: tudo deste projeto fica em `C:\Users\Levy\Desktop\BRIEFING TINDER`.

## 20/10/2026, 15h40 (Artifact versão 3): Quarto filha adolescente
- Estilos: Minimalista / Clean, Moderno / Contemporâneo, Romântico / Delicado, Fashion / Pinterest, Criativo / Colorido.
- Cores: opção "Outra" abre campo para digitar a cor ou combinação preferida.
- Hobbies: "Estudar e ler" num só card. Ao marcar, pergunta se precisa de espaço para muitos livros; com Sim, pergunta quantos (até 50, 50 a 100, 100 a 200, mais de 200).
- Paredes: desligada por padrão.
- Cama: opção "Arquiteto define".
- Nova pergunta: espaço para rede no quarto.
- Equipamentos: sem fita de LED e sem a pergunta do tipo de ar-condicionado.

## 20/10/2026, 15h50 (Artifact versão 4): novo ambiente Quarto filho adolescente
- id `quarto_teen_m`, repetível, mesma estrutura do quarto da filha (Quem é ele, Rotina no quarto, Mobiliário e equipamentos).
- Estilos: Minimalista / Clean, Moderno / Contemporâneo, Industrial / Urbano, Gamer / Tech, Esportivo / Descontraído.
- Cores (com "Outra" e campo), hobbies com "Estudar e ler" + perguntas de livros, paredes desligada por padrão, cama com "Arquiteto define", rede.
- Perguntas próprias: joga no quarto, equipamentos esportivos, muitos tênis. Equipamentos com videogame e cadeira gamer, sem fita de LED e sem tipo de ar.
- 12 referências do Pexels em `img/quarto_teen_m`, capa em `img/capas/quarto_teen_m.jpg`.

## 20/10/2026, 16h (Artifact versão 5): planta baixa na capa
- No editor do briefing, em "Ambientes deste briefing", acima da lista: opção "Planta baixa", desligada por padrão. Ligada, aceita PNG, JPG ou WebP.
- Com planta enviada, a tela de abertura do cliente mostra a planta grande abaixo do nome, sobre o fundo escuro, com sombra suave. Toque amplia em tela cheia.
- Sem a opção ligada, a abertura continua igual.
- Protótipo: a imagem é reduzida para 1400 px e guardada no navegador (limite de 2,5 MB). No site, a planta deve ir para o servidor.
- Exemplo usado nos testes: `referencias/exemplo_planta_baixa.png`.

## 20/10/2026, 16h (Artifact versão 6): planta baixa cancelada
- A opção de planta baixa na capa foi retirada a pedido. O briefing voltou a abrir como antes. Nada mais mudou.

## 20/10/2026, 16h (Artifact versão 7): excluir briefing
- No editor de um briefing já salvo, barra de baixo: botão "Excluir briefing" (no celular, só o ícone de lixeira).
- Abre uma janela de confirmação: é preciso marcar "Entendo que essa exclusão é definitiva" para liberar "Excluir definitivamente". "Cancelar" fecha sem apagar.
- A exclusão apaga o briefing e as respostas do cliente e volta para a lista. Em briefing novo, ainda não salvo, o botão não aparece.

## 20/10/2026, 16h30 (Artifact versão 8): curadoria de referências e suíte de hóspedes única
- Referências retiradas (números das folhas em `curadoria_referencias`): sala 01, 03, 04, 06, 10, 11 · cozinha 01, 02, 08, 09, 10, 12, 15, 16 · suíte master 03, 06, 11, 14, 15, 17, 21 · banheiro master 01, 03, 08, 10, 11 · quarto filho 03, 06, 10 · quarto filha 04, 06, 07, 08, 09, 11, 12 · suíte de hóspedes 05, 06, 07, 08, 10 · banheiros da casa 09, 10. Os arquivos continuam na pasta img, só saem do baralho.
- Totais agora: sala 18, cozinha 13, suíte master 14, banheiro master 9, quarto filha 5, quarto filho 9, suíte de hóspedes 5, banheiros da casa 9.
- Suíte de hóspedes térreo e superior viraram um só ambiente, "Suíte de hóspedes", que pode entrar mais de uma vez no briefing. Briefings já salvos com a superior passam a usar o modelo único, sem perder respostas.

## 20/10/2026, 16h40 (Artifact versão 9): bebidas em Sobre a família
- Página "Rotina e convivência", depois de receber visitas: "Costumam beber e guardar bebidas em casa?" (Sim, bastante · Às vezes · Não).
- Com Sim ou Às vezes: "O que precisa ser previsto?" (adega climatizada, cristaleira, bar ou bancada de drinks, espaço para destilados, Arquiteto define).
- Com adega marcada: "Mais ou menos quantas garrafas de vinho?" (até 12, 12 a 30, 30 a 60, mais de 60).

## 20/10/2026, 16h50 (Artifact versão 10): novo ambiente Cinema
- id `cinema`, 11 referências do Pexels em `img/cinema`, capa `img/capas/cinema.jpg`.
- Página "Assentos e tela": quantas pessoas; assentos (poltronas de cinema, sofá confortável, sofá-cama, Arquiteto define); com poltronas, pergunta da segunda fileira mais alta; TV, projetor ou ambos; tamanho da TV (com TV ou ambos); tela do projetor (com projetor ou ambos).
- Página "Som, luz e conforto": tratamento acústico; sistema de som; escurecimento total; iluminação; outros usos (games, esportes, karaokê, hóspedes); itens a prever (videogame, frigobar, pipoqueira, bancada ou bar, armário de equipamentos, ar-condicionado); observação.

## 20/10/2026, 17h10 (Artifact versão 11): ajustes no Cinema
- "Precisa escurecer totalmente o ambiente?" e "Como imaginam a iluminação?" desligadas por padrão.
- Ar-condicionado saiu de "O que mais deve ser previsto?".
- Referências do cinema serão trocadas pelas fotos que o escritório vai enviar.

## 20/10/2026, 17h40 (Artifact versão 12): nova capa de Sobre a família
- Foto enviada pelo escritório, com leve desfoque. O degradê escuro embaixo continua (é do próprio layout).
- A capa anterior foi guardada em `referencias/capa_geral_antiga.jpg`.

## 20/10/2026, 17h45 (Artifact versão 13): nova capa da Sala de estar e jantar
- Foto enviada pelo escritório, com leve desfoque e o mesmo degradê. No celular aparece o centro (espelho redondo e sofá).
- A capa anterior foi guardada em `referencias/capa_sala_antiga.jpg`.

## 20/10/2026, 17h50 (Artifact versão 14): nova capa da Cozinha
- Foto enviada pelo escritório, com leve desfoque e o mesmo degradê. Capa anterior em `referencias/capa_cozinha_antiga.jpg`.

## 20/10/2026, 17h50 (Artifact versão 15): nova capa da Varanda gourmet
- Foto enviada pelo escritório, com leve desfoque e o mesmo degradê. Capa anterior em `referencias/capa_gourmet_antiga.jpg`.

## 20/10/2026, 17h55 (Artifact versão 16): nova capa da Suíte master
- Foto enviada pelo escritório, com leve desfoque e o mesmo degradê. Capa anterior em `referencias/capa_master_antiga.jpg`.

## 20/10/2026, 17h55 (Artifact versão 17): nova capa do Lavabo interno
- Foto enviada pelo escritório, com leve desfoque e o mesmo degradê. Capa anterior em `referencias/capa_lavabo_interno_antiga.jpg`.

## 20/10/2026, 17h55 (Artifact versão 18): nova capa do Lavabo externo
- Foto enviada pelo escritório, com leve desfoque e o mesmo degradê. Capa anterior em `referencias/capa_lavabo_externo_antiga.jpg`.

## 20/10/2026, 18h (Artifact versão 19): nova capa do Quarto filho adolescente
- Foto enviada pelo escritório, com leve desfoque e o mesmo degradê. Capa anterior em `referencias/capa_quarto_teen_m_antiga.jpg`.

## 20/10/2026, 18h (Artifact versão 20): nova capa do Quarto filha adolescente
- Foto enviada pelo escritório, com leve desfoque e o mesmo degradê. Capa anterior em `referencias/capa_quarto_teen_antiga.jpg`.

## 20/10/2026, 18h (Artifact versão 21): nova capa da Área de serviço
- Foto enviada pelo escritório, com leve desfoque e o mesmo degradê. Capa anterior em `referencias/capa_servico_antiga.jpg`.

## 20/10/2026, 18h (Artifact versão 22): nova capa do Banheiro master
- Foto enviada pelo escritório, com leve desfoque e o mesmo degradê. Capa anterior em `referencias/capa_banho_master_antiga.jpg`.

## 20/10/2026, 18h30 (Artifact versão 23): referências do escritório + lavabo único
- 128 fotos da pasta `IMAGENS BRIEFING` entraram nos ambientes: sala, cozinha, varanda gourmet, suíte master, closet master, banheiro master, cinema, suíte de hóspedes, quartos filho/filha adolescente, banheiros da casa e os dois lavabos. Cada foto recebeu marcas de estilo (editáveis na Biblioteca).
- Em briefings novos, só as fotos do escritório vêm ligadas. As antigas continuam na biblioteca, mas desligadas. Exceção: Closet master, onde antigas e novas vêm ligadas.
- Quarto (genérico) e Closet suíte não mudaram (não havia pasta).
- Lavabo: no painel, um único item "Lavabo" com a escolha Interno ou Externo. Cada um traz as próprias fotos (pasta LAVABO e pasta LAVABO EXTERNO) e as próprias perguntas.
- Briefings já criados antes desta versão mantêm o que estava marcado neles.

## 20/10/2026, 18h15 (Artifact versão 24): nova capa do Hall de entrada
- Foto enviada pelo escritório, com leve desfoque e o mesmo degradê. Capa anterior em `referencias/capa_hall_antiga.jpg`.

## 20/10/2026, 18h35 (Artifact versões 25 e 26): fotos carregando mais rápido
- Todas as fotos foram recomprimidas (carregamento progressivo, no máximo 1080 px): de 52,6 MB para 36,3 MB no total; nenhuma passa de 210 KB.
- Ao abrir as referências de um ambiente, as próximas fotos já baixam em segundo plano (3 por vez, na ordem em que aparecem).
- Se uma foto falhar (rede fraca), o site tenta de novo até 3 vezes em vez de deixar o cartão preto.
- Enquanto a foto carrega, aparece um indicador girando no cartão.

## 20/10/2026, 18h30 (Artifact versão 27): pré-carregamento mais leve
- O pré-carregamento da versão 25 baixava todas as fotos do ambiente e disputava a conexão com os ícones das perguntas. Agora baixa só as próximas fotos (2 à frente do que está na tela), com prioridade baixa e no máximo 2 ao mesmo tempo.
- Lembrete: como as fotos foram recomprimidas, o navegador baixa tudo de novo uma vez; das próximas vezes vem do cache.

## 20/10/2026, 18h30 (Artifact versão 28): capas estáticas
- As capas dos ambientes não fazem mais o zoom lento ao abrir; ficam paradas.

## 20/10/2026, 19h50 (Artifact versões 29 a 31): WebP até 100 KB e carregamento por etapa
- As 358 imagens do briefing (fotos, capas e ilustrações das perguntas) foram convertidas para WebP a partir dos originais. Nenhuma passa de 100.000 bytes (a maior tem 96.868). Total: de 52,6 MB (JPG) para 24,0 MB. Pesos de cada arquivo em `PESOS_IMAGENS.csv`.
- 24 fotos muito detalhadas foram reduzidas um pouco de tamanho (mesma proporção) para caber no limite sem perder nitidez; nenhuma ficou abaixo de qualidade 64.
- Os JPG originais continuam guardados (pasta IMAGENS BRIEFING e os ZIPs do projeto); o site publicado usa só WebP.
- Carregamento: cada tela baixa só as próprias imagens e prepara a próxima tela provável, já considerando as respostas dadas. Na capa de um ambiente, prepara o primeiro cartão; nas referências, mantém a foto atual + as 2 seguintes; na última etapa do ambiente, prepara a capa do próximo.
- Enquanto uma foto carrega, o cartão mostra a cor média dela e as escolhas ficam bloqueadas (não dá para marcar a foto errada). Se passar de 8 s, aparecem "Tentar de novo" e "Pular esta".
- Fotos enviadas pelo escritório na Biblioteca também são salvas em WebP até 100 KB.

## 20/10/2026, 19h57 (Artifact versão 32): nova capa do Cinema
- Foto enviada pelo escritório, com leve desfoque e o mesmo degradê, em WebP (34.564 bytes). Capa anterior em `referencias/capa_cinema_antiga.jpg`.

## 20/10/2026, 20h (Artifact versão 33): foto movida da cozinha para a sala
- A primeira referência da cozinha (ambiente com poltronas e adega iluminada) saiu da cozinha e entrou na sala de estar e jantar como a 7ª foto da sequência (arquivo `sala/37`). A cozinha agora começa pela foto seguinte.

## 20/10/2026, 20h (Artifact versão 34): nova foto da Perla Santana (cozinha)
- Na pergunta "Pedra da bancada" da cozinha, a opção Perla Santana usa a foto enviada pelo escritório, recortada em 4:3 como as outras pedras, em WebP. Foto anterior em `referencias/opcao_perla_santana_antiga.jpg`.

## 20/10/2026, 20h05 (Artifact versão 35): cartão sem foto duplicada
- O cartão de referência não desenha mais uma segunda cópia desfocada da foto ao fundo. O espaço em volta da foto passa a ser a cor média dela. Menos memória e mais fluidez em celulares simples.

## 20/10/2026, 20h20 (Artifact versão 36): gerador de PDF carregado só quando precisa
- O gerador de PDF (~419 KB) saiu da página e virou o arquivo `pdf.js`, ao lado do `index_v33.html` (os dois precisam ficar juntos).
- A página caiu de 870 KB para 451 KB (comprimida, de ~264 KB para ~129 KB): a primeira tela abre com metade do peso.
- O gerador baixa em segundo plano quando o cliente chega na revisão ou na tela final, ou na hora de exportar no painel. Enquanto não chega, o botão mostra "Gerando PDF...".
- Se a internet falhar nesse momento, aparece "Não foi possível gerar" e um novo toque tenta baixar de novo.
- Testado: o PDF gerado é idêntico ao da versão anterior (4 páginas, sem nenhuma diferença de imagem ou texto).

## 20/10/2026, 20h20 (Artifact versão 37): mais uma foto da cozinha para a sala
- A 8ª referência da cozinha (sala com painel de madeira e TV) foi para a sala de estar e jantar como a 9ª foto da sequência (arquivo `sala/38`).

## 20/10/2026, 20h25 (Artifact versão 38): não volta mais ao início quando a página recarrega
- Causa: a página às vezes recarrega sozinha (no iPad, quando o Safari precisa liberar memória ou ao trocar de app; e a cada nova versão publicada). Depois disso ela abria no painel (no "Ver como cliente") ou na lista "Que bom ter vocês de volta" (no link do cliente). As respostas nunca se perdiam, só a posição.
- Agora, depois de recarregar, o briefing volta exatamente para a tela onde estava (testado: referências da sala, foto 3 → recarregar → foto 3).
- A lista "Que bom ter vocês de volta" só aparece quando o cliente volta depois de mais de 30 minutos sem mexer.

## 20/10/2026, 20h30 (Artifact versão 39): compartilhar o briefing de novo
- Na aba Briefings, ao clicar no nome do cliente (página de Respostas), há o botão "Compartilhar" (ícone de link). Ele abre o link do briefing com "Copiar", a mensagem pronta para o cliente, "Enviar no WhatsApp", "Copiar mensagem" e, no celular/iPad, "Compartilhar..." (menu de compartilhar do aparelho).
- O que o cliente já respondeu continua salvo; é o mesmo link.

## 20/10/2026, 20h40 (Artifact versão 40): ajustes para publicação e entrega ao Lucas (fim da 1ª etapa)
- Configuração única no `<head>` (`window.TRIOMA_CONFIG`): modo de teste, endereço do site, API do e-mail, WhatsApp do escritório e link da política de privacidade.
- Em modo de produção: o cliente que abre pelo link não vê o botão "Painel"; sem selo "Protótipo", sem "Restaurar exemplos" e sem clientes de exemplo.
- Aviso de privacidade na tela inicial do cliente.
- Prévia do link (título, descrição e imagem para WhatsApp) e ícones do site.
- Correção: na rota `/briefing/<código>`, imagens e gerador de PDF agora carregam da raiz do site (`<base href="/">`).
- Correção: abrir o link do cliente e depois voltar para o painel não reabre mais o cliente.
- O Artifact continua em modo de teste. A pasta "PARA ENVIAR PRO LUCAS" tem o zip de hospedagem (modo de produção), o LEIA-ME (.md e .html) e os artefatos do projeto.
