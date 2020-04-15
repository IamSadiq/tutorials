import unittest
from reservation import Reservation

class ReservationTest(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        self.server = MockServer() # mock server
        self.reserver = Reservation(self.server)

    # test find available tables
    def test_find_available_tables_finds_all_tables(self):
        availableTables = self.reserver.find_available_tables()
        self.assertEqual([1,2,3,4,5,6], availableTables)

    # test if any table is available
    def test_make_reservation_has_available_table(self):
        response = self.reserver.make_reservation("Mariam")
        self.assertEqual(True, response)

    # test find available tables
    def test_find_available_tables_after_making_reservation(self):
        self.reserver.make_reservation("Adam", 1)
        availableTables = self.reserver.find_available_tables()
        self.assertNotIn(1, availableTables)

    # test if table is invalid
    def test_make_reservation_table_is_invalid(self):
        response = self.reserver.make_reservation("Ahmad", table=11)
        self.assertEqual(False, response)

    # test if table is not taken
    def test_make_reservation_table_is_not_taken(self):
        response = self.reserver.make_reservation("Ameer", table=5)
        self.assertEqual(True, response)

    # test if table is taken
    def test_make_reservation_table_is_taken(self):
        self.reserver.make_reservation("Scott", table=2)
        response = self.reserver.make_reservation("Aisha", table=2)
        self.assertEqual(False, response)

    # test that reservation exists
    # def test_change_reservation_check_reservation_exists(self):
    #     self.reserver.make_reservation("Matt", table=2)
    #     response = self.reserver.change_reservation("Matt", table=3)
    #     self.assertEqual(True, response)
    
    # # test that reservation doesnt exists
    # def test_change_reservation_check_reservation_doesnt_exists(self):
    #     response = self.reserver.change_reservation("Greg", table=3)
    #     self.assertEqual(False, response)


# our mock server
class MockServer:
    def __init__(self):
        super().__init__()
        self.tables = [1, 2, 3, 4, 5, 6]
        self.reservations = {i: None for i in self.tables}

    def getTables(self):
        return self.tables

    def getReservations(self):
        return self.reservations