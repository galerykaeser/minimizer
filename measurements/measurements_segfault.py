import statistics

# delete option: operator
operator_single = [482.681, 487.492, 472.290, 491.014, 458.708]
operator_total = [482.681, 487.492, 472.290, 491.014, 458.708]
operator_resulting_operators = [18, 35, 18, 35, 18]

# delete option: variable
variable_single = [57.812, 57.816, 58.523, 62.808, 57.582]
variable_total = [57.812, 57.816, 58.524, 62.808, 57.582]
variable_resulting_operators = [432, 432, 432, 432, 432]
variable_resulting_variables = [2, 2, 2, 2, 2]

# delete option: operator variable
operator_variable_operator_single = [442.969, 477.680, 473.826, 427.935, 435.412]
operator_variable_variable_single = [31.620, 38.732, 39.317, 34.059, 34.227]
operator_variable_total = [474.589, 516.413, 513.143, 461.994, 469.640]
operator_variable_resulting_operators = [32, 32, 8, 24, 32]
operator_variable_resulting_variables = [17, 17, 2, 8, 17]


# delete option: variable operator
variable_operator_variable_single = [57.559, 57.773, 57.327, 70.391, 56.592]
variable_operator_operator_single = [79.911, 79.595, 79.450, 76.758, 78.397]
variable_operator_total = [137.470, 137.369, 136.777, 147.149, 134.989]
variable_operator_resulting_variables = [2, 2, 2, 2, 2]
variable_operator_resulting_operators = [2, 2, 2, 2, 2]

print("operator_single: {} +-{}".format(statistics.mean(operator_single), statistics.stdev(operator_single)))
print("operator_total: {} +-{}".format(statistics.mean(operator_total), statistics.stdev(operator_total)))
print("operator_resulting_operators: {} +-{}".format(statistics.mean(operator_resulting_operators), statistics.stdev(operator_resulting_operators)))
print()
print("variable_single: {} +-{}".format(statistics.mean(variable_single), statistics.stdev(variable_single)))
print("variable_total: {} +-{}".format(statistics.mean(variable_total), statistics.stdev(variable_total)))
print()
print("operator_variable_operator_single: {} +-{}".format(statistics.mean(operator_variable_operator_single), statistics.stdev(operator_variable_operator_single)))
print("operator_variable_variable_single: {} +-{}".format(statistics.mean(operator_variable_variable_single), statistics.stdev(operator_variable_variable_single)))
print("operator_variable_total: {} +-{}".format(statistics.mean(operator_variable_total), statistics.stdev(operator_variable_total)))
print("operator_variable_resulting_operators: {} +-{}".format(statistics.mean(operator_variable_resulting_operators), statistics.stdev(operator_variable_resulting_operators)))
print("operator_variable_resulting_variables: {} +-{}".format(statistics.mean(operator_variable_resulting_variables), statistics.stdev(operator_variable_resulting_variables)))
print()
print("variable_operator_variable_single: {} +-{}".format(statistics.mean(variable_operator_variable_single), statistics.stdev(variable_operator_variable_single)))
print("variable_operator_operator_single: {} +-{}".format(statistics.mean(variable_operator_operator_single), statistics.stdev(variable_operator_operator_single)))
print("variable_operator_total: {} +-{}".format(statistics.mean(variable_operator_total), statistics.stdev(variable_operator_total)))


