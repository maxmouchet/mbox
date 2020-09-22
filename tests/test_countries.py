from mtoolbox.countries import countries, iso2iso3


def test_countries():
    for iso3, country in countries.items():
        iso2 = country["#country+code+v_iso2"]
        assert iso2iso3[iso3] == iso2
        assert iso2iso3[iso2] == iso3
