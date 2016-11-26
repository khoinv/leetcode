class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        centers = {}
        tmps = {}
        maxEl = {'start': 0, 'end' : 0, 'count': 1, 'isOK': True}

        for i, c in enumerate(s):
            i = i*2
            centers[i] = {'start': i, 'end' : i, 'count': 1, 'isOK': True}

            def isOK(new_index, old_index, count):
                distance = new_index - old_index
                return count == (distance/2 + 1)

            if c in tmps:
                for k, v in enumerate(tmps[c]):
                    index = (i + v)/2
                    if(index in centers):
                        if centers[index]['isOK'] :
                            if isOK(i, v, centers[index]['count'] + 2):
                                centers[index]['count'] += 2
                                centers[index]['start'] = v
                                centers[index]['end'] = i
                                if centers[index]['count'] > maxEl['count']:
                                    maxEl = centers[index]
                            else:
                                centers[index]['isOK'] = False
                    else:
                        centers[index] = {'start':v, 'end':i, 'count': 2, 'isOK': True}
                        if centers[index]['count'] > maxEl['count']:
                            maxEl = centers[index]

            else:
                tmps[c] = []

            tmps[c].append(i)

        return s[maxEl['start'] / 2 : maxEl['end'] / 2 + 1]


def main():
    s ="civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    solution = Solution()
    print(solution.longestPalindrome(s))


if __name__ == '__main__':
    main()
