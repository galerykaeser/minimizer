import statistics

# delete option: action
action_single = [0.826, 0.839, 0.855, 0.829, 0.832]
action_total = [0.826, 0.839, 0.855, 0.829, 0.832]
action_action_result = [3, 3, 3, 3, 3]
action_object_result = [5, 5, 5, 5, 5]
action_predicate_result = [6, 6, 6, 6, 6]

# delete option: object
object_single = [1.429, 1.599, 1.470, 1.487, 1.473]
object_total = [1.429, 1.599, 1.470, 1.487, 1.473]
object_action_result = [3, 3, 3, 3, 3]
object_object_result = [5, 5, 5, 5, 5]
object_predicate_result = [6, 6, 6, 6, 6]

# delete option: predicate
predicate_normal_single = [2.738, 2.760, 2.659, 2.842, 2.766]
predicate_normal_total = [2.738, 2.760, 2.659, 2.842, 2.766]
predicate_normal_action_result = [3, 3, 3, 3, 3]
predicate_normal_object_result = [5, 5, 5, 5, 5]
predicate_normal_predicate_result = [3, 3, 3, 3, 3]

# delete option: predicate --truth
predicate_truth_single = [2.711, 2.769, 2.711, 2.735, 2.746]
predicate_truth_total = [2.711, 2.769, 2.711, 2.735, 2.746]
predicate_truth_action_result = [3, 3, 3, 3, 3]
predicate_truth_object_result = [5, 5, 5, 5, 5]
predicate_truth_predicate_result = [3, 3, 3, 3, 3]

# delete option: predicate --falsity
predicate_falsity_single = [1.834, 1.777, 1.819, 1.777, 1.827]
predicate_falsity_total = [1.834, 1.778, 1.819, 1.777, 1.827]
predicate_falsity_action_result = [3, 3, 3, 3, 3]
predicate_falsity_object_result = [5, 5, 5, 5, 5]
predicate_falsity_predicate_result = [6, 6, 6, 6, 6]

# delete option: action object predicate
action_object_predicate_action_single = [0.873, 0.847, 0.868, 0.877, 0.876]
action_object_predicate_object_single = [1.437, 1.446, 1.400, 1.388, 1.455]
action_object_predicate_predicate_single = [2.692, 2.757, 2.718, 2.677, 2.840]
action_object_predicate_total = [5.002, 5.050, 4.986, 4.943, 5.172]
action_object_predicate_action_result = [3, 3, 3, 3, 3]
action_object_predicate_object_result = [5, 5, 5, 5, 5]
action_object_predicate_predicate_result = [3, 3, 3, 3, 3]

# delete option: action predicate object
action_predicate_object_action_single = [0.800, 0.863, 0.854, 0.916, 0.839]
action_predicate_object_predicate_single = [2.589, 2.748, 2.696, 2.687, 2.644]
action_predicate_object_object_single = [1.880, 1.915, 1.966, 1.962, 1.944]
action_predicate_object_total = [5.269, 5.526, 5.516, 5.566, 5.427]
action_predicate_object_action_result = [3, 3, 3, 3, 3]
action_predicate_object_object_result = [3, 3, 3, 3, 3]
action_predicate_object_predicate_result = [3, 3, 3, 3, 3]

# delete option: object action predicate
object_action_predicate_object_single = [1.432, 1.572, 1.467, 1.398, 1.443]
object_action_predicate_action_single = [0.872, 0.867, 1.222, 0.859, 0.827]
object_action_predicate_predicate_single = [2.739, 2.728, 2.817, 2.643, 2.727]
object_action_predicate_total = [5.044, 5.168, 5.506, 4.900, 4.998]
object_action_predicate_action_result = [3, 3, 3, 3, 3]
object_action_predicate_object_result = [5, 5, 5, 5, 5]
object_action_predicate_predicate_result = [3, 3, 3, 3, 3]

# delete option: object predicate action
object_predicate_action_object_single = [1.466, 1.431, 1.461, 1.407, 1.459]
object_predicate_action_predicate_single = [2.639, 2.727, 2.654, 2.662, 2.845]
object_predicate_action_action_single = [1.020, 0.965, 0.965, 1.022, 1.180]
object_predicate_action_total = [5.126, 5.124, 5.081, 5.091, 5.484]
object_predicate_action_action_result = [1, 1, 1, 1, 1]
object_predicate_action_object_result = [5, 5, 5, 5, 5]
object_predicate_action_predicate_result = [3, 3, 3, 3, 3]

# delete option: predicate action object
predicate_action_object_predicate_single = [2.717, 2.798, 2.680, 2.652, 2.813]
predicate_action_object_action_single = [1.011, 1.035, 1.012, 0.987, 1.034]
predicate_action_object_object_single = [1.946, 1.918, 1.874, 1.848, 1.913]
predicate_action_object_total = [5.674, 5.751, 5.566, 5.487, 5.761]
predicate_action_object_action_result = [1, 1, 1, 1, 1]
predicate_action_object_object_result = [3, 3, 3, 3, 3]
predicate_action_object_predicate_result = [3, 3, 3, 3, 3]

# delete option: predicate object action
predicate_object_action_predicate_single = [2.562, 2.595, 2.563, 2.674, 2.739]
predicate_object_action_object_single = [1.863, 1.876, 1.879, 1.903, 1.849]
predicate_object_action_action_single = [0.889, 0.948, 0.908, 0.976, 0.942]
predicate_object_action_total = [5.315, 5.419, 5.350, 5.553, 5.531]
predicate_object_action_action_result = [1, 1, 1, 1, 1]
predicate_object_action_object_result = [3, 3, 3, 3, 3]
predicate_object_action_predicate_result = [3, 3, 3, 3, 3]


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

