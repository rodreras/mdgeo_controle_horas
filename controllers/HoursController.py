import services.database as db
import models.Hours as hours


def incluir(hours):
    sql = '''INSERT INTO bd_horas (employee_name, cc_number, mon, mon_h, tue, tue_h, wed, wed_h, thu, thu_h, fri, fri_h, commentary)
            VALUES (%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s)'''
    args_tuple = (hours.name, hours.cc, 
            hours.date_mon, hours.hours_mon,
            hours.date_tue, hours.hours_tue, 
            hours.date_wed, hours.hours_wed,
            hours.date_thu, hours.hours_thu,
            hours.date_fri, hours.hours_fri,
            hours.commentary)
    count = db.cursor.execute( sql, args_tuple)
    db.conn.commit()

def consultar(query):
        db.cursor.execute(query)
        hoursList = []

        for row in db.cursor.fetchall():
                hoursList.append(hours.Hours(row[0],row[1],row[2],row[3],
                                             row[4],row[5],row[6],row[7],
                                             row[8],row[9],row[10],row[11],row[12]
                ))
        
        return hoursList

def consultar2(query):
        db.cursor.execute(query)
        
