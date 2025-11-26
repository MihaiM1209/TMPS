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

class TradeCommand(Command):
    def __init__(self, item, cost):
        self.item = item
        self.cost = cost

    def execute(self, player):
        if player.money >= self.cost:
            player.money -= self.cost
            player.inventory.append(self.item)
            print(f"Traded {self.cost} credits for {self.item}.")
        else:
            print("Not enough credits to complete the trade!")


class RestCommand(Command):
    def __init__(self, stamina_gain):
        self.stamina_gain = stamina_gain

    def execute(self, player):
        player.stamina += self.stamina_gain
        print(f"Rested and gained {self.stamina_gain} stamina. Current stamina: {player.stamina}")


class HideCommand(Command):
    def __init__(self, stamina_loss, item_found=None):
        self.stamina_loss = stamina_loss
        self.item_found = item_found

    def execute(self, player):
        player.stamina -= self.stamina_loss
        print(f"Stayed hidden and lost {self.stamina_loss} stamina. Current stamina: {player.stamina}")

        if self.item_found:
            player.inventory.append(self.item_found)
            print(f"While hiding, you found: {self.item_found}")