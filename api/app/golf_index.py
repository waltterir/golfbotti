# Raja-arvot perustuvat 5 golfari kaverin vastauksiin (mediaanit)

# --- Tuuli (m/s): ihanne 0–2, maksimi 8 ---
WIND_PERFECT_MAX = 2.5
WIND_GOOD_MAX = 5.5
WIND_OK_MAX = 7.5
WIND_PLAYABLE_MAX = 8.5

# --- Lämpötila (°C): minimi 10, ihanne 18–23, maksimi 28 ---
TEMP_UNPLAYABLE_MAX = 9.5
TEMP_COOL_MAX = 13.5
TEMP_GOOD_MAX = 17.5
TEMP_PERFECT_MAX = 23.5
TEMP_PLAYABLE_MAX = 28.5

# --- Sade (mm/h): korkeintaan tihku ---
RAIN_DRY_MAX = 0.1
RAIN_DRIZZLE_MAX = 0.3


def wind_score(wind: float) -> int:
    if wind <= WIND_PERFECT_MAX:
        return 10
    elif wind <= WIND_GOOD_MAX:
        return 8
    elif wind <= WIND_OK_MAX:
        return 5
    elif wind <= WIND_PLAYABLE_MAX:
        return 3
    else:
        return 0


def temp_score(temp: float) -> int:
    if temp <= TEMP_UNPLAYABLE_MAX:
        return 0
    elif temp <= TEMP_COOL_MAX:
        return 5
    elif temp <= TEMP_GOOD_MAX:
        return 8
    elif temp <= TEMP_PERFECT_MAX:
        return 10
    elif temp <= TEMP_PLAYABLE_MAX:
        return 7
    else:
        return 0


def rain_score(rain: float) -> int:
    if rain <= RAIN_DRY_MAX:
        return 10
    elif rain <= RAIN_DRIZZLE_MAX:
        return 5
    else:
        return 0