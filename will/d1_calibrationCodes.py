
def determineCalibrationCodesPt1(lines):
    res = []
    for l in lines:
        cc = ""
        for c in l:
            ascii = ord(c)
            if (ascii > 47 and ascii < 58):
                # it's a digit!
                cc += c
        # this will work for single char or many
        cc = int(cc[0]+cc[-1])
        res.append(cc)
    return sum(res)

def determineCalibrationCodesPt2(lines):
    res = []
    res2 = 0
    written_nums = {"one":"1",
                    "two":"2",
                    "three":"3",
                    "four":"4",
                    "five":"5",
                    "six":"6",
                    "seven":"7",
                    "eight":"8",
                    "nine":"9"}
    for l in lines:
        cc = ""
        # checkr is LEFT index of string start
        checkr = 0
        for idx, c in enumerate(l):
            ascii = ord(c)
            if ascii == 10:
                break
            if (ascii > 47 and ascii < 58):
                # it's a digit!
                cc += c
                checkr = idx + 1
            else:
                curr_end = idx+1 if idx < (len(l)-1) else None
                if idx - checkr >= 2:
                    sub_checkr = l[checkr:curr_end][-3:]
                    if sub_checkr in written_nums:
                        cc += written_nums[sub_checkr]

                        continue
                    if idx - checkr >= 3:
                        sub_checkr = l[checkr:curr_end][-4:]
                        if sub_checkr in written_nums:
                            cc += written_nums[sub_checkr]

                            continue
                    if idx - checkr >= 4:
                        sub_checkr = l[checkr:curr_end][-5:]
                        if sub_checkr in written_nums:
                            cc += written_nums[sub_checkr]

                            continue
        # this will work for single char or many
        cc = int(cc[0]+cc[-1])
        res.append(cc)
        res2 += cc
    return sum(res)
    
with open('/Users/williamhbelew/Hacking/AoC_2023/puzzle_inputs/d1_strings.txt') as f:
    lines = f.readlines()
    print(determineCalibrationCodesPt2(lines))