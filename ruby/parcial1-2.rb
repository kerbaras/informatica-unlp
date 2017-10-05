module B
  attr_accessor :f

  def to_proc
    ->(i, args = nil) { g = f; self.f += 1; g }
  end
end

class A
  include B

  def initialize(a)
    self.f = a
  end
end

[1, 2, 3, 4].map &A.new(4) # <- (a)