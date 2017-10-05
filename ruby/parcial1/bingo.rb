require_relative "my_random"
require_relative "moderator"

class Bingo
    include Moderator
    
    def initialize()
        @numbers = MyRandom.new(99)
    end

    def jugar()
        self.jugadas.each do |numero, linea, bingo|
            puts "Salio el #{numero}"
            if(linea) then
                puts "Hay linea!"
            end
            if(bingo) then
                puts "Bingo!!!"
                return true
            end
        end
        puts "No hay mas numeros!"
        return false
    end

    def jugadas()
        line = false
        bingo = false
        Enumerator.new do |y|
            while(not bingo) do
                break if @numbers.available.empty?

                number = @numbers.next
                if (line) then
                    if(self.bingo? number) then
                        y.yield(number, false, true)
                        return nil
                    else
                        y.yield(number, false, false)
                    end
                else
                    line = self.line? number
                    y.yield(number, line, false)
                end
            end
        end
    end
end

Bingo.new().jugar()

