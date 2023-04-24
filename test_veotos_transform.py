from veotos_transform import find_new_text


def test_transform_Erik():
    text_to_convert = 'Erik'
    assert text_to_convert == find_new_text(text_to_convert, 0)
    assert 'Isol' == find_new_text(text_to_convert)


def test_transform_Leo():
    text_to_convert = 'Leo'
    assert text_to_convert == find_new_text(text_to_convert, 0)
    assert 'Miu' == find_new_text(text_to_convert)


def test_transform_Taisir():
    text_to_convert = 'Taisir'
    assert text_to_convert == find_new_text(text_to_convert, 0)
    assert 'Veotos' == find_new_text(text_to_convert)
    assert 'Zaiyix' == find_new_text(text_to_convert, 5)


def test_transform_Taisir_Aviles_with_special_character():
    text_to_convert = 'Taisir Avilés'
    assert text_to_convert == find_new_text(text_to_convert, 0)
    assert 'Veotos Ewomít' == find_new_text(text_to_convert)


def test_transform_España():
    """
    ñ doesn't change
    """

    text_to_convert = 'España'
    assert text_to_convert == find_new_text(text_to_convert, 0)
    assert 'Itqeñe' == find_new_text(text_to_convert)


def test_transform_back_again():
    """
    105 = the product of 5 vowels and 23 consonants (least common multiple)
    The least common multiple in iteration number results in the same text.
    """
    text_to_convert = 'Lorem ipsum dolor sit amet'
    assert text_to_convert == find_new_text(text_to_convert, 105)


def test_encircle_text():
    """
    105 = the product of 5 vowels and 23 consonants (least common multiple)
    The least common multiple in iteration number results in the same text.
    """
    text_to_convert = 'Lorem ipsum dolor sit amet Taisir Avilés áéíóú äëïöü'
    new_text = 'ⓁⓄⓇⒺⓂ ⒾⓅⓈⓊⓂ ⒹⓄⓁⓄⓇ ⓈⒾⓉ ⒶⓂⒺⓉ ⓉⒶⒾⓈⒾⓇ ⒶⓋⒾⓁⒺⓈ ⒶⒺⒾⓄⓊ ⒶⒺⒾⓄⓊ'
    assert new_text == find_new_text(text_to_convert, 105, encircle='y')
