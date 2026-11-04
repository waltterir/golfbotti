WIND_LOW_MAX = 3.5
WIND_MID_MAX = 6.5
WIND_HIGH_MAX = 8.5
WIND_FINAL_MAX = 10.5

TEMP_LOW_MAX = 3.5
TEMP_LOWMID_MAX = 5.5
TEMP_MID_MAX = 11.5
TEMP_HIGHMID_MAX = 17.5

RAIN_LOW_MAX = 0.5
RAIN_MID_MAX = 1.0


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

def temp_score(temp: float) -> int: 
    if temp <= TEMP_LOW_MAX:
        return 0
    elif temp <= TEMP_LOWMID_MAX:
        return 3
    elif temp <= TEMP_MID_MAX:
        return 6
    elif temp <= TEMP_HIGHMID_MAX:
        return 8
    else: 
        return 10

def rain_score(rain: float) -> int:
    if rain <= RAIN_LOW_MAX:
        return 10
    elif rain <= RAIN_MID_MAX:
        return 3
    else: 
        return 0