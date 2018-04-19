# Gobble
Rest API for restaurant food ordering system

Requirements:
	1. java
	2. python3
	3. pip

Run the following from the root directory of the app

* For setup: 
```
make setup
```

* For running the app:
```
make run
```

* For running the unit tests:
```
make test
```

Example API requests:

GET requests:

```
curl http://localhost:5000/Restaurant

curl http://localhost:5000/Restaurant/3

curl http://localhost:5000/Menus/3

curl http://localhost:5000/Menus/3/Lunch

```

POST requests:
```
curl http://localhost:5000/Restaurant  -H "Content-Type: application/json" -d '{"restaurant_id":17}' -X POST -v

curl http://localhost:5000/Restaurant  -H "Content-Type: application/json" -d '{"restaurant_id":300, "restaurant_name":"lalala", "menus":[{"category":"Lunch", "item":[{"item_id":2, "item_name":"Cheese", "item_price":25000}]}]}' -X POST -v

curl http://localhost:5000/Restaurant  -H "Content-Type: application/json" -d '{"restaurant_id":121, "restaurant_name":"Bloom", "menus":[]}' -X POST -v

curl http://localhost:5000/Menus/3  -H "Content-Type: application/json" -d '[{"category":"Lunch", "items":[{"item_id":2, "item_name":"Cakes", "item_price":25}]}]' -X POST -v



```

PUT requests:
```
curl http://localhost:5000/Restaurant/17  -H "Content-Type: application/json" -d '{"restaurant_id":17, "restaurant_name":"Feather"}' -X PUT -v



```

DELETE requests:
```
curl http://localhost:5000/Restaurant/17 -X DELETE -v

curl http://localhost:5000/Menus/3 -X DELETE -v

```