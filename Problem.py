from typing import List, str

class Problem:
    def __init__(self, name: str, difficulty: str):
        self.name = name
        self.problem_difficulty = difficulty
        self.key_data_structures = []
        self.key_algorithms = []
        self.hint = ""
    
    def add_data_structure(self, data_structure: str):
        self.key_data_structures.append(data_structure)
        
    def add_algorithm(self, algorithm: str):
        self.key_algorithms.append(algorithm)
    
    def set_hint(self, hint: str):
        self.hint = hint
    
    
    


def main():
    problem1 = Problem("Two Sum", "Easy")
    problem1.print_info()

if __name__ == "__main__":
    main()