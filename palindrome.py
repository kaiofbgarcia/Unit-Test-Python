def palindromo(texto) -> bool:
    if not isinstance(texto, str):
        return False

    textoSemEspacos = texto.replace(' ', '')
    textoMinusculo = textoSemEspacos.lower()
    textoInvertido = textoMinusculo[::-1]
    if textoInvertido == textoMinusculo:
        return True
    else:
        return False