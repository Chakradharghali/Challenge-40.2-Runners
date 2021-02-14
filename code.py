def solution(start_position,speed):
    length=len(speed)
    cardinality={}
    for i in range(length):
        for j in range(1,length):
            posdiff = float(start_position[j]-start_position[i])
            speeddiff=float(speed[i]-speed[j])
            if speeddiff==0:
                continue
            _time=str(posdiff/speeddiff)
            if not _time in cardinality:
                cardinality[_time]=set()
            cardinality[_time]|={i,j}
            if len(cardinality[_time])==length:
                return length
    results=[len(p) for p in cardinality.values()]
    results.sort(reverse=True)
    if not results:
        return -1
    else:
        return results[0] if results[0]>1 else -1
