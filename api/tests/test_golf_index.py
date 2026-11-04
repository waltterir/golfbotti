from app.golf_index import wind_score, temp_score, rain_score

def test_golf_index_import():
    assert True

def test_wind_score():
    assert wind_score(3.5) == 10
    assert wind_score(6.5) == 8
    assert wind_score(8.5) == 5
    assert wind_score(10.5) == 3
    assert wind_score(11) == 0

def test_temp_score():
    assert temp_score(-5) == 0
    assert temp_score(3.5) == 0
    assert temp_score(5.5) == 3
    assert temp_score(11.5) == 6
    assert temp_score(17.5) == 8
    assert temp_score(26) == 10

def test_rain_score():
    assert rain_score(0.0) == 10
    assert rain_score(0.5) == 10
    assert rain_score(1) == 3
    assert rain_score(1.1) == 0
    assert rain_score(2) == 0