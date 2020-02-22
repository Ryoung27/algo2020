function reverseWords(str){
  res = str.split(" ")
  res.reverse()
  str = res.join(" ")
  return str; // reverse those words
}
