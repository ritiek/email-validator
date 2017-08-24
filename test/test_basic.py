import evalidator


def test_googlemail():
    valid = evalidator.validate('someone@gmail.com')
    invalid = evalidator.validate('thisemaildoesnotexisthehe@gmail.com')
    assert (valid and not invalid)


def test_yahoomail():
    valid = evalidator.validate('hello@yahoo.com')
    invalid = evalidator.validate('thisemaildoesnotexisthehe@yahoo.com')
    assert (valid and not invalid)
