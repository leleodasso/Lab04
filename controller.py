import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSpellChecker(self, e):
        if self._view._txtIn.value is None:
            self._view._txtOut.controls.append(ft.Text(value="Non hai inserito alcuna frase", color="red"))
            self._view.page.update()
            return
        testo = self._view._txtIn.value
        lingua = self._view._language_selector.value
        if lingua is None:
            self._view._txtOut.controls.append(ft.Text(value="Non hai inserito alcuna lingua", color="red"))
            self._view.page.update()
            return
        modalita = self._view._select_modality.value
        if modalita is None:
            self._view._txtOut.controls.append(ft.Text(value="Non hai inserito alcuna modalità", color="red"))
            self._view.page.update()
            return
        self._view._txtOut.controls.append(ft.Text(value=f"Frase inserita: {testo}", color="green"))
        self._view.page.update()
        risultato = self.handleSentence(testo, lingua, modalita)
        if risultato is not None:
            paroleErrate, tempo = risultato
            self._view._txtOut.controls.append(ft.Text(value=f"parole errate: {paroleErrate}", color="red"))
            self._view._txtOut.controls.append(ft.Text(value=f"tempo richiesto alla ricerca: {tempo}", color="red"))
            self._view.page.update()



    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())
        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text


