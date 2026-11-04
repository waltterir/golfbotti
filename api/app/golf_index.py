WIND_LOW_MAX = 3.5
WIND_MID_MAX = 6.5
WIND_HIGH_MAX = 8.5
WIND_FINAL_MAX = 10.5

def wind_score(wind: float) -> int: 
    if wind <= WIND_LOW_MAX:
        return 10
    elif wind <= WIND_MID_MAX:
        return 8
    elif wind <= WIND_HIGH_MAX:
        return 5
    elif wind <= WIND_FINAL_MAX:
        return 3
    else:
        return 0