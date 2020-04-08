import pytest
import os
import subprocess

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


@pytest.mark.parametrize("number", [1, 2, 3, 4])
def test_converter(number):
    """Generic test for the converter exercises"""
    run_exercise("converter{}.py".format(number))
    oname = "converted{}.dat".format(number)
    assert os.path.exists(os.path.join(ex_dir, oname))
    import numpy as np
    got = np.loadtxt(os.path.join(ex_dir, oname), dtype='float')
    exp = np.loadtxt(os.path.join(cheat_dir, oname), dtype='float')
    assert np.allclose(got, exp, rtol=1e-3)


@pytest.mark.parametrize("name",
                         ["warmup1.py",
                          "warmup2.py",
                          "algebra1.py",
                          "matplot1.py",
                          "equation1.py",
                          "fitting1.py",
                          ])
def test_smoke_run(name):
    run_exercise(name)

