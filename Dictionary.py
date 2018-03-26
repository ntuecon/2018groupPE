"""Created on Mon Mar 26 14:32:39 2018"""

"""@author: WeiJin"""

total_consumers_d = "Number of consumers in the defined economy"

total_goods_d = "Number of types of goods available in the defined economy"

total_factors_d = "Number of types of factors available in the defined economy"

C_list_d = "An array containing the quantity of each good consumed by each consumer in the economy. Length of array = total_consumers * total_goods. Array elements grouped by consumer."

F_list_d = "An array containing the quantity of each factor used to produce one unit of each good. Length of array = total_goods * total_factors. Array elements grouped by goods."

total_cons_d = "An array containing the total consumption quantity of each good in the economy. Length of array = total_goods."

X_d = "Parameter ξ that enters the production function. It varies by goods. Array length = total_goods"

P_d = " Parameter ψ that enters the production function. It varies by goods and factors. Array length = total_goods * total_factors."

weighted_F_list_d = "An array containing the un-summed version of the production function. Array length = total_goods * total_factors."

weightedflist_d = "Just a dummy for looping."

total_prod_d = "An array containing the total production quantity of each good in the defined economy. Array length = total_goods."

factor_list_d = "An array containing the quantity of each factor supplied by each consumer in the defined economy. Array length = total_consumers * total_factors."

total_factor_dd_d = "An array containing the total quantity of each factor demanded by producers in the defiend economy. Array length = total_factors."

total_factor_ss_d = "An array containing the total quantity of each factor supplied by consumers in the defined economy. Array length = total_factors."

utility_weights_d = "An array containing the weight attached to the utility function of each consumer. Array length = total_consumers."

y_d = "Parameter γ that enters the utility function. It does not vary with anything."

s_d = "Parametr σ that enters the utility function. It does not vary with anything."

A_d = "Parameter α that enters the utility function. It varies with both consumers and goods. Array length = total_consumers * total_goods."

B_d = "Parameter β that enters the utility function. It varies with consumers. Array length = total_consumers."

T_d = "Parameter θ that enters the utility function. It varies with factors. Array length = total_factors."

weighted_utility_subc_d = "An array containing the non-summed version of the consumption part of the utility function. Array length = total_consumers * total_goods."

utility_subc_d = "An array containing the summed version of the consumption part of the utility function. Array length = total_consumers."

tweighted_utility_subf_d = "An array containing the un-summed version of the factor part of the utility function, weighted by θ+1. Array length = total_consumers * total_factors."

weighted_utility_subf_d = "An array containing the un-summed version of the factor part of the utiltiy function. Array length = total_factors."

utility_subf_d = "An array containing the summed version of the factor part of the utility function. Array length = total_consumers."

utility_list_d = "An array containing the utility level of each consumer. Array length = total_consumers."

overall_weight = "Parameter that enters the welfare maximisation functions. It does not vary with anything."

utility_list_square_d = "Just the utility_list with each element squared to make them positive."

welfare_max_d = "The welfare level that takes into account the utiltiy level of each consumer in the defined economy."
