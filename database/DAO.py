from database.DB_connect import DBConnect
from model.constructor import Constructor
from model.driverScore import DriverScore


class DAO():
    @staticmethod
    def getYears():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT DISTINCT `year` 
                    from races r 
                    order by `year` desc"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row['year'])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllConstructors():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                    from constructors"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Constructor(row["constructorId"],
                                   row["constructorRef"],
                                   row["name"],
                                   row["nationality"],
                                   row["url"], {}))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getResultsConstructorYear(constructorId, year):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT c.constructorId, r.raceId, r.driverId, r.position, r2.year, r2.circuitId 
                    FROM constructors c, results r, races r2 
                    WHERE c.constructorId = r.constructorId and r.raceId = r2.raceId 
                    and c.constructorId = %s
                    and r2.year = %s"""

        cursor.execute(query, (constructorId, year))

        res = []
        for row in cursor:
            res.append(DriverScore(row["driverId"], row["position"], row["circuitId"]))

        cursor.close()
        cnx.close()
        return res

