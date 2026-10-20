# Briefing Trioma

Lucas, este é o pacote da primeira etapa do briefing de interiores da Trioma. Ele substitui o PDF de 40 a 60 páginas por uma página interativa. O escritório monta o briefing de cada cliente e envia um link. O cliente arrasta fotos de referência (gosto / não gosto / neutro) e responde perguntas pelo celular, iPad ou computador. No fim, o escritório vê um relatório com o perfil de estilo e exporta um PDF.

Data: 20/10/2026.

---

## 1. O que tem neste repositório

| Pasta | O que é |
|---|---|
| `site/` | **Arquivos para hospedar o site** (modo de produção). Publique o conteúdo desta pasta na raiz do domínio (ver seção 3). Com `modoTeste: true` na configuração, ele vira a versão de demonstração, com clientes de exemplo. |
| `docs/` | Este guia em HTML, histórico de todas as mudanças (`ATUALIZACOES.md`), catálogo de ambientes e perguntas, contexto completo do projeto e manifesto. |
| `dados/` | Catálogo de ambientes em JSON e clientes de exemplo, que mostram o formato dos dados. |
| `codigo_legivel/` | O script e o CSS da build formatados para leitura. |
| `servidor/notify.py` | Rota FastAPI que envia o PDF por e-mail quando o cliente conclui. |
| `relatorios/` | Planilha de otimização de imagens, peso de cada imagem (`PESOS_IMAGENS.csv`) e um PDF de exemplo gerado pelo sistema. |
| `capturas_de_tela/` | Telas do celular, do iPad e do painel. São da versão de 14/10: a estrutura é a mesma, mas as fotos de referência e as capas mudaram depois. |

As fotos originais escolhidas pelo escritório (JPG) não estão no repositório. As usadas no site já estão convertidas em `site/img/`.

---

## 2. Situação atual: leia antes de publicar

**A interface está pronta e testada. O que falta é o servidor.** Hoje todos os dados ficam no `localStorage` do navegador de quem usa:

- O briefing que o escritório monta no painel fica só no aparelho do escritório.
- Quando o cliente abrir o link no celular dele, vai ver **"Briefing não encontrado"**, porque aquele navegador não tem os dados.
- As respostas do cliente também ficam só no aparelho dele.

**Publicar a pasta `site/` como está serve para testar no próprio aparelho, mas ainda não para atender clientes.**

### O que precisa existir no servidor

1. **Banco de dados e API** para:
   - salvar e listar os briefings (clientes, ambientes escolhidos, personalizações);
   - entregar um briefing pelo código do link;
   - receber e salvar as respostas do cliente.
2. **Login no painel.** Hoje qualquer pessoa que abrir a raiz do site entra no painel.
3. **Armazenamento das fotos que o escritório sobe pela Biblioteca.** Hoje elas ficam no IndexedDB do aparelho (banco `trioma-briefing`, tabela `images`).
4. **E-mail automático:** a rota de `servidor/notify.py`, com conta SMTP. Destinatários padrão: `levybezerradomingos00@gmail.com` e `pbstudioarq@gmail.com`.

### Onde ligar o front na API

Só existe a **build compilada** (um único `index.html` com o JavaScript minificado). O código-fonte original em React/TypeScript se perdeu em sessões anteriores. Dá para integrar editando a build em poucos pontos, que estão nomeados para facilitar a busca:

| Função na build | O que faz hoje | O que trocar |
|---|---|---|
| `function Zw()` | Lê todo o estado do `localStorage` (chave `trioma-briefing:v2`). | No **painel**: `GET` dos briefings do escritório. No **link do cliente**: `GET /briefings/<codigo>`, que devolve o briefing, a biblioteca e as respostas. |
| `function Kw(e)` | Salva todo o estado no `localStorage` a cada mudança. | `PUT` das respostas (cliente) ou do briefing (painel). Vale salvar com intervalo de ~1 s, para não chamar a API a cada toque. |
| `function zzNotify(e,t)` | Gera o PDF e faz `POST {apiUrl}/briefings/{token}/concluido` quando o cliente conclui. | Já pronto. Só precisa do `apiUrl` na configuração e da rota do `notify.py`. |
| `t6()` / `n6()` (IndexedDB) | Guardam as fotos que o escritório sobe. | Upload para o servidor e uso da URL retornada. |

O formato do estado está em `dados/clientes_exemplo_v32.json`:
- `clients[]`: cada cliente com `token`, `environments[]`, `hiddenImages` e `hiddenQuestions`;
- `responses{}`: por cliente, com `swipes`, `answers`, `notes`, `step`, `startedAt` e `completedAt`;
- `library{}`: personalizações da Biblioteca.

Se for mais simples, outra opção é **reconstruir o projeto Vite** a partir da build, do catálogo (`dados/`) e das capturas de tela. A stack combinada no início foi React + TypeScript + Vite no front e FastAPI + SQLAlchemy no backend.

---

## 3. Como hospedar

### 3.1 Conteúdo

