class Reservation:
    def __init__(self, server):
        self.server = server
        self.reservations = self.server.getReservations()
        self.tables = self.server.getTables()

    def find_available_tables(self):
        return [t for t in self.tables if self.reservations[t] is None]

    def make_reservation(self, name, table=None):
        if table is None:
            for t in self.tables:
                if self.reservations[t] is None:
                    self.reservations[t] = name
                    return True
            return False
        else:
            if table not in self.tables: return False # check if table is invalid
            if self.reservations[table] is not None: return False # check if table is taken
            
            self.reservations[table] = name
            return True

    def has_reservation(self, name):
        for t, n in self.reservations.items():
            if n == name:
                return True
        return False

    def find_reservation(self, name):
        for t, n in self.reservations.items():
            if n == name:
                return t, n
        return None, name

    def change_reservation(self, name, table):
        t, n = self.find_reservation(name)

        if t is None: return False # check if reservation exists
        if table not in self.tables: return False # check if new table is invalid
        if self.reservations[table] is not None: return False # check if new table is taken

        self.reservations[t] = None
        self.reservations[table] = name
        return True

    def cancel_reservation(self, name):
        t, n = self.find_reservation(name)
        if t is None: return False # check if reservation exists
        
        self.reservations[t] = None
        return True
