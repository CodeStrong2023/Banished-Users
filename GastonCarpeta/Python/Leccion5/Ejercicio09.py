#ejercicio 9: mostramos una frase sin espacios y contar su longitud
#hacer un programa donde el ususaario ingrese una frase, se le
#devolvera la misma frase pero sin espacios en blanco, y
#ademas un contador de cuantos caracteres tiene la frase
#(sin contar los espacios en blanco)
#ejmeplo: frase =vivir por siempre en paz
#frase final= vivirporsiempreenpaz
#n de caracteres = 20

frase1 = input("digite una frase: " )
frase2 = " "
for i in frase1:

        if i != " ":
            frase2 += i
frase1 = frase2
print(f'\n frase final: {frase1}')
print(f'N° de caracteres: {len(frase1)}')