from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO
        self.lista_strumenti=[]
        try:
            conn = get_connection()
            cursore = conn.cursor()
            query = "SELECT * FROM strumento"
            cursore.execute(query)
            for riga in cursore:
                strumento = Strumento(
                    codice=riga[0],
                    tipo=riga[1],
                    marca=riga[2],
                    anno_acquisto=riga[3],
                    valore=riga[4],
                    disponibile=True
                )
                self.lista_strumenti.append(strumento)
            cursore.close()
            conn.close()
            #print(self.lista_strumenti)
            return self.lista_strumenti
        except Exception as e:
            return None

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO
        self.lista_per_tipo=[]
        try:
            conn = get_connection()
            cursore = conn.cursor()
            query = "SELECT * FROM strumento WHERE tipo = %s"
            cursore.execute(query, (tipo,))
            for riga in cursore:
                strumento_tipo = Strumento(
                    codice=riga[0],
                    tipo=riga[1],
                    marca=riga[2],
                    anno_acquisto=riga[3],
                    valore=riga[4],
                    disponibile=True
                )
                self.lista_per_tipo.append(strumento_tipo)
            return self.lista_per_tipo
        except Exception as e:
            return None