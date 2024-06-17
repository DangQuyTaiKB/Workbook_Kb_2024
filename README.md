# Workbook_Kb_2024

## 23/4/2024: Receive topic. Hiep Nguyen x Dang Quy Tai
#### Zadaní 10. Program na tvorbu Excel dokumentů.
Jako parametr vezme definici kontingenční tabulky, GQL dotaz, dotaz zrealizuje, a data vloží do sešitu Excel spolu s kontingenční tabulkou. Vytvořte jako FastAPI službu.

### Společné podmínky
- Vytvořit GQL dotaz na základě existující federace,
- Definovat transformaci GQL response -> table rows (vstup pro kontingenční tabulku)
- Vytvořit kontingenční tabulku
- Vytvořit koláčový / sloupcový graf
- Vytvořit Sunburst / Chord graf
- Výsledek realizujte jako ipynb notebook (autentizace jménem a heslem, realizace aiohttp transformace response, vytvoření tabulky, vytvoření grafu).

## 23/4/2024: First commit
- $uvicorn main:app --reload

## 25/4/2024: Second commit
- @app.get: data, users, query

## 28/5/2024: Third commit
- send_payload function with token; @app.get("/download/{file_format}")

## 17/6/2024: Fourth commit
- os.remove(filename), unique filename
