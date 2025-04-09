# Meremaid

E' uno strumento utile e potente che aiuta a redigere la documentazione

l'utilità della documentazione consiste nell'aiutarci e nell'aiutare a riprendere il lavoro interrotto da pause dettate 
da impellenze maggiori o per riprendere il lavoro lasciato interrotto da un altro developer

trovi la documentazione dettagliata su Mermaid chart [Documentazione semplificata](https://www.mermaidchart.com/)
o piu completa su [Documentazione completa](https://mermaid.js.org/syntax/flowchart.html)

Noi vedremo quasi solo i Flow chart (Diagrammi di flusso)

```mermaid
    graph LR
    A[Start] --> B [Is it raining ?]
    B -- yes -->C [Take an umbrella]
    B -- no --> D [Go outside withot umbrella]
    C --> E[Reach destination]
    D --> E[Reach destination]
```