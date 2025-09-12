class solution:
    def TwoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, x in enumerate(list):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        return []
