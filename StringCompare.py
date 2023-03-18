text1 = input("digite uma string qualquer \n")
text2 = input("digite outra string qualquer \n")

print(f"A string ({text1}) têm {len(text1)} caracteres")
print(f"A string ({text2}) têm {len(text2)} caracteres")

if len(text1) > len(text2):
	print(f"A string ({text1}) é maior que a string ({text2})")
else:
	print(f"A string ({text2}) é maior que a string ({text1})")