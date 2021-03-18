#aula sobre Herança Múltipla - este arquivo pertence a aula_88

class LogMixing:
    @staticmethod
    def write(msg):
        with open('log.txt', 'a+') as file:
            file.write(msg)
            file.write('\n')

    def log_info(self,msg):
        self.write(f'Info: {msg}')

    def log_error(self,msg):
        self.write(f'Error: {msg}')

