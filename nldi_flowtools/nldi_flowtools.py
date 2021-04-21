from flowtrace import Flowtrace
from splitcatchment import SplitCatchment


def splitcatchment(lon, lat, boolean):
    results = SplitCatchment(lon, lat, boolean)
    results = results.serialize()
    return results


def flowtrace(lon, lat, boolean, direction):
    results = Flowtrace(lon, lat, boolean, direction)
    results = results.serialize()
    print('flowtools.py results: ', results)
    return results
