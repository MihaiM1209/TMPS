import json
from client.player import Player
from domain.command import *
from domain.strategy import *

class GameManager:
    def __init__(self, player_file='Lab3/data/player.json', story_file='Lab3/data/story_state.json'):
        try:
            self.player = Player.load(player_file)
        except Exception as e:
            self.player = Player()
        self.story_file = story_file
        self.current_chapter = None

    def load_story(self):
        with open(self.story_file, 'r') as f:
            self.story_data = json.load(f)

    def start_game(self):
        self.load_story()
        print("Welcome to The Whispering Wasteland!")
        self.play_chapter("Chapter 1")

    def play_chapter(self, chapter_name):
        # ENDING handler (clear ending)
        if chapter_name == "ENDING":
            print("\n*** GAME OVER ***")
            print("You finished the game!")
            return
        self.current_chapter = self.story_data[chapter_name]
        print(f"--- {self.current_chapter['title']} ---")
        print(self.current_chapter['description'])
        print(f"\nStats: HP={self.player.hp}, Hunger={self.player.hunger}, Thirst={self.player.thirst}, Money={self.player.money}")
        print(f"Inventory: {self.player.inventory}")
        for idx, choice in enumerate(self.current_chapter['choices'], 1):
            print(f"{idx}. {choice['text']}")
        while True:
            try:
                choice_idx = int(input("Choose an option: ")) - 1
                if 0 <= choice_idx < len(self.current_chapter['choices']):
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a valid number.")
        result = self.execute_choice(self.current_chapter['choices'][choice_idx])
        # Autosave after every choice
        self.player.save('Lab3/data/player.json')
        if result.get("next_chapter"):
            self.play_chapter(result["next_chapter"])

    def execute_choice(self, choice):
        print(choice['result']['description'])
        # Handle stat/inventory updates
        updates = choice['result'].get('updates', {})
        for key, value in updates.items():
            if key == 'items' or key == 'item':
                items = value if isinstance(value, list) else [value]
                for item in items:
                    self.player.add_item(item)
            elif hasattr(self.player, key):
                setattr(self.player, key, getattr(self.player, key) + value)
            # else: ignore silently
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
            elif command_data['type'] == 'rest':
                command = RestCommand(command_data.get('stamina_gain', 10))
            elif command_data['type'] == 'hide':
                command = HideCommand(command_data.get('stamina_loss', 5), command_data.get('item_found'))
            else:
                print(f"Unknown command type: {command_data['type']}")
                return {}
            if command:
                command.execute(self.player)
        return choice['result']
