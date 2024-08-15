class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = b.zfill(len(a))
        elif len(b) > len(a):
            a = a.zfill(len(b))

        aa = a[::-1]
        bb = b[::-1]
        returned = []
        remainder = 0

        for i in range(len(aa)):
            if int(aa[i]) + int(bb[i]) + remainder == 3:
                returned.append("1")
                remainder = 1
            elif int(aa[i]) + int(bb[i]) + remainder == 2:
                returned.append("0")
                remainder = 1
            elif int(aa[i]) + int(bb[i]) + remainder == 1:
                returned.append("1")
                remainder = 0
            else:
                returned.append("0")
                remainder = 0
        if remainder == 1:
            returned.append("1")

        return "".join(returned[::-1])