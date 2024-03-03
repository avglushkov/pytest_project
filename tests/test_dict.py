from utils import dicts

def test_dicts():
    assert dicts.get_val({"vcs":"mercurial"}, "vcs", "git") == "mercurial"
    assert dicts.get_val({"vcs": "mercurial"}, "wcs", "git") == "git"
    assert dicts.get_val({}, "wcs", "git") == "git"
    assert dicts.get_val({}, "wcs", "bazaar") == "bazaar"
