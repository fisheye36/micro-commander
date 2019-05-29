from decorators import settings
from analyser import Analyser



DUMMY_SETTINGS = {'magicWords' : {'dosłownie' : 1}}


@settings(DUMMY_SETTINGS)
def test_shouldReturnCorrectList():
    a = Analyser()
    a.analyse("dosłownie dosłownie")
    assert ["dosłownie"] == a.getFinalCommand()

@settings(DUMMY_SETTINGS)
def test_shouldReturnCorrfdfsdfdsectList():
    a = Analyser()
    a.analyse("dosłownie dosłownie dosłownie dosłownie")
    assert ["dosłownie", "dosłownie"] == a.getFinalCommand()