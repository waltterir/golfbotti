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

# --- Painot (yhteensä 1.0) ---
# Tuuli ja sade pilaavat kierroksen eniten (kaverien palaute)
WEIGHT_WIND = 0.4
WEIGHT_TEMP = 0.2
WEIGHT_RAIN = 0.4

# --- Aikaikkunat ---
TIME_WINDOWS = {"morning": (8, 12), "day": (12, 16), "evening": (16, 20)}


# --- Lasketaan tuuli pisteet --- 
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

# --- Lasketaan lämpötila pisteet --- 
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

# --- Lasketaan Sade pisteet --- 
def rain_score(rain: float) -> int:
    if rain <= RAIN_DRY_MAX:
        return 10
    elif rain <= RAIN_DRIZZLE_MAX:
        return 5
    else:
        return 0

# --- Lasketaan indexi kaikille kolmelle säälle ---
def calculate_index(wind: float, temp: float, rain: float) -> float:
    wind_points = wind_score(wind)
    temp_points = temp_score(temp)
    rain_points = rain_score(rain)

    points_list = [wind_points, temp_points, rain_points]
    if 0 in points_list:
        return 0.0
    sum_points = wind_points * WEIGHT_WIND + temp_points * WEIGHT_TEMP + rain_points * WEIGHT_RAIN
    return sum_points

# --- Lasketaan ikkuna Index --- 
def window_index(hours: list[dict], start: int, end: int) -> float:
    hour_indexes = []
    for h in hours:
        if start <= h["hour"] < end:
            hour_index = calculate_index(h["wind"], h["temp"], h["rain"])
            hour_indexes.append(hour_index)
    if not hour_indexes:
        return 0.0
    return sum(hour_indexes) / len(hour_indexes)