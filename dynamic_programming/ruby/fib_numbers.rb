def fib(n)
  fibs = [0,1]
  for i in 2..n
    fibs << fibs[i-2] + fibs[i-1]
  end
  return fibs[n]
end

puts fib(12)
