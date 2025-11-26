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