import fitz
with fitz.open("students.pdf") as pdf:
  #text = ''
  for page in pdf:
    text = page.get_text()
    print(20*'-')
    print(text)
    