"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""


def nameNumber(num):
    if num<10:
        return ["one","two","three","four","five","six","seven","eight","nine"][num-1]
    if num<20:
        return ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"][num-10]
    if num<100:
        tens = ["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"][num//10-1]
        laterPart = num%10
        if laterPart: return tens+"-"+nameNumber(laterPart)
        return tens
    if num<1000:
        laterPart = num%100
        if laterPart: return nameNumber(num//100)+" hundred and "+nameNumber(laterPart)
        return nameNumber(num//100)+" hundred"
    laterPart = num%1000
    if laterPart: return nameNumber(num//1000)+" thousand "+nameNumber(laterPart)
    return nameNumber(num//1000)+" thousand"

def countLetters(start,end):
    letters = 0
    for num in range(start,end+1):
        letters += len(nameNumber(num).replace("-","").replace(" ",""))
    return letters

print(countLetters(1,1000))