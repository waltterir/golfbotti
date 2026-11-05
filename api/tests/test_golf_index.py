import pytest

from app.golf_index import wind_score, temp_score, rain_score, calculate_index, window_index


@pytest.mark.parametrize("wind, expected", [
    (0.0, 10),
    (2.5, 10),   # raja
    (2.6, 8),
    (5.5, 8),    # raja
    (5.6, 5),
    (7.5, 5),    # raja
    (7.6, 3),
    (8.5, 3),    # raja: viimeinen pelattava
    (8.6, 0),
    (15.0, 0),
])
def test_wind_score(wind, expected):
    assert wind_score(wind) == expected


@pytest.mark.parametrize("temp, expected", [
    (-5.0, 0),   # pakkanen
    (9.5, 0),    # raja
    (9.6, 5),
    (13.5, 5),   # raja
    (13.6, 8),
    (17.5, 8),   # raja
    (17.6, 10),
    (23.5, 10),  # raja
    (23.6, 7),
    (28.5, 7),   # raja: viimeinen pelattava
    (28.6, 0),
    (32.0, 0),   # helle
])
def test_temp_score(temp, expected):
    assert temp_score(temp) == expected


@pytest.mark.parametrize("rain, expected", [
    (0.0, 10),   # pouta
    (0.1, 10),   # raja
    (0.2, 5),    # tihku
    (0.3, 5),    # raja
    (0.4, 0),
    (2.0, 0),    # sade
])
def test_rain_score(rain, expected):
    assert rain_score(rain) == expected


@pytest.mark.parametrize("wind, temp, rain, expected", [
    (1.0, 20.0, 0.0, 10), 
    (12.0, 20.0, 0.0, 0),
    (4.0, 12.0, 0.2, 6.2),
    (1.0, 26.0, 0.0, 9.4)
])
def test_calculate_index(wind, temp, rain, expected):
    assert calculate_index(wind, temp, rain) == pytest.approx(expected)

PERFECT = {"wind": 2.0, "temp": 18.0, "rain": 0.0}
RAINY = {"wind": 2.0, "temp": 18.0, "rain": 1.0}
WINDY = {"wind": 9.0, "temp": 18.0, "rain": 0.0}
COLD = {"wind": 2.0, "temp": 0.0, "rain": 0.0}
MEDIOCRE = {"wind": 4.0, "temp": 12.0, "rain": 0.2}

def make_hour(hour: int, weather: dict) -> dict:
    result = {"hour": hour, **weather}
    return result

def test_window_all_perfect():
    hours = [make_hour(8, PERFECT), make_hour(9, PERFECT), make_hour(10, PERFECT), make_hour(11, PERFECT)]
    assert window_index(hours, 8, 12) == 10.0
