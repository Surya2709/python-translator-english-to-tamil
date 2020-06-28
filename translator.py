from translate import Translator as ts 
#importing translator module as ts
def Translate(words):
    if words==1:
        return False
    else:
        translator=ts(to_lang="Tamil")
        translation=translator.translate(words)
        return translation

if __name__ == "__main__":
    while(1):
        try:
            words=input('Enter the words to translate(Enter 1 to exit ! ):')
        except:
            print("try again !")
        finally:
            print(Translate(words))