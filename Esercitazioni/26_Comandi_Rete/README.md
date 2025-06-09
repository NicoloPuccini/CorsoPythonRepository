# CONFIGURAZIONE RASPBERRY PI

Installazione di Raspberry Pi OS Lite
- Scaricare l'immagine di Raspberry Pi OS Lite dal sito ufficiale di Raspberry Pi.
- Configurare la connessione Wi-Fi e le impostazioni di base (come il nome host) durante il primo avvio.
- Scegliere se si desidera utilizzare SSH per accedere al Raspberry Pi senza un monitor.
- Abilitare SSH per accedere al Raspberry Pi da remoto.
- Scegliere se si desidera accedere con SSH password o chiave pubblica.
- Utilizzare Raspberry Pi Imager per scrivere l'immagine su una scheda SD.
- Inserire la scheda SD nel Raspberry Pi e accenderlo.

 # Visual studio code

 Scaricare l estensione Remote - SSH per Visual Studio Code.
- Aprire Visual Studio Code e accedere al Raspberry Pi tramite SSH.
```bash
ssh pi@<IP_ADDRESS>
# oppure
ssh pi@<HOSTNAME>
ssh allievo@rasp0-a.local
```

Se non riesci a connetterti prova 
```bash
ssh -v rasp0-a
```

Il comando ssh pi@<IP_ADDRESS> consente di accedere al Raspberry Pi tramite SSH.
oppure utilizzare il comando ssh pi@<HOSTNAME> se si è configurato un nome host.

> In questo caso il nome host è raspberrypi ed pi è l utente predefinito.

# Configurare il Raspberry Pi in Visual Studio Code
- Premere `CTRL + SHIFT + P` per aprire il menu dei comandi.
- Digitare "Apri file di configurazione SSH" e selezionare il file di configurazione SSH.
- Aggiungere la seguente riga al file di configurazione SSH:
```
Host raspberrypi
    HostName <IP_ADDRESS>
    User pi
```
- Sostituire `<IP_ADDRESS>` con l'indirizzo IP del Raspberry Pi.

# Connettersi al Raspberry Pi
- Digitare "Remote-SSH: Connect to Host" e selezionare il Raspberry Pi dall'elenco.
- Selezionare "Apri cartella" e scegliere la cartella in cui si desidera lavorare.

# Verificare l ip che è stato assegnato al raspberry
- Per verificare l'indirizzo IP del Raspberry Pi, utilizzare il comando `hostname -I`.
```bash
hostname -I
```
- Oppure usare il comando `ip a` per visualizzare le informazioni di rete.
```bash
ip a
```
- Per visualizzare le informazioni di rete, utilizzare il comando `ifconfig`.
```bash
ifconfig
ip addr
ip route
ip link
ip neigh
```
# Aggiornare il Raspberry Pi
- Per aggiornare il Raspberry Pi, utilizzare i seguenti comandi:
```bash
# aggiornare l'elenco dei pacchetti disponibili
sudo apt update
# aggiornare i pacchetti installati
sudo apt upgrade
# eseguire il reboot del raspberry
sudo reboot
```
- Per installare i pacchetti necessari, utilizzare il comando `sudo apt install` seguito dal nome del pacchetto.
```bash
sudo apt install nome_pacchetto
```


# Appunti miei

### Accesso al dispositivo con ssh
Va scaricata l'estensione live server

```
ssh nomeUtente@nomeDispositivo.local
```

```
ssh allievo@rasp0-b.local
```
ctrl + shift + p per aprire il menu a tendina, cerca ssh confg per impostare
idirizi e porte, l'ip nel config deve essere quello giusto attuale se no non ti
fa connettere, puoi verificare l'ip con ``` ip a ```

```
exit
```
Per fare il logut


Per aggiornare il firmware:
```
sudo apt update
apt list --upgrade
sudo reboot
```

Pe conoscere il nome a cui sei connesso nel modem :
```
hostname -I
```