```
index.html            página única (painel + briefing do cliente)
pdf.js                gerador de PDF, carregado só quando precisa (~419 KB)
img/                  358 imagens WebP (todas abaixo de 100 KB) + og.jpg (prévia do link)
favicon-32.png, icon-512.png, apple-touch-icon.png
_redirects, _headers  regras para Netlify / Cloudflare Pages
.htaccess             as mesmas regras para Apache
```

O total é de cerca de 25 MB. Tudo é estático: não há build nem dependências. (Na pasta do Lucas, o mesmo conteúdo vai como `briefing-trioma-site.zip`.)

### 3.2 Configuração: um único bloco no `<head>` do `index.html`

```js
window.TRIOMA_CONFIG = {
  modoTeste: false,                 // true = clientes de exemplo, selo "Protótipo" e botão "Painel" no link do cliente
  siteUrl: "https://SEU-DOMINIO",   // monta o link do cliente: <siteUrl>/briefing/<codigo>
  apiUrl: "",                       // endereço da API; vazio = não envia o PDF por e-mail
  whatsappEscritorio: "",           // só números com DDI; vazio = o WhatsApp abre para escolher contato ou grupo
  politicaPrivacidadeUrl: ""        // aparece na tela inicial do cliente
};
```

Também no `<head>`:
- troque `SEU-DOMINIO` em `og:image` pelo domínio real. É a foto que aparece na prévia do link no WhatsApp, e precisa ser um endereço completo;
- `<base href="/">` diz em que pasta o site está. Se ficar numa subpasta, ajuste (ex.: `/briefing-app/`).

### 3.3 Regras do servidor (obrigatórias)

- **`/briefing/<codigo>` deve abrir o `index.html`.** O código do link é lido pelo próprio endereço. Os arquivos `_redirects` e `.htaccess` já fazem isso.
- **Tipo dos arquivos:** sirva `.webp` como `image/webp` e `.js` como `text/javascript`. O `pdf.js` é carregado com `import()` e precisa vir do mesmo domínio.
- **Cache longo** para `img/` e `pdf.js`, e `no-cache` no `index.html`. Já está no `_headers` e no `.htaccess`.
- **Compressão (gzip/brotli):** o `index.html` cai de 451 KB para ~129 KB.

### 3.4 Testar localmente

Abra o `index.html` por um servidor local, porque o `pdf.js` não carrega direto do disco:

```
cd site
python -m http.server 8000
```

Depois acesse `http://localhost:8000`. Para testar a rota `/briefing/<codigo>` localmente é preciso um servidor com a regra de reescrita. Sem ela, use `http://localhost:8000/#b-<codigo>`, que também funciona.

---

## 4. O que já foi feito e testado nesta etapa

- **Fotos de referência do escritório** em 13 ambientes. As fotos antigas continuam na Biblioteca, mas desligadas por padrão. No Closet master ficam as duas.
- **Lavabo unificado**, com a escolha Interno ou Externo ao montar o briefing.
- **Imagens em WebP** abaixo de 100 KB: de 52,6 MB para 24,0 MB. Detalhes em `relatorios/`.
- **Carregamento por etapa:** cada tela baixa só as próprias imagens e prepara a próxima tela provável, já considerando as respostas. Nas referências fica pronta a foto atual + 2.
- **Rede lenta:**
  - o cartão mostra a cor média da foto enquanto ela carrega;
  - não deixa escolher antes de a foto aparecer;
  - depois de 8 s oferece "Tentar de novo" ou "Pular esta".
- **Gerador de PDF separado** (`pdf.js`). A página abre com metade do peso. O PDF gerado é idêntico ao da versão anterior.
- **Recarregar a página volta para a mesma tela.** O Safari do iPad recarrega quando falta memória. A lista "Que bom ter vocês de volta" só aparece depois de 30 minutos parado.
- **Botão "Compartilhar"** na página de respostas do cliente, para reenviar o link.
- **Modo de produção:**
  - no link do cliente não aparece o botão "Painel";
  - sem selo de protótipo e sem clientes de exemplo;
  - aviso de privacidade na tela inicial do cliente;
  - prévia do link com título, descrição e foto, e ícones do site.

Todos esses itens foram testados em navegador simulando celular, iPad e computador, inclusive com rede lenta. **O teste em aparelho físico e no domínio real ainda precisa ser feito.**

---

## 5. Checklist antes de abrir para clientes

- [ ] API e banco ligados em `Zw` / `Kw` (seção 2)
- [ ] Login no painel
- [ ] Upload das fotos da Biblioteca para o servidor
- [ ] `siteUrl`, `og:image` e `<base href>` com o domínio real
- [ ] `apiUrl` + SMTP do `notify.py` (e-mail com o PDF)
- [ ] Política de privacidade publicada e `politicaPrivacidadeUrl` preenchida (LGPD: o briefing coleta rotina, composição da família e pets)
- [ ] Regras de `/briefing/*`, cache e compressão ativas no servidor
- [ ] Teste completo num iPhone e num iPad reais: abrir o link, responder, concluir e baixar o PDF

## 6. Pendências de conteúdo (não impedem a publicação)

- Botão "Editar texto"
- Separar as páginas dos banheiros
- Pergunta de Organização na cozinha
- "Para dormir" na suíte master
- Trocar "Os dois" por "Ambos"
