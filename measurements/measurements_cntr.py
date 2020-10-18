import statistics

# delete option: action
action_single = [257.744, 249.898, 241.455, 257.729, 248.608]
action_total = [257.744, 249.899, 241.456, 257.729, 248.608]

# delete option: object
object_single = [81.133, 83.319, 83.623, 84.088, 84.957]
object_total = object_single

# delete option: predicate
predicate_normal_single = [477.477, 346.193, 328.694, 622.117, 365.160]
predicate_normal_total = [477.478, 346.193, 328.694, 622.117, 365.160]

# delete option: predicate --truth
predicate_truth_single = [1846.217, 1548.769, 1350.507, 1829.933, 1398.724]
predicate_truth_total = [1846.217, 1548.770, 1350.507, 1829.933, 1398.724]

# delete option: predicate --falsity
predicate_falsity_single = [111.899, 111.241, 129.053, 141.132, 128.562]
predicate_falsity_total = [111.900, 111.241, 129.053, 141.133, 128.562]

# delete option: action object predicate
action_object_predicate_action_single = [238.594, 236.628, 235.832, 270.371, 250.725]
action_object_predicate_object_single = [83.156, 81.344, 81.984, 90.413, 87.352]
action_object_predicate_predicate_single = [2.410, 2.260, 2.235, 2.506, 2.215]
action_object_predicate_total = [324.159, 320.231, 320.052, 363.290, 340.292]

# delete option: action predicate object
action_predicate_object_action_single = [268.462, 244.440, 269.100, 266.537, 268.144]
action_predicate_object_predicate_single = [39.403, 50.036, 40.968, 43.292, 41.687]
action_predicate_object_object_single = [6.028, 6.565, 7.535, 7.479, 7.985]
action_predicate_object_total = [313.893, 301.042, 317.604, 317.309, 317.816]

# delete option: object action predicate
object_action_predicate_object_single = [85.866, 87.849, 90.072, 83.770, 81.522]
object_action_predicate_action_single = [0.779, 0.950, 0.767, 0.802, 0.798]
object_action_predicate_predicate_single = [2.253, 3.165, 2.286, 2.327, 2.328]
object_action_predicate_total = [88.899, 91.965, 93.124, 86.899, 84.649]

# delete option: object predicate action
object_predicate_action_object_single = [87.324, 83.729, 79.077, 101.717, 102.207]
object_predicate_action_predicate_single = [2.496, 2.485, 2.105, 3.304, 3.972]
object_predicate_action_action_single = [0.434, 0.395, 0.351, 0.615, 0.861]
object_predicate_action_total = [90.255, 86.609, 81.534, 105.636, 107.040]

# delete option: predicate action object
predicate_action_object_predicate_single = [225.695, 223.871, 220.588, 187.167, 236.526]
predicate_action_object_action_single = [333.342, 333.994, 349.349, 275.498, 331.410]
predicate_action_object_object_single = [8.714, 8.836, 9.017, 7.503, 8.677]
predicate_action_object_total = [567.751, 566.701, 578.953, 470.169, 576.613]

# delete option: predicate object action
predicate_object_action_predicate_single = [179.961, 244.563, 233.674, 215.708, 227.156]
predicate_object_action_object_single = [33.210, 34.747, 35.603, 35.226, 34.893]
predicate_object_action_action_single = [0.384, 0.335, 0.378, 0.355, 0.407]
predicate_object_action_total = [213.556, 279.645, 269.655, 251.290, 262.455]


