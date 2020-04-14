import copy

class BadNeighbors(object):

	def __init__(self):
		self.prices = None
		self.graph = None






	def maxDonations(self, prices):

		
		state_vector = [0 for i in range(len(prices))]
		zero_inc = [False for i in range(len(prices))]
		i_included = [False for i in range(len(prices))]


		flag_for_first = 1

		for i in range(len(prices)):

			if i == 0:
				state_vector[i] = prices[0]
				zero_inc[i] = True
				i_included[i] = True

			elif i == 1:
				state_vector[i] = max(prices[i], state_vector[i - 1])
				if state_vector[i] != prices[i]:
					zero_inc[i] = True
				else:
					i_included[i] = True


			else:
				state_vector[i] = max(state_vector[i - 1], state_vector[i - 2] + prices[i])
				if state_vector[i] == state_vector[i - 1]:
					i_included[i] = False
					zero_inc[i] = zero_inc[i - 1]
				else:
					i_included[i] = True
					zero_inc[i] = zero_inc[i - 2]


		if zero_inc[-1] and i_included[-1]:

			tmp = max(state_vector[-1] - prices[-1], state_vector[-2])
			tmp2 = max(tmp, state_vector[-1] - prices[0])

			state_vector[-1] = tmp2





		return state_vector[-1]









if __name__ == '__main__':
	test = BadNeighbors()
	print(test.maxDonations([94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72 ]))
