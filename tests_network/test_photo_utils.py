def test_gps_location():
    gps_data = [50, 49, 859 / 100, "N", 0, 8, 249 / 20, "W"]
    expected = "Big Fish Trading Co., Grand Junction Road, Queen's Park, Brighton, Brighton and Hove, South East, England, BN2 1TD, UK"
    assert pu.get_gps_location(*gps_data) == expected
