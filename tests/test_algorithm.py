from src.algorithm import core_algorithm, validate_input, ImprocResult

def test_core_algorithm_basic():
    data = {"nodes": ["A","B"], "edges": [["A","B",1]]}
    res = core_algorithm(data, seed=7)
    assert isinstance(res, ImprocResult)
    assert "acc" in res.result

def test_validate_input():
    try:
        validate_input(None)
        assert False, "should have raised"
    except ValueError:
        assert True
