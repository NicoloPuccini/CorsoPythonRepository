# Comandi Linux

```
ls 
```
Elenca il contenuto della working directory

---

```
ls /path-directory
```
Elenca il contenuto della directory

---

```
ls -a
```
Fa vedere anche i contenuti nascosti (quelli che anno il nome che inizia con .)

---

```
cd nome_cartella
```
per entrare nella cartella

---


```
cd ..
```
Torna indietro alla cartella superiore

---

```
whoami
```
Ritorna il nome dell'utente attuale

---

```
pwd
```
Stampa il path della working directory

---

```
chmod 775 path/cartella
```
permette di cambiare i privilegi di lettura scrittura ed esucuzione
i tre numeri sono relativi ai permessi garantiti a :
- primo numero L'utente amministratore
- secondo numero l'organizzazione dell'utente
- tutti gli altri utenti 
I numeri indicano i tipi di permessi
- 1 (x) sola Esecuzione
- 2 (w) sola Scrittura
- 4 (r) sola Lettura
Facendo le somme si ottengono i permessi come:
5 = 1 + 4 (Esecuzione e Lettura)
7 = 1 + 2 + 4 (Tutti i permessi)

---

```
mkdir nuova_cartella
```
permette di creare una nuova cartella

---



### Creare Gruppi, Utenti ecc ecc
sudo è il comando con privilegi di amministratore (super user do)

---

```
sudo addgroup nome_gruppo
```
Crea un nuovo gruppo

---

```
sudo adduser nome_user
```
Crea un nuovo utente

---

```
sudo usermod -aG nome_gruppo nome_utente
```
Aggiunge un utente al gruppo

---

```
getent group nome_gruppo
```
Mostra tutti gli utenti del gruppo

---

```
groups nome_utente
```
Mostra tutti i gruppi dell'utente

---

```
su nome_utente - 
```
Permette di switchare da un utente all'altro

---

### Comandi per la gestione del dispositivo

```
uname -a
```
Stampa i dati relativi al sistema operativo

---

```
su -h
```
Elenca le cartelle nel filesystem e relativo peso

---

```
htop
```
Apre una specie di taskmanager , vedi tutti i processi dinamicamente

---

```
free -h
```
Stampa una panoramica dell'ingobro della ram

---

```
df -h
```
Stampa l'ingobro della memoria solida

---

```
lsblk
```
Stampa tutte le periferiche collegate al dispositivo