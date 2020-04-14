class FlowerGarden(object):

	def __init__(self):
		pass

	def getOrdering(self, height, bloom, wilt):


		mat = [[-1 for i in range(len(height))] for i in range(365)]
		sorted_height = sorted(height)


		for pos in range(365):

			for 