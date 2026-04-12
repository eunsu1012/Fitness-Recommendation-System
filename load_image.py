import json
import os
from cassandra.cluster import Cluster

print("attemepting to connect to cassandra")
cluster = Cluster(['172.17.0.2'], port = 9042)
session = cluster.connect('my_keyspace')

json_path = "/home/wengel/free-exercise-db/dist/exercises.json"
images_folder = "/home/wengel/free-exercise-db/exercises"

with open(json_path,'r') as f:
	metadata=json.load(f)

for item in metadata:
	images = item.get('images',[])
	if not images:
		print('no image found')
		continue

	for image_file in images:
		image_path = os.path.join(images_folder,image_file) if image_file else None


		query = """
		INSERT INTO image_data (id, name, force, level, mechanic, equipment, primarymuscles, instructions, secondarymuscles, category, image_path)
		VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
		"""
		session.execute(query,(
			item['id'],
			item['name'],
			item.get('force', None),
			item['level'],
			item.get('mechanic', None),
			item.get('equipment', None),
			item.get('primarymuscles', []),
			item.get('secondarymuscles', []),
			item.get('instructions', []),
			item['category'],
			image_path
		))

print("data inserted successfully!")
