# Virtual Enviroment



```text
python -m venv nome_virtual_enviroment 
```

Permette di creare nella working directory un virtual enviroment.
Serve ad usare librerie e altre dipendenze senza inquinare l'istallazione di python , in questo modo su ogni progetto puoi avere librerie diverse o versioni piu o meno recenti delle librerie 

Dalla cartella che contiene il venv :
```text
./nome_venv/Scripts/activate
```
se usi git bash per attivare usa :

```text
. nome_venv/Scripts/activate
```

Entro nell'ambiente virtuale per istallare nell'ambiente virtuale quello che mi serve 
Se non entri nell'ambiente virtuale inquini l'istallazione di python


```
deactivate
```
Per uscire da un ambiente virtuale

```
pip install rich
```
Istallo nel venv la libreria rich 

```
pip freeze > requirements.txt
```
Creo il file requirements nel venv è utile per fare un istallazione veloce in 
un altro venv di tutte le librerie che abbiamo installato in questo venv
Tiene conto anche della versione delle librerie istallate


## Per copiare le librerie di un altro vev

Copio il file requirements.txt nella cartella dove voglio installare le librerie che ho nell'altra venv

Entro nel nuovo venv

```
pip install -r .\requirements.txt
```
Installo le librerie nel nuovo venv
