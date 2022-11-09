car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
cost=10000

print(car.items())

print(car.get("model"))

print(car.keys())

print(car.values())

car["model"]="Mustang"

print(car.pop("model"))
print(car)

print(car.popitem())
print(car)

car.update({"Mileage" : "30"})
print(car)

x = car.setdefault("color", "pink")
print(x)

b=car.fromkeys(car,cost)
print(b)
print(car)