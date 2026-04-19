For `robots.csv` and similar files:

* `battery_level` must be an integer between 0 and 100.
* `max_load` must be a non-negative floating point number.
* `zone` must be a non-empty string consisting of only upper case alphabetical characters.

For `destinations.csv` and similar files:

* `zone` must be a non-empty string consisting of only upper case alphabetical characters.

For `packages.csv` and similar files:

* `weight` must be a non-negative floating point number.

For `tasks.csv` and similar files:

* `source_id` must exist in the destination data,
* `target_id` must exist in the destination data,
* `package_id` must exist in the package data,
* `status` must be one of `pending` or `complete`.


rebort
['robot_id', 		'battery_level', 'max_load', 	'zone']


destinations
['destination_id', 							'zone']


packages
['package_id', 	'weight']

tasks
['task_id', 		'source_id', 		'target_id', 		'package_id', 		'status']
