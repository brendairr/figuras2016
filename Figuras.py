class Figuras():
	"""docstring for Figuras"""
	def cuadrado(self, lado):
		try:
			lado = int(lado)
			return lado * lado
		except Exception:
			return 'dato incorrecto'