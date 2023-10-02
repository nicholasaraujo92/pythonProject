class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_valido(documento):
            self.cpf = documento
        else:
            raise ValueError('O CPF digitado é inválido.')

    def __str__(self):
        return self.cpf_formatado()

    def cpf_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            False

    def cpf_formatado(self):
        primeiro_bloco = self.cpf[:3]
        segundo_bloco = self.cpf[3:6]
        terceiro_bloco = self.cpf[6:9]
        digitos = self.cpf[9:]
        return(
            '{}.{}.{}-{}'.format(
                primeiro_bloco, segundo_bloco, terceiro_bloco, digitos)
        )