    def test_deluxe_fee_is_exactly_double_the_normal_fee(self):
        normal_fine = DuckFine("M001")
        deluxe_fine = DuckFine("M002")

        normal_fee = normal_fine.charge(5)
        deluxe_fee = deluxe_fine.charge(5, deluxe=True)

        self.assertEqual(deluxe_fee, normal_fee * 2)
