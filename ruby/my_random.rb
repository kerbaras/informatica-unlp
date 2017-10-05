# Dado el siguiente código, que deberás guardar en un archivo llamado "my_random.rb" y en uno llamado "moderator.rb", implementá un simulador del juego de azar Bingo. Para esto, deberás utilizar el motor de aleatoriedad provisto en la clase Random e implementar, utilizando clases y/o módulos (según consideres adecuado) la simulación de las tiradas del sorteo de Bingo.

class MyRandom
  attr_accessor :maximum, :available, :taken

  def initialize(maximum)
    self.maximum = maximum
    self.available = (0..maximum).to_a
    self.taken = []
  end

  def next
    raise 'Se agotaron los números posibles' if available.empty?
    value = self.available.shuffle!.shift
    self.taken << value
    value
  end
end
