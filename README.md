# Combat Simulator

Um mini-jogo de RPG de texto, criado em Python puro, onde um herói customizável enfrenta um vilão pré-definido. O jogo utiliza uma mecânica de turnos e probabilidades para determinar o vencedor da batalha, oferecendo ao jogador opções de ataque, defesa e fuga.

Este projeto foi desenvolvido como um exercício prático para aplicar os conceitos fundamentais de lógica de programação e estrutura de dados.

## Tecnologias Utilizadas

* Python 3
* Biblioteca nativa: `random`

### Como Rodar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone [https://github.com/Silea-dev/combat_simulator.git](https://github.com/Silea-dev/combat_simulator.git)
   ```
2. **Navegue até a pasta do projeto:**

   ```bash
   cd combat_simulator
   ```
3. **(Opcional, mas recomendado) Crie e ative um ambiente virtual:**

   ```bash
   # Criar o ambiente
   python -m venv .venv

   # Ativar no Windows
   .\.venv\Scripts\activate

   # Ativar no Linux/macOS
   source .venv/bin/activate
   ```
4. **Execute o jogo:**

   ```bash
   python main.py
   ```

## Conceitos Praticados

Este projeto foi um campo de testes para aplicar e solidificar os seguintes conceitos fundamentais de programação e engenharia de software:

* **Estrutura de Repetição (`while`):**
  Utilizada para controlar o fluxo principal da batalha, que continua executando turno após turno enquanto ambos os combatentes estiverem vivos.
* **Estrutura de Decisão (`if/elif/else`):**
  Usada para processar as escolhas do jogador (Atacar, Defender, Fugir) e para determinar os resultados aleatórios de cada ação, criando diferentes desfechos.
* **Estrutura de Dados Heterogênea (Dicionários):**
  Os personagens Herói e Vilão são modelados como "Registros", utilizando dicionários para agrupar seus diferentes atributos (nome, vida, ataque, defesa) em uma única entidade.
* **Modularização de Código:**
  O código é organizado com uma clara "Separação de Responsabilidades", onde `main.py` cuida da inicialização e da interação com o usuário, enquanto `core.py` contém toda a lógica e as regras do jogo.
* **Funções e Passagem de Parâmetros:**
  A lógica principal é encapsulada na função `game()`, que recebe os dados dos combatentes como parâmetros, tornando o código reutilizável e fácil de testar.

## Atualizações:

### Atualização

Um novo paradigma, foi adicionado uma `Ficha de Personagem` ao jogo! (13/09/2025)

``Versão: V1.1.0``

### Atualização

Adiconado sistema de escolha de classes! (17/09/2025)

``Versão: V2.0``

### Atualização

Lançando aplicativo ``.exe``

``Versão V2.1.1``

## Lore (atualização V2.1.0)

``Lore: A história se passa em um mundo paralelo, onde seus status social é definido por sua capacidade de controlar itens chamados de "Peças do tabuleiro real". Nosso prota (1/prodígio), ao se perceber neste mundo, percebe que essas peças lembram muito o jogo que muito gostava em seu antigo mundo, xadrez. Este, planeja usar suas habilidades para tentar sobreviver neste novo mundo.``

## Licenciamento

O código-fonte deste projeto é licenciado sob a  **Licença MIT** , conforme detalhado no arquivo `LICENSE`.

Todos os ativos criativos, incluindo, mas não se limitando a, a história, nomes de personagens, diálogos e descrições do universo, são propriedade intelectual de Isaías Eloy (Silea) e estão protegidos por  **copyright (Todos os Direitos Reservados)** . A reutilização destes ativos em outros projetos requer permissão explícita.
