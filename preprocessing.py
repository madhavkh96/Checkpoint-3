# pip install json
import json

# pip install psycopg2
import psycopg2

def rowToDict(row):

    # update these fields as needed
    return {
        'officer_id': row[0],
        'salary': row[1],
        'pay_grade': row[2],
        'rank_changed': row[3],
        'rank': row[4],
        'year': row[5]
    }


if __name__ == '__main__':
    with open('secrets.json') as f:
      secrets = json.load(f)

    connection = psycopg2.connect(
        database="cpdb",
        user="cpdb-student",
        password=secrets['db_password'],
        host=secrets['db_host'],
        port='5432'
    )

    query = """select doaa.race, daa.area_id, EXTRACT(YEAR FROM CAST(doaa.shift_start AS DATE)), count(*) as year from data_officerassignmentattendance as doaa
inner join data_officer d on d.id = doaa.officer_id
inner join data_officerallegation doa on d.id = doa.officer_id
inner join data_allegation_areas daa on doa.allegation_id = daa.allegation_id
where doaa.race is not null and doaa.shift_start is not null
GROUP BY doaa.race, daa.area_id, EXTRACT(YEAR FROM CAST(doaa.shift_start AS DATE))"""

    cur = connection.cursor()
    cur.execute(query)

    with open('python_results.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        for r in results:
            writer.writerow(list(r))