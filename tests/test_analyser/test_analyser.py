from decorators import settings
from analyser import Analyser

DUMMY_SETTINGS = {'magicWords' : {'dosłownie' : 1}}

# there will be new tests created
# these tests sucked

@settings(DUMMY_SETTINGS)
def test_shouldReturnCorrectList():
    text = "Ala ma kota"
    sut = Analyser()
    assert ["Ala", "ma", "kota"] == sut.analyse(text)
