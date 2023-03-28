iris = dict()


def add_iris(id_n, species, petal_l, petal_w, **specs):
    other = ["species", "petal_length", "petal_width"]

    iris[id_n] = dict.fromkeys(other)

    for k, v in iris.items():
        v["species"] = species
        v["petal_length"] = petal_l
        v["petal_width"] = petal_w
        for key, value in specs.items():
            v[key] = value

#     return iris
#
#
# i = add_iris(0, 'Iris versicolor', 4.0, 1.3)
#
# print(i)
