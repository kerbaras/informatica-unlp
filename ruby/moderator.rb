# Dado el siguiente código, que deberás guardar en un archivo llamado "my_random.rb" y en uno llamado "moderator.rb", implementá un simulador del juego de azar Bingo. Para esto, deberás utilizar el motor de aleatoriedad provisto en la clase Random e implementar, utilizando clases y/o módulos (según consideres adecuado) la simulación de las tiradas del sorteo de Bingo.

module Moderator
  def line?(number)
    # Simulación
    @line_queries ||= 0
    @line_queries += 1
    @line_queries > 25 || @line_queries > 8 && rand(0..99) == number
  end
  
  def bingo?(number)
    # Simulación
    @bingo_queries ||= 0
    @bingo_queries += 1
    @bingo_queries > 40 && rand(0..99) == number
  end
end
