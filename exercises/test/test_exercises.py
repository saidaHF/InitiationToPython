import pytest
import os
import subprocess
import importlib

test_dir = os.path.dirname(__file__)
ex_dir = os.path.dirname(test_dir)
cheat_dir = os.path.join(ex_dir, "cheat")


def run_exercise(name, args=()):
    """
    Runs the given exercise. It skips if the exercise file was not modified

    :param name: name of the exercise file (relative to the exercises dir)
    :param args: optional list of arguments as strings
    """
    fname = os.path.join(ex_dir, name)
    print('Running "{}"'.format(name))
    with open(fname) as f:
        r = f.read()
        if "# Write your solution here" in r:
            usercode = r.rsplit("# Write your solution here")[-1].strip()
            if not usercode:
                pytest.skip("Unmodified exercise file. Skipping")
    with open(fname + "-OUTPUT.txt", "w") as stdout:
        p = subprocess.run(
            ["python", fname] + list(args),
            stdout=stdout,
            stderr=stdout,
            cwd=ex_dir,
        )
        assert p.returncode == 0


def import_exercise(name):
    fname = os.path.join(ex_dir, name + ".py")
    print('Running "{}"'.format(name))
    with open(fname) as f:
        r = f.read()
        if "# Write your solution here" in r:
            usercode = r.rsplit("# Write your solution here")[-1].strip()
            if not usercode:
                pytest.skip("Unmodified exercise file. Skipping")
    try:
        os.chdir(ex_dir)
        m = importlib.import_module(name)
    finally:
        os.chdir(test_dir)
    return m

@pytest.mark.parametrize("number", [1, 2, 3, 4])
def test_converter(number):
    """Generic test for the converter exercises"""
    run_exercise("converter{}.py".format(number))
    oname = "converted{}.dat".format(number)
    assert os.path.exists(os.path.join(ex_dir, oname))
    import numpy as np
    got = np.loadtxt(os.path.join(ex_dir, oname), dtype='float')
    exp = np.loadtxt(os.path.join(cheat_dir, oname), dtype='float')
    np.testing.assert_allclose(got, exp, rtol=1e-3)

@pytest.mark.parametrize(
    "name",
    [
        "tsp0.dat",
        "tsp1.dat",
        "tsp2.dat",
        "tsp3",
        os.path.join(os.path.pardir, "sp8c.dat"),
    ]
)
def test_converter3_split(name):
    """test converter3.split_file()"""
    ex = import_exercise("converter3")
    h, d = ex.split_file(name)
    assert isinstance(h, str)
    assert 'GAIN' in h
    assert 'OFFSET' in h
    assert isinstance(d, list)
    assert isinstance(d[0], (int, float))


@pytest.mark.parametrize(
    "name",
    [
        "tsp0.dat",
        "tsp1.dat",
        "tsp2.dat",
        "tsp3",
        os.path.join(os.path.pardir, "sp8c.dat"),
    ]
)
def test_converter3_parse(name):
    """test converter3.parse_header()"""
    ex = import_exercise("converter3")
    with open(name) as f:
        h = f.read().split("DATA")[0]
    d = ex.parse_header(h)
    assert isinstance(d, dict)
    assert 'gain' in d
    assert 'offset' in d
    assert d['gain'] == 50
    assert d['offset'] == 1000


@pytest.mark.parametrize(
    "data,kw,t,y",
    [
        ([2, 4, 8], {"norm": 2}, [0, 1, 2], [1., 2., 4.]),
        ([2, 4, 8], {"gain": 10}, [0, 10, 20], [0.25, .5, 1]),
        ([2, 4, 8], {"offset": 100}, [100, 101, 102], [0.25, .5, 1]),
        ([0, 0, 0], {}, [0, 1, 2], [0, 0, 0]),
    ]
)
def test_converter3_write(data, kw, t, y, tmp_path):
    """Generic test for converter3.write_2columns"""
    ex = import_exercise("converter3")
    name = tmp_path / "out.dat"
    ex.write_2columns(data, name=name, **kw)
    import numpy as np
    t_out, y_out = np.loadtxt(name, dtype='float').T
    np.testing.assert_allclose(t_out, t, rtol=1e-3)
    np.testing.assert_allclose(y_out, y, rtol=1e-3)


def test_matplot1():
    run_exercise("matplot1.py")
    assert os.path.exists(os.path.join(ex_dir, "mp1.png"))
    assert os.path.exists(os.path.join(ex_dir, "mp2.png"))


def test_fitting1():
    run_exercise("fitting1.py")
    assert os.path.exists(os.path.join(ex_dir, "fit.png"))


@pytest.mark.parametrize("name",
                         ["warmup1.py",
                          "warmup2.py",
                          "algebra1.py",
                          "equation1.py",
                          ]
                         )
def test_smoke_run(name):
    run_exercise(name)

