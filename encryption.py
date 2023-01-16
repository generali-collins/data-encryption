def encrypt(text):

     rail1 = ""

     rail2 = ""

     rail3 = ""

 

     for i in range(len(text)):

          char = text[i]

          if i % 3 == 0:

               rail1 = rail1 + char

          elif i % 3 == 1:

               rail2 = rail2 + char

          else:

               rail3 = rail3 + char

    

     result = rail3 + rail2 + rail1

     return result
