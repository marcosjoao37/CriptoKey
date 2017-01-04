class criptografia:

    def cripto(self, chave, mensagem):

        """ 
        Criptografa a mensagem, somando o valor ASCII de cada letra a um valor ASCII da chave
        transformada anteriormente. Caso a palavra seja maior do que o tamanho da chave,
        começasse a somar a partir da primeira posição da lista quando ela chegar ao final.
        Logo após a soma dos valores ASCII, transformasse o novo valor no caractere
        correspondente na tabela ASCII.
        """

        # Variaveis de armazenamento
        self.msg_secreta = ""
        self.num_chave = []
        x = 0 # Contador
        
        # Transforma o valor da chave em código ASCII e adiciona a uma lista para leitura posterior
        for elemento in chave:
            self.num_chave.append(ord(elemento))

        # Criptografa a mensagem
        for letra in mensagem:
            if x > len(self.num_chave)-1:
                x = 0
            self.msg_secreta += str(ord(letra)+self.num_chave[x])+" "
            x += 1

        #Retorna a mensagem secreta criptografada
        return self.msg_secreta

    def descripto(self, chave, mensagem):

        """ 
        Descriptografa a mensagem, subtraindo o valor ASCII de cada letra a um valor ASCII da chave
        transformada anteriormente. Caso a palavra seja maior do que o tamanho da chave,
        começasse a subtrair a partir da primeira posição da lista quando ela chegar ao final.
        Logo após a subtração dos valores ASCII, transformasse o novo valor ASCII no caractere
        correspondente na tabela ASCII.
        """

        # Variaveis de armazenamento
        self.msg_secreta = ""
        self.num_chave = []
        x = 0 # Contador
        y = 0 # Contador
        
        # Transforma o valor da chave em código ASCII e adiciona a uma lista para leitura posterior
        for elemento in chave:
            self.num_chave.append(ord(elemento))

        # Retira os espaços em branco
        mensagem_list = mensagem.split(" ")

        # Retira o espaço em branco que possa existir no final; Estava ocasionando erro
        for posicao in mensagem_list:
            if posicao == "":
                del mensagem_list[(mensagem_list.index(posicao))]

        # Descriptografar a mensagem
        for cod in mensagem_list:
            if x > len(self.num_chave)-1:
                x = 0
            self.msg_secreta += chr(int(cod)-self.num_chave[x])
            x += 1
            
        #Retorna a mensagem secreta descriptografada
        return self.msg_secreta

    # def verifica_chave(self, chave):
    #     # Se o tamanho da chave for maior do que 16 (16 bits), ele cancela a operação de criptografia
    #     if len(chave) > 16:
    #         return False
    #     else:
    #         return True