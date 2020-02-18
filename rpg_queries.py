import sqlite3
 
 
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = """SELECT 
count(distinct character_id)
FROM charactercreator_character"""
 
curs.execute(query)

results = curs.execute(query).fetchall()



query = """SELECT
character_id, id
FROM charactercreator_character_inventory
group by character_id"""

curs.execute(query)

results = curs.execute(query).fetchall()



query = """SELECT 
count(distinct item_id)
FROM armory_item"""

curs.execute(query)

results = curs.execute(query).fetchall()



#How many are weapons? 

query = """SELECT COUNT(item_id)
FROM armory_item, armory_weapon
WHERE item_ptr_id = item_id
ORDER BY item_id"""

curs.execute(query)

results = curs.execute(query).fetchall()


#How many are not weapons

query = """SELECT COUNT(item_id)
FROM armory_item, armory_weapon
WHERE item_ptr_id != item_id
ORDER BY item_id"""

curs.execute(query)

results = curs.execute(query).fetchall()


#Calculate How many ITEMS each character has 

query = """SELECT
count(item_id) character_id
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20 """

curs.execute(query)

results = curs.execute(query).fetchall()

#How many weapons each character has?

query = """SELECT count(item_ptr_id), character_id
FROM charactercreator_character_inventory, armory_weapon
WHERE item_ptr_id = item_id
GROUP BY character_id"""

curs.execute(query)

results = curs.execute(query).fetchall()

breakpoint()




