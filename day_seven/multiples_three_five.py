def solution(number):
  answer = 0
  for i in range(number):
      if i % 3 == 0:
          answer += i
      elif i % 5 == 0:
          answer += i
  return answer
