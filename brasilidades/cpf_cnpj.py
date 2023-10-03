from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento

        documento = str(documento)

        if self.tipo_documento == "cpf":
            if self.cpf_valido(documento):
                self.cpf = documento
            else:
                raise ValueError('O CPF digitado é inválido.')
        elif self.tipo_documento == "cnpj":
            if self.cnpj_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError('O CNPJ digitado é inválido')
        else:
            raise ValueError('Documento inválido.')
    def __str__(self):
        if self.tipo_documento == 'cpf':
            return self.cpf_formatado()
        elif self.tipo_documento == 'cnpj':
            return self.cnpj_formatado()

    def cpf_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError('Quantidade de dígitos inválida.')

    def cpf_formatado(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


    def cnpj_valido(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError('Quantidade de digitos inválida.')

    def cnpj_formatado(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)


