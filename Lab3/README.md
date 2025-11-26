# Behavioral Design Patterns

This project focuses on learning and applying **Behavioral Design Patterns** in the development of a terminal-based interactive story game. The goal was to learn how these patterns, specifically the **Strategy and Command** patterns, can be used to manage complex behaviors and actions in a game. By implementing these patterns, I aimed to enhance the game's flexibility, scalability, and maintainability, while also gaining hands-on experience in applying design patterns to real-world software development scenarios.

## Project Status

This project is a **work in progress**. The game is not yet finished but includes foundational mechanics, including combat strategies and command-based player actions, which are highlighted below.

---

## Design Pattern Implementations

### 1. Strategy Pattern

The **Strategy Pattern** is used to define various combat strategies that players can choose during battles. Each strategy implements a specific behavior, allowing the player to adapt to different combat scenarios. This pattern is implemented through the following classes:

- **`CombatStrategy`**: The abstract base class for all combat strategies.
- **`AggressiveStrategy`**: Prioritizes inflicting maximum damage on the enemy.
- **`DefensiveStrategy`**: Focuses on reducing incoming damage.
- **`BalancedStrategy`**: Strikes a balance between offense and defense.

#### Example Code:
```python
class CombatStrategy:
    def execute(self, player, enemy):
        pass

class AggressiveStrategy(CombatStrategy):
    def execute(self, player, enemy):
        damage = 15
        enemy['hp'] -= damage
        print(f"Player attacks aggressively for {damage} damage!")

class DefensiveStrategy(CombatStrategy):
    def execute(self, player, enemy):
        reduced_damage = max(0, enemy['attack'] - 5)
        player.hp -= reduced_damage
        print(f"Player defends, reducing damage to {reduced_damage}.")

class BalancedStrategy(CombatStrategy):
    def execute(self, player, enemy):
        damage = 10
        enemy['hp'] -= damage
        player.hp -= enemy['attack'] // 2
        print(f"Player trades blows for {damage} damage.")

```

### 2. Command Pattern

The **Command Pattern** encapsulates player actions as objects, making it easier to manage and extend game commands. Each command defines a specific action, such as searching for items, trading, resting, or engaging in combat. The following commands have been implemented:

- **`SearchCommand`**: Allows players to search for and collect items.
- **`FightCommand`**: Engages the player in combat using a specified combat strategy.
- **`TradeCommand`**: Facilitates trading items with NPCs.
- **`RestCommand`**: Restores player stamina.
- **`HideCommand`**: Reduces stamina in exchange for staying hidden and possibly discovering items.

#### Example Code:
```python
class Command:
    def execute(self, player):
        pass

class SearchCommand(Command):
    def __init__(self, items_found):
        self.items_found = items_found

    def execute(self, player):
        player.inventory.extend(self.items_found)
        print(f"Found: {', '.join(self.items_found)}")
        player.hunger += 20
        player.thirst += 10

class FightCommand(Command):
    def __init__(self, enemy_name, enemy_hp, enemy_attack, combat_strategy):
        self.enemy = {"name": enemy_name, "hp": enemy_hp, "attack": enemy_attack}
        self.combat_strategy = combat_strategy

    def execute(self, player):
        print(f"Engaging in combat with {self.enemy['name']} (HP: {self.enemy['hp']}, Attack: {self.enemy['attack']})")
        
        self.combat_strategy.execute(player, self.enemy)
        
        if self.enemy["hp"] <= 0:
            print(f"You defeated {self.enemy['name']}!")
        elif player.hp <= 0:
            print("You have been defeated!")
        else:
            print(f"Combat continues. Enemy HP: {self.enemy['hp']}, Player HP: {player.hp}")

```
The **`FightCommand`** incorporates the **Strategy Pattern** by utilizing a combat strategy ( aggressive, defensive, or balanced ) during execution. This combination demonstrates how behavioral patterns can be integrated to create modular, reusable code.

### Integration with Game Logic

The game logic, located in **`game_manager.py`**, connects player choices to the corresponding **commands and strategies**. The **`execute_choice`** function parses the player's input and dynamically selects the appropriate command or strategy.

#### Example Code:
```python
    def execute_choice(self, choice):
        print(choice['result']['description'])

        if 'command' in choice['result']:
            command_data = choice['result']['command']
            command = None

            if command_data['type'] == 'search':
                command = SearchCommand(command_data['items_found'])
            elif command_data['type'] == 'trade':
                command = TradeCommand(command_data['item'], command_data.get('price', 0))
            elif command_data['type'] == 'combat':
                
                combat_type = command_data['combat_type']
                if combat_type == 'aggressive':
                    strategy = AggressiveStrategy()
                elif combat_type == 'defensive':
                    strategy = DefensiveStrategy()
                elif combat_type == 'balanced':
                    strategy = BalancedStrategy()
                else:
                    print(f"Unknown combat type: {combat_type}")
                    return {}

                command = FightCommand(
                    enemy_name=command_data['enemy'],
                    enemy_hp=command_data.get('enemy_hp', 50),
                    enemy_attack=command_data.get('enemy_attack', 10),
                    combat_strategy=strategy
                )
            else:
                print(f"Unknown command type: {command_data['type']}")
                return {}

            if command:
                command.execute(self.player)

        return choice['result']
```

The **`execute_choice`** function demonstrates how commands and strategies are tied to gameplay. For example, a player's choice to engage in combat dynamically selects a CombatStrategy and executes a **FightCommand**.

## Conclusion:

In conclusion, this laboratory work has been a valuable learning experience in applying Behavioral Design Patterns. Through the **Strategy Pattern**, I was able to create flexible combat systems, allowing players to choose their approach based on different strategies. The **Command Pattern** helped decouple game actions, making it easier to manage and extend player interactions. These patterns not only simplified the game's architecture but also provided a solid foundation for future expansions, highlighting the importance of design patterns in creating maintainable and scalable systems.