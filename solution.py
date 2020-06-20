# This fuction is used for sort all the list like (machines, costs, capacities)
# in the increasing order of their costs per machine
def sortedCostsCapacitiesRatio(machines, costs, capacities):

    no_of_machines = len(machines)
    ratio = []
    
    for i in range(no_of_machines):
        ratio.append(costs[i]/capacities[i])
    
    sorted_ratio = sorted(ratio)
    
    arranged_machine = []
    sorted_capacities = []
    sorted_costs = []
    
    for number in sorted_ratio:
        for i in range(no_of_machines):
            if number == (costs[i]/capacities[i]):
                sorted_costs.append(costs[i])
                sorted_capacities.append(capacities[i])
                arranged_machine.append(machines[i])
                break

    return arranged_machine, sorted_costs, sorted_capacities
    
    

# This function is used to find the minimal cost of Particular Region
def findMinimumTotalCostPerRegion(region, machine, costs, capacities, required_capacity, hours):

    no_of_machines = len(machine)
    total_cost = 0
    region_dict = dict();
    region_dict['region'] = region
    region_dict['machines'] = []
    
    for i in range(no_of_machines):
        if capacities[i] <= required_capacity:
            for j in range(100):
                if (capacities[i]*(j+1)) > required_capacity:
                    required_capacity -= (capacities[i]*(j))
                    total_cost += (costs[i]*(j))*hours
                    paticular_machine = (machine[i], j)
                    region_dict['machines'].append(paticular_machine)
                    break
        
    region_dict['total_cost'] = total_cost

    return region_dict
    


# This function return the Minimal Cost Detail of Region
def resourceAllocator(required_capacity, hours): 
    
    output = []
    
    machines = ['Large', 'XLarge', '2XLarge', '4XLarge', '8XLarge', '10XLarge']
    capacities = [10, 20, 40, 80, 160, 320]
    
    new_york_costs = [120, 230, 450, 774, 1400, 2820] 
    india_costs = [140, 5000, 413, 890, 1300, 2970] 
    china_costs = [110, 200, 5000, 670, 1180, 5000] 
    
    # It will find New York's Minimal Cost Detail
    new_york_machine, costs, new_york_capacities = sortedCostsCapacitiesRatio(machines, new_york_costs, capacities)
    new_york_dict = findMinimumTotalCostPerRegion("New York", new_york_machine, costs, new_york_capacities, required_capacity, hours)
    output.append(new_york_dict)
    
    # It will find India's Minimal Cost Detail
    india_machine, costs, india_capacities = sortedCostsCapacitiesRatio(machines, india_costs, capacities)
    india_dict = findMinimumTotalCostPerRegion("India", india_machine, costs, india_capacities, required_capacity, hours)
    output.append(india_dict)
    
    # It will find China's Minimal Cost Detail
    china_machine, costs, china_capacities = sortedCostsCapacitiesRatio(machines, china_costs, capacities)
    china_dict = findMinimumTotalCostPerRegion("China", china_machine, costs, china_capacities, required_capacity, hours)
    output.append(china_dict)
    
    return output


# Form here we start our code and we take input from user
input_line = input() 
split_in_list = input_line.split()

# Here we grab the required capacity and hours
required_capacity = int(split_in_list[2])
hours = int(split_in_list[5])

final_output = dict();

# Here we call our main function which return dictionary
output = resourceAllocator(required_capacity, hours)

final_output['output'] = output

# Finally we print our expected output
print(final_output) 
