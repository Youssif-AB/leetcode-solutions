class Solution(object):
    def compress(self, chars):
        current_letter = chars[0]
        amount = 0
        i = 0
        while i < len(chars):
            if chars[i] == current_letter:
                amount += 1

                if amount > 1:
                    chars.pop(i)
                    i -= 1

            else:
                current_letter = chars[i]
                if amount > 1:
                    if amount > 9:
                        for j in str(amount):
                            chars.insert(i, j)
                            i += 1
                    else:
                        chars.insert(i, str(amount))
                        i += 1
            
                amount = 0
                i -= 1
            i += 1


        if amount > 1:
            if amount > 9:
                for j in str(amount):
                    chars.append(j)
            else:
                chars.append(str(amount))

        return (len(chars)) 
        