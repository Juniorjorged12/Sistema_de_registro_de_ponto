# Sistema de Registro de Funcionários e Ponto

Este projeto é um sistema desenvolvido em **Django** para gerenciar funcionários e controlar o registro de ponto (entrada e saída) através de uma senha numérica.  
O foco principal foi o **backend**, garantindo regras de negócio sólidas e persistência correta dos dados.  
O **frontend** é propositalmente simples, utilizando apenas HTML básico, já que o objetivo era demonstrar a lógica e não a estética.

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

---
