class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        else:
            phone = {
                "2": ["a", "b", "c"],
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"]
            }
            combinations = [""]
            for digit in digits:
                new = []
                for combination in combinations:
                    for letter in phone[digit]:
                        new.append(combination + letter)
                combinations = new
                
            return combinations