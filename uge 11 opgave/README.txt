Kære kunde,

Hermed er mit kode for den ønskede PDF Downloader som I har efterspurgt, således at jeres studentermedhjælper kan benytte løsningen fremadrettet. 
Jeg vil hertil gøre jer opmærksom på vigtige elementer for at koden skal kunne virke til dens formål, samt potentielle risikoer jeg har læst ud fra jeres data, som jeg vil anbefale i får kigget på i fremtiden.

1. Sikre at download biblotekker korrekt
- Det er meget vigtigt at jeres studentermedhjælper har downloadet de relevante biblotekker der indgår i koden, hvilket kan gøres igennem en pip install som skal gøres for det enkelte biblotek men det findes der guides til.
- I får her en kort opsummering af hvad hvert bibloteks funktionalitet gør for koden:
   * pandas(pd) - til datahåndtering og dataanalyse af tabel-lignende data som f.eks. excel filer som i har bidraget
   * requests - til at sende anmodninger til at håndtere svar til f.eks. sikring af at vi har downloadet eller ikke har downloadet en filer
   * logging - til at registrere enkelte beskeder under kørsel af programmet, dette giver os mulighed for at se om en fil er downloadet og har fået sit BRnummer eller giver fejl i dets url
   * os - gør det muligt at kunne arbejde med filer og mapper, og er især vigtigt når der bliver tildelt en ny fil
   * ThreadPoolExecutor - et biblotek til at udfører givende opgaver i baggrunden, i dette tilfælde atr det så vi kan download flere filer samtidigt og reducere vente tiden
   * Tkinter- til nemt at kunne vælge fil uden behov for at definere filsti
2. Sikre sti til datafilen
- Jeg har sikret sådan at i koden at studentermedhjælperen kan finde filen for sig selv og ikke behøver at angive sin fil sti i koden, dog være OBS på at hver gang koden skal køres
så skal filen vælges igennem
3. Forvent vente tid
- Jeg har ved bedste evne forsøgt at reducere vente tiden det tager at få downloadet alle filer uden at det giver stor netværksproblemer, men forvent at der stadig går 20-30 min. alt
afhængig af fil størrelse før alt er downloadet
4. Vær på en stabil internet forbindelse
- Ved download af alle filer kan det måske opleves at internet forbindelse vil fungere langsomt ved andres computere, det er som forventet og desværre ikke så meget der kan gøres ved
uden at det skaber riscii for at hele programmet crasher, men der er limiters på så at dette problem undgås.

Jeg håber at I er tilfredse med løsningen og ellers så tøv ikke i at tage fat i mig igen hvis i har spørgsmål

Mvh
Jacob Ravn 
Konsulent ved Specialisterne
