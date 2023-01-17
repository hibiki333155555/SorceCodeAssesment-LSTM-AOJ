while (n = gets.to_i) != 0
    puts n.to_s.split("").map(&:to_i).inject(:+)
end
