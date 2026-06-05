class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            length = len(string)
            encoded_string += f"{length}#{string}"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        def get_string_length(s: str, curr_idx: int) -> tuple[int, int]:
            length = ""
            while curr_idx < len(s) and s[curr_idx] != "#":
                length += s[curr_idx]
                curr_idx += 1
            return int(length), curr_idx + 1
        
        curr_idx = 0
        n = len(s)
        strs = []
        while curr_idx < n:
            length, curr_idx = get_string_length(s, curr_idx)
            strs.append(s[curr_idx: curr_idx + length])
            curr_idx = curr_idx + length
        return strs


            