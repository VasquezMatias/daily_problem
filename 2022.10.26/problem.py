

class BiggestXOR():
    def biggest_xor(self, nums:list):
        a, b, biggest = 0, 0, 0

        for i, val_a in enumerate(nums):
            for val_b in nums[i+1:]:
                xor_val = val_a ^ val_b
                if xor_val > biggest:
                    biggest = xor_val
                    a = val_a
                    b = val_b

        return a, b, biggest



nums = [4, 7, 9, 10]

xor = BiggestXOR()
print(xor.biggest_xor(nums))