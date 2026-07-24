# Sistema de Registro de Funcionários e Ponto

Este projeto é um sistema desenvolvido em **Django** para gerenciar funcionários e controlar o registro de ponto (entrada e saída) através de uma senha numérica.  
O foco principal foi o **backend**, garantindo regras de negócio sólidas e persistência correta dos dados.  
O **frontend** foi feito usando HTML CSS e Bootstrap, porem com o auxilio do  copilot pare melhorar e alinhas os templates.

---

## ⚙️ Ferramentas utilizadas
- **Python 3.x**
- **Django** (framework principal)
- **SQLite** (banco de dados padrão do Django, pode ser substituído por outro)
- **xhtml2pdf** (para exportar relatórios em PDF)
- **HTML básico** (templates simples, sem CSS avançado ou JavaScript complexo)

---

## 📋 Funcionalidades
- **CRUD de Funcionários**
  - Cadastro, edição, listagem e exclusão de funcionários
  - Cada funcionário possui uma senha numérica usada para registro de ponto

- **Registro de Ponto**
  - Funcionário digita sua senha
  - Se não houver ponto aberto → cria registro com data/hora de entrada
  - Se já houver ponto aberto → fecha registro com data/hora de saída
  - Mensagem exibida na tela informando a ação

- **Relatórios**
  - Relatório individual por funcionário
  - Filtro por intervalo de datas
  - Exportação para PDF com rodapé para assinatura

## 🚀 Deploy no Render

O projeto já está preparado para deploy no Render com os arquivos:
- render.yaml
- build.sh

Passos:
1. Envie o projeto para um repositório no GitHub.
2. Acesse o Render e crie um novo Web Service conectando esse repositório.
3. O Render vai usar o arquivo render.yaml automaticamente.
4. Após o deploy, a aplicação ficará disponível em uma URL do Render.

---