print("action_single: {} +-{}s".format(statistics.mean(action_single), statistics.stdev(action_single)))
print("action_total: {} +-{}s".format(statistics.mean(action_total), statistics.stdev(action_total)))
print()
print("object_single: {} +-{}s".format(statistics.mean(object_single), statistics.stdev(object_single)))
print("object_total: {} +-{}s".format(statistics.mean(object_total), statistics.stdev(object_total)))
print()
print("predicate_normal_single: {} +-{}".format(statistics.mean(predicate_normal_single), statistics.stdev(predicate_normal_single)))
print("predicate_normal_total: {} +-{}".format(statistics.mean(predicate_normal_total), statistics.stdev(predicate_normal_total)))
print()
print("predicate_truth_single: {} +-{}".format(statistics.mean(predicate_truth_single), statistics.stdev(predicate_truth_single)))
print("predicate_truth_total: {} +-{}".format(statistics.mean(predicate_truth_total), statistics.stdev(predicate_truth_total)))
print()
print("predicate_falsity_single: {} +-{}".format(statistics.mean(predicate_falsity_single), statistics.stdev(predicate_falsity_single)))
print("predicate_falsity_total: {} +-{}".format(statistics.mean(predicate_falsity_total), statistics.stdev(predicate_falsity_total)))
print()
print("action_object_predicate_action_single: {} +-{}".format(statistics.mean(action_object_predicate_action_single), statistics.stdev(action_object_predicate_action_single)))
print("action_object_predicate_object_single: {} +-{}".format(statistics.mean(action_object_predicate_object_single), statistics.stdev(action_object_predicate_object_single)))
print("action_object_predicate_predicate_single: {} +-{}".format(statistics.mean(action_object_predicate_predicate_single), statistics.stdev(action_object_predicate_predicate_single)))
print("action_object_predicate_total: {} +-{}".format(statistics.mean(action_object_predicate_total), statistics.stdev(action_object_predicate_total)))
print()
print("action_predicate_object_action_single: {} +-{}".format(statistics.mean(action_predicate_object_action_single), statistics.stdev(action_predicate_object_action_single)))
print("action_predicate_object_predicate_single: {} +-{}".format(statistics.mean(action_predicate_object_predicate_single), statistics.stdev(action_predicate_object_predicate_single)))
print("action_predicate_object_object_single: {} +-{}".format(statistics.mean(action_predicate_object_object_single), statistics.stdev(action_predicate_object_object_single)))
print("action_predicate_object_total: {} +-{}".format(statistics.mean(action_predicate_object_total), statistics.stdev(action_predicate_object_total)))
print()
print("object_action_predicate_object_single: {} +-{}".format(statistics.mean(object_action_predicate_object_single), statistics.stdev(object_action_predicate_object_single)))
print("object_action_predicate_action_single: {} +-{}".format(statistics.mean(object_action_predicate_action_single), statistics.stdev(object_action_predicate_action_single)))
print("object_action_predicate_predicate_single: {} +-{}".format(statistics.mean(object_action_predicate_predicate_single), statistics.stdev(object_action_predicate_predicate_single)))
print("object_action_predicate_total: {} +-{}".format(statistics.mean(object_action_predicate_total), statistics.stdev(object_action_predicate_total)))
print()
print("object_predicate_action_object_single: {} +-{}".format(statistics.mean(object_predicate_action_object_single), statistics.stdev(object_predicate_action_object_single)))
print("object_predicate_action_predicate_single: {} +-{}".format(statistics.mean(object_predicate_action_predicate_single), statistics.stdev(object_predicate_action_predicate_single)))
print("object_predicate_action_action_single: {} +-{}".format(statistics.mean(object_predicate_action_action_single), statistics.stdev(object_predicate_action_action_single)))
print("object_predicate_action_total: {} +-{}".format(statistics.mean(object_predicate_action_total), statistics.stdev(object_predicate_action_total)))
print()
print("predicate_action_object_predicate_single: {} +-{}".format(statistics.mean(predicate_action_object_predicate_single), statistics.stdev(predicate_action_object_predicate_single)))
print("predicate_action_object_action_single: {} +-{}".format(statistics.mean(predicate_action_object_action_single), statistics.stdev(predicate_action_object_action_single)))
print("predicate_action_object_object_single: {} +-{}".format(statistics.mean(predicate_action_object_object_single), statistics.stdev(predicate_action_object_object_single)))
print("predicate_action_object_total: {} +-{}".format(statistics.mean(predicate_action_object_total), statistics.stdev(predicate_action_object_total)))
print()
print("predicate_object_action_predicate_single: {} +-{}".format(statistics.mean(predicate_object_action_predicate_single), statistics.stdev(predicate_object_action_predicate_single)))
print("predicate_object_action_object_single: {} +-{}".format(statistics.mean(predicate_object_action_object_single), statistics.stdev(predicate_object_action_object_single)))
print("predicate_object_action_action_single: {} +-{}".format(statistics.mean(predicate_object_action_action_single), statistics.stdev(predicate_object_action_action_single)))
print("predicate_object_action_total: {} +-{}".format(statistics.mean(predicate_object_action_total), statistics.stdev(predicate_object_action_total)))

