class Solution:
    def permute(self, nums):
        perms = [[]]   
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm)+1):   
                    new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
                    print(new_perms)
            perms = new_perms
        return perms

        