from veotos_transform import find_new_text


def test_transform_Erik():
    text_to_convert = 'Erik'
    assert text_to_convert == find_new_text(text_to_convert, 0)
    assert 'Isol' == find_new_text(text_to_convert, 1)


def test_transform_Leo():
    text_to_convert = 'Leo'
    assert text_to_convert == find_new_text(text_to_convert, 0)
    assert 'Miu' == find_new_text(text_to_convert, 1)


def test_transform_Taisir_Aviles():
    text_to_convert = 'Taisir Aviles'
    assert text_to_convert == find_new_text(text_to_convert, 0)
    assert 'Veotos Ewomit' == find_new_text(text_to_convert, 1)


def test_transform_Taisir_Aviles_with_special_character():
    text_to_convert = 'Taisir Avilés'
    assert text_to_convert == find_new_text(text_to_convert, 0)
    assert 'Veotos Ewomít' == find_new_text(text_to_convert, 1)


def test_transform_España():
    """
    ñ doesn't change
    """

    text_to_convert = 'España'
    assert text_to_convert == find_new_text(text_to_convert, 0)
    assert 'Itqeñe' == find_new_text(text_to_convert, 1)


def test_transform_back_again():
    """
    105 = the product of 5 vowels and 23 consonants (minimum common multiple)
    The minimum common multiple in iteration number results in the same text.
    """
    text_to_convert = 'Lorem ipsum dolor sit amet'
    assert text_to_convert == find_new_text(text_to_convert, 105)
