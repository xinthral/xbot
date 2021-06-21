import re
from pprint import pprint as pp

slFile = list[str]
kvSymbol = dict[str, int]

SYMBOLS = dict()
RGX = r"(?<=\(\(\'(\W))"

def getLog(fileName: str) -> slFile:
    with open(fileName, 'r') as f:
        outFile = f.readlines()
    return(outFile)

def chkRecord(symbol: str) -> None:
    global SYMBOLS
    if ( symbol not in SYMBOLS.keys() ):
        SYMBOLS[symbol] = 1
    else:
        SYMBOLS[symbol] += 1

def parseRecords(records: slFile) -> None:
    test_str = '\n'.join(records)
    regex = RGX
    matches = re.finditer(regex, test_str, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            symb = match.group(groupNum)
            chkRecord(symb)

def main() -> None:
    logFile = getLog('logs/master.log')
    parseRecords(logFile)
    pp(SYMBOLS)

if __name__ == '__main__':
    main()
