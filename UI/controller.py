import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def ottieni_strumenti(self, e):
        lista = self._model.get_strumenti()
        self._view.lista_strumenti.controls.clear()
        for strum in lista:
            testo_visual = ft.Text(f"{strum.codice} {strum.tipo} {strum.marca} "
                                   f"{strum.anno_acquisto} {strum.valore} {strum.disponibile}")
            self._view.lista_strumenti.controls.append(testo_visual)
        self._view.page.update()

    def cerca_strumento(self, e):
        tipo_strum = self._view.input_tipo_strumento.value
        lista_tipo = self._model.cerca_strumenti_per_tipo(tipo_strum)
        self._view.lista_strumenti_ricerca.controls.clear()
        if lista_tipo:
            for s in lista_tipo:
                testo = ft.Text(f"{s.codice} {s.tipo} {s.marca} "
                                f"{s.anno_acquisto} {s.valore} {s.disponibile}")
                self._view.lista_strumenti_ricerca.controls.append(testo)
            self._view.page.update()
        else:
            self._view.lista_strumenti_ricerca.controls.append(
                ft.Text("Non esiste nessuno strumento di questo tipo."),
                color="red")