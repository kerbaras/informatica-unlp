require 'minitest/autorun'

# Método
def numero_a_palabras(n)
  # Asumir implementado el método que convierte el número `n'
  # a su correspondiente representación en palabras en español
	['Uno', 'Dos', 'Tres'][n-1]
end

def convertir(v)
  v.map { |i| i.odd? ? numero_a_palabras(i) : i }
end

# Assertion
describe 'convertir' do
	it '1' do
		assert_equal ['Uno', 2, 'Tres'], convertir([1, 3, 2])
	end
	it '2' do
		assert_equal ['Uno', 2, 'Tres'], convertir([1, 2, 3])
	end
	it '3' do
		assert_equal ['Uno', 2, 'Tres'], convertir(3.downto(1))
	end
	it '4' do
		assert_equal ['Uno', 2, 'Tres'], convertir(1..3)
	end
	it '5' do
		assert_equal ['Uno', 2, 'Tres'], convertir(1...3)
	end
end

