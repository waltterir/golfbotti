from app.golf_index import wind_score

def test_golf_index_import():
    assert True

def test_wind_score():
    assert wind_score(3.5) == 10
    assert wind_score(6.5) == 8
    assert wind_score(8.5) == 5
    assert wind_score(10.5) == 3
    assert wind_score(11) == 0