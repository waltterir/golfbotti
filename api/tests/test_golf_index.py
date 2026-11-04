from app.golf_index import wind_score, temp_score

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
    