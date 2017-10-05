module B
  def uno
   ", ¿cómo andás?"
  end
end

class A
  extend B


  def self.dos
    saludo = "Hola#{uno}"
    puts saludo
    2
  end
end

A.dos