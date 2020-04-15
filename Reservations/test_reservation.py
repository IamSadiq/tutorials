import unittest
from reservation import Reservation

class ReservationTest(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        
    def setUp(self):
        self.server = MockServer() # mock server
        self.reserver = Reservation(self.server)
        
    def tearDown(self):
        pass

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
    def test_change_reservation_check_reservation_exists(self):
        self.reserver.make_reservation("Matt", table=2)
        response = self.reserver.change_reservation("Matt", table=3)
        self.assertEqual(True, response)
    
    # test that reservation doesnt exists
    def test_change_reservation_check_reservation_doesnt_exists(self):
        response = self.reserver.change_reservation("Greg", table=3)
        self.assertEqual(False, response)

    # test change reservation table is invalid
    def test_change_reservation_table_is_invalid(self):
        self.reserver.make_reservation("Kemi", table=2)
        response = self.reserver.change_reservation("Kemi", table=11)
        self.assertEqual(False, response)

    # test change reservation table is not taken
    def test_change_reservation_table_is_not_taken(self):
        self.reserver.make_reservation("Ayo", table=1)
        response = self.reserver.change_reservation("Ayo", table=5)
        self.assertEqual(True, response)

    # test change reservation table is taken
    def test_change_reservation_table_is_taken(self):
        self.reserver.make_reservation("Dora", table=2)
        self.reserver.make_reservation("Nusi", table=3)
        response = self.reserver.change_reservation("Nusi", table=2)
        self.assertEqual(False, response)

    # test that change reservation frees previous reservation table
    def test_change_reservation_frees_previous_table(self):
        self.reserver.make_reservation("Mujaheed", table=4)
        self.reserver.change_reservation("Mujaheed", table=3)
        availableTables = self.reserver.find_available_tables()
        self.assertIn(4, availableTables)

    # test that change reservation changes reservation table
    def test_that_change_reservation_changes_reservation_table(self):
        self.reserver.make_reservation("Ayo", table=1)
        self.reserver.change_reservation("Ayo", table=5)
        availableTables = self.reserver.find_available_tables()
        self.assertNotIn(5, availableTables)

    # test find reservation doesn't find reservation
    def test_find_reservation_doesnt_find_reservation(self):
        t, n = self.reserver.find_reservation("Kris")
        self.assertIs(t, None)

    # test find reservation finds reservation
    def test_find_reservation_actually_finds_reservation(self):
        response = self.reserver.make_reservation("Kris", 6)
        t, n = self.reserver.find_reservation("Kris")
        self.assertEqual(t, 6)

    # test cancel reservation doesnt find reservation
    def test_cancel_reservation_doesnt_find_reservation(self):
        response = self.reserver.cancel_reservation("Luka")
        self.assertEqual(response, False)

    # test cancel reservation finds reservation
    def test_cancel_reservation_finds_reservation(self):
        self.reserver.make_reservation("Modric", 6)
        response = self.reserver.cancel_reservation("Modric")
        self.assertEqual(response, True)

    # test cancel reservation frees table
    def test_cancel_reservation_frees_table(self):
        self.reserver.make_reservation("Xavi", 4)
        response = self.reserver.cancel_reservation("Xavi")
        availableTables = self.reserver.find_available_tables()
        self.assertIn(4, availableTables)



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